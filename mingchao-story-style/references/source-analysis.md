# Source Analysis

This file records corpus-level findings from the user-provided TXT. It intentionally stores no source paragraphs.

## Corpus Shape

- Source size: 4,747,199 bytes.
- Estimated nonempty lines: 31,614.
- Estimated headings: 720.
- Estimated prose paragraphs: 30,893.
- Candidate analyzable slices detected by markers: 38.

## Length Profile

Paragraphs are short.

| Metric | Paragraph Length Without Punctuation |
|---|---:|
| p25 | 21 |
| median | 37 |
| p75 | 57 |
| mean | 42.18 |
| max | 281 |

Sentences are also compact.

| Metric | Sentence Length Without Punctuation |
|---|---:|
| p25 | 18 |
| median | 31 |
| p75 | 47 |
| mean | 34.96 |
| max | 202 |

Execution implication:
- Prefer 20-60 Chinese characters per paragraph for normal passages.
- Prefer 1-2 sentences per paragraph.
- Use longer paragraphs only for setup, inventory, or compressed chronology.

## Marker Counts

High-frequency style signals:

| Marker Category | Count |
|---|---:|
| Light humor / parenthetical aside | 5631 |
| Direct reader relation | 5113 |
| Historical anchor | 4624 |
| Turn / contrast | 4026 |
| Scene movement | 3480 |
| Judgment | 2274 |
| Plain-language translation | 1475 |

Execution implication:
- The style is not only "funny history"; it is reader-guided explanation with frequent turns.
- Humor should appear after the reader understands the fact.
- Historical or factual anchors must remain visible.

## Transition Counts

Most frequent transition signals:

| Transition | Count |
|---|---:|
| 所以 | 1518 |
| 终于 | 1018 |
| 于是 | 993 |
| 然而 | 832 |
| 不过 | 635 |
| 可是 | 622 |
| 其实 | 544 |
| 当然 | 482 |
| 后来 | 438 |
| 但是 | 251 |
| 事实上 | 228 |
| 从此 | 139 |
| 在我看来 | 89 |
| 这个时候 | 60 |
| 问题是 | 56 |
| 换句话说 | 50 |
| 也就是说 | 46 |

Execution implication:
- Use "于是/终于" to push chronology.
- Use "然而/不过/可是/但是" to create reversal.
- Use "其实/事实上/换句话说/也就是说" to convert facts into explanation.
- Use "所以" to close local reasoning.

## Label Distribution

Estimated paragraph function labels:

| Label | Count |
|---|---:|
| narration | 20453 |
| turn | 3758 |
| scene | 3200 |
| ending | 2499 |
| judgment | 2115 |
| explanation | 1835 |
| opening | 927 |

Execution implication:
- Default to narrative movement.
- Insert explanation and judgment at decision points, not as long essays.
- Use turns often enough that the prose keeps moving.

## Practical Distillation

The corpus points to this formula:

```text
短段落 + 旁白关系 + 历史/事实锚点 + 转折推进 + 白话解释 + 可控调侃 + 明确判断
```

For non-history topics, replace "historical anchor" with "fact anchor": data, use case, process step, product constraint, or observed field problem.

## Full Slice Follow-Up

A second pass sliced the full book into 1831 continuous functional slices. The complete metadata-only index is stored in `references/slice-index.csv`, with a readable summary in `references/slice-analysis-index.md`.

Full-slice primary function distribution:

| Function | Count |
|---|---:|
| dialogue_scene | 477 |
| humor_aside | 373 |
| turn | 372 |
| narration | 170 |
| judgment | 134 |
| character | 99 |
| closure | 93 |
| explanation | 85 |
| inventory | 28 |

Interpretation:
- The book's readable energy comes from scene/dialogue movement, controlled aside, and frequent reversal.
- Explanation is present but usually inserted into movement instead of becoming a standalone lecture.
- Closure appears repeatedly at local section level, not only at chapter endings.
