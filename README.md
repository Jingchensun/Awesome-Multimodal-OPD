<h1 align="center">Awesome Multimodal On-Policy Distillation</h1>

<p align="center">Multimodal <b>OPD / OPSD</b> papers across image, video, audio, generation and embodied AI —<br>ranked by GitHub stars, refreshed every day.</p>

<p align="center">
  <a href="https://jingchensun.github.io/Awesome-Multimodal-OPD/"><img src="https://img.shields.io/badge/Interactive_reader-EN_%2F_%E4%B8%AD%E6%96%87-1f6feb?style=flat-square" alt="Interactive reader"></a>
  <img src="https://img.shields.io/badge/papers-158-4E6813?style=flat-square" alt="papers">
  <img src="https://img.shields.io/badge/with_code-61-2E86C1?style=flat-square" alt="with code">
  <img src="https://img.shields.io/badge/updated-2026.10.09-purple?style=flat-square" alt="updated">
</p>

<p align="center">
  <a href="#imageqa">Image (57)</a> · <a href="#videoqa">Video (15)</a> · <a href="#audioqa">Audio (16)</a> · <a href="#generation">Generation (45)</a> · <a href="#embodied">Embodied (25)</a>
</p>

> **On-policy distillation (OPD)** — the student learns from *its own* rollouts `y ~ π_student(·|x)`, while a teacher scores or corrects those student-generated samples. **OPSD** is the self-distillation case: the teacher is the same model, given privileged information.

