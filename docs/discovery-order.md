# Discovery order / 展示排序

Reviewed: **2026-11-11**. Configuration: [data/discovery-order.json](../data/discovery-order.json). The four README editions and generated version catalogs share that configuration. It is editorial navigation, not a model performance or popularity benchmark.

## Priority contract

1. Honor an explicitly requested topic focus or important new platform/version within the relevant category. Record the reason and source; do not infer official availability from a community label.
2. Where popularity is measured, compare only compatible metrics, sources, observation times, and windows within the same scope. Keep `metric`, `source`, `observed_at`, `window`, and `reason`. Never compare a video's views with a repository's stars as if they were the same measure.
3. Missing popularity is unknown, never zero. Disclose incomplete coverage and fall back to a named editorial order rather than manufacturing a leaderboard.
4. Within a version, use complete source dates newest first, with descending case ID as the same-day tie-breaker. Missing or partial dates go last. A list labeled recent posts remains date-based and is not called a popularity ranking.

## Current implementation and limits

The 183 main records contain no comparable engagement metrics or observation timestamps. Family order therefore stays stable; no family is presented as more popular. Version priorities are explicit. Qwen 4 Max Preview and Qwen 4.0 Preview now precede Qwen3.8 27B as current-generation editorial entries, using the inventory's source labels, not an official-release claim. Each family example comes from its first populated priority version.

The current renderer **does not calculate popularity scores**. Before enabling a popularity sort, collect compatible source-linked snapshots, define their scope and missing-data treatment, and add comparator/coverage tests. Do not merely change `status` to imply a ranking has been implemented.

## 简体中文

先遵循用户明确指定的专题重点或重要新平台／版本；有可核实且同口径的热度数据时，再在同层级中比较热度。必须记录指标、来源、采样时间、统计窗口和排序理由。缺失不记为零，最新也不等于最热。

当前 183 条主案例没有可比互动量，因此不编造模型热度榜。家族顺序暂时保持稳定；版本采用明确的编辑优先级，Qwen 4 Max Preview、Qwen 4.0 Preview 提到 Qwen3.8 27B 前面。来源日期只用于同版本内排序和明确标为「近期原帖」的列表。日后真正启用热度排序，须先补证据、比较规则与测试。
