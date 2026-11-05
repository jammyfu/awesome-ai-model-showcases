#!/usr/bin/env bash
# Run locally with a GitHub CLI installation authenticated as the intended owner.
set -euo pipefail
cd "$(dirname "$0")"
REPO="jammyfu/awesome-gpt-image-gifs"
if ! command -v gh >/dev/null 2>&1; then
  echo 'GitHub CLI (gh) is required: https://cli.github.com/' >&2
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo 'Sign in first: gh auth login' >&2
  exit 1
fi
if [[ ! -d .git ]]; then
  git init -b main
fi
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  git add .
  git commit -m 'feat: launch AI animated GIF gallery with prompts'
fi
if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository already exists: $REPO"
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$REPO.git"
  fi
  git push -u origin main
else
  gh repo create "$REPO" --public --source . --remote origin --push --description 'Curated GPT Image 2.6 animated GIF gallery — free AI GIF examples, memes, prompts and seamless loops.'
fi
printf '\nPublished repository: https://github.com/%s\n' "$REPO"
printf 'Now configure Settings → Pages → Build and deployment → GitHub Actions.\n'