Search, filter and read a four-point summary of every paper in the **[interactive reader](https://jingchensun.github.io/Awesome-Multimodal-OPD/)** ([mirror](https://htmlpreview.github.io/?https://github.com/Jingchensun/Awesome-Multimodal-OPD/blob/main/index.html)).

## 🔥 Most starred

| # | Paper | Domain | Affiliation | Code |
| :-: | :-- | :-- | :-- | :-: |
| 1 | [SenseNova-U1.5: Towards Native Unified Visual Intelligence](https://arxiv.org/abs/2609.11929) | Generation | SenseTime | [⭐ 6.9k](https://github.com/OpenSenseNova/SenseNova-U1) |
| 2 | [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765) | Audio | Alibaba | [⭐ 4k](https://github.com/QwenLM/Qwen3-Omni) |
| 3 | [HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://arxiv.org/abs/2604.07430) | Embodied | Tencent | [⭐ 875](https://github.com/Tencent-Hunyuan/HY-Embodied) |
| 4 | [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473) | Generation | Tsinghua University | [⭐ 815](https://github.com/NVlabs/rcm) |
| 5 | [Kwai Keye-VL-2.0 Technical Report](https://arxiv.org/abs/2606.10651) | Video | Kuaishou | [⭐ 813](https://github.com/Kwai-Keye/Keye) |
| 6 | [Step-Audio-R1 Technical Report](https://arxiv.org/abs/2511.15848) | Audio | StepFun | [⭐ 701](https://github.com/stepfun-ai/Step-Audio-R1) |
| 7 | [OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766) | Generation | Meituan | [⭐ 692](https://github.com/MeiGen-AI/OPSD-V) |
| 8 | [On-Policy Self-Distillation in Diffusion Models](https://arxiv.org/abs/2608.24646) | Generation | ByteDance | [⭐ 679](https://github.com/worldbench/DiffusionOPSD) |
| 9 | [pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation](https://arxiv.org/abs/2510.14974) | Generation | Stanford University | [⭐ 475](https://github.com/Lakonik/piFlow) |
| 10 | [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724) | Generation | NUS | [⭐ 441](https://github.com/NVlabs/AnyFlow) |

<h2 id="imageqa">🖼️ Image Domain</h2>

Vision-language reasoning, VQA, fine-grained perception, OCR, medical and industrial VLMs, visual-token compression and VLM speculative decoding. **57 papers**, 25 with code.

| Paper | Affiliation | Date | Code | Cited |
| :-- | :-- | :-: | :-: | :-: |
| [Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation](https://arxiv.org/abs/2605.18740) | ISCAS | 2026-05-18 | [⭐ 330](https://github.com/VisionOPD/Vision-OPD) | 77 |
| [Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://arxiv.org/abs/2604.28123) | HKUST (GZ) | 2026-04-30 | [⭐ 101](https://github.com/XIAO4579/PRISM) | 9 |
| [V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning](https://arxiv.org/abs/2606.25319) | Sichuan University | 2026-06-24 | [⭐ 73](https://github.com/eVI-group-SCU/V-Zero) | 10 |
| [ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding](https://arxiv.org/abs/2509.15235) | Peking University | 2025-09-17 | [⭐ 71](https://github.com/KangJialiang/ViSpec) | 24 |
| [Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe](https://arxiv.org/abs/2605.03677) | Zhejiang University | 2026-05-05 | [⭐ 57](https://github.com/WenjinHou/Uni-OPD) | 47 |
| [VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy Distillation](https://arxiv.org/abs/2607.28590) | Shanghai Jiao Tong University | 2026-07-30 | [⭐ 50](https://github.com/DeepExperience/VAD_Multimodal_OPD) | 6 |
| [Speculative Decoding Reimagined for Multimodal Large Language Models](https://arxiv.org/abs/2505.14260) | Xiamen University | 2025-05-20 | [⭐ 38](https://github.com/Lyn-Lucy/MSD) | 9 |
| [OPD-V: Visual On-Policy Self-Distillation with Modality Balance](https://arxiv.org/abs/2608.05131) | LMU Munich | 2026-08-05 | [⭐ 28](https://github.com/aniri15/OPD-V) | 9 |
| [ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation](https://arxiv.org/abs/2606.05718) | Shanghai AI Laboratory | 2026-06-04 | [⭐ 22](https://github.com/tiankanghui/ViCuR) | 13 |
| [Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation](https://arxiv.org/abs/2606.06076) | Tsinghua University | 2026-06-04 | [⭐ 22](https://github.com/Oranger-l/MGSD) | 1 |
| [ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation](https://arxiv.org/abs/2608.20122) | Ant Group | 2026-08-20 | [⭐ 20](https://github.com/ant-research/ArmorOCR) | 0 |
| [Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction](https://arxiv.org/abs/2609.32353) | Shanghai Jiao Tong University | 2026-09-26 | [⭐ 13](https://github.com/Yrxxxxxxxx1007/LT-OPD) | 0 |
| [RP-OPSD: Resolution-Privileged On-Policy Self-Distillation for Multimodal Large Language Models](https://arxiv.org/abs/2607.24447) | USTC | 2026-07-27 | [⭐ 12](https://github.com/sansanyuchen/RP-OPSD) | 6 |
| [OPD-Aha: From Linguistic Momentum to Visual Reflection in Multimodal On-Policy Distillation](https://arxiv.org/abs/2609.16459) | Arizona State University | 2026-09-15 | [⭐ 11](https://github.com/Echochef/OPD-Aha) | 0 |
| [Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation](https://arxiv.org/abs/2606.08719) | Peking University | 2026-06-07 | [⭐ 10](https://github.com/walkeralan123/Imagine-OPD) | 9 |
| [Veritas++: Value-aware On-Policy Distillation for Perception-Enhanced AIGI Detection](https://arxiv.org/abs/2607.27113) | Institute of Automation, CAS | 2026-07-29 | [⭐ 10](https://github.com/EricTan7/VeritasPP) | 2 |
| [Med-OPD: Improving Medical Vision-Language Models via Evidence-Aware On-Policy Distillation](https://arxiv.org/abs/2607.16303) | NUS | 2026-07-14 | [⭐ 10](https://github.com/yunhang8658/MedOPD) | 2 |
| [Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding](https://arxiv.org/abs/2606.00564) | KAIST | 2026-05-30 | [⭐ 8](https://github.com/hee-suk-yoon/Decomposed_OPD) | 9 |
| [H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation](https://arxiv.org/abs/2607.02592) | BUPT | 2026-07-01 | [⭐ 8](https://github.com/buptyqx/H-OPD) | 7 |
| [SpecVLM: Fast Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2509.11815) | Xi'an Jiaotong University | 2025-09-15 | [⭐ 8](https://github.com/haiduo/SpecVLM) | 7 |
| [Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization](https://arxiv.org/abs/2606.07000) | Tianjin University | 2026-06-05 | [⭐ 7](https://github.com/XszNeverSleep/PTD-PO) | 1 |
| [Perception Before Supervision: Self-Contained Visual Distillation from Counterfactual Blind Spots](https://arxiv.org/abs/2608.09931) | MBZUAI | 2026-08-10 | [⭐ 5](https://github.com/mbzuai-oryx/CVPD) | 2 |
| [ADOPD: Reference-Privileged On-Policy Distillation for MLLM-Based Industrial Anomaly Detection](https://arxiv.org/abs/2608.09789) | Zhejiang University | 2026-08-10 | [⭐ 5](https://github.com/withTai/ADOPD) | 0 |
| [Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization](https://arxiv.org/abs/2606.09091) | OPPO AI Center | 2026-06-08 | [⭐ 2](https://github.com/OPPO-Mente-Lab/GNDPO) | 2 |
| [KEPO: Knowledge-Enhanced Preference Optimization for Multimodal Reasoning with Applications to Medical VQA](https://arxiv.org/abs/2602.00400) | Chapman University | 2026-01-30 | [⭐ 2](https://github.com/Corleno/KEPO) | 0 |

<details>
<summary>📄 32 more without public code (newest first)</summary>

| Paper | Affiliation | Date | Cited |
| :-- | :-- | :-: | :-: |
| [Revisit to Segment: Working Memory Distillation for Reasoning Segmentation](https://arxiv.org/abs/2609.34863) | Xiaohongshu | 2026-09-28 | 0 |
| [Evidence-Aligned Multimodal On-Policy Self-Distillation for Fine-Grained Visual Understanding](https://arxiv.org/abs/2609.34672) | Beihang University | 2026-09-28 | 0 |
| [K-OPSD: Verifiable On-Policy Self-Distillation for Post-Training Vision-Language Models on AEC Drawings](https://arxiv.org/abs/2609.34082) | Amazon Web Services | 2026-09-28 | 0 |
| [SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models](https://arxiv.org/abs/2609.34044) | University of Toronto | 2026-09-28 | 0 |
| [CT-OPD: Counterfactual Trace On-Policy Distillation for Diffusion Vision-Language Models](https://arxiv.org/abs/2609.32781) | Institute of Automation, CAS | 2026-09-26 | 0 |
| [MM-OPD: Towards One More Bottleneck Between Perception and Reasoning](https://arxiv.org/abs/2609.32690) | HUST | 2026-09-26 | 0 |
| [Progressive-View On-Policy Distillation for Regional-to-Global Transfer in Multimodal LLMs](https://arxiv.org/abs/2609.32333) | Baidu | 2026-09-26 | 0 |
| [Pistis Technical Report](https://arxiv.org/abs/2609.28554) | ByteDance | 2026-09-23 | 0 |
| [BAS-OPD: Budget-Aware Selective On-Policy Self-Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2609.25891) | HFIPS, Chinese Academy of Sciences | 2026-09-22 | 0 |
| [Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World](https://arxiv.org/abs/2609.23038) | Zhejiang University | 2026-09-19 | 0 |
| [ReDraft, Don't Just Distill: Reference-Driven Revision for Continual VLLM Post-Training](https://arxiv.org/abs/2609.16639) | Fudan University | 2026-09-15 | 0 |
| [Reason What Matters: Retrieval-Grounded Reasoning for Universal Multimodal Embeddings](https://arxiv.org/abs/2609.15296) | Tsinghua University | 2026-09-14 | 0 |
| [CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction](https://arxiv.org/abs/2609.02401) | Tianjin University | 2026-09-02 | 2 |
| [PailitaoGR: Latent Think-with-Images for Generative Image Retrieval](https://arxiv.org/abs/2608.26658) | Alibaba | 2026-08-27 | 0 |
| [Self-Supervised Visual On-Policy Distillation](https://arxiv.org/abs/2608.14144) | UC San Diego | 2026-08-14 | 7 |
| [Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/abs/2608.13505) | Shanghai AI Laboratory | 2026-08-13 | 3 |
| [Reading is not Reasoning: Bridging the Agentic Policy Gap in Vision-Text Compression](https://arxiv.org/abs/2608.08960) | City University of Hong Kong | 2026-08-09 | 1 |
| [Same Semantics, Different Paths: Self-Improving Alignment for Vision-Text Compression](https://arxiv.org/abs/2608.02109) | Southeast University | 2026-08-03 | 2 |
| [Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2608.01263) | Tianjin University | 2026-08-02 | 4 |
| [Correcting What You Cannot See: Credit Assignment for Perception Distillation in Multimodal Reasoners](https://arxiv.org/abs/2607.28336) | — | 2026-07-30 | 0 |
| [Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation](https://arxiv.org/abs/2607.23125) | HKUST (GZ) | 2026-07-25 | 5 |
| [Visual Contrastive Self-Distillation](https://arxiv.org/abs/2607.21556) | UMD | 2026-07-23 | 9 |
| [MOPDA: Mixed-Trajectory On-Policy Distillation for Language-Guided Industrial Anomaly Detection](https://arxiv.org/abs/2607.18850) | Tsinghua University | 2026-07-21 | 1 |
| [OvisOCR2 Technical Report](https://arxiv.org/abs/2607.13639) | Alibaba | 2026-07-15 | 5 |
| [MOSAIC: Adaptive Inter-layer Composition for Efficient Heterogeneous Vision-Language Models](https://arxiv.org/abs/2607.09029) | Li Auto | 2026-07-10 | 0 |
| [Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient Multimodal On-Policy Self-Distillation](https://arxiv.org/abs/2606.19120) | SIA, CAS | 2026-06-17 | 4 |
| [Visual-OPSD: Cross-Modal On-Policy Self-Distillation for Efficient Unified Multimodal Reasoning](https://arxiv.org/abs/2606.18974) | Xi'an Jiaotong University | 2026-06-17 | 15 |
| [Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts](https://arxiv.org/abs/2606.10334) | Microsoft | 2026-06-09 | 1 |
| [Visual-Advantage On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2605.21924) | Institute of Automation, CAS | 2026-05-21 | 23 |
| [DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](https://arxiv.org/abs/2605.15532) | NVIDIA | 2026-05-15 | 0 |
| [VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation](https://arxiv.org/abs/2510.23497) | University of Tuebingen | 2025-10-27 | 31 |
| [MASSV: Multimodal Adaptation and Self-Data Distillation for Speculative Decoding of Vision-Language Models](https://arxiv.org/abs/2505.10526) | Cerebras | 2025-05-15 | 4 |

</details>

<h2 id="videoqa">🎬 Video Domain</h2>

Video QA, long-video and streaming understanding, video reasoning and temporal grounding. **15 papers**, 6 with code.

| Paper | Affiliation | Date | Code | Cited |
| :-- | :-- | :-: | :-: | :-: |
| [Kwai Keye-VL-2.0 Technical Report](https://arxiv.org/abs/2606.10651) | Kuaishou | 2026-06-09 | [⭐ 813](https://github.com/Kwai-Keye/Keye) | 3 |
| [Enhancing Video-LLM Reasoning via Agent-of-Thoughts Distillation](https://arxiv.org/abs/2412.01694) 🔎 | Shanghai Jiao Tong University | 2024-12-02 | [⭐ 61](https://github.com/zhengrongz/AoTD) | 45 |
| [VISD: Enhancing Video Reasoning via Structured Self-Distillation](https://arxiv.org/abs/2605.06094) | HUST | 2026-05-07 | [⭐ 26](https://github.com/Koreyoshi01/VISD) | 13 |
| [World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning](https://arxiv.org/abs/2606.03603) | University of Macau | 2026-06-02 | [⭐ 22](https://github.com/yczhou001/PF-OPSD) | 2 |
| [World Model Self-Distillation: Training World Models to Solve General Tasks](https://arxiv.org/abs/2606.12072) | University of Bern | 2026-06-10 | [⭐ 19](https://github.com/sebastian-stapf/world-model-self-distillation) | 0 |
| [Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision](https://arxiv.org/abs/2609.04203) | Aalto University | 2026-09-03 | [⭐ 4](https://github.com/AaltoML/s3t) | 1 |

<details>
<summary>📄 9 more without public code (newest first)</summary>

| Paper | Affiliation | Date | Cited |
| :-- | :-- | :-: | :-: |
| [Counterfactual Attention Policy Distillation for Temporal Video Grounding](https://arxiv.org/abs/2609.34581) | Xiamen University | 2026-09-28 | 0 |
| [Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding](https://arxiv.org/abs/2609.09300) | Tongji University | 2026-09-08 | 1 |
| [Video-OPSD: Exploiting Privileged Visual Evidence for On-Policy Self-Distillation in Video Large Language Models](https://arxiv.org/abs/2608.27065) | NTU | 2026-08-27 | 4 |
| [Where to Look Matters: On-Policy Self-Distillation for Long-Video Understanding](https://arxiv.org/abs/2608.25356) | UMD | 2026-08-26 | 4 |
| [StreamOPD: A Post-Training Recipe with Spatio-Temporal Cue Gating for Streaming Video Understanding](https://arxiv.org/abs/2608.16320) | Tsinghua University | 2026-08-17 | 0 |
| [Deep Thought Alignment: Trajectory-Level Latent Distillation for Video Reasoning](https://arxiv.org/abs/2608.16316) | Tencent Youtu Lab | 2026-08-17 | 2 |
| [InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning](https://arxiv.org/abs/2606.12195) | Shanghai Innovation Institute | 2026-06-10 | 5 |
| [Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation](https://arxiv.org/abs/2602.02994) | Xiaomi | 2026-02-03 | 33 |
| [Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning](https://arxiv.org/abs/2508.04416) 🔎 | Tsinghua University | 2025-08-06 | 94 |

</details>

<h2 id="audioqa">🔊 Audio Domain</h2>

Speech and audio-language models, ASR, omni models, and cross-modal transfer of text reasoning into audio. **16 papers**, 6 with code.

| Paper | Affiliation | Date | Code | Cited |
| :-- | :-- | :-: | :-: | :-: |
| [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765) | Alibaba | 2025-09-22 | [⭐ 4k](https://github.com/QwenLM/Qwen3-Omni) | 570 |
| [Step-Audio-R1 Technical Report](https://arxiv.org/abs/2511.15848) | StepFun | 2025-11-19 | [⭐ 701](https://github.com/stepfun-ai/Step-Audio-R1) | 52 |
| [On-Policy Self-Distillation for Multi-Dialect ASR: Mastering Dialects, Retaining Mandarin](https://arxiv.org/abs/2608.11898) | NWPU | 2026-08-12 | [⭐ 99](https://github.com/ASLP-lab/CN-MultiDialect-ASR) | 2 |
| [OPOD: On-Policy Omni Distillation](https://arxiv.org/abs/2607.20918) | Renmin University of China | 2026-07-23 | [⭐ 56](https://github.com/VincentZhao2002/OPOD) | 1 |
| [ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models](https://arxiv.org/abs/2606.10581) | CUHK (Shenzhen) | 2026-06-09 | [⭐ 6](https://github.com/AmphionTeam/ParaBridge) | 7 |
| [Reward-Tilted On-Policy Distillation for Acoustic Grounding in Audio-Language Models](https://arxiv.org/abs/2609.28778) | NEC Laboratories America | 2026-09-23 | [⭐ 1](https://github.com/KaiyangLi1992/RT-OPD) | 0 |

<details>
<summary>📄 10 more without public code (newest first)</summary>

| Paper | Affiliation | Date | Cited |
| :-- | :-- | :-: | :-: |
| [TS-OPD: Reconciling ASR and QA in Speech Language Models via Task-Specific On-Policy Distillation](https://arxiv.org/abs/2609.29464) | Nankai University | 2026-09-24 | 0 |
| [Qwen-Audio-3.1-Realtime: Towards Reliable Agentic Voice Interaction](https://arxiv.org/abs/2609.25176) | Alibaba | 2026-09-21 | 1 |
| [Reducing the Output-Mode Gap in Speech Language Models via Joint-Output On-Policy Distillation](https://arxiv.org/abs/2609.15313) | Huawei | 2026-09-14 | 0 |
| [X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment](https://arxiv.org/abs/2607.21550) | Tencent Hunyuan | 2026-07-23 | 4 |
| [OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing](https://arxiv.org/abs/2606.15920) | Shenzhen University | 2026-06-14 | 6 |
| [Data-Efficient On-Policy Distillation for Automatic Speech Recognition](https://arxiv.org/abs/2605.28139) | AutoArk-AI | 2026-05-27 | 1 |
| [EchoDistill:Alignment Noisy-to-Clean Self-Distillation for Robust Audio LLMs](https://arxiv.org/abs/2605.23954) | NTU | 2026-05-11 | 0 |
| [Qwen3.5-Omni Technical Report](https://arxiv.org/abs/2604.15804) | Alibaba | 2026-04-17 | 167 |
| [X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs](https://arxiv.org/abs/2603.24596) | Tencent Hunyuan | 2026-03-06 | 14 |
| [CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation](https://arxiv.org/abs/2601.16547) | Baidu | 2026-01-23 | 10 |

</details>

<h2 id="generation">🎨 Image / Video Generation</h2>

Diffusion, flow-matching and autoregressive generators: few-step distillation, multi-teacher OPD, streaming video, editing and 3D. **45 papers**, 17 with code.

| Paper | Affiliation | Date | Code | Cited |
| :-- | :-- | :-: | :-: | :-: |
| [SenseNova-U1.5: Towards Native Unified Visual Intelligence](https://arxiv.org/abs/2609.11929) | SenseTime | 2026-09-10 | [⭐ 6.9k](https://github.com/OpenSenseNova/SenseNova-U1) | 3 |
| [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473) | Tsinghua University | 2026-06-24 | [⭐ 815](https://github.com/NVlabs/rcm) | 20 |
| [OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766) | Meituan | 2026-07-09 | [⭐ 692](https://github.com/MeiGen-AI/OPSD-V) | 12 |
| [On-Policy Self-Distillation in Diffusion Models](https://arxiv.org/abs/2608.24646) | ByteDance | 2026-08-25 | [⭐ 679](https://github.com/worldbench/DiffusionOPSD) | 5 |
| [pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation](https://arxiv.org/abs/2510.14974) | Stanford University | 2025-10-16 | [⭐ 475](https://github.com/Lakonik/piFlow) | 29 |
| [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724) | NUS | 2026-05-13 | [⭐ 441](https://github.com/NVlabs/AnyFlow) | 27 |
| [LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation](https://arxiv.org/abs/2512.23576) | SII / SJTU | 2025-12-29 | [⭐ 353](https://github.com/GAIR-NLP/LiveTalk) | 8 |
| [Flow-OPD: On-Policy Distillation for Flow Matching Models](https://arxiv.org/abs/2605.08063) | USTC | 2026-05-08 | [⭐ 313](https://github.com/CostaliyA/Flow-OPD) | 33 |
| [Scaling Properties of Text Conditioning in Visual Generation](https://arxiv.org/abs/2607.29679) | ByteDance | 2026-07-31 | [⭐ 186](https://github.com/heheyas/context-scaling) | 2 |
| [Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher](https://arxiv.org/abs/2608.26872) | Tsinghua University | 2026-08-27 | [⭐ 51](https://github.com/Shiy-Zhang/Self-OPD) | 1 |
| [CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2605.25378) | Zhejiang University | 2026-05-25 | [⭐ 32](https://github.com/Qwen-Applications/CollectionLoRA) | 3 |
| [KwaiMind Technical Report](https://arxiv.org/abs/2609.26375) | Kuaishou | 2026-09-22 | [⭐ 30](https://github.com/KwaiMmu/KwaiMind) | 0 |
| [HPSD: Hybrid-Policy Self-Distillation for Text-Image-to-Video Diffusion Models](https://arxiv.org/abs/2608.13205) | Shanghai Jiao Tong University | 2026-08-13 | [⭐ 23](https://github.com/Bujiazi/HPSD) | 2 |
| [GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models](https://arxiv.org/abs/2605.29398) | UCL | 2026-05-28 | [⭐ 22](https://github.com/GaryBall/GDSD) | 5 |
| [Adversarial Dual On-Policy Distillation from Expressive Teacher](https://arxiv.org/abs/2605.27095) | NTU | 2026-05-26 | [⭐ 12](https://github.com/vanzll/FA-OPD) | 0 |
| [Latent Reward Registers for Diffusion Preference Alignment](https://arxiv.org/abs/2608.03929) | USTC | 2026-08-04 | [⭐ 4](https://github.com/Guanys-dar/latent-reward-register) | 0 |
| [TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM](https://arxiv.org/abs/2605.09536) | Renmin University of China | 2026-05-10 | [⭐ 3](https://github.com/BHmingyang/TAD) | 2 |

<details>
<summary>📄 28 more without public code (newest first)</summary>

| Paper | Affiliation | Date | Cited |
| :-- | :-- | :-: | :-: |
| [On-Policy Self-Distillation for Multi-Turn Image Editing](https://arxiv.org/abs/2609.35611) | KAUST | 2026-09-28 | 0 |
| [G$^3$-LoRA: Organizing Reward-Weighted Video Data with Gradient-Guided Grouped LoRA](https://arxiv.org/abs/2609.35189) | HKUST (GZ) | 2026-09-28 | 0 |
| [CapField-OPD: Learning Continuous Capability Fields via Joint-Anchored Multi-Teacher On-Policy Distillation for Flow Models](https://arxiv.org/abs/2609.34658) | USTC | 2026-09-28 | 0 |
| [From Static to Dynamic: On-Policy Distillation from Image to Video Diffusion Models](https://arxiv.org/abs/2609.34371) | HKU | 2026-09-28 | 0 |
| [Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer](https://arxiv.org/abs/2609.07137) | Shanghai Jiao Tong University | 2026-09-07 | 1 |
| [OracleZoom: On-Policy Self-Distillation Inspired Reference-Constrained Recursive Image Super Resolution](https://arxiv.org/abs/2609.06490) | UMBC | 2026-09-06 | 1 |
| [Beyond Attention Masks: Instruction Anchoring for Efficient In-Context Diffusion Generation](https://arxiv.org/abs/2608.21229) | HIT | 2026-08-21 | 0 |
| [Exploring the Performance Frontier of Compact Unified Image Generation Models](https://arxiv.org/abs/2608.20334) | — | 2026-08-20 | 0 |
| [Accelerating Visual On-Policy Distillation with Batched Speculative Jacobi Rollouts](https://arxiv.org/abs/2608.18183) | HIT (Shenzhen) | 2026-08-18 | 0 |
| [TransAnyText: Translating Arbitrary Text in E-commerce Images via Structured Visual Generation](https://arxiv.org/abs/2608.16284) | Wuhan University | 2026-08-17 | 0 |
| [Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation](https://arxiv.org/abs/2608.13391) | NVIDIA | 2026-08-13 | 4 |
| [DreOPD: Degraded-Reference Extrapolative On-Policy Distillation for Flow-matching Models](https://arxiv.org/abs/2608.09233) | HIT (Shenzhen) | 2026-08-10 | 2 |
| [FlowErase-OPD: Multi-Concept Erasure via Anchored On-Policy Distillation in Flow Matching Models](https://arxiv.org/abs/2608.07620) | HIT (Shenzhen) | 2026-08-07 | 1 |
| [InsertFuse: A Unified Framework for Multi-Category Reference-Guided Image Insertion](https://arxiv.org/abs/2608.06490) | Shanghai Jiao Tong University | 2026-08-06 | 1 |
| [STEP-OPD: Rethinking Output Targets and Internal Dynamics in On-Policy Distillation for Diffusion Models](https://arxiv.org/abs/2608.04887) | Shanghai Jiao Tong University | 2026-08-05 | 2 |
| [Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Selectable Flow Models](https://arxiv.org/abs/2608.04349) | Joy Future Academy | 2026-08-05 | 3 |
| [Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via Representation-Space Bridging](https://arxiv.org/abs/2608.03316) | Joy Future Academy | 2026-08-04 | 4 |
| [Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation](https://arxiv.org/abs/2607.24731) | Alibaba | 2026-07-27 | 5 |
| [FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models](https://arxiv.org/abs/2607.24522) | Northeastern University | 2026-07-27 | 1 |
| [Qwen-Image-2.0-RL Technical Report](https://arxiv.org/abs/2606.27608) | Alibaba | 2026-06-25 | 4 |
| [MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model](https://arxiv.org/abs/2606.17800) | Catnip AI | 2026-06-16 | 4 |
| [GeoStream: Toward Precise Camera Controlled Streaming Video Generation](https://arxiv.org/abs/2606.15162) | Carnegie Mellon University | 2026-06-13 | 5 |
| [Knowledge Distillation for Visual Autoregressive Models](https://arxiv.org/abs/2606.06078) | Qualcomm AI Research | 2026-06-04 | 2 |
| [On-Policy Adversarial Flow Distillation for Autoregressive Video Generation](https://arxiv.org/abs/2605.26105) | NUS | 2026-05-25 | 3 |
| [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605) | HKUST (GZ) | 2026-05-20 | 16 |
| [DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models](https://arxiv.org/abs/2605.15055) | Fudan University | 2026-05-14 | 35 |
| [D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models](https://arxiv.org/abs/2605.05204) | HKUST | 2026-05-06 | 21 |
| [Di$\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator](https://arxiv.org/abs/2503.15457) | École Polytechnique | 2025-03-19 | 6 |

</details>

<h2 id="embodied">🤖 Embodied / VLA / World Model</h2>

VLA policies, world (action) models, driving, navigation and GUI agents supervised on their own visual trajectories. **25 papers**, 7 with code.

| Paper | Affiliation | Date | Code | Cited |
| :-- | :-- | :-: | :-: | :-: |
| [HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://arxiv.org/abs/2604.07430) | Tencent | 2026-04-08 | [⭐ 875](https://github.com/Tencent-Hunyuan/HY-Embodied) | 18 |
| [HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents](https://arxiv.org/abs/2605.07177) | Xiaohongshu | 2026-05-08 | [⭐ 76](https://github.com/DeepExperience/HyperEyes) | 12 |
| [UI-MOPD: Multi-Platform On-Policy Distillation for Unified GUI Agents](https://arxiv.org/abs/2607.04425) | Tsinghua University | 2026-07-05 | [⭐ 61](https://github.com/EliSpectre/UI-MOPD) | 6 |
| [Refined Policy Distillation: From VLA Generalists to RL Experts](https://arxiv.org/abs/2503.05833) | Univ. of Tech. Nuremberg | 2025-03-06 | [⭐ 23](https://github.com/Refined-Policy-Distillation/RPD) | 29 |
| [ME-VLM: A Unified VLM for Embodied Cognition and Agent Coordination](https://arxiv.org/abs/2609.24526) | Li Auto | 2026-09-21 | [⭐ 7](https://github.com/MachEmbodied/ME-VLM) | 0 |
| [GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving](https://arxiv.org/abs/2606.02774) | Univ. of Wisconsin-Madison | 2026-06-01 | [⭐ 2](https://github.com/gray311/CulturalDrive-Bench) | 0 |
| [FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving](https://arxiv.org/abs/2608.13395) | HIT | 2026-08-13 | [⭐ 1](https://github.com/forever-free1/FIRE-VLA) | 1 |

<details>
<summary>📄 18 more without public code (newest first)</summary>

| Paper | Affiliation | Date | Cited |
| :-- | :-- | :-: | :-: |
| [PIVOT: Pivot-Aware On Policy Self Distillation for Multi-Turn VLM Agents](https://arxiv.org/abs/2609.35303) | HKUST (GZ) | 2026-09-28 | 0 |
| [WAM-OPD: Sharpening World Action Models via On-Policy Distillation](https://arxiv.org/abs/2609.34250) | USTC | 2026-09-28 | 0 |
| [PlanGuard: A Guardrail for Multi-Step Plan Safety in Embodied Agents](https://arxiv.org/abs/2609.32801) | Anhui Key Lab of Digital Security | 2026-09-26 | 0 |
| [Learn How to Act from Your Own Interactions: On-Policy Self-Distillation for GUI Agents](https://arxiv.org/abs/2609.27307) | IIE, CAS | 2026-09-23 | 0 |
| [WAM-OPD: On-Policy Distillation for World Action Models](https://arxiv.org/abs/2608.22364) | UCL | 2026-08-23 | 2 |
| [Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation](https://arxiv.org/abs/2608.11191) | NJUST | 2026-08-11 | 1 |
| [SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation](https://arxiv.org/abs/2608.10775) | Peking University | 2026-08-11 | 2 |
| [MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation](https://arxiv.org/abs/2607.29320) | Xi'an Jiaotong University | 2026-07-31 | 3 |
| [SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation](https://arxiv.org/abs/2607.19850) | Hokkaido University | 2026-07-22 | 0 |
| [Teach it to stop, not just to click](https://arxiv.org/abs/2607.17136) | Cabal AI | 2026-07-19 | 1 |
| [ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models](https://arxiv.org/abs/2606.25800) | University of New South Wales | 2026-06-24 | 0 |
| [Scaling Self-Play for End-to-End Driving](https://arxiv.org/abs/2606.19641) | Mila | 2026-06-17 | 4 |
| [Trust the Right Teacher: Quality-Aware Self-Distillation for GUI Grounding](https://arxiv.org/abs/2606.18101) | University of Georgia | 2026-06-16 | 4 |
| [LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning](https://arxiv.org/abs/2605.07505) | Moore Threads | 2026-05-08 | 4 |
| [Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://arxiv.org/abs/2605.00642) | IIE, CAS | 2026-05-01 | 11 |
| [Co-Evolving Policy Distillation](https://arxiv.org/abs/2604.27083) | IIE, CAS | 2026-04-29 | 5 |
| [Device-Conditioned Neural Architecture Search for Efficient Robotic Manipulation](https://arxiv.org/abs/2604.10170) | HKU | 2026-04-11 | 0 |
| [VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation](https://arxiv.org/abs/2603.26666) | HKUST (GZ) | 2026-03-27 | 11 |

</details>

## Contributing

Add an entry to [`papers.json`](papers.json) and open a PR. `README.md` and `index.html` are generated by [`scripts/update_stats.py`](scripts/update_stats.py), so please do not edit them by hand. Stars come from the GitHub API and citations from Semantic Scholar, refreshed daily by [a GitHub Action](.github/workflows/refresh.yml) (last run: 2026-10-09 10:33 UTC).

## Acknowledgments

Seeded from [thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD), [chrisliu298/awesome-on-policy-distillation](https://github.com/chrisliu298/awesome-on-policy-distillation) and [nick7nlp/Awesome-LLM-On-Policy-Distillation](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation), then extended with arXiv search (🔎 marks entries found by web search). Summaries are paraphrased from abstracts and may contain errors — the papers are the reference.

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) — public-domain dedication.
