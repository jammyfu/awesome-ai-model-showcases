# Type and discovery audit — 2026-11-12

## Baseline and applied scope

Reviewed merged PR #16 at `01bf3e3`. This is a source-data and navigation repair, not a new model benchmark, media grant, playtest, or deployment claim. The existing six family tables, 183 main records, 51-case GPT Image subproject, and separate licensed source spotlights retain their identities.

## Work-type repair

The old classifier prioritized media format and generic Three.js/Blender pipeline descriptions. Consequently, all 183 main records were labeled either animation (114) or HTML/3D (69), with no mini-games, even when their recorded titles explicitly described a game, playable remake, RPG, or FPS.

`data/work-type-overrides.json` now records ten reviewed exceptions. Each binds a stable case ID to the exact source URL, title, and pipeline in `playbooks/research/frontier-models-inventory.json`, plus the inventory revision, review time, and classification reason. Source changes invalidate the exception rather than silently carrying an old label forward. The review relies on the existing source inventory and its cited provenance; it does not claim fresh access to every original post or successful gameplay.

The affected records are Dragon game, Theme Park HD, First Crush, the Felix Rieseberg FPS examples, Fishslop, Vibe Check Delivery, Mirror Earth, Three Games, VOWLORN, and the portal-arena FPS. Collections and comparisons remain one catalog record each. No source-only media is embedded, and no model or author claim is strengthened.

Recalculation yields **107 animations, 66 HTML/3D scenes, and 10 mini-games**, totaling the same 183 main records. The existing fallback classifier remains unchanged for other records. Unreviewed uses of “game” or “60fps” do not trigger broad reclassification.

## Auditable ordering

`data/discovery-order.json` now describes five existing ordering scopes: family navigation, versions within families, dated case lists, README selections, and separate licensed source spotlights. Each records its source, actual repository-review timestamp, editorial basis, missing-data group treatment, confidence, reason, and stable tie-break rule.

Comparable current popularity remains **unknown**, with metric, value, and observation window set to null. The timestamp records inspection of the ordering inputs, not engagement collection. The historical 3,434-star observation remains one cumulative source-repository snapshot, not two film measurements, recent growth, or a cross-model ranking. Existing ordering arrays remain the rendering source of truth.

## Additional measured findings

- All four READMEs passed the pinned Git Project Harness offline README checker before this repair. That check does not establish external-link availability or GitHub layout quality.
- The baseline README references 10,514,138 bytes of local image files. The 4,896,530-byte Imagen valley and 3,969,831-byte Codex launch image account for 84.3% of those bytes despite being displayed as small table previews. Any display derivatives require recorded dimensions, hashes, modification notices, and the same rights checks as other public assets.
- The six supplemental licensed works were discoverable in README tables but not in the existing Pages spotlight, which displayed one Claude image. A separate licensed-work browsing surface can improve this path without counting those works as part of the 183-record catalog.
- Stored translation coverage reports 312 records for titles, production methods, verification notes, and model claims in each of four locales; 73 records have nonempty translated prompts. These include archival/appendix records, are not 312 main cases, and remain AI-translated without independent human review.

## Verification for this subtask

- **Passed:** the new five-test suite first produced 16 expected failing assertions for missing classification, stale-source rejection, and ordering records; its negative-keyword test already passed. After implementation, all 14 presentation tests passed with `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools python3 -m unittest tools.test_readme_presentation -v`.
- **Passed:** source-bound classification, stale source rejection, four-language type-navigation counts, non-game negative cases, ordering evidence/null checks, and `git diff --check`.
- **Not run by this subtask:** generators and the aggregate `python3 tools/verify.py`. These are intentionally left to the integrating change so parallel work and generated output remain synchronized. This focused pass is not an aggregate verification result.
- **Not established:** new live gameplay, new external-media playback, fresh comparative popularity, or linguistic human review.
- **Separate rendering evidence:** the existing review records English and Simplified Chinese GitHub rendering for `487e63b` with all eight result previews loaded and six tables without internal overflow. That evidence is not a four-language narrow-screen pass and does not validate a later revision.
