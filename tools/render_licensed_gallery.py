"""Readable, full-width source works, separate from the main case count."""
import json
from html import escape as e
from PIL import Image
from media_policy import ROOT, is_public_asset

LANGS=('en','zh-CN','zh-TW','ja','ko')
LABELS={
"ko":('허가된 작품을 크게 보기', '출처가 공개한 8개 작품, 6개 모델 계열입니다. 추가 작품은 주요 목록 집계에 포함하지 않습니다. 정지 이미지 미리보기는 재생 확인이나 모델 성능의 증거가 아닙니다.', '주요 목록 보기 (영어)', '출처', '게시 허가', '원본 이미지', '저작자 표시 및 변경 사항', '사례 제안', '소개는 사람이 검수하지 않은 AI 번역입니다. 모델 정보는 출처의 주장이고 생성을 다시 실행하지 않았습니다. 비교 가능한 최근 인기도 자료가 없으므로 누적 stars 순위가 아니라 모델 계열별로 배열합니다.', '정지 이미지 미리보기', '영상 프레임', '게임 캐릭터 제작 과정', '게임 일러스트', '이미지 편집', '생성 이미지', 'SVG 작품', '모델 선택'),
'en':('Licensed works, up close','Eight source-published works, six model families. These supplemental works are separate from the main catalog. Still previews are not playback or proof of model performance.','Browse the main catalog','Source','Permission','Full image','Credits & changes','Contribute a case','AI-translated descriptions, not human-reviewed. Model attribution is source-reported; no generation was rerun. Current comparable popularity is unknown; order follows model families, not cumulative stars.','Still preview','Film frame','Game character workflow','Game illustration','Image edit','Generated image','SVG result','Choose a model'),
'zh-CN':('放大看授权作品','八件来源发布的作品，覆盖六个模型家族。这些补充作品不计入主目录。静态预览不代表播放验证或模型性能证明。','浏览主目录','原始来源','授权依据','查看原图','署名与修改','贡献案例','介绍为 AI 翻译，未经人工审校。模型归属为来源声明，未重新生成。缺少可比的近期热度数据；按模型家族编排，不按累计 stars 排榜。','静态预览','短片画面','游戏角色制作流程','游戏插画','图像编辑','生成图像','SVG 作品','选择模型'),
'zh-TW':('放大看授權作品','八件來源發布的作品，涵蓋六個模型家族。這些補充作品不計入主目錄。靜態預覽不代表播放驗證或模型效能證明。','瀏覽主目錄','原始來源','授權依據','查看原圖','署名與修改','貢獻案例','介紹為 AI 翻譯，未經人工審校。模型歸屬為來源聲明，未重新生成。缺少可比的近期熱度資料；按模型家族編排，不按累計 stars 排榜。','靜態預覽','短片畫面','遊戲角色製作流程','遊戲插畫','影像編輯','生成影像','SVG 作品','選擇模型'),
'ja':('許諾済み作品を大きく見る','公開元による8作品、6つのモデル系列。追加作品は主目録の件数に含みません。静止画は再生確認やモデル性能の証明ではありません。','主目録を見る','出典','掲載許諾','元画像を見る','クレジットと変更','事例を投稿','紹介は AI 翻訳で、人による校閲は未実施です。モデルは公開元の申告で、生成の再実行はしていません。比較可能な最近の人気データは不明です。累積 stars 順ではなく、モデル系列ごとに掲載します。','静止画プレビュー','映像のフレーム','ゲームキャラクター制作工程','ゲーム用イラスト','画像編集','生成画像','SVG 作品','モデルを選ぶ')}
TYPES={'licensed-gpt-godot-character':11,'licensed-gpt-codex-launch-scene':12,'licensed-qwen-image21-snowy-street':13,'licensed-deepseek-crowned-frog':15}
CSS='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#10131a;color:#f0f2f5;font:17px/1.6 system-ui,sans-serif}main{max-width:1000px;margin:auto;padding:24px}a{color:#c2ff67;text-underline-offset:4px}nav{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}h1{font-size:clamp(28px,5vw,48px);line-height:1.15}h2{font-size:clamp(22px,4vw,30px);line-height:1.25}article{margin:40px 0 64px;scroll-margin-top:20px}figure{margin:16px 0}img{display:block;width:100%;height:auto;max-height:720px;object-fit:contain;background:#191e28;border-radius:12px}p,h1,h2,a{overflow-wrap:anywhere}nav a{min-height:36px;display:inline-flex;align-items:center}.meta{color:#bac2cd}.type{color:#c2ff67;font-weight:700}footer{border-top:1px solid #39414e;padding-top:24px}article:target{outline:2px solid #c2ff67;outline-offset:12px}@media(max-width:480px){main{padding:18px}article{margin-bottom:44px}body{font-size:16px}}'''
def write_licensed_gallery():
    first=json.loads((ROOT/'data/readme-featured-cases.json').read_text())['cases']
    extra=json.loads((ROOT/'data/readme-supplemental-previews.json').read_text())['cases']
    families=json.loads((ROOT/'data/discovery-order.json').read_text())['family_order']
    rows=sorted(first+extra,key=lambda r:families.index(r.get('model_family','claude')))
    for lang in LANGS:
        w=LABELS[lang];parts=[f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{e(w[1])}"><title>{e(w[0])} · Awesome AI Model Showcases</title><style>{CSS}</style></head><body><main>', '<nav aria-label="Languages">'+ ' · '.join(f'<a href="licensed-gallery.{l}.html" lang="{l}">{label}</a>' for l,label in zip(LANGS,['English','简体中文','繁體中文','日本語','한국어']))+'</nav>',f'<h1>{e(w[0])}</h1><p>{e(w[1])}</p>',f'<a href="index.html?lang={"en" if lang in ("en","ja","ko") else "zh"}">{e(w[2])} →</a>',f'<nav aria-label="{e(w[16])}">']
        for family in families:
            row=next(r for r in rows if r.get('model_family','claude')==family)
            parts.append(f'<a href="#{row["id"]}">{dict(claude="Claude",gemini="Gemini",grok="Grok",qwen="Qwen",deepseek="DeepSeek",**{"gpt-code":"GPT"})[family]}</a>')
        parts.append('</nav>')
        for n,row in enumerate(rows):
            if not is_public_asset(row['image_path']):raise ValueError(f'Unapproved gallery image {row["id"]}')
            loc=row['locales'][lang];path=row['image_path'].removeprefix('docs/')
            with Image.open(ROOT/row['image_path']) as img:width,height=img.size
            credit=row.get('display_credit',row.get('author',''))
            typ=w[TYPES.get(row['id'],10 if row in first else 14)]
            parts += [f'<article id="{row["id"]}"><p class="type">{e(typ)} · {e(w[9])}</p><h2>{e(loc["title"])}</h2><p class="meta">{e(row["model"])} · {e(credit)}</p>',f'<figure><a href="{path}" aria-label="{e(w[5])}"><img src="{path}" width="{width}" height="{height}" alt="{e(loc["alt"])}" loading="{"eager" if n==0 else "lazy"}" decoding="async"></a></figure>',f'<p>{e(loc["summary"])}</p>']
            if loc.get('changes'):parts.append(f'<p class="meta">{e(loc["changes"])}</p>')
            links=[(row['source_url'],w[3]),(row['license_evidence_url'],w[4]),(row['license_url'],row['license']),(path,w[5])]
            if row in first:links += [(row['demo_url'],{'en':'Watch the film','zh-CN':'观看成片','zh-TW':'觀看成片','ja':'映像を見る','ko':'영상 보기'}[lang]),(row['local_license_path'].removeprefix('docs/'),w[6])]
            else:links.append(('https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/readme-preview-credits.md#'+row['id'],w[6]))
            parts.append('<nav>'+' · '.join(f'<a href="{e(url)}">{e(label)}</a>' for url,label in links)+'</nav></article>')
        parts += [f'<footer><p>{e(w[8])}</p><a href="https://github.com/jammyfu/awesome-ai-model-showcases/issues/new?template=case-submission.yml">{e(w[7])}</a></footer></main></body></html>']
        (ROOT/f'docs/licensed-gallery.{lang}.html').write_text('\n'.join(parts)+'\n')
if __name__=='__main__':write_licensed_gallery()
