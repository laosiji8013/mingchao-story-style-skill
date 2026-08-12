---
name: mingchao-story-style
description: Write, rewrite, explain, or review Chinese content using transferable writing mechanisms distilled through full-text extraction and slicing of 《明朝那些事儿》. Use when the user asks for 明朝那些事儿式文风, 明朝故事化文风, 讲人话的故事化表达, readable Chinese explanations, 人物小传, event retrospectives, or rewriting AI, product, business, process, and technical material for general readers. Apply distilled structure, pacing, plain-language explanation, and story progression without impersonating the author or copying protected text.
---

# 《明朝那些事儿》文风切片蒸馏

本 Skill 的文风来源是《明朝那些事儿》。它把从全书提取、切片和蒸馏出的可迁移写作机制，用于把复杂事实写成普通人愿意读、读得懂、读完知道重点的故事化中文。

本 Skill 不是作者角色模仿或一段系统提示词。它是对《明朝那些事儿》完整长篇文本进行连续切片、功能统计、规律筛选和跨主题测试后得到的方法蒸馏。执行时使用结构、节奏、解释机制和质量闸门，不检索或重建原书。

## 读取参考

- 写作或改写前，读取 `references/style-profile.md`、`references/writing-units.md` 和 `references/output-rules.md`。
- 需要设计长文结构时，再读取 `references/structure-patterns.md`。
- 需要示例或诊断草稿时，读取 `references/examples.md` 和 `references/anti-examples.md`。
- 需要解释本 Skill 的来源或继续蒸馏时，读取 `references/distillation-method.md` 和 `references/evidence-summary.md`。

## 获取输入

识别或补齐：

- 主题
- 目标读者
- 事实材料
- 使用场景
- 禁止说法或敏感边界
- 长度与格式

材料不足时，明确指出缺口。不要虚构数据、事件、人物心理或因果关系。

## 执行流程

1. 提取不能改变的事实和限制。
2. 判断读者真正需要解决的问题。
3. 尽早给出有事实支撑的核心判断。
4. 用场景、人物压力、时间推进或对比组织材料。
5. 将术语翻译为普通中文，再补必要的专业解释。
6. 使用短段落推进，每段只承担一个主要任务。
7. 在读者预期需要改变时使用转折，不制造无事实依据的戏剧性。
8. 只在有助理解时加入轻微幽默或旁白。
9. 写出限制、代价或不确定性。
10. 用结论、边界或下一步完成收束。
11. 按 `references/output-rules.md` 执行终检后再交付。

## 默认结构

```text
事实锚点 → 明确判断 → 具体场景 → 压力/问题 → 转折 → 白话解释 → 边界 → 收束
```

根据材料调整，不要机械填满每一步。

## 输出

普通写作任务默认输出：

```text
标题

正文
```

用户要求审校、过程或可追溯性时，再附简短终检说明。不要默认把分析过程写进成品。

## 边界

- 不冒充当年明月或任何在世作者。
- 不声称逐句复刻《明朝那些事儿》或其他作品。
- 不复制、续写或重建用户未提供的受保护文本。
- 用户要求完全模仿作者身份时，简要说明只能使用机制层特征，然后提供原创版本。
- 保留用户事实，不用故事感掩盖证据缺口。
- 法律、公文、学术和高风险说明优先保证准确、完整和正式度，必要时降低幽默与叙事强度。
