#!/usr/bin/env python3
"""Build a separate, fail-closed Pages artifact. Never upload the archive tree."""
from __future__ import annotations
import argparse
import re
import shutil
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from media_policy import ROOT, LFS_HEADER, MEDIA_EXTENSIONS, grants, is_public_asset
from media_format import probe_media

TEXT_EXTENSIONS = {'.html','.js','.css','.json','.md','.txt'}

class MediaRefs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {'img','video','audio','source','iframe','embed','object'}:
            for key in ('src','poster','data'):
                if attrs.get(key): self.refs.append((attrs[key],True))
            # No current templates need srcset. Reject instead of misparsing URLs.
            if attrs.get('srcset'): self.refs.append(('unsupported-srcset:',True))
        if tag in {'image','use'}:
            for key in ('href','xlink:href'):
                if attrs.get(key): self.refs.append((attrs[key],True))
        if tag == 'input' and attrs.get('type','').lower() == 'image' and attrs.get('src'):
            self.refs.append((attrs['src'],True))
        if tag == 'a' and attrs.get('href'):
            self.refs.append((attrs['href'],False))


def check_references(file: Path, root: Path, *, staged: bool = False) -> None:
    text = file.read_text(encoding='utf-8')
    parser = MediaRefs(); parser.feed(text)
    refs = parser.refs
    refs += [(m.group(1), True) for m in re.finditer(r'!\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)',text)]
    refs += [(m.group(1), False) for m in re.finditer(r'(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)',text)]
    refs += [(m.group(1), True) for m in re.finditer(r'url\([\s\'"]*([^\s\'"\)]+)',text)]
    for url, embed in refs:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            if embed and not (parts.scheme == 'https' and parts.netloc == 'img.shields.io' and parts.path.startswith('/badge/')):
                raise ValueError(f'{file}: external/unapproved media embed: {url}')
            continue
        if not parts.path: continue
        target = (file.parent / unquote(parts.path)).resolve()
        if not embed and target.suffix.lower() not in MEDIA_EXTENSIONS: continue
        try:
            rel = target.relative_to(root.resolve()).as_posix()
        except ValueError:
            raise ValueError(f'{file}: media reference escapes public root: {url}')
        if not target.is_file():
            raise ValueError(f'{file}: missing/unapproved media reference: {url}')
        if not staged and not is_public_asset(rel,root):
            raise ValueError(f'{file}: unapproved media reference: {url}')


def validate_site(output: Path, source: Path) -> None:
    allowed = grants(source)
    for file in output.rglob('*'):
        if file.is_symlink(): raise ValueError(f'public symlink: {file}')
        if not file.is_file(): continue
        with file.open('rb') as stream: head=stream.read(128)
        if head.startswith(LFS_HEADER): raise ValueError(f'LFS pointer in public artifact: {file}')
        if file.suffix.lower() in MEDIA_EXTENSIONS:
            rel='docs/'+file.relative_to(output).as_posix()
            if rel not in allowed or not is_public_asset(rel,source):
                raise ValueError(f'unapproved public asset: {rel}')
            import hashlib
            if hashlib.sha256(file.read_bytes()).hexdigest() != allowed[rel]['sha256']:
                raise ValueError(f'public bytes changed: {rel}')
            # Actual decoded image/video, not merely a pointer oid/size check.
            probe_media(file,ext=file.suffix.lstrip('.'))
        if file.suffix in {'.html','.md','.css'}:
            check_references(file,output,staged=True)


def build_site(source: Path, output: Path) -> None:
    source=source.resolve(); output=output.resolve()
    if output.exists(): raise FileExistsError(f'Refusing to overwrite existing output: {output}')
    if output == source or source in output.parents and output.parts[len(source.parts)] == 'docs':
        raise ValueError('Output must not be inside docs')
    for rel in grants(source):
        if not is_public_asset(rel,source):
            raise ValueError(f'public grant has missing/changed/unapproved bytes: {rel}')
        with (source/rel).open('rb') as stream:
            if stream.read(128).startswith(LFS_HEADER):
                raise ValueError(f'LFS pointer is not publishable media: {rel}')
    output.mkdir(parents=True)
    for file in sorted((source/'docs').rglob('*')):
        if file.is_symlink(): raise ValueError(f'Unexpected docs symlink: {file}')
        if not file.is_file(): continue
        rel=file.relative_to(source).as_posix()
        if file.suffix.lower() in MEDIA_EXTENSIONS:
            if not is_public_asset(rel,source): continue
        elif file.suffix not in TEXT_EXTENSIONS and file.name != '.nojekyll':
            continue
        target=output/file.relative_to(source/'docs')
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(file,target)
    validate_site(output,source)
    print(f'public Pages artifact verified: {sum(p.is_file() for p in output.rglob("*"))} files; no unapproved media or LFS pointers')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.output: build_site(ROOT,args.output)
    else:
        with tempfile.TemporaryDirectory(prefix='showcase-public-') as tmp:
            build_site(ROOT,Path(tmp)/'site')

if __name__=='__main__': main()
