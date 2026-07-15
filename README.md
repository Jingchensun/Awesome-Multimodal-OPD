# 🖼️ Awesome Multimodal On-Policy Distillation

> A curated, **auto-refreshed** list of **multimodal On-Policy Distillation (OPD / OPSD)** papers — organized by **Image QA · Video QA · Audio QA** (plus generation, speculative decoding, and embodied/VLA).

<p align="center">
  <a href="https://jingchensun.github.io/Awesome-Multimodal-OPD/"><img src="https://img.shields.io/badge/%F0%9F%9A%80%20OPEN%20INTERACTIVE%20READER-Search%20%C2%B7%20Filter%20%C2%B7%20EN%2F%E4%B8%AD%E6%96%87-1f6feb?style=for-the-badge&logoColor=white" alt="Open Interactive Reader"></a>
  <a href="https://htmlpreview.github.io/?https://github.com/Jingchensun/Awesome-Multimodal-OPD/blob/main/index.html"><img src="https://img.shields.io/badge/mirror-htmlpreview-555?style=for-the-badge" alt="htmlpreview mirror"></a>
</p>

<p align="center"><b>👉 <a href="https://jingchensun.github.io/Awesome-Multimodal-OPD/">Live interactive reader</a></b> — searchable, filterable, bilingual (EN / 中文), one click, no install &nbsp;·&nbsp; <a href="https://htmlpreview.github.io/?https://github.com/Jingchensun/Awesome-Multimodal-OPD/blob/main/index.html">instant mirror (no Pages needed)</a></p>

