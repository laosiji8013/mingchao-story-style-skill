---
name: mingchao-story-style
description: Write, rewrite, explain, or polish Chinese content using a distilled plainspoken, story-driven, fact-first, lightly humorous narrative style inspired by legally provided excerpts from 《明朝那些事儿》. Use when the user asks for 明朝那些事儿式文风, 讲人话故事化表达, complex concept explanation in plain Chinese, AI/product/equipment/process content rewriting, or a transferable book-style skill for another agent.
---

# Mingchao Story Style

## Quick Start

Use this skill to turn complex material into Chinese prose that reads like a clear story: conclusion first, concrete scene second, plain explanation third, and a clean ending.

Before writing:
- Read `references/source-analysis.md` for corpus-level measurements.
- Read `references/slice-analysis-index.md` when whole-book slice-level evidence is needed.
- Read `references/style-units.md` for the distilled transferable units.
- Read `references/narrative-units.md` for story movement.
- Read `references/character-writing-units.md` when writing people, founders, users, or operators.
- Read `references/explanation-units.md` when explaining abstract or technical material.
- Read `references/humor-units.md` before using humor or asides.
- Read `references/flesh-units.md` for 人物活化、场景开场、对话——给文字补血肉。
- Read `references/punchline-units.md` for 金句/包袱句式骨架——让结尾能转发。
- Read `references/chapter-rhythm.md` for long-form structure.
- Read `references/style-profile.md` for the target voice.
- Read `references/structure-patterns.md` for openings, turns, and endings.
- Read `references/rhetoric-patterns.md` for sentence-level controls.
- Read `references/output-rules.md` for execution rules, business adaptation, and quality checks.

When continuing the distillation from source material:
- Read `references/input-spec.md` before accepting source excerpts.
- Read `references/distillation-workflow.md` before updating the style rules.
- Do not store long copyrighted passages or reconstruct the source book.

## Required Inputs

Identify or ask for:
- Topic
- Target reader
- Fact material
- Intended use case
- Forbidden claims or sensitive boundaries
- Desired length and format

If fact material is thin, write only from known facts, state assumptions briefly, and avoid invented details.

## Execution Workflow

1. Identify the reader and the practical question they need answered.
2. Extract the clearest conclusion from the facts.
3. Translate professional terms into ordinary Chinese.
4. Pick a flesh engine to open with — 人物 / 场景 / 对话 / 反常识判断 — per `references/flesh-units.md`.
5. Rebuild the content with this order: hook → scene → pressure → turn → explanation → boundary → closing.
6. Use short paragraphs. Put one idea in each paragraph.
7. Deploy 2-3 punchlines at hook/turn/ending, per `references/punchline-units.md` — hung on facts, never empty slogans.
8. Add light humor only when it helps understanding and does not weaken factual accuracy.
9. Run the quality gate in `references/output-rules.md` before final output.

## Output Contract

For writing or rewriting tasks, output:
- Title
- Main text
- Brief final-check note when the user asks for traceability or validation

For skill-transfer tasks, output or update:
- `SKILL.md`
- `references/style-profile.md`
- `references/source-analysis.md`
- `references/slice-analysis-index.md`
- `references/slice-index.csv`
- `references/style-units.md`
- `references/narrative-units.md`
- `references/character-writing-units.md`
- `references/explanation-units.md`
- `references/humor-units.md`
- `references/flesh-units.md`
- `references/punchline-units.md`
- `references/chapter-rhythm.md`
- `references/structure-patterns.md`
- `references/rhetoric-patterns.md`
- `references/output-rules.md`
- `references/examples.md`
- `references/anti-examples.md`
- `references/glossary.md`
- `references/test-prompts.json`
- `references/test-results.md`
- `references/handoff.md`

## Boundaries

Do not imitate a living author's identity, claim to reproduce the original book, or quote protected source text unless the user provides a short lawful excerpt and the task requires brief analysis. Distill mechanisms: stance, structure, pacing, explanation method, and quality gates.
