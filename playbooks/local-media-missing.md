# Local media download gaps

Date 2026-11-06. Failures are listed, not skipped silently.

- `krouxzz-wave-ref` x-dynamic https://video.twimg.com/tweet_video/HWWn8n7b0AAN1xP.mp4 — HTTP 404: empty
- `luffy-x-article` media — inventory has no attachment URL; the X article/post API attempt did not retrieve media (article id 2118269816821919744 returned API 404 as a post). That cannot assert the original longform has no media. Announcement 2118274913337552992 has no attachments in the inventory. Prompts archived in prompt.md. Not replaced with SVG.

Notes:
- Krouxzz live attachment is `HWWnk8IXsAE0aXq.mp4` (archived). `HWWn8n7b0AAN1xP.mp4` was a stale catalog URL and 404s.
- Ravivit paper-boat GIF requires a browser User-Agent; Atlas 403s the inventory bot UA.