![papers](https://img.shields.io/badge/papers-52-4E6813?style=flat-square) ![web--added](https://img.shields.io/badge/web--added-2-2E86C1?style=flat-square) ![updated](https://img.shields.io/badge/stats_updated-2026.07.15-purple?style=flat-square)

**What is OPD?** `C1`: the student samples its own trajectories `y ~ π_student(·|x)` during training; `C2`: a teacher provides per-token / sequence-level supervision on those **student-generated** samples. **OPSD** is the special case where the teacher is the *same model* conditioned on privileged information.

Each paper is tagged with **arXiv link · date · first-author affiliation · code · ⭐ stars · citations**. ⭐ Stars and citations are **refreshed daily** by [a GitHub Action](.github/workflows/refresh.yml) (⭐ via GitHub API; citations via Semantic Scholar). For four-point summaries per paper, open the [interactive reader](https://jingchensun.github.io/Awesome-Multimodal-OPD/).

> 🔄 **Stats last updated: 2026-07-15 05:41 UTC**

## 📊 Overview

| Subfield | # |
| :-- | :--: |
| 🖼️ Image QA / VQA / Visual Reasoning | 14 |
| 🎬 Video QA / Video Reasoning / Temporal Grounding | 7 |
| 🔊 Audio QA / Speech | 7 |
| 🎨 Image / Video Generation (Diffusion · Flow) | 12 |
| ⚡ Multimodal Speculative-Decoding Distillation | 4 |
| 🤖 Embodied / VLA / GUI Visual Agents | 8 |
| **Total** | **52** |

## 🖼️ Image QA / VQA / Visual Reasoning

On-policy distillation that transfers reasoning into vision-language models and trains on VQA / visual-reasoning rollouts.

| Paper | arXiv | Date | First-author affiliation | Code | ⭐ Stars | Citations |
| :-- | :--: | :--: | :-- | :--: | :--: | :--: |
| Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts | [link](https://arxiv.org/abs/2606.10334) | 2026-06-09 | Microsoft | — | — | 0 |
| Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization | [link](https://arxiv.org/abs/2606.09091) | 2026-06-08 | OPPO AI Center | [GitHub](https://github.com/OPPO-Mente-Lab/GNDPO) | 2 | 1 |
| Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation | [link](https://arxiv.org/abs/2606.08719) | 2026-06-07 | Peking University | — | — | 0 |
| Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization | [link](https://arxiv.org/abs/2606.07000) | 2026-06-05 | Tianjin University | [GitHub](https://github.com/XszNeverSleep/PTD-PO) | 6 | 0 |
| ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation | [link](https://arxiv.org/abs/2606.05718) | 2026-06-04 | Shanghai AI Laboratory | [GitHub](https://github.com/tiankanghui/ViCuR) | 15 | 1 |
| Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation | [link](https://arxiv.org/abs/2606.06076) | 2026-06-04 | Tsinghua University | — | — | 0 |
| Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding | [link](https://arxiv.org/abs/2606.00564) | 2026-05-30 | KAIST | — | — | 1 |
| Visual-Advantage On-Policy Distillation for Vision-Language Models | [link](https://arxiv.org/abs/2605.21924) | 2026-05-21 | Institute of Automation, CAS | — | — | 1 |
| Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation | [link](https://arxiv.org/abs/2605.18740) | 2026-05-18 | ISCAS | [GitHub](https://github.com/VisionOPD/Vision-OPD) | 185 | 7 |
| DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation | [link](https://arxiv.org/abs/2605.15532) | 2026-05-15 | NVIDIA Research | — | — | 0 |
| Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe | [link](https://arxiv.org/abs/2605.03677) | 2026-05-05 | Zhejiang University | [GitHub](https://github.com/WenjinHou/Uni-OPD) | 49 | 13 |
| Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL | [link](https://arxiv.org/abs/2604.28123) | 2026-04-30 | HKUST (GZ) | [GitHub](https://github.com/XIAO4579/PRISM) | 96 | 3 |
| KEPO: Knowledge-Enhanced Preference Optimization for Multimodal Reasoning with Applications to Medical VQA | [link](https://arxiv.org/abs/2602.00400) | 2026-01-30 | Chapman University | [GitHub](https://github.com/Corleno/KEPO) | 2 | 0 |
| VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation | [link](https://arxiv.org/abs/2510.23497) | 2025-10-27 | University of Tuebingen | — | — | 12 |

## 🎬 Video QA / Video Reasoning / Temporal Grounding

OPD / self-distillation for video question answering, video reasoning and temporal grounding (incl. closely-related AoTD, VITAL).

| Paper | arXiv | Date | First-author affiliation | Code | ⭐ Stars | Citations |
| :-- | :--: | :--: | :-- | :--: | :--: | :--: |
| InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning | [link](https://arxiv.org/abs/2606.12195) | 2026-06-10 | Shanghai Innovation Institute | — | — | 0 |
| World Model Self-Distillation: Training World Models to Solve General Tasks | [link](https://arxiv.org/abs/2606.12072) | 2026-06-10 | University of Bern | — | — | 0 |
| World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning | [link](https://arxiv.org/abs/2606.03603) | 2026-06-02 | University of Macau | — | — | 0 |
| VISD: Enhancing Video Reasoning via Structured Self-Distillation | [link](https://arxiv.org/abs/2605.06094) | 2026-05-07 | HUST | — | — | 6 |
| Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation | [link](https://arxiv.org/abs/2602.02994) | 2026-02-03 | Xiaomi | — | — | 11 |
| 🔎 Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning | [link](https://arxiv.org/abs/2508.04416) | 2025-08-06 | Tsinghua University | — | — | 73 |
| 🔎 Enhancing Video-LLM Reasoning via Agent-of-Thoughts Distillation | [link](https://arxiv.org/abs/2412.01694) | 2024-12-02 | Shanghai Jiao Tong University | [GitHub](https://github.com/zhengrongz/AoTD) | 58 | 36 |

## 🔊 Audio QA / Speech

Cross-modal transfer of text reasoning into audio/speech, and OPD for audio understanding / ASR.

| Paper | arXiv | Date | First-author affiliation | Code | ⭐ Stars | Citations |
| :-- | :--: | :--: | :-- | :--: | :--: | :--: |
| OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing | [link](https://arxiv.org/abs/2606.15920) | 2026-06-14 | Shenzhen University | — | — | 0 |
| Data-Efficient On-Policy Distillation for Automatic Speech Recognition | [link](https://arxiv.org/abs/2605.28139) | 2026-05-27 | AutoArk-AI | — | — | 0 |
| Qwen3.5-Omni Technical Report | [link](https://arxiv.org/abs/2604.15804) | 2026-04-17 | Alibaba | — | — | 67 |
| X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs | [link](https://arxiv.org/abs/2603.24596) | 2026-03-06 | Tencent Hunyuan | — | — | 6 |
| CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation | [link](https://arxiv.org/abs/2601.16547) | 2026-01-23 | Baidu | — | — | 5 |
| Step-Audio-R1 Technical Report | [link](https://arxiv.org/abs/2511.15848) | 2025-11-19 | StepFun | [GitHub](https://github.com/stepfun-ai/Step-Audio-R1) | 685 | 31 |
| Qwen3-Omni Technical Report | [link](https://arxiv.org/abs/2509.17765) | 2025-09-22 | Alibaba | — | — | 373 |

## 🎨 Image / Video Generation (Diffusion · Flow)

OPD / self-distillation for diffusion and flow-matching generative models (few-step generation, trajectory self-distillation, adversarial distillation).

| Paper | arXiv | Date | First-author affiliation | Code | ⭐ Stars | Citations |
| :-- | :--: | :--: | :-- | :--: | :--: | :--: |
| Knowledge Distillation for Visual Autoregressive Models | [link](https://arxiv.org/abs/2606.06078) | 2026-06-04 | Qualcomm AI Research | — | — | 0 |
| GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models | [link](https://arxiv.org/abs/2605.29398) | 2026-05-28 | UCL | — | — | 1 |
| Adversarial Dual On-Policy Distillation from Expressive Teacher | [link](https://arxiv.org/abs/2605.27095) | 2026-05-26 | NTU | — | — | 0 |
| CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation | [link](https://arxiv.org/abs/2605.25378) | 2026-05-25 | Zhejiang University | — | — | 0 |
| DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models | [link](https://arxiv.org/abs/2605.15055) | 2026-05-14 | Fudan University | — | — | 4 |
| AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation | [link](https://arxiv.org/abs/2605.13724) | 2026-05-13 | NUS | — | — | 4 |
| TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM | [link](https://arxiv.org/abs/2605.09536) | 2026-05-10 | Renmin University of China | [GitHub](https://github.com/BHmingyang/TAD) | 2 | 0 |
| Flow-OPD: On-Policy Distillation for Flow Matching Models | [link](https://arxiv.org/abs/2605.08063) | 2026-05-08 | USTC | — | — | 6 |
| D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models | [link](https://arxiv.org/abs/2605.05204) | 2026-05-06 | HKUST | — | — | 6 |
| LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation | [link](https://arxiv.org/abs/2512.23576) | 2025-12-29 | SII / SJTU | — | — | 6 |
| pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation | [link](https://arxiv.org/abs/2510.14974) | 2025-10-16 | Stanford University | [GitHub](https://github.com/Lakonik/piFlow) | 451 | 23 |
| Di$\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator | [link](https://arxiv.org/abs/2503.15457) | 2025-03-19 | École Polytechnique | — | — | 6 |

## ⚡ Multimodal Speculative-Decoding Distillation

Training on-policy draft models for vision-language models to speed up inference.

| Paper | arXiv | Date | First-author affiliation | Code | ⭐ Stars | Citations |
| :-- | :--: | :--: | :-- | :--: | :--: | :--: |
| ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding | [link](https://arxiv.org/abs/2509.15235) | 2025-09-17 | Peking University | — | — | 15 |
| SpecVLM: Fast Speculative Decoding in Vision-Language Models | [link](https://arxiv.org/abs/2509.11815) | 2025-09-15 | Xi'an Jiaotong University | — | — | 5 |
| Speculative Decoding Reimagined for Multimodal Large Language Models | [link](https://arxiv.org/abs/2505.14260) | 2025-05-20 | Xiamen University | — | — | 6 |
| MASSV: Multimodal Adaptation and Self-Data Distillation for Speculative Decoding of Vision-Language Models | [link](https://arxiv.org/abs/2505.10526) | 2025-05-15 | Cerebras | — | — | 0 |

## 🤖 Embodied / VLA / GUI Visual Agents

The student is a visual agent or VLA policy supervised on its own visual trajectories.

| Paper | arXiv | Date | First-author affiliation | Code | ⭐ Stars | Citations |
| :-- | :--: | :--: | :-- | :--: | :--: | :--: |
| GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving | [link](https://arxiv.org/abs/2606.02774) | 2026-06-01 | Univ. of Wisconsin-Madison | — | — | 0 |
| HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents | [link](https://arxiv.org/abs/2605.07177) | 2026-05-08 | Xiaohongshu | [GitHub](https://github.com/DeepExperience/HyperEyes) | 69 | 2 |
| LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning | [link](https://arxiv.org/abs/2605.07505) | 2026-05-08 | Moore Threads | — | — | 1 |
| Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding | [link](https://arxiv.org/abs/2605.00642) | 2026-05-01 | IIE, CAS | — | — | 2 |
| Co-Evolving Policy Distillation | [link](https://arxiv.org/abs/2604.27083) | 2026-04-29 | IIE, CAS | — | — | 2 |
| HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents | [link](https://arxiv.org/abs/2604.07430) | 2026-04-08 | Tencent | [GitHub](https://github.com/Tencent-Hunyuan/HY-Embodied) | 763 | 6 |
| VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation | [link](https://arxiv.org/abs/2603.26666) | 2026-03-27 | HKUST (GZ) | — | — | 5 |
| Refined Policy Distillation: From VLA Generalists to RL Experts | [link](https://arxiv.org/abs/2503.05833) | 2025-03-06 | Univ. of Tech. Nuremberg | [GitHub](https://github.com/Refined-Policy-Distillation/RPD) | 22 | 21 |

## 🙏 Acknowledgments

This list is compiled and de-duplicated from three awesome repositories, plus web search for a few multimodal entries missing from them. Full credit to the maintainers of:

- [thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD)
- [chrisliu298/awesome-on-policy-distillation](https://github.com/chrisliu298/awesome-on-policy-distillation)
- [nick7nlp/Awesome-LLM-On-Policy-Distillation](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation)

Summaries are paraphrased from the papers' arXiv abstracts and may contain errors — please refer to the original papers. To add a paper, edit [`papers.json`](papers.json); the tables and the interactive reader regenerate automatically. ⭐ stars and citations are snapshots that change over time.

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) Released under CC0 (public-domain dedication).
