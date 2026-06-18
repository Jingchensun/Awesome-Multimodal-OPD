# 🖼️ Awesome Multimodal On-Policy Distillation

> 多模态 **On-Policy Distillation (OPD / OPSD)** 论文精选 —— 聚焦 **VQA、Video QA、视觉推理、语音、生成、具身/VLA** 等多模态场景。

![papers](https://img.shields.io/badge/papers-53-4E6813?style=for-the-badge) ![subfields](https://img.shields.io/badge/subfields-6-1F4CAD?style=for-the-badge) ![web--added](https://img.shields.io/badge/web--added-3-2E86C1?style=for-the-badge)

本列表从三个 awesome 仓库筛取多模态相关条目，并经**网络检索查漏补缺**：
[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) · [chrisliu298/awesome-on-policy-distillation](https://github.com/chrisliu298/awesome-on-policy-distillation) · [nick7nlp/Awesome-LLM-On-Policy-Distillation](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation)。

**什么是 OPD？** `C1` 学生在训练时采样自己的轨迹 `y ~ π_student(·|x)`；`C2` 教师在这些**学生自生成样本**上提供逐 token / 序列级监督。**OPSD** 是其特例：教师=同一模型，但被特权信息（验证轨迹 / 答案 / 区域视觉细节 / 更长上下文…）所条件化。

每篇论文按**四问**速览：① 问题与重要性 · ② 方法与独特贡献 · ③ 任务/数据集/模型 · ④ 局限与未来工作。

**标记说明**：🔎 = 不在上述三库、经网络检索补入；`严格度` 徽标标注是否为严格 OPD（严格 / OPD+RL / 自蒸馏 / 相关·非OPD）。⭐ Star 徽标实时更新；被引数抓取自 Semantic Scholar（2026-06，多为新论文，数值仍在变化，仅供参考）。

## 📊 概览

| 子方向 | 篇数 | 跳转 |
| :-- | :--: | :-- |
| 🖼️ VLM 理解 / VQA / 视觉推理 OPD | 15 | [↳](#-vlm-理解--vqa--视觉推理-opd) |
| 🎬 视频 / VideoQA / 时序定位 OPD | 7 | [↳](#-视频--videoqa--时序定位-opd) |
| 🎨 图像 / 视频生成（扩散 · 流匹配）OPD | 12 | [↳](#-图像--视频生成扩散--流匹配opd) |
| 🔊 语音 / 音频 OPD | 7 | [↳](#-语音--音频-opd) |
| ⚡ 多模态投机解码蒸馏 | 4 | [↳](#-多模态投机解码蒸馏) |
| 🤖 具身 / VLA / GUI / 视觉智能体 OPD | 8 | [↳](#-具身--vla--gui--视觉智能体-opd) |
| **合计** | **53** | |

## 🖼️ VLM 理解 / VQA / 视觉推理 OPD

把推理能力迁移进视觉语言模型、在 VQA / 视觉推理上做在策略蒸馏的核心工作。

| 论文 | 时间/会议 | 🌟 | 被引 | 严格 |
| :-- | :--: | :--: | :--: | :--: |
| [ICLR 2026 · 旗舰 VLM: VOLD — LLM→VLM OPD](https://arxiv.org/abs/2510.23497) | ICLR 2026 | `📄 paper-only` | 10 | OPD |
| [统一配方: Uni-OPD — Unified OPD across LLMs & MLLMs](https://arxiv.org/abs/2605.03677) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/WenjinHou/Uni-OPD?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/WenjinHou/Uni-OPD) | 5 | OPD |
| [arXiv 2026: Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation](https://arxiv.org/abs/2605.18740) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/VisionOPD/Vision-OPD?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/VisionOPD/Vision-OPD) | 2 | OPD |
| [arXiv 2026: Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://arxiv.org/abs/2604.28123) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/XIAO4579/PRISM?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/XIAO4579/PRISM) | 2 | OPD |
| [arXiv 2026: ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation](https://arxiv.org/abs/2606.05718) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/tiankanghui/ViCuR?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/tiankanghui/ViCuR) | 1 | OPD |
| [arXiv 2026: Visual-Advantage On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2605.21924) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding](https://arxiv.org/abs/2606.00564) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [KEPO: KEPO — Knowledge-Enhanced Preference Optimization (Medical VQA)](https://arxiv.org/abs/2602.00400) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/Corleno/KEPO?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/Corleno/KEPO) | 0 | OPD |
| [arXiv 2026: DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](https://arxiv.org/abs/2605.15532) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization](https://arxiv.org/abs/2606.09091) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/OPPO-Mente-Lab/GNDPO?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/OPPO-Mente-Lab/GNDPO) | 0 | OPD |
| [arXiv 2026: Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts](https://arxiv.org/abs/2606.10334) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization](https://arxiv.org/abs/2606.07000) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/XszNeverSleep/PTD-PO?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/XszNeverSleep/PTD-PO) | 0 | OPD |
| [arXiv 2026: Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation](https://arxiv.org/abs/2606.08719) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation](https://arxiv.org/abs/2606.06076) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| 🔎 [Beta-KD: β-KD — Uncertainty-Aware Knowledge Distillation for Multimodal LLMs](https://arxiv.org/abs/2603.21426) | CVPR 2026 | [![Stars](https://img.shields.io/github/stars/Jingchensun/beta-kd?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/Jingchensun/beta-kd) | 0 | 相关·非OPD(离线KD) |

<details>
<summary><b>ICLR 2026 · 旗舰 VLM</b> — VOLD — LLM→VLM OPD</summary>

`ICLR 2026` · [arXiv](https://arxiv.org/abs/2510.23497) · 被引 `10`

- **① 问题与重要性**：把纯文本 LLM 的推理能力迁移到 VLM 很难。这是 VLM OPD 的旗舰配方。
- **② 方法与独特贡献**：冷启动 SFT 对齐 + 统一 RL+KD：GRPO + 在策略 KL 蒸馏，文本 LLM 为师。
- **③ 任务 / 数据集 / 模型**：LLM→VLM 视觉推理，学生 rollout。
- **④ 局限与未来工作**：仓库占位、复现待完善。未来：更多模态与更大 VLM。

</details>

<details>
<summary><b>统一配方</b> — Uni-OPD — Unified OPD across LLMs & MLLMs</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.03677) · [code](https://github.com/WenjinHou/Uni-OPD) · 被引 `5`

- **① 问题与重要性**：OPD 在 LLM 与 MLLM 间缺乏统一配方，且存在学生状态探索不足、教师监督不可靠两大痛点。统一很有价值。
- **② 方法与独特贡献**：双视角配方：用数据平衡解决信息丰富学生状态探索不足，用边际校准恢复正确/错误轨迹的序一致性以解决教师监督不可靠；支持强到弱与跨模态、单/多教师。
- **③ 任务 / 数据集 / 模型**：5 个领域 / 16 个基准的 LLM 与 MLLM，学生 rollout。
- **④ 局限与未来工作**：配方较重、需调多组件。未来：自动化双视角调度。

</details>

<details>
<summary><b>arXiv 2026</b> — Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.18740) · [code](https://github.com/VisionOPD/Vision-OPD) · 被引 `2`

- **① 问题与重要性**：多模态LLM在细粒度视觉理解上仍困难，答案常依赖全图中微小但决定性的证据；作者观察到”区域到全局感知差距”：同一MLLM在证据中心裁剪图上比全图更准确，说明许多失败源于难以聚焦相关证据而非局部识别能力不足。
- **② 方法与独特贡献**：作者提出Vision-OPD，一个区域到全局的自蒸馏框架：从同一MLLM实例化裁剪图条件的teacher与全图条件的student，student生成on-policy rollout，最小化师生沿这些rollout的token级下一词分布散度，使模型内化视觉放大的好处，且无需外部教师、真值标签、奖励验证器或推理时工具。
- **③ 任务 / 数据集 / 模型**：面向多模态LLM的细粒度视觉理解任务（摘要被截断，具体数据集与基础MLLM详见原文，代码已开源VisionOPD/Vision-OPD）。
- **④ 局限与未来工作**：裁剪证据的获取方式与质量依赖、在无明确局部证据的任务上的适用性、以及对不同MLLM骨干的泛化性是潜在局限。

</details>

<details>
<summary><b>arXiv 2026</b> — Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2604.28123) · [code](https://github.com/XIAO4579/PRISM) · 被引 `2`

- **① 问题与重要性**：大型多模态模型标准后训练(SFT后RLVR)中SFT引入分布漂移，既不保留原能力也不忠实匹配监督分布，且多模态下感知与推理失败的漂移模式不同会在RL中复合，缓解此漂移很重要。
- **② 方法与独特贡献**：作者提出PRISM三阶段流程，在SFT和RLVR之间插入显式分布对齐阶段，基于OPD思想把对齐建模为策略与MoE判别器(含感知与推理专家)之间的黑盒响应级对抗博弈，无需教师logits即可提供解耦纠正信号。
- **③ 任务 / 数据集 / 模型**：面向多模态推理任务，使用1.26M公开演示做SFT初始化，对齐阶段需更高保真监督；具体模型和基准详见原文(摘要被截断)。
- **④ 局限与未来工作**：高保真对齐监督的获取成本较高；未来可降低判别器复杂度并扩展到更多多模态任务。

</details>

<details>
<summary><b>arXiv 2026</b> — ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.05718) · [code](https://github.com/tiankanghui/ViCuR) · 被引 `1`

- **① 问题与重要性**：多模态在线策略蒸馏中常用答案侧特权教师，但答案侧特权造成训练-测试不匹配，诱导学生走捷径模仿而非真正的视觉接地推理，解决这一问题对可靠的多模态推理很重要。
- **② 方法与独特贡献**：作者提出ViCuR，用视觉线索(输入中与问题相关的证据)替代答案侧特权，并引入轻量的线索恢复模块，通过专用sink-token交叉注意力在prefill阶段聚合任务相关视觉证据，不改变推理接口也无需额外的线索生成损失。
- **③ 任务 / 数据集 / 模型**：在七个基准上用Qwen3-VL-2B和8B作为学生进行多模态推理实验，ViCuR持续带来改进。
- **④ 局限与未来工作**：线索恢复模块依赖训练时可标注的视觉证据，摘要未充分说明其对噪声线索的鲁棒性；未来可扩展到更多模态和更复杂的视觉推理场景。

</details>

<details>
<summary><b>arXiv 2026</b> — Visual-Advantage On-Policy Distillation for Vision-Language Models</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.21924) · 被引 `0`

- **① 问题与重要性**：针对On-Policy蒸馏在视觉语言模型(VLM)上应用不足的问题：标准OPD虽能提升学生输出质量，却未能增强其对视觉输入的依赖，在视觉关键token上学生预测几乎不随细粒度视觉细节变化。
- **② 方法与独特贡献**：作者提出视觉优势(VA)概念——教师在有/无细粒度视觉细节下对学生rollout打分的token级log概率差，发现VA集中于少数携带视觉监督信号的token，并据此提出VA-OPD，在rollout级和token级两个粒度上区别对待这些高VA token。
- **③ 任务 / 数据集 / 模型**：面向视觉语言/VQA类任务，采用rollout级按轨迹平均VA重加权和token级KL方法，具体数据集与VLM型号摘要未明确，详见原文。
- **④ 局限与未来工作**：VA依赖教师对视觉细节的敏感性，方法在更细粒度视觉任务、不同VLM架构及视觉幻觉缓解上的泛化性仍待进一步验证。

</details>

<details>
<summary><b>arXiv 2026</b> — Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.00564) · 被引 `0`

- **① 问题与重要性**：本文研究多模态领域on-policy蒸馏的优化动力学这一欠探索问题，挑战将VLM蒸馏视为单一整体目标的标准做法。
- **② 方法与独特贡献**：作者将蒸馏损失数学分解为语言先验和视觉grounding两部分，发现二者梯度近乎正交，提出Visual Gradient Steering（VGS），动态重定向更新向量以优先视觉子空间。
- **③ 任务 / 数据集 / 模型**：在多个蒸馏设置和复杂多模态benchmark上实验（摘要未给出具体数据集与模型名），训练小型推理VLM，VGS显著优于标准整体式on-policy蒸馏。
- **④ 局限与未来工作**：梯度正交性假设和视觉为主要瓶颈的判断可能依任务而异；未来可扩展到更多模态、更大模型并自适应平衡语言与视觉子空间。

</details>

<details>
<summary><b>KEPO</b> — KEPO — Knowledge-Enhanced Preference Optimization (Medical VQA)</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2602.00400) · [code](https://github.com/Corleno/KEPO) · 被引 `0`

- **① 问题与重要性**：医疗 VQA 中可验证奖励稀疏、探索易坍缩，单纯 RL 难以稳定提升，而医疗场景对正确性与知识接地要求极高。
- **② 方法与独特贡献**：提出知识增强偏好优化(KEPO)：用质量门控的在策略蒸馏，只对高质量轨迹施加密集教师指导，并用教师知识做 hint-aware 探索，缓解探索坍缩。
- **③ 任务 / 数据集 / 模型**：医疗视觉问答(Medical VQA)为明确应用场景；具体数据集/模型详见原文。
- **④ 局限与未来工作**：偏 OPD+RL 半严格形态，依赖可靠的质量门控与教师知识库；未来可扩展到更广医疗多模态任务与更严格的逐 token 监督。

</details>

<details>
<summary><b>arXiv 2026</b> — DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.15532) · 被引 `0`

- **① 问题与重要性**：蒸馏可让紧凑VLM获得强推理能力，但驱动蒸馏的prompt通常靠简单启发式选取，作者发现标准图表/文档推理数据集中高达69%的prompt是”零delta”——师生已诱导出完全相同的答案分布，提供极少学习信号，使student随数据规模快速饱和。
- **② 方法与独特贡献**：作者回归第一性原理——蒸馏本质是最小化分布散度，故prompt只有暴露师生功能能力差距才有价值——用答案散度(Δ)量化该差距，并提出分阶段合成流水线，以现有数据集为种子、主动针对student失败模式生成更优prompt，构建20万规模的DeltaPrompts数据集。
- **③ 任务 / 数据集 / 模型**：在图表/文档推理(多模态VLM)任务上实验，针对紧凑VLM做蒸馏（摘要被截断，具体模型名详见原文）。
- **④ 局限与未来工作**：该工作侧重prompt选择而非on-policy蒸馏机制本身；Δ估计的计算成本、在其他多模态任务上的迁移性、以及合成数据多样性的上限是潜在局限。

</details>

<details>
<summary><b>arXiv 2026</b> — Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.09091) · [code](https://github.com/OPPO-Mente-Lab/GNDPO) · 被引 `0`

- **① 问题与重要性**：在线策略蒸馏作为后训练范式优于依赖稀疏结果反馈的RLVR，但朴素token级蒸馏会因离群状态的幅度失配导致梯度不稳定。
- **② 方法与独特贡献**：作者提出GNDPO(全局归一化蒸馏策略优化)，把原始KL分数转换为批级相对优势，从而缓解梯度爆炸并保留token级引导的好处。
- **③ 任务 / 数据集 / 模型**：在多模态推理任务上实验，GNDPO显著提升训练鲁棒性和下游性能。
- **④ 局限与未来工作**：全局归一化为实用稳定化手段，对极端分布或更长轨迹的效果未充分讨论；未来可推广到更多模态任务和不同教师-学生设置。

</details>

<details>
<summary><b>arXiv 2026</b> — Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.10334) · 被引 `0`

- **① 问题与重要性**：生成可视化产物(图表、网页、幻灯片)的代码大模型在观察渲染前就提交代码，常产生元素重叠、文字裁切、对齐错乱、对比度低、溢出等视觉缺陷，缺乏对渲染反馈的利用。
- **② 方法与独特贡献**：作者提出Visual-SDPO自蒸馏策略优化框架，把渲染后的视觉反馈作为权重共享教师的特权上下文蒸馏给编码学生，并引入视觉接地代码信用加权将每个缺陷溯源到责任代码语句以增强其蒸馏信号，同时用序列级GRPO项奖励可执行且视觉高质量的rollout。
- **③ 任务 / 数据集 / 模型**：面向代码生成可视化产物任务(图表/网页/幻灯片),摘要未明确具体数据集和模型，详见原文。
- **④ 局限与未来工作**：缺陷溯源依赖可检测的视觉缺陷与代码元素对应，复杂或语义性缺陷的检测可能受限；未来可扩展缺陷检测器和更丰富的视觉产物类型。

</details>

<details>
<summary><b>arXiv 2026</b> — Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.07000) · [code](https://github.com/XszNeverSleep/PTD-PO) · 被引 `0`

- **① 问题与重要性**：RLVR下可验证奖励稀疏，对失败rollout几乎无token级监督，导致复杂多模态推理探索低效，而外部教师蒸馏开销大、答案条件调优又会泄露答案诱发捷径生成。
- **② 方法与独特贡献**：作者提出PTD-PO，从空间注意力引导和中间文本推理步骤构造结构化特权提示，通过上下文学习产生逐步token分布监督，学生仍在原始无答案上下文中优化，其失败rollout与提示增强参考对齐，实现密集引导且不暴露答案。
- **③ 任务 / 数据集 / 模型**：针对大型视觉语言模型(LVLM)的多模态推理任务，摘要未明确具体数据集和模型，详见原文。
- **④ 局限与未来工作**：特权提示的构造质量影响监督效果，对提示噪声的鲁棒性未充分讨论；未来可推广到更多模态推理场景和不同提示来源。

</details>

<details>
<summary><b>arXiv 2026</b> — Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.08719) · 被引 `0`

- **① 问题与重要性**：‘看图思考’范式通过放大区域、对裁剪图推理获取局部证据，但带来冗余工具调用和更长推理轨迹，且仅靠结果奖励学到的中间裁剪可能噪声大、不忠实于任务相关证据。
- **② 方法与独特贡献**：作者提出Imagine-OPD在线策略自蒸馏框架，训练时教师扮演‘看图思考’推理者、接收源自标注区域的特权放大证据视图，监督模型自身的‘想象’推理轨迹，使模型内化‘在哪看、想象会看到什么’而无需真正调用工具，且不需外部教师或高质量想象示范。
- **③ 任务 / 数据集 / 模型**：面向细粒度视觉推理任务，摘要未明确具体数据集和模型，详见原文。
- **④ 局限与未来工作**：想象监督依赖训练时可用的区域标注，对无标注场景的扩展性未明；未来可减少对区域标注的依赖并验证想象证据的忠实度。

</details>

<details>
<summary><b>arXiv 2026</b> — Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.06076) · 被引 `0`

- **① 问题与重要性**：视觉语言模型在视觉空间规划上表现欠佳，根源在于感知-推理间的模态鸿沟(需从像素推断潜在状态再据此推理出有效动作)，弥合该鸿沟对可靠的视觉规划很重要。
- **② 方法与独特贡献**：作者提出MGSD两阶段模态鸿沟感知自蒸馏框架：先用冷启动接地阶段让视觉学生获得可靠状态表征，再用特权教师借助显式符号状态监督学生自身视觉rollout前缀以在线策略蒸馏方式传递规划能力，符号数据仅用于训练、推理纯视觉。
- **③ 任务 / 数据集 / 模型**：在视觉规划基准上，用4B和8B骨干分别将宏平均提升19.3%和18.4%。
- **④ 局限与未来工作**：方法依赖训练时可用的符号状态标注，获取成本可能较高；未来可降低对符号标注的依赖并推广到更长视野的规划任务。

</details>

<details>
<summary><b>🔎 Beta-KD</b> — β-KD — Uncertainty-Aware Knowledge Distillation for Multimodal LLMs</summary>

`CVPR 2026` · [arXiv](https://arxiv.org/abs/2603.21426) · [code](https://github.com/Jingchensun/beta-kd) · 被引 `0` · `相关·非OPD(离线KD)`

- **① 问题与重要性**：多模态大模型蒸馏中学生应多大程度信任教师并不确定，统一权重会让噪声/不可靠教师信号污染学生，自适应加权对 VLM 蒸馏很关键。
- **② 方法与独特贡献**：提出不确定性感知的 β-KD：把教师信号建模为学生激活上的 Gibbs 先验，用摊销优化联合推断激活与加权参数，得到闭式的不确定性感知加权。
- **③ 任务 / 数据集 / 模型**：多模态 VQA 基准：从 MobileVLM-7B 蒸馏 1.7B 学生，扩大迁移集后在 6 个多模态基准上最优配置平均最高 +2.0 分。
- **④ 局限与未来工作**：为离线 KD（非学生自采样 on-policy rollout），可作 VQA 蒸馏的强相关基线；未来可把该不确定性加权迁入在策略 OPD 框架。

</details>


## 🎬 视频 / VideoQA / 时序定位 OPD

面向视频问答、视频推理与时序定位的 OPD / 自蒸馏工作，以及强相关的 AoTD、VITAL。

| 论文 | 时间/会议 | 🌟 | 被引 | 严格 |
| :-- | :--: | :--: | :--: | :--: |
| 🔎 [VITAL: VITAL / Thinking With Videos — Multimodal Tool-Augmented RL for Long Video Reasoning](https://arxiv.org/abs/2508.04416) | arXiv 2025.08 | `📄 paper-only` | 66 | 含OPD·主体为RL |
| 🔎 [AoTD: AoTD — Enhancing Video-LLM Reasoning via Agent-of-Thoughts Distillation](https://arxiv.org/abs/2412.01694) | CVPR 2025 | [![Stars](https://img.shields.io/github/stars/zhengrongz/AoTD?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/zhengrongz/AoTD) | 34 | 相关·非严格OPD |
| [视频定位: Video-OPD](https://arxiv.org/abs/2602.02994) | arXiv 2026 | `📄 paper-only` | 8 | OPD |
| [arXiv 2026: VISD: Enhancing Video Reasoning via Structured Self-Distillation](https://arxiv.org/abs/2605.06094) | arXiv 2026 | `📄 paper-only` | 3 | OPD |
| [arXiv 2026: InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning](https://arxiv.org/abs/2606.12195) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: World Model Self-Distillation: Training World Models to Solve General Tasks](https://arxiv.org/abs/2606.12072) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning](https://arxiv.org/abs/2606.03603) | arXiv 2026 | `📄 paper-only` | 0 | OPD |

<details>
<summary><b>🔎 VITAL</b> — VITAL / Thinking With Videos — Multimodal Tool-Augmented RL for Long Video Reasoning</summary>

`arXiv 2025.08` · [arXiv](https://arxiv.org/abs/2508.04416) · 被引 `66` · `含OPD·主体为RL`

- **① 问题与重要性**：MLLM 的视频推理对 VideoQA 与时序定位至关重要，但纯文本 CoT 跨模态交互弱、长视频/长链时易幻觉。
- **② 方法与独特贡献**：提出端到端智能体框架 VITAL，配视觉工具箱可按需密集采样视频帧并生成多模态 CoT；构建 MTVR-CoT-72k(SFT) 与 MTVR-RL-110k(RL) 数据集，提出难度感知 DGRPO；分阶段训练含持续预训练、SFT、规则RL 与在策略蒸馏。
- **③ 任务 / 数据集 / 模型**：长视频理解，在 11 个视频理解基准上的 VideoQA 与时序定位均超越现有方法，尤其长视频场景。
- **④ 局限与未来工作**：是融合 RL 的复杂系统、OPD 仅为其中一环，单独 OPD 贡献不易拆分；未来可消融在策略蒸馏的独立增益。

</details>

<details>
<summary><b>🔎 AoTD</b> — AoTD — Enhancing Video-LLM Reasoning via Agent-of-Thoughts Distillation</summary>

`CVPR 2025` · [arXiv](https://arxiv.org/abs/2412.01694) · [code](https://github.com/zhengrongz/AoTD) · 被引 `34` · `相关·非严格OPD`

- **① 问题与重要性**：Video-LLM 在 VideoQA 上虽榜单分高，却缺乏可解释性与时空定位能力，难以做多步时空推理。
- **② 方法与独特贡献**：提出 Agent-of-Thoughts Distillation：用智能体系统把复杂问题分解为子任务、调用专用视觉模型，把中间结果作为思维链(CoT)，再用 LLM 验证可靠性后蒸馏进指令微调。
- **③ 任务 / 数据集 / 模型**：视频问答(VideoQA)，在多项选择与开放式 Video-LLM 基准上验证，提升明显。
- **④ 局限与未来工作**：CoT 由智能体离线生成并经指令微调注入，属离线 CoT 蒸馏而非严格在策略 teacher-token KL；未来可与在策略 rollout 监督结合。

</details>

<details>
<summary><b>视频定位</b> — Video-OPD</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2602.02994) · 被引 `8`

- **① 问题与重要性**：视频时序定位需要强推理，多模态 OPD 稀缺。把 OPD 引入视频有价值。
- **② 方法与独特贡献**：在学生 rollout 上做 token 级 KL，LLM 教师，做时序视频定位。
- **③ 任务 / 数据集 / 模型**：视频时序定位（MLLM 学生），学生 rollout。
- **④ 局限与未来工作**：视频域特定。未来：长视频与多事件。

</details>

<details>
<summary><b>arXiv 2026</b> — VISD: Enhancing Video Reasoning via Structured Self-Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.06094) · 被引 `3`

- **① 问题与重要性**：训练VideoLLM做复杂推理受序列级奖励稀疏和长时序推理轨迹缺乏细粒度信用分配之困，RLVR监督可靠但无法捕获token级贡献，改进视频推理监督很重要。
- **② 方法与独特贡献**：作者提出结构化自蒸馏框架VISD，用视频感知判别模型把推理质量分解为答案正确性、逻辑一致性、时空接地等多维特权信息并指导教师策略提供token级监督，并用方向-幅度解耦机制(奖励算优势定方向、结构化特权信号调幅度)稳定融合密集监督与RL。
- **③ 任务 / 数据集 / 模型**：面向视频推理任务，使用VideoLLM；具体数据集详见原文(摘要被截断)。
- **④ 局限与未来工作**：依赖视频感知判别模型的质量与多维分解设计；未来可扩展到更多视频理解任务和更高效的判别器。

</details>

<details>
<summary><b>arXiv 2026</b> — InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.12195) · 被引 `0`

- **① 问题与重要性**：基础模型正转向涉及多步推理与工具使用的智能体行为，但开源工作多聚焦文本主导设置，长视野多模态(尤其视频)任务探索不足。
- **② 方法与独特贡献**：作者提出InternVideo3，通过多模态上下文推理(MCR)把长视频理解建模为在共享演化上下文上的闭环证据累积与验证，并引入M²LA(多模态多头潜在注意力)压缩KV-cache同时保留完整token流，训练分阶段包含持续预训练、短到长SFT、规则强化学习和在线策略蒸馏。
- **③ 任务 / 数据集 / 模型**：在Video-MME、MLVU、EgoSchema等视频理解基准上实验，取得强性能，并实例化为视频智能体。
- **④ 局限与未来工作**：在线策略蒸馏只是其多阶段训练的一环，摘要未单独分析其贡献；作为工业级系统，组件较多、训练成本高，未来可精简流程并扩展更多视频智能体能力。

</details>

<details>
<summary><b>arXiv 2026</b> — World Model Self-Distillation: Training World Models to Solve General Tasks</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.12072) · 被引 `0`

- **① 问题与重要性**：预训练视频生成器是有前景的视觉世界模型并展现新兴任务求解能力，但依赖详细文本描述限制了其直接用于规划与决策，而监督微调需昂贵难扩展的配对任务-执行视频。
- **② 方法与独特贡献**：作者提出可扩展框架结合自蒸馏与强化学习：用VLM从无标注场景图像生成候选任务和分步解，该解条件化预训练视频扩散模型(演示者),再把其行为蒸馏进仅以图像和短任务提示为条件的执行者，并用VLM反馈的强化学习进一步改进执行者。
- **③ 任务 / 数据集 / 模型**：面向世界模型/视频生成的通用任务求解，输入为无标注场景图像，摘要未明确具体数据集，详见原文。
- **④ 局限与未来工作**：方法依赖VLM生成任务与判断质量，可能引入VLM偏差；未来可提升任务生成质量并扩展到更复杂的真实决策场景。

</details>

<details>
<summary><b>arXiv 2026</b> — World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.03603) · 被引 `0`

- **① 问题与重要性**：本文研究世界模型与多模态LLM在从静态视觉观察预测未来上的互补性，关键挑战是判断何时该用视觉模拟、rollout是否可信、以及如何影响最终答案。
- **② 方法与独特贡献**：作者将其形式化为controlled concrete reasoning，提出Privileged-Future On-Policy Self-Distillation（PF-OPSD）：训练时用ground-truth未来视频和答案仅作教师侧特权上下文来评估on-policy具体推理轨迹，可部署的学生测试时不观察真实未来。
- **③ 任务 / 数据集 / 模型**：构建两个人工验证基准VRQABench（可控空间lookahead）和OpenWorldQA（开放域物理预测）评测（摘要未给出具体模型名）。
- **④ 局限与未来工作**：依赖ground-truth未来视频作特权信息，获取成本高且任务限于这两个基准；未来可扩展到更多物理预测场景并减少对真实未来标注的依赖。

</details>


## 🎨 图像 / 视频生成（扩散 · 流匹配）OPD

把 OPD / 自蒸馏用于扩散与流匹配生成模型（少步生成、轨迹自蒸馏、对抗蒸馏等）。

| 论文 | 时间/会议 | 🌟 | 被引 | 严格 |
| :-- | :--: | :--: | :--: | :--: |
| [ICLR 2026 · 扩散: π-Flow — Image / Flow OPD](https://arxiv.org/abs/2510.14974) | ICLR 2026 | [![Stars](https://img.shields.io/github/stars/Lakonik/piFlow?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/Lakonik/piFlow) | 18 | OPD |
| [arXiv 2025: Di$\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator](https://arxiv.org/abs/2503.15457) | arXiv 2025 | `📄 paper-only` | 5 | OPD |
| [arXiv.org: LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation](https://arxiv.org/abs/2512.23576) | arXiv.org | `📄 paper-only` | 5 | OPD |
| [arXiv 2026: Flow-OPD: On-Policy Distillation for Flow Matching Models](https://arxiv.org/abs/2605.08063) | arXiv 2026 | `📄 paper-only` | 3 | OPD |
| [arXiv 2026: D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](https://arxiv.org/abs/2605.05204) | arXiv 2026 | `📄 paper-only` | 3 | OPD |
| [arXiv 2026: DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models](https://arxiv.org/abs/2605.15055) | arXiv 2026 | `📄 paper-only` | 1 | OPD |
| [arXiv 2026: AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724) | arXiv 2026 | `📄 paper-only` | 1 | OPD |
| [arXiv 2026: TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM](https://arxiv.org/abs/2605.09536) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/BHmingyang/TAD?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/BHmingyang/TAD) | 0 | OPD |
| [arXiv 2026: GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models](https://arxiv.org/abs/2605.29398) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [CollectionLoRA: CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2605.25378) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: Adversarial Dual On-Policy Distillation from Expressive Teacher](https://arxiv.org/abs/2605.27095) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: Knowledge Distillation for Visual Autoregressive Models](https://arxiv.org/abs/2606.06078) | arXiv 2026 | `📄 paper-only` | 0 | OPD |

<details>
<summary><b>ICLR 2026 · 扩散</b> — π-Flow — Image / Flow OPD</summary>

`ICLR 2026` · [arXiv](https://arxiv.org/abs/2510.14974) · [code](https://github.com/Lakonik/piFlow) · 被引 `18`

- **① 问题与重要性**：流/扩散模型多步采样慢，蒸馏常脱离学生自身轨迹。扩散上的严格 OPD 有价值。
- **② 方法与独特贡献**：学生沿自身轨迹在每个时间步预测策略，用教师速度场做 L2 模仿蒸馏（扩散版严格 OPD）。
- **③ 任务 / 数据集 / 模型**：图像生成（流模型），学生轨迹。
- **④ 局限与未来工作**：限于流/扩散框架。未来：更少步数、文本到图像更广基准。

</details>

<details>
<summary><b>arXiv 2025</b> — Di$\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator</summary>

`arXiv 2025` · [arXiv](https://arxiv.org/abs/2503.15457) · 被引 `5`

- **① 问题与重要性**：论文要解决掩码扩散模型（MDM）推理需多步、速度慢的问题。
- **② 方法与独特贡献**：作者提出Di[M]O，将MDM蒸馏为一步生成器：用辅助模型的on-policy框架做token级分布匹配优化输出logits，并用token初始化策略注入随机性以解决初始分布缺乏熵的问题。
- **③ 任务 / 数据集 / 模型**：在类别条件和文本条件图像生成任务上实验，达到与多步教师可比的性能且大幅降低推理时间；摘要未给出具体数据集名，首次实现MDM一步蒸馏与离散文生图蒸馏。
- **④ 局限与未来工作**：局限在于聚焦图像生成；未来可推广到更多模态和更高分辨率生成。

</details>

<details>
<summary><b>arXiv.org</b> — LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation</summary>

`arXiv.org` · [arXiv](https://arxiv.org/abs/2512.23576) · 被引 `5`

- **① 问题与重要性**：扩散模型的实时视频生成对构建通用多模态交互AI系统至关重要，但其双向注意力下对所有帧的迭代去噪阻碍了实时交互，且现有蒸馏方法多聚焦文本到视频、人机交互不自然。
- **② 方法与独特贡献**：作者针对多模态上下文（文本、图像、音频）条件下的实时交互视频扩散，发现领先的on-policy蒸馏方法Self Forcing在多模态条件下出现闪烁、黑帧、质量退化等问题，提出改进的蒸馏配方，强调条件输入质量以及on-policy优化的初始化与调度。
- **③ 任务 / 数据集 / 模型**：在多模态条件（音频、图像、文本）的虚拟人视频生成任务上实验，使用HDTF、AVSpeech和CelebV-HQ基准，详见原文。
- **④ 局限与未来工作**：方法聚焦于虚拟人/avatar视频，在更开放场景或更长时序生成的稳定性仍待验证，未来可扩展到更通用的实时多模态生成。

</details>

<details>
<summary><b>arXiv 2026</b> — Flow-OPD: On-Policy Distillation for Flow Matching Models</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.08063) · 被引 `3`

- **① 问题与重要性**：现有Flow Matching文本生图模型在多任务对齐下面临标量奖励稀疏和异构目标联合优化的梯度干扰，产生指标'跷跷板效应'与奖励作弊问题。
- **② 方法与独特贡献**：提出Flow-OPD，首个将on-policy蒸馏整合进Flow Matching的统一后训练框架：先用单奖励GRPO培养领域专家教师，再经Flow冷启动建立初始策略，通过on-policy采样、任务路由标注与密集轨迹监督将异构专长整合进单一学生，并引入Manifold Anchor Regularization锚定。
- **③ 任务 / 数据集 / 模型**：在文本生图（多任务对齐）任务上实验；摘要未明确具体数据集与模型名称，详见原文。
- **④ 局限与未来工作**：两阶段流程依赖多个专家教师训练，成本较高且对任务路由准确性敏感；未来可扩展到更多生成模态与更高效的专家整合方式。

</details>

<details>
<summary><b>arXiv 2026</b> — D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.05204) · 被引 `3`

- **① 问题与重要性**：高性能图像生成正从低效多步模型转向高效少步模型(如Z-Image-Turbo、FLUX.2-klein)，但这些模型直接连续SFT会损害其少步推理能力，解决持续微调很重要。
- **② 方法与独特贡献**：作者提出D-OPSD，利用现代扩散模型(LLM/VLM作编码器)继承的上下文能力，把训练表述为on-policy自蒸馏：同一模型兼任师生，学生仅条件于文本特征、教师条件于文本+目标图像的多模态特征，在学生自身rollout上最小化两预测分布。
- **③ 任务 / 数据集 / 模型**：面向步蒸馏扩散模型的图像生成微调任务，涉及Z-Image-Turbo、FLUX.2-klein等少步模型；具体基准详见原文(摘要被截断)。
- **④ 局限与未来工作**：方法依赖编码器的多模态上下文能力，适用范围受模型架构限制；未来可推广到更多少步生成模型与任务。

</details>

<details>
<summary><b>arXiv 2026</b> — DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.15055) · 被引 `1`

- **① 问题与重要性**：RL虽能改进扩散文生图模型，但现有方法多限于单任务优化；扩展到多任务时联合优化存在跨任务干扰与不均衡，级联RL又繁琐且易灾难性遗忘。
- **② 方法与独特贡献**：作者提出DiffusionOPD，先独立训练任务专属教师再沿student自身rollout轨迹蒸馏进统一student，解耦单任务探索与多任务整合；理论上把OPD从离散token提升到连续状态马尔可夫过程，导出统一SDE与ODE的闭式逐步KL目标，并证明该解析梯度比PPO式策略梯度方差更低、泛化更好。
- **③ 任务 / 数据集 / 模型**：面向扩散文生图(text-to-image)的多任务训练（摘要被截断，具体数据集与基础模型详见原文）。
- **④ 局限与未来工作**：方法需先训练多个任务专属教师，教师质量与数量对最终student的影响、以及在更多任务与更大模型上的扩展性是潜在局限。

</details>

<details>
<summary><b>arXiv 2026</b> — AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.13724) · 被引 `1`

- **① 问题与重要性**：少步视频生成靠一致性蒸馏取得进展，但一致性蒸馏模型在测试时分配更多采样步反而性能下降，限制了”任意步”视频扩散，根因是一致性采样轨迹替换了原始概率流ODE轨迹、削弱了测试时缩放行为。
- **② 方法与独特贡献**：作者提出AnyFlow，首个基于流图(flow map)的任意步视频扩散蒸馏框架，把蒸馏目标从端点一致性映射改为任意时间区间的流图转移学习，并提出”流图反向模拟”将完整Euler rollout分解为捷径流图转移，实现高效on-policy蒸馏以减少测试时离散化误差与暴露偏差。
- **③ 任务 / 数据集 / 模型**：面向少步/任意步视频扩散生成任务（摘要未给出具体数据集与基础模型名，详见原文）。
- **④ 局限与未来工作**：摘要未给出定量结果，方法在不同视频骨干、更高分辨率与更长视频上的表现及训练成本仍待评估。

</details>

<details>
<summary><b>arXiv 2026</b> — TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.09536) · [code](https://github.com/BHmingyang/TAD) · 被引 `0`

- **① 问题与重要性**：扩散大语言模型（dLLM）提供并行文本生成潜力，但面临准确性-并行性权衡，增加每次前向token数（TPF）常降低生成质量，现有加速方法多以牺牲准确换速度。
- **② 方法与独特贡献**：提出TAD（时序感知轨迹自蒸馏）：教师以prompt和真值响应为条件生成解码轨迹并记录中间掩码状态，按距揭示的剩余步数将掩码位置分为近/远子集，近token用硬交叉熵、远token用软KL监督，自然形成时序感知划分与两种部署配置。
- **③ 任务 / 数据集 / 模型**：在扩散大语言模型并行文本生成任务上实验；摘要未明确具体数据集与基座，详见原文（仓库BHmingyang/TAD）。
- **④ 局限与未来工作**：依赖真值条件下教师轨迹构建，近/远划分阈值需设定，对未见分布的泛化待验证；未来可扩展到更多dLLM与更长生成任务。

</details>

<details>
<summary><b>arXiv 2026</b> — GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.29398) · 被引 `0`

- **① 问题与重要性**：针对RL可改进扩散大语言模型(dLLM)的去噪器策略，但策略似然不可解，主流用ELBO替代似然却因训练-推理失配引入偏差、损害性能的问题。
- **② 方法与独特贡献**：作者提出引导去噪器自蒸馏(GDSD)，直接从优势引导的自教师(由反向KL正则化RL的闭式最优解导出)蒸馏dLLM去噪器，用无归一化目标匹配去噪器logit到教师，将RL化为无似然自蒸馏从而绕过训练-推理失配偏差，并指出近期ELBO方法是其在不同蒸馏散度下的特例。
- **③ 任务 / 数据集 / 模型**：在规划、数学、代码基准上、用LLaDA-8B和Dream-7B评测，GDSD一致优于先前最先进方法。
- **④ 局限与未来工作**：方法针对扩散语言模型这一特定范式，其在更大dLLM、更多任务及与自回归模型RL对比上的优势与可扩展性仍待进一步验证。

</details>

<details>
<summary><b>CollectionLoRA</b> — CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.25378) · 被引 `0`

- **① 问题与重要性**：针对定制化图像编辑中随着所需效果增多需存储和动态加载大量效果LoRA带来部署开销，且与加速模块级联会引发参数干扰、概念串扰和风格退化的问题。
- **② 方法与独特贡献**：作者提出CollectionLoRA，一种多教师On-Policy蒸馏框架，可将多达50个效果LoRA的概念连同少步生成能力蒸馏进单个LoRA，并引入概率双流路由、非对称正交提示、由粗到细蒸馏等机制解决特征干扰。
- **③ 任务 / 数据集 / 模型**：面向扩散模型的定制化图像编辑/视觉效果任务，将50种效果蒸馏入单LoRA，具体扩散模型与数据集摘要未完全展开，详见原文。
- **④ 局限与未来工作**：方法面向预设效果集合，对效果数量进一步扩展、未见效果组合及不同扩散骨干的泛化性与质量上限仍待检验。

</details>

<details>
<summary><b>arXiv 2026</b> — Adversarial Dual On-Policy Distillation from Expressive Teacher</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.27095) · 被引 `0`

- **① 问题与重要性**：针对具身控制中从示范学习常被建模为行为克隆，扩散/流匹配策略虽建模多模态专家动作但仍是离线监督学习者、在实际访问状态上得不到纠正信号，而标准OPD又假设存在不可得的强固定教师的问题。
- **② 方法与独特贡献**：作者提出FA-OPD，一种对抗式双On-Policy蒸馏方法：从示范学习流匹配(FM)教师并与轻量MLP学生协同训练，教师在学生rollout上提供奖励通道(专家相似性目标驱动在线探索)和动作通道(在学生访问状态提供密集局部目标稳定利用)两类互补信号。
- **③ 任务 / 数据集 / 模型**：面向具身控制/从示范学习的智能体任务，具体仿真环境与数据集摘要未完全展开，详见原文。
- **④ 局限与未来工作**：教师本身从有限示范学习而非强固定教师，其质量受示范覆盖限制，方法在真实机器人、长时序复杂任务及更高维动作空间的稳定性仍待验证。

</details>

<details>
<summary><b>arXiv 2026</b> — Knowledge Distillation for Visual Autoregressive Models</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.06078) · 被引 `0`

- **① 问题与重要性**：自回归图像生成模型表达力强但计算开销大，需要有效压缩，而知识蒸馏在视觉自回归生成中的行为尚未被充分研究。
- **② 方法与独特贡献**：作者首次系统研究AR图像模型的蒸馏策略，发现语言领域方法不能直接迁移(长解码视野和视觉token歧义使教师监督不可靠)，进而提出VarKD，在学生样本上蒸馏、选择性施加教师监督并降低token级歧义。
- **③ 任务 / 数据集 / 模型**：在ImageNet上跨多个AR骨干做图像生成实验，VarKD持续优于此前蒸馏基线，缩小与大规模模型的差距。
- **④ 局限与未来工作**：方法针对图像token歧义设计，跨其他生成模态(如视频)的适用性未验证；未来可扩展到更大规模或多模态自回归生成。

</details>


## 🔊 语音 / 音频 OPD

把文本推理跨模态迁入音频/语音、或在音频理解与 ASR 上做 OPD 的工作。

| 论文 | 时间/会议 | 🌟 | 被引 | 严格 |
| :-- | :--: | :--: | :--: | :--: |
| [arXiv.org: Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765) | arXiv.org | `📄 paper-only` | 316 | OPD |
| [Alibaba · 跨模态: Qwen3.5-Omni](https://arxiv.org/abs/2604.15804) | arXiv 2026 | `📄 paper-only` | 45 | OPD |
| [音频推理: Step-Audio-R1](https://arxiv.org/abs/2511.15848) | arXiv 2025 | [![Stars](https://img.shields.io/github/stars/stepfun-ai/Step-Audio-R1?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/stepfun-ai/Step-Audio-R1) | 28 | OPD |
| [语音 LLM: X-OPD — Speech LLM](https://arxiv.org/abs/2603.24596) | arXiv 2026 | `📄 paper-only` | 5 | OPD |
| [百度 Ernie: CORD — Reasoning: Text ➡️ Audio](https://arxiv.org/abs/2601.16547) | arXiv 2026 | `📄 paper-only` | 4 | OPD |
| [arXiv 2026: Data-Efficient On-Policy Distillation for Automatic Speech Recognition](https://arxiv.org/abs/2605.28139) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing](https://arxiv.org/abs/2606.15920) | arXiv 2026 | `📄 paper-only` | 0 | OPD |

<details>
<summary><b>arXiv.org</b> — Qwen3-Omni Technical Report</summary>

`arXiv.org` · [arXiv](https://arxiv.org/abs/2509.17765) · 被引 `316`

- **① 问题与重要性**：如何用单一多模态模型在文本、图像、音频、视频上同时达到SOTA且相对单模态版本无性能退化，是构建统一全模态大模型的重要问题。
- **② 方法与独特贡献**：作者提出Qwen3-Omni，采用Thinker-Talker MoE架构统一感知与生成，Talker用多码本方案自回归预测离散语音编码降低首包延迟，并用轻量因果ConvNet替代块状扩散实现流式合成。
- **③ 任务 / 数据集 / 模型**：在36个音频与音视频基准上实验，32个达开源SOTA、22个总体SOTA，超过Gemini-2.5-Pro、Seed-ASR、GPT-4o-Transcribe等闭源模型，支持119种语言文本交互。
- **④ 局限与未来工作**：作为综合技术报告，部分能力（如语音生成仅10种语言）覆盖范围有限，未来可扩展更多语言与更低延迟的实时交互。

</details>

<details>
<summary><b>Alibaba · 跨模态</b> — Qwen3.5-Omni</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2604.15804) · 被引 `45`

- **① 问题与重要性**：如何把文本推理迁移到音频输入推理？跨模态 OPD 对全模态模型重要。
- **② 方法与独特贡献**：跨模态在策略蒸馏：把文本推理能力迁入音频输入推理，Thinker-Talker + Hybrid Attention MoE。
- **③ 任务 / 数据集 / 模型**：音频/音视频：215 子任务 SOTA，256k 上下文，含 ARIA 流式稳定与 10 语种语音生成。
- **④ 局限与未来工作**：全模态系统复杂。未来：更低延迟流式与更多模态。

</details>

<details>
<summary><b>音频推理</b> — Step-Audio-R1</summary>

`arXiv 2025` · [arXiv](https://arxiv.org/abs/2511.15848) · [code](https://github.com/stepfun-ai/Step-Audio-R1) · 被引 `28`

- **① 问题与重要性**：音频推理模型缺乏自我提升机制。迭代自蒸馏用于音频有意义。
- **② 方法与独特贡献**：迭代自蒸馏 + SFT + PPO/RLVR，仅用音频相关问题做自蒸馏，模态接地的自我。
- **③ 任务 / 数据集 / 模型**：音频推理任务，学生 rollout。
- **④ 局限与未来工作**：音频域特定；迭代成本。未来：跨模态联合推理。

</details>

<details>
<summary><b>语音 LLM</b> — X-OPD — Speech LLM</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2603.24596) · 被引 `5`

- **① 问题与重要性**：语音 LLM 能力对齐难。跨模态把文本 LLM 能力迁入语音重要。
- **② 方法与独特贡献**：跨模态 token 级 KL，文本 LLM 为师，做语音 LLM 能力对齐。
- **③ 任务 / 数据集 / 模型**：语音 LLM 任务，学生 rollout。
- **④ 局限与未来工作**：语音域特定。未来：更多语种与下游语音任务。

</details>

<details>
<summary><b>百度 Ernie</b> — CORD — Reasoning: Text ➡️ Audio</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2601.16547) · 被引 `4`

- **① 问题与重要性**：文本推理能力难迁移到音频。跨模型推理对齐重要。
- **② 方法与独特贡献**：token 级反向 KL + 序列级 KL + GRPO，自身带文本，对齐跨模型推理。
- **③ 任务 / 数据集 / 模型**：文本→音频推理，学生 rollout。
- **④ 局限与未来工作**：对齐质量依赖文本端。未来：更广音频任务。

</details>

<details>
<summary><b>arXiv 2026</b> — Data-Efficient On-Policy Distillation for Automatic Speech Recognition</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.28139) · 被引 `0`

- **① 问题与重要性**：针对构建有竞争力的自动语音识别(ASR)模型通常需大规模音频监督、复现与专精成本高的问题，探究强教师能否通过On-Policy蒸馏迁移额外识别能力。
- **② 方法与独特贡献**：作者研究0.6B参数、用10万小时语音训练的音频条件语言模型Ark-ASR，采用On-Policy蒸馏让Qwen-ASR强教师在学生生成转写上提供监督，并用支持重叠诊断分析教师-学生局部兼容性。
- **③ 任务 / 数据集 / 模型**：在中英文ASR基准上，所提训练配方一致优于纯SFT，并在五个评测集中的四个上超过同规模Qwen3-ASR-0.6B基线，仅用10万小时语音(对比Qwen3-Omni AuT编码器报告的2000万小时)，更大的Qwen3-ASR-1.7B仍更强。
- **④ 局限与未来工作**：紧凑学生与更大教师间仍有差距，方法在更多语言、噪声/口音场景及更小音频预算下进一步缩小差距的潜力仍待探索。

</details>

<details>
<summary><b>arXiv 2026</b> — OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.15920) · 被引 `0`

- **① 问题与重要性**：多模态大模型的强化学习在复杂推理中常受奖励稀疏所困，在涉及状态、情绪、意图、行为的人本场景中尤为突出，高质量CoT标注昂贵难得，而直接用真值标签做SFT会诱发感知捷径且对安全关键的人机交互缺乏透明度。
- **② 方法与独特贡献**：作者提出OmniOPSD(理由特权在线策略自蒸馏),把前沿模型生成的证据感知理由仅作为训练时的教师侧特权证据上下文而非学生模仿目标，学生从原始多模态输入采样自身rollout，理由特权教师对相同token打分提供密集监督。
- **③ 任务 / 数据集 / 模型**：面向情感计算/人本多模态推理任务，摘要未明确具体数据集和模型，详见原文。
- **④ 局限与未来工作**：依赖前沿模型生成高质量理由，理由质量影响监督效果；未来可降低对前沿模型的依赖并扩展到更多人本多模态场景。

</details>


## ⚡ 多模态投机解码蒸馏

为视觉语言模型训练在策略草稿器以加速推理。

| 论文 | 时间/会议 | 🌟 | 被引 | 严格 |
| :-- | :--: | :--: | :--: | :--: |
| [arXiv.org: ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding](https://arxiv.org/abs/2509.15235) | arXiv.org | `📄 paper-only` | 14 | OPD |
| [arXiv.org: Speculative Decoding Reimagined for Multimodal Large Language Models](https://arxiv.org/abs/2505.14260) | arXiv.org | `📄 paper-only` | 6 | OPD |
| [arXiv.org: SpecVLM: Fast Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2509.11815) | arXiv.org | `📄 paper-only` | 4 | OPD |
| [多模态草稿: MASSV — Multimodal SD Draft](https://arxiv.org/abs/2505.10526) | arXiv 2025 | `📄 paper-only` | 0 | OPD |

<details>
<summary><b>arXiv.org</b> — ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding</summary>

`arXiv.org` · [arXiv](https://arxiv.org/abs/2509.15235) · 被引 `14`

- **① 问题与重要性**：投机解码在LLM上广泛应用，但在VLM上探索不足且现有方法加速比有限（小于1.5倍），随着多模态能力日益核心，弥补这一差距很重要。
- **② 方法与独特贡献**：作者提出视觉感知投机解码ViSpec，用轻量视觉适配器将图像token压缩为紧凑表示融入草稿模型注意力并保留位置信息，并为每张图提取全局特征向量增强后续文本token的多模态连贯性。
- **③ 任务 / 数据集 / 模型**：在视觉语言模型推理加速任务上实验，并通过改造现有数据集构建了含长助手回复的专用训练集，摘要未明确具体VLM名，详见原文。
- **④ 局限与未来工作**：依赖视觉token可被逐层有效过滤的假设，专用长回复数据集构建有一定成本，未来可扩展到视频及更多模态的草稿模型设计。

</details>

<details>
<summary><b>arXiv.org</b> — Speculative Decoding Reimagined for Multimodal Large Language Models</summary>

`arXiv.org` · [arXiv](https://arxiv.org/abs/2505.14260) · 被引 `6`

- **① 问题与重要性**：投机解码可加速LLM推理且不损精度，但现有方法应用于多模态大模型（MLLM）时无法获得同等加速比，如何为MLLM重新设计投机解码很重要。
- **② 方法与独特贡献**：作者提出多模态投机解码MSD，基于两条原则：文本与视觉token特性不同需在草稿阶段分开处理，以及草稿模型同时需要语言建模与视觉感知能力，并采用两阶段训练（先文本指令微调，再渐进引入多模态数据）。
- **③ 任务 / 数据集 / 模型**：在多模态大模型（MLLM）推理加速任务上实验，摘要未明确具体数据集与模型名，详见原文。
- **④ 局限与未来工作**：方法围绕草稿模型设计，两阶段训练与文本/视觉解耦可能增加训练复杂度，未来可探索更多模态及更通用的草稿架构。

</details>

<details>
<summary><b>arXiv.org</b> — SpecVLM: Fast Speculative Decoding in Vision-Language Models</summary>

`arXiv.org` · [arXiv](https://arxiv.org/abs/2509.11815) · 被引 `4`

- **① 问题与重要性**：投机解码可加速自回归LLM，但直接移植到视觉语言模型VLM面临视觉token主导prefill、KV缓存膨胀等系统约束，需为VLM专门设计。
- **② 方法与独特贡献**：作者提出SpecVLM系统，建立EAGLE-2式强基线EagleVLM，引入弹性视觉压缩器自适应选择剪枝/池化/卷积/重采样原语，并提出在线logit蒸馏协议用实时教师logit和倒数第二层特征以交叉熵加Smooth L1目标训练草稿模型，避免离线蒸馏语料。
- **③ 任务 / 数据集 / 模型**：在视觉语言模型推理加速任务上实验，相对全自回归推理获得1.5-2.3倍端到端加速，摘要未明确具体VLM基准名，详见原文。
- **④ 局限与未来工作**：在线蒸馏的训练时扩展效应需较长训练，弹性压缩器的原语选择策略可能增加系统复杂度，未来可扩展到视频与更长上下文场景。

</details>

<details>
<summary><b>多模态草稿</b> — MASSV — Multimodal SD Draft</summary>

`arXiv 2025` · [arXiv](https://arxiv.org/abs/2505.10526) · 被引 `0`

- **① 问题与重要性**：多模态模型缺乏适配的投机解码草稿。多模态 SD 草稿有价值。
- **② 方法与独特贡献**：多模态草稿模型上 KD CE，草稿采样在策略。
- **③ 任务 / 数据集 / 模型**：多模态推理加速，草稿采样。
- **④ 局限与未来工作**：多模态对齐难。未来：更多模态与更大目标。

</details>


## 🤖 具身 / VLA / GUI / 视觉智能体 OPD

学生为视觉智能体或 VLA 策略，在自身视觉轨迹上由教师/自身监督。

| 论文 | 时间/会议 | 🌟 | 被引 | 严格 |
| :-- | :--: | :--: | :--: | :--: |
| [IROS 2026 · VLA: Refined Policy Distillation (RPD)](https://arxiv.org/abs/2503.05833) | IROS 2026 | [![Stars](https://img.shields.io/github/stars/Refined-Policy-Distillation/RPD?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/Refined-Policy-Distillation/RPD) | 16 | OPD |
| [Tencent · 具身: HY-Embodied-0.5](https://arxiv.org/abs/2604.07430) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HY-Embodied?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/Tencent-Hunyuan/HY-Embodied) | 4 | OPD |
| [HKUST · 桥接 SFT/RL: VLA-OPD](https://arxiv.org/abs/2603.26666) | arXiv 2026 | `📄 paper-only` | 3 | OPD |
| [双粒度效率: HyperEyes — Parallel Multimodal Search Agent](https://arxiv.org/abs/2605.07177) | arXiv 2026 | [![Stars](https://img.shields.io/github/stars/DeepExperience/HyperEyes?style=flat&label=%E2%AD%90&color=ffd700)](https://github.com/DeepExperience/HyperEyes) | 1 | OPD |
| [CoPD: CoPD — Co-Evolving Policy Distillation](https://arxiv.org/abs/2604.27083) | arXiv 2026 | `📄 paper-only` | 1 | OPD |
| [arXiv 2026: Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://arxiv.org/abs/2605.00642) | arXiv 2026 | `📄 paper-only` | 1 | OPD |
| [arXiv 2026: GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving](https://arxiv.org/abs/2606.02774) | arXiv 2026 | `📄 paper-only` | 0 | OPD |
| [arXiv 2026: LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning](https://arxiv.org/abs/2605.07505) | arXiv 2026 | `📄 paper-only` | 0 | OPD |

<details>
<summary><b>IROS 2026 · VLA</b> — Refined Policy Distillation (RPD)</summary>

`IROS 2026` · [arXiv](https://arxiv.org/abs/2503.05833) · [code](https://github.com/Refined-Policy-Distillation/RPD) · 被引 `16`

- **① 问题与重要性**：VLA/机器人操作的 RL 奖励稀疏、模仿易脱离学生分布。干净的 VLA-OPD 配方有价值。
- **② 方法与独特贡献**：教师 VLA 动作 + 在学生 rollout 上 PPO + 行为克隆，被称最干净的 VLA-OPD 配方。
- **③ 任务 / 数据集 / 模型**：VLA / 机器人操作任务，学生 rollout。
- **④ 局限与未来工作**：依赖教师 VLA；真机迁移需验证。未来：更多机器人平台。

</details>

<details>
<summary><b>Tencent · 具身</b> — HY-Embodied-0.5</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2604.07430) · [code](https://github.com/Tencent-Hunyuan/HY-Embodied) · 被引 `4`

- **① 问题与重要性**：把 32B 具身模型蒸到 2B 边缘端仍保持能力很难。具身强到弱 OPD 重要。
- **② 方法与独特贡献**：前向 KL 在策略蒸馏：32B→MoT-2B 边缘版，学生生成具身推理轨迹、教师给 FKL 目标；MoT 架构 + 视觉潜 token。
- **③ 任务 / 数据集 / 模型**：具身：22 个具身基准，下游 VLA 真机双臂控制(Xtrainer)。
- **④ 局限与未来工作**：边缘算力受限。未来：更多真机任务与更小模型。

</details>

<details>
<summary><b>HKUST · 桥接 SFT/RL</b> — VLA-OPD</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2603.26666) · 被引 `3`

- **① 问题与重要性**：VLA 离线 SFT 与在线 RL 之间有鸿沟，RL 奖励稀疏。用 OPD 桥接很有价值。
- **② 方法与独特贡献**：专家 VLA 教师在学生轨迹上密集 token 级监督，用反向 KL（避免 FKL 熵爆炸与硬 CE 坍缩）替代稀疏 RL，保留通才先验、缓解灾难性遗忘。
- **③ 任务 / 数据集 / 模型**：VLA / 机器人操作：LIBERO、RoboTwin2.0，学生轨迹。
- **④ 局限与未来工作**：代码待放出；真机泛化待证。未来：更大规模真机。

</details>

<details>
<summary><b>双粒度效率</b> — HyperEyes — Parallel Multimodal Search Agent</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.07177) · [code](https://github.com/DeepExperience/HyperEyes) · 被引 `1`

- **① 问题与重要性**：多模态搜索智能体在效率与质量间难平衡。宏微双粒度优化有价值。
- **② 方法与独特贡献**：TRACE（轨迹级自适应成本效率）+ OPD（token 级）+ GRPO，外部教师，宏（轨迹）+微（token）双粒度。
- **③ 任务 / 数据集 / 模型**：并行多模态搜索智能体任务，学生 rollout。
- **④ 局限与未来工作**：组件多、调参复杂。未来：更统一的效率-质量目标。

</details>

<details>
<summary><b>CoPD</b> — CoPD — Co-Evolving Policy Distillation</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2604.27083) · 被引 `1`

- **① 问题与重要性**：把多个专家能力整合进单一模型时，混合RLVR受跨能力发散代价之苦，而先训专家再OPD虽避免发散却因教师-学生行为模式差距大而吸收不足，解决能力整合很重要。
- **② 方法与独特贡献**：作者提出协同演化策略蒸馏(CoPD)，并行训练各专家并在每个专家持续RLVR过程中引入OPD(而非训练完成后)，让专家互为教师实现双向OPD协同演化，使行为模式更一致同时保留互补知识。
- **③ 任务 / 数据集 / 模型**：在文本、图像、视频推理能力的一体化整合上验证，显著优于混合RLVR和MOPD等强基线，甚至超过领域专家模型；具体模型详见原文。
- **④ 局限与未来工作**：并行多专家训练带来更高计算开销；未来可推广到更多模态和更大规模的专家集合。

</details>

<details>
<summary><b>arXiv 2026</b> — Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.00642) · 被引 `1`

- **① 问题与重要性**：GUI grounding把指令映射到目标元素的视觉坐标，是自主GUI智能体核心能力，现有RL方法(如GRPO)依赖昂贵的多次rollout且在难样本上信号稀疏，寻找更优替代很重要。
- **② 方法与独特贡献**：作者提出首个面向GUI grounding的OPSD框架GUI-SD，用目标框和高斯软掩码为教师构建视觉增强的特权上下文(不泄露精确坐标)，并采用基于数字重要性与教师置信度的熵引导蒸馏。
- **③ 任务 / 数据集 / 模型**：在六个代表性GUI grounding基准上实验，一致优于基于GRPO的方法和朴素蒸馏；具体模型详见原文(摘要被截断)。
- **④ 局限与未来工作**：特权上下文构造(高斯掩码、框信息)针对GUI任务定制，迁移性待验证；未来可扩展到更复杂的多步GUI智能体任务。

</details>

<details>
<summary><b>arXiv 2026</b> — GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2606.02774) · 被引 `0`

- **① 问题与重要性**：本文解决自动驾驶VLM处理地区特定交通规则能力欠探索的问题，这关乎其在全球多样场景下的安全部署。
- **② 方法与独特贡献**：作者构建GeoDrive-Bench基准（覆盖六国驾驶文化的5053个人工验证多选QA，含感知、预测、规划、区域推理四类任务），并设计一种将地区交通规则知识注入VLM内部表示的蒸馏算法。
- **③ 任务 / 数据集 / 模型**：在九个SOTA VLM上实验，显示各任务跨地理驾驶文化存在显著性能差异，所提baseline模型展现更好的地理文化对齐推理。
- **④ 局限与未来工作**：数据集聚焦六国和多选QA格式，覆盖范围和真实开放驾驶场景的泛化有限；未来可扩展到更多国家、开放式问答和真实驾驶决策。该蒸馏为知识注入而非学生自采样on-policy蒸馏。

</details>

<details>
<summary><b>arXiv 2026</b> — LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning</summary>

`arXiv 2026` · [arXiv](https://arxiv.org/abs/2605.07505) · 被引 `0`

- **① 问题与重要性**：针对端侧轻量级视觉-语言GUI智能体模型容量有限、传统SFT易过拟合与灾难性遗忘的问题，而高效跨平台自动化交互又亟需提升小模型能力，因此该问题很重要。
- **② 方法与独特贡献**：提出无需SFT的训练范式：将通用知识蒸馏首次系统引入GUI领域，通过引入oracle参考轨迹和动态检索机制进行Guided On-policy Distillation以减少幻觉，并设计Multi-solution Dual-level GRPO框架联合对齐宏观子任务规划与微观执行匹配。
- **③ 任务 / 数据集 / 模型**：在GUI智能体（跨平台自动化交互、长程操作）任务上验证；摘要未明确具体数据集与基座模型名称，详见原文。
- **④ 局限与未来工作**：方法依赖oracle参考轨迹和检索机制，构建成本与对多解任务的泛化能力可能受限；未来可扩展到更多端侧场景与更长程任务，并验证检索机制的鲁棒性。

</details>


## 🙏 致谢 & 说明

- 本列表的论文来源与四问总结整理自上述三个 awesome 仓库的技术细节表、各论文 arXiv 摘要及公开资料，可能存在偏差，**请以原论文为准**。
- 🔎 网络补充条目：[AoTD](https://arxiv.org/abs/2412.01694) · [VITAL / Thinking With Videos](https://arxiv.org/abs/2508.04416) · [β-KD (Uncertainty-Aware KD, CVPR 2026)](https://arxiv.org/abs/2603.21426)。
- 数据抓取时间：2026-06。⭐ Star 徽标由 shields.io 实时刷新；被引数来自 Semantic Scholar，会随时间变化。
- 欢迎 PR 补充新论文 / 修正信息。

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 本列表以 CC0 公有领域贡献发布，可自由使用。
