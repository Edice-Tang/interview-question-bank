# Workflow and Output Contract

## 1. Task setup

Create a task ID as `YYYYMMDD_公司_岗位_地区`. Copy the files in `assets/templates/` into the task folder when files are requested.

Record company aliases, role aliases, region, requested type, preferred time range (12 months), fallback range (3 years), and search languages.

Search in this order when precise results are insufficient:

1. same role in other major cities;
2. adjacent role at the same company, retaining the actual role;
3. FT and Intern cross-reference, retaining the actual type;
4. sources from the last 3 years, marked `[较旧，仅供参考]` in the final output.

## 2. Source statuses

| Status | Meaning | Eligible for final draft |
|---|---|---|
| `NO_HIT` | Required query set and applicable expansions completed, but no candidate URL found | No |
| `HIT_NOT_ACCESSIBLE` | URL or snippet found, but the body cannot be read legally | No |
| `ACCESSIBLE_NO_QUESTION` | Body readable, but no traceable candidate question | No |
| `QUESTION_VERIFIED` | Body readable, original question and URL are traceable | Yes |

Never label one focused search with no result as `NO_HIT`; record it as an incomplete search attempt.

For every `QUESTION_VERIFIED` source, also record `interview_text_status` as `FULL`, `PARTIAL`, or `NOT_PRESENT`:

- `FULL`: the complete visible candidate-authored `Interview` field was read and saved as minimum necessary evidence;
- `PARTIAL`: the field is truncated, collapsed, or only partly visible;
- `NOT_PRESENT`: the record has no separately identifiable `Interview` field.

Only `FULL` content may be published under `Interview 原文` in the final draft. A question may remain verified even when its accompanying interview text cannot be published as complete.

## 3. Stage 1 chat output

Always output the following in the conversation after the search scope is complete:

```md
## 搜索任务结论

一句话结论：{本轮已执行的平台、命中情况和是否获得可核验题目。}

| 平台 | 执行情况与结果 | 是否需要人工补充 |
|---|---|---|
| 平台名称 | 已检索/已打开/受限/未完成及结果 | 否；或写明具体人工动作 |

## 需要人工补充

- {没有则写“无”。}

# 待核验题目

1. {原题，尽量保留原文}
   - 原帖链接：{完整 URL}
   - 来源：{平台}
   - 实际岗位 / 地区 / 类型：{仅填写来源明确提及的字段}
   - 核验状态：`QUESTION_VERIFIED`

{没有合格题目时写：暂无可核验的真实面试题。}

是否【最终成稿】？回复“最终成稿”后，我将仅使用以上 `QUESTION_VERIFIED` 题目生成最终题库。
```

## 4. Stage 2 final-draft format

Only run after explicit user confirmation. Use only verified questions shown in Stage 1.

```md
# 面经_[公司]_[岗位]_[FT或Intern]_[地区]

面试时间：{仅在来源明确时填写}
面试轮次：{仅在来源明确时填写}
面经内容：{仅在来源明确概述时填写}

## Interview 原文

### 来源 {source_id}

{逐字保留该原帖完整、可见的 `Interview` 字段正文。保留原语言、段落、列表、标点和拼写；不翻译、不摘要、不润色、不补写。}

{如没有 `FULL` 原文：`该来源的 Interview 正文未能完整读取，需人工补充；不以片段替代完整原文。`}

## 面试流程

{只写来源明确的总轮数、形式、时长、语言、OA、适用地区与类型、来源时间范围。此处是辅助摘要，不能替代或改写上方原文。}

## 真实面试经验库 / 题库

1. {原题}
```

Company, role, and `FT` or `Intern` are mandatory for a formal filename and H1. Region is optional. If a mandatory field is missing, do not guess; mark the draft as pending instead.

`Interview 原文` must be grouped by source. Only copy the complete, visible candidate-authored `Interview` field, not the entire page. When a platform separately exposes `Application` content, it may be placed in an optional `申请情况原文` section using the same verbatim rule; it never substitutes for `Interview 原文`. Do not claim a complete original text when it is collapsed, paywalled, clipped, or inferred from a snippet.

In the question-bank section, output only questions: no URLs, sources, dates, locations, notes, frequency, or explanations. Preserve original wording where possible and deduplicate only clearly identical questions.

## 5. Evidence and privacy

Store the minimum necessary evidence: URL, access date, source status, match fields, `interview_text_status`, and the complete `Interview` field only when it is needed for the requested final draft. Do not retain passwords, cookies, tokens, irrelevant personal data, or the rest of the source page. Do not copy entire posts into the final output.
