# Slice Analysis Index

This is the full-book slice-level distillation index. It stores metadata only: no source paragraphs, no long quotes, and no reconstructable source text.

## Full Index

The complete machine-readable index is in `references/slice-index.csv`.

Each row represents one full-book slice and includes:
- `slice_id`
- position percentage and decile
- anonymized section key
- paragraph and line span
- length and rhythm metrics
- primary and secondary function labels
- marker counts for reader relation, turn, explanation, humor, facts, character pressure, dialogue, and closure

## Corpus Slicing Result

- Total slices: 1831
- Estimated heading counts: `{'volume': 7, 'sub': 3, 'part': 20, 'chapter': 156}`
- Slice length without punctuation: `{'min': 460, 'p25': 708, 'median': 733, 'p75': 749, 'max': 760, 'mean': 713.69}`
- Paragraphs per slice: `{'min': 4, 'p25': 13, 'median': 17, 'p75': 21, 'max': 47, 'mean': 17.16}`
- Sentences per slice: `{'min': 6, 'p25': 16, 'median': 19, 'p75': 22, 'max': 44, 'mean': 19.39}`

## Primary Function Distribution

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

## Position Deciles

| Decile | Slice Count | Top Functions |
|---:|---:|---|
| 1 | 184 | humor_aside:44, dialogue_scene:34, narration:27, turn:27, judgment:21 |
| 2 | 183 | dialogue_scene:47, turn:43, humor_aside:25, narration:17, judgment:15 |
| 3 | 183 | humor_aside:43, dialogue_scene:34, turn:31, narration:30, judgment:23 |
| 4 | 183 | dialogue_scene:92, turn:32, humor_aside:21, character:12, narration:12 |
| 5 | 183 | dialogue_scene:74, turn:45, humor_aside:31, character:11, judgment:8 |
| 6 | 183 | dialogue_scene:57, turn:56, humor_aside:24, narration:9, explanation:9 |
| 7 | 183 | humor_aside:50, dialogue_scene:45, turn:38, narration:15, closure:13 |
| 8 | 183 | humor_aside:48, turn:46, dialogue_scene:31, judgment:16, narration:16 |
| 9 | 183 | humor_aside:46, dialogue_scene:41, turn:30, narration:24, character:12 |
| 10 | 183 | humor_aside:41, closure:34, turn:24, dialogue_scene:22, judgment:22 |

## Function Rhythm Stats

| Function | Count | Avg Chars | Avg Paragraphs | Avg Transition Hits |
|---|---:|---:|---:|---:|
| character | 99 | 706.9 | 16.08 | 3.4 |
| closure | 93 | 716.19 | 18.47 | 5.15 |
| dialogue_scene | 477 | 717.69 | 19.26 | 3.87 |
| explanation | 85 | 722.69 | 15.72 | 4.94 |
| humor_aside | 373 | 714.17 | 16.43 | 3.98 |
| inventory | 28 | 711.79 | 14.61 | 3.86 |
| judgment | 134 | 711.81 | 16.86 | 4.13 |
| narration | 170 | 702.37 | 15.67 | 3.77 |
| turn | 372 | 713.2 | 16.48 | 5.73 |

## Marker Totals

| Marker | Total Hits |
|---|---:|
| transition_hits | 8004 |
| dialogue_hits | 6629 |
| fact_anchor_hits | 5820 |
| humor_hits | 5635 |
| direct_reader_hits | 5121 |
| scene_hits | 4301 |
| turn_hits | 4027 |
| closure_hits | 2903 |
| character_pressure_hits | 2307 |
| judgment_hits | 2292 |
| inventory_hits | 1840 |
| plain_translation_hits | 1478 |

## How To Use This Index

Use the CSV when an agent needs to inspect the whole-book rhythm without loading source text.

Recommended lookup patterns:
- Find slices where `primary_function=turn` to study reversal density.
- Find slices where `primary_function=explanation` to study plain-language translation.
- Find slices where `primary_function=character` to study the character-as-pressure model.
- Find slices with high `humor_hits` but also high `fact_anchor_hits` to study controlled humor.
- Compare `position_decile` distributions to see how the book alternates narration, judgment, explanation, and closure.

Do not treat the index as a replacement for source rights. It is an analysis map, not a text archive.
