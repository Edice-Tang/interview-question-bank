---
name: interview-question-bank
description: Collect, verify, and publish traceable real interview questions for a specified company, role, region, and employment type. Use when asked to search interview experiences or build an interview question bank, especially when the workflow must show platform results and candidate questions with original-post links before asking whether to produce the final draft.
---

# Interview Question Bank

Run a two-stage, evidence-first workflow. Do not blend search and final drafting.

## Before starting

1. Read [workflow.md](references/workflow.md).
2. Read [platform-routing.md](references/platform-routing.md) before accessing any platform.
3. Create a task folder from the files in `assets/templates/` when the user wants files saved locally.
4. Confirm the target company, role, region, and type. Treat an unspecified type as `不限` during search; never invent `FT` or `Intern` in the final title.

## Stage 1 — search and verify

Search the requested platforms according to the routing reference. Record each attempted platform and classify sources using the defined statuses.

Only treat a question as eligible when its source is `QUESTION_VERIFIED`, has an original-post URL, and has sufficient evidence. Do not use snippets, official recruiting content, media summaries, or generic preparation guides as the only evidence of a real question.

Before ending Stage 1, reply in the conversation with exactly these sections:

1. `## 搜索任务结论` — one-sentence conclusion plus the platform-status table.
2. `## 需要人工补充` — specific actions or `无`.
3. `# 待核验题目` — every eligible question must include its original-post link.
4. `是否【最终成稿】？` — wait for an explicit confirmation.

Do not draft the final question bank during Stage 1.

## Stage 2 — final draft

Run only after the user explicitly replies `最终成稿` or gives an equally unambiguous confirmation.

Use only the `QUESTION_VERIFIED` material presented in Stage 1. Follow the final-draft format in [workflow.md](references/workflow.md). If no valid question exists, state that no verifiable real interview question was obtained. If employment type is not known, mark the output as type pending instead of generating a formal `面经_[公司]_[岗位]_[FT或Intern]_[地区]` title.

## Non-negotiable boundaries

- Do not bypass login, CAPTCHA, paywalls, access controls, robots restrictions, or platform terms.
- Do not automate LinkedIn content collection; record a manual-review path instead.
- Do not store or expose credentials, cookies, tokens, or unnecessary personal data.
- Do not fill gaps with common questions, model knowledge, or invented process details.

