# 🖼️ Awesome Multimodal On-Policy Distillation

> A curated, **auto-refreshed** list of **multimodal On-Policy Distillation (OPD / OPSD)** papers — organized by **Image QA · Video QA · Audio QA** (plus generation, speculative decoding, and embodied/VLA).

![papers](https://img.shields.io/badge/papers-53-4E6813?style=for-the-badge) ![web--added](https://img.shields.io/badge/web--added-3-2E86C1?style=for-the-badge) ![updated](https://img.shields.io/badge/stats_updated-2026.06.18-purple?style=for-the-badge)

### 👉 [**Browse interactively (HTML)**](https://htmlpreview.github.io/?https://github.com/Jingchensun/Awesome-Multimodal-OPD/blob/main/index.html)

Open the searchable, filterable visual reader — one click, no install: **[https://htmlpreview.github.io/?https://github.com/Jingchensun/Awesome-Multimodal-OPD/blob/main/index.html](https://htmlpreview.github.io/?https://github.com/Jingchensun/Awesome-Multimodal-OPD/blob/main/index.html)**  
(If GitHub Pages is enabled for this repo, it is also served at [https://jingchensun.github.io/Awesome-Multimodal-OPD/](https://jingchensun.github.io/Awesome-Multimodal-OPD/).)

Compiled by filtering the multimodal entries of three awesome lists and augmented with web search: [thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) · [chrisliu298/awesome-on-policy-distillation](https://github.com/chrisliu298/awesome-on-policy-distillation) · [nick7nlp/Awesome-LLM-On-Policy-Distillation](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation).

**What is OPD?** `C1`: the student samples its own trajectories `y ~ π_student(·|x)` during training; `C2`: a teacher provides per-token / sequence-level supervision on those **student-generated** samples. **OPSD** is the special case where the teacher is the *same model* conditioned on privileged information.

Each paper is summarized along **four questions**: ① Problem & why it matters · ② Method & key contribution · ③ Task / dataset / model · ④ Limitations & future work. ⭐ Stars and Citations are **refreshed daily** by [a GitHub Action](.github/workflows/refresh.yml).

> 🔄 **Stats last updated: 2026-06-18 05:32 UTC** · ⭐ stars via GitHub API · Citations via Semantic Scholar (Google Scholar has no public API and is blocked in CI; see [`scripts/update_stats.py`](scripts/update_stats.py)).

## 📊 Overview

| Subfield | # |
| :-- | :--: |
| 🖼️ Image QA / VQA / Visual Reasoning | 15 |
| 🎬 Video QA / Video Reasoning / Temporal Grounding | 7 |
| 🔊 Audio QA / Speech | 7 |
| 🎨 Image / Video Generation (Diffusion · Flow) | 12 |
| ⚡ Multimodal Speculative-Decoding Distillation | 4 |
| 🤖 Embodied / VLA / GUI Visual Agents | 8 |
| **Total** | **53** |

## 🖼️ Image QA / VQA / Visual Reasoning

On-policy distillation that transfers reasoning into vision-language models and trains on VQA / visual-reasoning rollouts.

| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| VOLD — LLM→VLM OPD | [link](https://arxiv.org/abs/2510.23497) | 2025-10-27 | — | — | 11 | OPD |
| Uni-OPD — Unified OPD across LLMs & MLLMs | [link](https://arxiv.org/abs/2605.03677) | 2026-05-05 | [GitHub](https://github.com/WenjinHou/Uni-OPD) | 37 | 5 | OPD |
| Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation | [link](https://arxiv.org/abs/2605.18740) | 2026-05-18 | [GitHub](https://github.com/VisionOPD/Vision-OPD) | 130 | 2 | OPD |
| Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL | [link](https://arxiv.org/abs/2604.28123) | 2026-04-30 | [GitHub](https://github.com/XIAO4579/PRISM) | 90 | 2 | OPD |
| ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation | [link](https://arxiv.org/abs/2606.05718) | 2026-06-04 | [GitHub](https://github.com/tiankanghui/ViCuR) | 14 | 1 | OPD |
| Visual-Advantage On-Policy Distillation for Vision-Language Models | [link](https://arxiv.org/abs/2605.21924) | 2026-05-21 | — | — | 0 | OPD |
| Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding | [link](https://arxiv.org/abs/2606.00564) | 2026-05-30 | — | — | 0 | OPD |
| KEPO — Knowledge-Enhanced Preference Optimization (Medical VQA) | [link](https://arxiv.org/abs/2602.00400) | 2026-01-30 | [GitHub](https://github.com/Corleno/KEPO) | 2 | 0 | OPD+RL (semi-strict) |
| DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation | [link](https://arxiv.org/abs/2605.15532) | 2026-05-15 | — | — | 0 | OPD |
| Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization | [link](https://arxiv.org/abs/2606.09091) | 2026-06-08 | [GitHub](https://github.com/OPPO-Mente-Lab/GNDPO) | 2 | 0 | OPD |
| Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts | [link](https://arxiv.org/abs/2606.10334) | 2026-06-09 | — | — | 0 | OPD |
| Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization | [link](https://arxiv.org/abs/2606.07000) | 2026-06-05 | [GitHub](https://github.com/XszNeverSleep/PTD-PO) | 4 | 0 | OPD |
| Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation | [link](https://arxiv.org/abs/2606.08719) | 2026-06-07 | — | — | 0 | OPD |
| Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation | [link](https://arxiv.org/abs/2606.06076) | 2026-06-04 | — | — | 0 | OPD |
| 🔎 β-KD — Uncertainty-Aware Knowledge Distillation for Multimodal LLMs | [link](https://arxiv.org/abs/2603.21426) | 2026-03-22 | [GitHub](https://github.com/Jingchensun/beta-kd) | 7 | 0 | Related · not OPD (offline KD) |

<details>
<summary><b>VOLD — LLM→VLM OPD</b></summary>

`ICLR 2026` · 📅 2025-10-27 · [arXiv](https://arxiv.org/abs/2510.23497) · cited 11 · `OPD`

- **① Problem & importance**: Transferring the reasoning ability of a text-only LLM to a VLM is hard; this is the flagship recipe for VLM OPD.
- **② Method & contribution**: Cold-start SFT alignment plus a unified RL+KD scheme: GRPO with on-policy KL distillation, using a text LLM as the teacher.
- **③ Task / dataset / model**: LLM-to-VLM visual reasoning with student rollouts.
- **④ Limitations & future work**: The repo is a placeholder and reproduction is still incomplete; future work targets more modalities and larger VLMs.

</details>

<details>
<summary><b>Uni-OPD — Unified OPD across LLMs & MLLMs</b></summary>

`arXiv 2026` · 📅 2026-05-05 · [arXiv](https://arxiv.org/abs/2605.03677) · [code](https://github.com/WenjinHou/Uni-OPD) · ⭐ 37 · cited 5 · `OPD`

- **① Problem & importance**: OPD lacks a unified recipe across LLMs and MLLMs and suffers from two pain points: insufficient exploration of student states and unreliable teacher supervision; unification is valuable.
- **② Method & contribution**: A dual-view recipe: data balancing addresses insufficient exploration of information-rich student states, and margin calibration restores the order consistency of correct/incorrect trajectories to address unreliable teacher supervision; it supports strong-to-weak and cross-modal, single/multi-teacher settings.
- **③ Task / dataset / model**: LLMs and MLLMs across 5 domains / 16 benchmarks, with student rollouts.
- **④ Limitations & future work**: The recipe is fairly heavy and requires tuning multiple components; future work targets automated dual-view scheduling.

</details>

<details>
<summary><b>Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation</b></summary>

`arXiv 2026` · 📅 2026-05-18 · [arXiv](https://arxiv.org/abs/2605.18740) · [code](https://github.com/VisionOPD/Vision-OPD) · ⭐ 130 · cited 2 · `OPD`

- **① Problem & importance**: Multimodal LLMs still struggle with fine-grained visual understanding, since answers often hinge on tiny but decisive evidence within the full image; the authors observe a "region-to-global perception gap"—the same MLLM is more accurate on evidence-centric cropped images than on full images—indicating that many failures stem from difficulty focusing on relevant evidence rather than insufficient local recognition ability.
- **② Method & contribution**: The authors propose Vision-OPD, a region-to-global self-distillation framework: a crop-conditioned teacher and a full-image-conditioned student are instantiated from the same MLLM, the student generates on-policy rollouts, and the token-level next-word distribution divergence between teacher and student along these rollouts is minimized, so the model internalizes the benefits of visual zooming without an external teacher, ground-truth labels, reward verifier, or inference-time tools.
- **③ Task / dataset / model**: Targeting fine-grained visual understanding tasks for multimodal LLMs (the summary is truncated; specific datasets and base MLLM are in the original paper, code open-sourced at VisionOPD/Vision-OPD).
- **④ Limitations & future work**: Potential limitations include the dependence on how cropped evidence is obtained and its quality, applicability to tasks without explicit local evidence, and generalization to different MLLM backbones.

</details>

<details>
<summary><b>Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL</b></summary>

`arXiv 2026` · 📅 2026-04-30 · [arXiv](https://arxiv.org/abs/2604.28123) · [code](https://github.com/XIAO4579/PRISM) · ⭐ 90 · cited 2 · `OPD`

- **① Problem & importance**: In standard post-training of large multimodal models (SFT followed by RLVR), SFT introduces distribution drift that neither preserves original capabilities nor faithfully matches the supervision distribution, and in the multimodal setting perception and reasoning failures drift differently and compound during RL, so mitigating this drift is important.
- **② Method & contribution**: The authors propose the three-stage PRISM pipeline, inserting an explicit distribution-alignment stage between SFT and RLVR, modeling alignment (based on the OPD idea) as a black-box response-level adversarial game between the policy and an MoE discriminator (with perception and reasoning experts), providing decoupled corrective signals without teacher logits.
- **③ Task / dataset / model**: Targeting multimodal reasoning tasks, using 1.26M public demonstrations for SFT initialization, with the alignment stage requiring higher-fidelity supervision; specific models and benchmarks are in the original paper (summary truncated).
- **④ Limitations & future work**: Obtaining high-fidelity alignment supervision is relatively costly; future work could reduce discriminator complexity and extend to more multimodal tasks.

</details>

<details>
<summary><b>ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation</b></summary>

`arXiv 2026` · 📅 2026-06-04 · [arXiv](https://arxiv.org/abs/2606.05718) · [code](https://github.com/tiankanghui/ViCuR) · ⭐ 14 · cited 1 · `OPD`

- **① Problem & importance**: Multimodal on-policy distillation commonly uses answer-side privileged teachers, but answer-side privilege causes a train-test mismatch that induces the student to take shortcut imitation rather than genuine visually grounded reasoning, and solving this is important for reliable multimodal reasoning.
- **② Method & contribution**: The authors propose ViCuR, which replaces answer-side privilege with visual cues (question-relevant evidence in the input) and introduces a lightweight cue-recovery module that aggregates task-relevant visual evidence during prefill via dedicated sink-token cross-attention, without changing the inference interface or requiring an extra cue-generation loss.
- **③ Task / dataset / model**: Multimodal reasoning experiments on seven benchmarks using Qwen3-VL-2B and 8B as students, where ViCuR consistently brings improvements.
- **④ Limitations & future work**: The cue-recovery module depends on annotatable visual evidence at training time, and the summary does not fully address its robustness to noisy cues; future work could extend to more modalities and more complex visual reasoning scenarios.

</details>

<details>
<summary><b>Visual-Advantage On-Policy Distillation for Vision-Language Models</b></summary>

`arXiv 2026` · 📅 2026-05-21 · [arXiv](https://arxiv.org/abs/2605.21924) · cited 0 · `OPD`

- **① Problem & importance**: Addressing the under-application of on-policy distillation to VLMs: standard OPD improves student output quality but fails to strengthen reliance on visual input, so on visually critical tokens the student's predictions barely change with fine-grained visual details.
- **② Method & contribution**: The authors introduce the notion of visual advantage (VA)—the token-level log-probability gap when the teacher scores student rollouts with versus without fine-grained visual details—find that VA concentrates on a few tokens carrying visual supervision signal, and accordingly propose VA-OPD, which treats these high-VA tokens differently at both the rollout level and token level.
- **③ Task / dataset / model**: Targeting vision-language / VQA tasks, using trajectory-averaged VA reweighting at the rollout level and a token-level KL method; the specific datasets and VLM models are not stated in the summary, see the original paper.
- **④ Limitations & future work**: VA depends on the teacher's sensitivity to visual details, and the method's generalization to finer-grained visual tasks, different VLM architectures, and visual hallucination mitigation remains to be further verified.

</details>

<details>
<summary><b>Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding</b></summary>

`arXiv 2026` · 📅 2026-05-30 · [arXiv](https://arxiv.org/abs/2606.00564) · cited 0 · `OPD`

- **① Problem & importance**: This paper studies the under-explored optimization dynamics of on-policy distillation in the multimodal setting, challenging the standard practice of treating VLM distillation as a single monolithic objective.
- **② Method & contribution**: The authors mathematically decompose the distillation loss into a language-prior part and a visual-grounding part, find their gradients are nearly orthogonal, and propose Visual Gradient Steering (VGS), which dynamically redirects the update vector to prioritize the visual subspace.
- **③ Task / dataset / model**: Experiments across multiple distillation settings and challenging multimodal benchmarks (specific datasets and model names are not given in the summary) train a small reasoning VLM, where VGS significantly outperforms standard monolithic on-policy distillation.
- **④ Limitations & future work**: The gradient-orthogonality assumption and the judgment that vision is the main bottleneck may vary by task; future work could extend to more modalities and larger models and adaptively balance the language and visual subspaces.

</details>

<details>
<summary><b>KEPO — Knowledge-Enhanced Preference Optimization (Medical VQA)</b></summary>

`arXiv 2026` · 📅 2026-01-30 · [arXiv](https://arxiv.org/abs/2602.00400) · [code](https://github.com/Corleno/KEPO) · ⭐ 2 · cited 0 · `OPD+RL (semi-strict)`

- **① Problem & importance**: In medical VQA, verifiable rewards are sparse and exploration easily collapses, so pure RL struggles to improve stably, while medical settings demand very high correctness and knowledge grounding.
- **② Method & contribution**: The authors propose Knowledge-Enhanced Preference Optimization (KEPO): quality-gated on-policy distillation that applies dense teacher guidance only to high-quality trajectories, and uses teacher knowledge for hint-aware exploration to alleviate exploration collapse.
- **③ Task / dataset / model**: Medical VQA is the clear application setting; specific datasets/models are in the original paper.
- **④ Limitations & future work**: It leans toward a semi-strict OPD+RL form, relying on reliable quality gating and a teacher knowledge base; future work could extend to broader medical multimodal tasks and stricter per-token supervision.

</details>

<details>
<summary><b>DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation</b></summary>

`arXiv 2026` · 📅 2026-05-15 · [arXiv](https://arxiv.org/abs/2605.15532) · cited 0 · `OPD`

- **① Problem & importance**: Distillation can give compact VLMs strong reasoning ability, but the prompts driving distillation are usually selected by simple heuristics, and the authors find that up to 69% of prompts in standard chart/document reasoning datasets are "zero-delta"—teacher and student already induce identical answer distributions—providing little learning signal and causing the student to saturate quickly with data scale.
- **② Method & contribution**: The authors return to first principles—distillation essentially minimizes distribution divergence, so a prompt is valuable only if it exposes a teacher-student functional capability gap—use answer divergence (Δ) to quantify this gap, and propose a staged synthesis pipeline that seeds from existing datasets and actively targets student failure modes to generate better prompts, building the 200K-scale DeltaPrompts dataset.
- **③ Task / dataset / model**: Experiments on chart/document reasoning (multimodal VLM) tasks, distilling into compact VLMs (the summary is truncated; specific model names are in the original paper).
- **④ Limitations & future work**: This work focuses on prompt selection rather than the on-policy distillation mechanism itself; the computational cost of Δ estimation, transferability to other multimodal tasks, and the diversity ceiling of synthetic data are potential limitations.

</details>

<details>
<summary><b>Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization</b></summary>

`arXiv 2026` · 📅 2026-06-08 · [arXiv](https://arxiv.org/abs/2606.09091) · [code](https://github.com/OPPO-Mente-Lab/GNDPO) · ⭐ 2 · cited 0 · `OPD`

- **① Problem & importance**: On-policy distillation as a post-training paradigm outperforms RLVR that relies on sparse outcome feedback, but naive token-level distillation causes gradient instability due to magnitude mismatch from outlier states.
- **② Method & contribution**: The authors propose GNDPO (Globally Normalized Distillation Policy Optimization), which converts raw KL scores into batch-level relative advantages, thereby mitigating gradient explosion while retaining the benefits of token-level guidance.
- **③ Task / dataset / model**: Experiments on multimodal reasoning tasks, where GNDPO significantly improves training robustness and downstream performance.
- **④ Limitations & future work**: Global normalization is a practical stabilization technique, but its effect on extreme distributions or longer trajectories is not fully discussed; future work could generalize to more multimodal tasks and different teacher-student settings.

</details>

<details>
<summary><b>Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts</b></summary>

`arXiv 2026` · 📅 2026-06-09 · [arXiv](https://arxiv.org/abs/2606.10334) · cited 0 · `OPD`

- **① Problem & importance**: Code LLMs that generate visual artifacts (charts, web pages, slides) commit code before observing the rendering, often producing visual defects such as overlapping elements, clipped text, misalignment, low contrast, and overflow, lacking use of rendering feedback.
- **② Method & contribution**: The authors propose Visual-SDPO, a self-distillation policy optimization framework that distills post-render visual feedback as privileged context from a weight-sharing teacher into the coding student, introduces visually grounded code credit weighting to trace each defect to the responsible code statement and strengthen its distillation signal, and uses a sequence-level GRPO term to reward executable and visually high-quality rollouts.
- **③ Task / dataset / model**: Targeting code generation of visual artifacts (charts/web pages/slides); the summary does not specify datasets and models, see the original paper.
- **④ Limitations & future work**: Defect tracing depends on detectable visual defects mapping to code elements, and detection of complex or semantic defects may be limited; future work could extend the defect detectors and richer visual artifact types.

</details>

<details>
<summary><b>Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization</b></summary>

`arXiv 2026` · 📅 2026-06-05 · [arXiv](https://arxiv.org/abs/2606.07000) · [code](https://github.com/XszNeverSleep/PTD-PO) · ⭐ 4 · cited 0 · `OPD`

- **① Problem & importance**: Under RLVR, verifiable rewards are sparse and provide almost no token-level supervision for failed rollouts, making exploration inefficient for complex multimodal reasoning, while external-teacher distillation is costly and answer-conditioned tuning leaks answers and induces shortcut generation.
- **② Method & contribution**: The authors propose PTD-PO, which constructs structured privileged prompts from spatial attention guidance and intermediate textual reasoning steps, produces step-by-step token-distribution supervision via in-context learning, and keeps the student optimizing in the original answer-free context with its failed rollouts aligned to the prompt-augmented reference, achieving dense guidance without exposing answers.
- **③ Task / dataset / model**: Targeting multimodal reasoning tasks for large vision-language models (LVLMs); the summary does not specify datasets and models, see the original paper.
- **④ Limitations & future work**: The construction quality of privileged prompts affects supervision effectiveness, and robustness to prompt noise is not fully discussed; future work could generalize to more multimodal reasoning scenarios and different prompt sources.

</details>

<details>
<summary><b>Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation</b></summary>

`arXiv 2026` · 📅 2026-06-07 · [arXiv](https://arxiv.org/abs/2606.08719) · cited 0 · `OPD`

- **① Problem & importance**: The "thinking with images" paradigm acquires local evidence by zooming into regions and reasoning over cropped images, but it incurs redundant tool calls and longer reasoning trajectories, and intermediate crops learned from outcome rewards alone may be noisy and unfaithful to task-relevant evidence.
- **② Method & contribution**: The authors propose Imagine-OPD, an on-policy self-distillation framework where, during training, the teacher acts as a "thinking with images" reasoner receiving privileged zoomed-in evidence views derived from annotated regions and supervises the model's own "imagined" reasoning trajectories, so the model internalizes "where to look and what it would see" without actually invoking tools, requiring no external teacher or high-quality imagination demonstrations.
- **③ Task / dataset / model**: Targeting fine-grained visual reasoning tasks; the summary does not specify datasets and models, see the original paper.
- **④ Limitations & future work**: Imagination supervision relies on region annotations available at training time, and its extensibility to annotation-free settings is unclear; future work could reduce dependence on region annotations and verify the faithfulness of imagined evidence.

</details>

<details>
<summary><b>Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation</b></summary>

`arXiv 2026` · 📅 2026-06-04 · [arXiv](https://arxiv.org/abs/2606.06076) · cited 0 · `OPD`

- **① Problem & importance**: VLMs perform poorly on visual spatial planning, rooted in a modality gap between perception and reasoning (inferring latent states from pixels and then reasoning out valid actions), and bridging this gap is important for reliable visual planning.
- **② Method & contribution**: The authors propose MGSD, a two-stage modality-gap-aware self-distillation framework: a cold-start grounding stage first gives the visual student reliable state representations, then a privileged teacher uses explicit symbolic states to supervise the student's own visual rollout prefixes, transferring planning ability via on-policy distillation, with symbolic data used only for training and inference being purely visual.
- **③ Task / dataset / model**: On visual planning benchmarks, improving the macro average by 19.3% and 18.4% with 4B and 8B backbones respectively.
- **④ Limitations & future work**: The method depends on symbolic state annotations available at training time, which may be costly to obtain; future work could reduce dependence on symbolic annotations and generalize to longer-horizon planning tasks.

</details>

<details>
<summary><b>🔎 β-KD — Uncertainty-Aware Knowledge Distillation for Multimodal LLMs</b></summary>

`CVPR 2026` · 📅 2026-03-22 · [arXiv](https://arxiv.org/abs/2603.21426) · [code](https://github.com/Jingchensun/beta-kd) · ⭐ 7 · cited 0 · `Related · not OPD (offline KD)`

- **① Problem & importance**: In multimodal LLM distillation, how much the student should trust the teacher is uncertain, and uniform weighting lets noisy/unreliable teacher signals contaminate the student, so adaptive weighting is key for VLM distillation.
- **② Method & contribution**: The authors propose the uncertainty-aware β-KD: teacher signals are modeled as a Gibbs prior over student activations, and amortized optimization jointly infers the activations and weighting parameters, yielding closed-form uncertainty-aware weighting.
- **③ Task / dataset / model**: Multimodal VQA benchmarks: distilling a 1.7B student from MobileVLM-7B, and after enlarging the transfer set, the best configuration achieves up to +2.0 average points across 6 multimodal benchmarks.
- **④ Limitations & future work**: This is offline KD (not student-sampled on-policy rollouts) and can serve as a strongly related baseline for VQA distillation; future work could port this uncertainty weighting into an on-policy OPD framework.

</details>


## 🎬 Video QA / Video Reasoning / Temporal Grounding

OPD / self-distillation for video question answering, video reasoning and temporal grounding (incl. closely-related AoTD, VITAL).

| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| 🔎 VITAL / Thinking With Videos — Multimodal Tool-Augmented RL for Long Video Reasoning | [link](https://arxiv.org/abs/2508.04416) | 2025-08-06 | — | — | 66 | Contains OPD · mainly RL |
| 🔎 AoTD — Enhancing Video-LLM Reasoning via Agent-of-Thoughts Distillation | [link](https://arxiv.org/abs/2412.01694) | 2024-12-02 | [GitHub](https://github.com/zhengrongz/AoTD) | 58 | 34 | Related · not strict OPD |
| Video-OPD | [link](https://arxiv.org/abs/2602.02994) | 2026-02-03 | — | — | 8 | OPD |
| VISD: Enhancing Video Reasoning via Structured Self-Distillation | [link](https://arxiv.org/abs/2605.06094) | 2026-05-07 | — | — | 3 | OPD |
| InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning | [link](https://arxiv.org/abs/2606.12195) | 2026-06-10 | — | — | 0 | OPD |
| World Model Self-Distillation: Training World Models to Solve General Tasks | [link](https://arxiv.org/abs/2606.12072) | 2026-06-10 | — | — | 0 | OPD |
| World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning | [link](https://arxiv.org/abs/2606.03603) | 2026-06-02 | — | — | 0 | OPD |

<details>
<summary><b>🔎 VITAL / Thinking With Videos — Multimodal Tool-Augmented RL for Long Video Reasoning</b></summary>

`arXiv 2025.08` · 📅 2025-08-06 · [arXiv](https://arxiv.org/abs/2508.04416) · cited 66 · `Contains OPD · mainly RL`

- **① Problem & importance**: Video reasoning in MLLMs is crucial for VideoQA and temporal grounding, but pure text CoT has weak cross-modal interaction and is prone to hallucination on long videos / long chains.
- **② Method & contribution**: The paper proposes VITAL, an end-to-end agentic framework with a visual toolbox that densely samples video frames on demand and generates multimodal CoT; it builds the MTVR-CoT-72k (SFT) and MTVR-RL-110k (RL) datasets, proposes difficulty-aware DGRPO, and uses staged training including continual pre-training, SFT, rule-based RL, and on-policy distillation.
- **③ Task / dataset / model**: For long video understanding, it surpasses existing methods on VideoQA and temporal grounding across 11 video understanding benchmarks, especially in long-video scenarios.
- **④ Limitations & future work**: It is a complex system fusing RL where OPD is only one component, so the standalone OPD contribution is hard to disentangle; future work could ablate the independent gain of on-policy distillation.

</details>

<details>
<summary><b>🔎 AoTD — Enhancing Video-LLM Reasoning via Agent-of-Thoughts Distillation</b></summary>

`CVPR 2025` · 📅 2024-12-02 · [arXiv](https://arxiv.org/abs/2412.01694) · [code](https://github.com/zhengrongz/AoTD) · ⭐ 58 · cited 34 · `Related · not strict OPD`

- **① Problem & importance**: Video-LLMs score high on VideoQA leaderboards but lack interpretability and spatiotemporal grounding, making multi-step spatiotemporal reasoning hard.
- **② Method & contribution**: The authors propose Agent-of-Thoughts Distillation: an agent system decomposes a complex question into subtasks, invokes specialized visual models, treats the intermediate results as a chain-of-thought (CoT), and after an LLM verifies reliability, distills it into instruction tuning.
- **③ Task / dataset / model**: VideoQA, validated on multiple-choice and open-ended Video-LLM benchmarks with clear improvements.
- **④ Limitations & future work**: The CoT is generated offline by the agent and injected via instruction tuning, making it offline CoT distillation rather than strict on-policy teacher-token KL; future work could combine it with on-policy rollout supervision.

</details>

<details>
<summary><b>Video-OPD</b></summary>

`arXiv 2026` · 📅 2026-02-03 · [arXiv](https://arxiv.org/abs/2602.02994) · cited 8 · `OPD`

- **① Problem & importance**: Video temporal grounding requires strong reasoning, and multimodal OPD is scarce; bringing OPD to video is valuable.
- **② Method & contribution**: Token-level KL on student rollouts with an LLM teacher, for temporal video grounding.
- **③ Task / dataset / model**: Temporal video grounding (MLLM student), with student rollouts.
- **④ Limitations & future work**: Video-domain specific; future work targets long videos and multiple events.

</details>

<details>
<summary><b>VISD: Enhancing Video Reasoning via Structured Self-Distillation</b></summary>

`arXiv 2026` · 📅 2026-05-07 · [arXiv](https://arxiv.org/abs/2605.06094) · cited 3 · `OPD`

- **① Problem & importance**: Training a VideoLLM for complex reasoning is hampered by sparse sequence-level rewards and the lack of fine-grained credit assignment over long-horizon reasoning trajectories, since RLVR supervision is reliable but cannot capture token-level contributions, making improved supervision for video reasoning important.
- **② Method & contribution**: The authors propose VISD, a structured self-distillation framework that uses a video-aware discriminative model to decompose reasoning quality into multidimensional privileged information such as answer correctness, logical consistency, and spatiotemporal grounding to guide the teacher policy in providing token-level supervision, and uses a direction-magnitude decoupling mechanism (reward-computed advantage sets the direction, structured privileged signals modulate the magnitude) to stably fuse dense supervision with RL.
- **③ Task / dataset / model**: Targeting video reasoning tasks using a VideoLLM; specific datasets are in the original paper (summary truncated).
- **④ Limitations & future work**: It depends on the quality of the video-aware discriminative model and the multidimensional decomposition design; future work could extend to more video understanding tasks and more efficient discriminators.

</details>

<details>
<summary><b>InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning</b></summary>

`arXiv 2026` · 📅 2026-06-10 · [arXiv](https://arxiv.org/abs/2606.12195) · cited 0 · `OPD`

- **① Problem & importance**: Foundation models are shifting toward agentic behavior involving multi-step reasoning and tool use, but most open-source work focuses on text-dominated settings and under-explores long-horizon multimodal (especially video) tasks.
- **② Method & contribution**: The authors propose InternVideo3, which models long video understanding as closed-loop evidence accumulation and verification over a shared evolving context via multimodal contextual reasoning (MCR), and introduces M²LA (multimodal multi-head latent attention) to compress the KV-cache while retaining the full token stream, with staged training including continual pre-training, short-to-long SFT, rule-based RL, and on-policy distillation.
- **③ Task / dataset / model**: Experiments on video understanding benchmarks such as Video-MME, MLVU, and EgoSchema achieve strong performance, and it is instantiated as a video agent.
- **④ Limitations & future work**: On-policy distillation is only one stage of its multi-stage training and the summary does not analyze its contribution separately; as an industrial-scale system it has many components and high training cost, and future work could streamline the pipeline and extend more video agent capabilities.

</details>

<details>
<summary><b>World Model Self-Distillation: Training World Models to Solve General Tasks</b></summary>

`arXiv 2026` · 📅 2026-06-10 · [arXiv](https://arxiv.org/abs/2606.12072) · cited 0 · `OPD`

- **① Problem & importance**: Pre-trained video generators are promising visual world models that exhibit emergent task-solving ability, but reliance on detailed text descriptions limits their direct use for planning and decision-making, while supervised fine-tuning requires expensive, hard-to-scale paired task-execution videos.
- **② Method & contribution**: The authors propose a scalable framework combining self-distillation and reinforcement learning: a VLM generates candidate tasks and step-by-step solutions from unlabeled scene images, these solutions condition a pre-trained video diffusion model (the demonstrator), whose behavior is then distilled into an executor conditioned only on the image and a short task prompt, and the executor is further improved via reinforcement learning with VLM feedback.
- **③ Task / dataset / model**: Targeting general task solving for world models / video generation, with unlabeled scene images as input; the summary does not specify exact datasets, see the original paper.
- **④ Limitations & future work**: The method relies on a VLM to generate tasks and judge quality, which may introduce VLM bias; future work could improve task generation quality and extend to more complex real-world decision-making scenarios.

</details>

<details>
<summary><b>World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning</b></summary>

`arXiv 2026` · 📅 2026-06-02 · [arXiv](https://arxiv.org/abs/2606.03603) · cited 0 · `OPD`

- **① Problem & importance**: This paper studies the complementarity of world models and multimodal LLMs in predicting the future from static visual observations, where the key challenges are deciding when to use visual simulation, whether the rollout is trustworthy, and how it affects the final answer.
- **② Method & contribution**: The authors formalize this as controlled concrete reasoning and propose Privileged-Future On-Policy Self-Distillation (PF-OPSD): during training, ground-truth future videos and answers are used only as privileged teacher-side context to evaluate on-policy concrete reasoning trajectories, while the deployable student does not observe the true future at test time.
- **③ Task / dataset / model**: They build two human-verified benchmarks, VRQABench (controlled spatial lookahead) and OpenWorldQA (open-domain physical prediction), for evaluation (the summary does not give specific model names).
- **④ Limitations & future work**: It relies on ground-truth future videos as privileged information, which is costly to obtain, and the tasks are limited to these two benchmarks; future work could extend to more physical prediction scenarios and reduce reliance on true-future annotations.

</details>


## 🔊 Audio QA / Speech

Cross-modal transfer of text reasoning into audio/speech, and OPD for audio understanding / ASR.

| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| Qwen3-Omni Technical Report | [link](https://arxiv.org/abs/2509.17765) | 2025-09-22 | — | — | 317 | OPD |
| Qwen3.5-Omni | [link](https://arxiv.org/abs/2604.15804) | 2026-04-17 | — | — | 45 | OPD |
| Step-Audio-R1 | [link](https://arxiv.org/abs/2511.15848) | 2025-11-19 | [GitHub](https://github.com/stepfun-ai/Step-Audio-R1) | 677 | 28 | OPD |
| X-OPD — Speech LLM | [link](https://arxiv.org/abs/2603.24596) | 2026-03-06 | — | — | 5 | OPD |
| CORD — Reasoning: Text ➡️ Audio | [link](https://arxiv.org/abs/2601.16547) | 2026-01-23 | — | — | 4 | OPD |
| Data-Efficient On-Policy Distillation for Automatic Speech Recognition | [link](https://arxiv.org/abs/2605.28139) | 2026-05-27 | — | — | 0 | OPD |
| OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing | [link](https://arxiv.org/abs/2606.15920) | 2026-06-14 | — | — | 0 | OPD |

<details>
<summary><b>Qwen3-Omni Technical Report</b></summary>

`arXiv.org` · 📅 2025-09-22 · [arXiv](https://arxiv.org/abs/2509.17765) · cited 317 · `OPD`

- **① Problem & importance**: How to use a single multimodal model to simultaneously reach SOTA on text, image, audio, and video without performance degradation relative to single-modality versions is an important problem for building unified omni-modal large models.
- **② Method & contribution**: The authors propose Qwen3-Omni, which uses a Thinker-Talker MoE architecture to unify perception and generation; the Talker uses a multi-codebook scheme to autoregressively predict discrete speech codes to reduce first-packet latency, and replaces block-wise diffusion with a lightweight causal ConvNet for streaming synthesis.
- **③ Task / dataset / model**: Experiments on 36 audio and audio-video benchmarks achieve open-source SOTA on 32 and overall SOTA on 22, surpassing closed-source models such as Gemini-2.5-Pro, Seed-ASR, and GPT-4o-Transcribe, and support text interaction in 119 languages.
- **④ Limitations & future work**: As a comprehensive technical report, some capabilities (e.g., speech generation in only 10 languages) have limited coverage; future work could extend to more languages and lower-latency real-time interaction.

</details>

<details>
<summary><b>Qwen3.5-Omni</b></summary>

`arXiv 2026` · 📅 2026-04-17 · [arXiv](https://arxiv.org/abs/2604.15804) · cited 45 · `OPD`

- **① Problem & importance**: How can text reasoning be transferred to reasoning over audio inputs? Cross-modal OPD is important for omni-modal models.
- **② Method & contribution**: Cross-modal on-policy distillation transfers text reasoning capabilities into reasoning over audio inputs, using Thinker-Talker + Hybrid Attention MoE.
- **③ Task / dataset / model**: Audio / audio-video: SOTA on 215 sub-tasks, 256k context, including ARIA streaming stability and 10-language speech generation.
- **④ Limitations & future work**: The omni-modal system is complex. Future: lower-latency streaming and more modalities.

</details>

<details>
<summary><b>Step-Audio-R1</b></summary>

`arXiv 2025` · 📅 2025-11-19 · [arXiv](https://arxiv.org/abs/2511.15848) · [code](https://github.com/stepfun-ai/Step-Audio-R1) · ⭐ 677 · cited 28 · `OPD`

- **① Problem & importance**: Audio reasoning models lack a self-improvement mechanism; iterative self-distillation is meaningful for audio.
- **② Method & contribution**: Iterative self-distillation + SFT + PPO/RLVR, using only audio-related questions for self-distillation, a modality-grounded self.
- **③ Task / dataset / model**: For audio reasoning tasks, along the student rollout.
- **④ Limitations & future work**: Audio-domain specific; iteration cost; future work: cross-modal joint reasoning.

</details>

<details>
<summary><b>X-OPD — Speech LLM</b></summary>

`arXiv 2026` · 📅 2026-03-06 · [arXiv](https://arxiv.org/abs/2603.24596) · cited 5 · `OPD`

- **① Problem & importance**: Aligning the capabilities of speech LLMs is difficult; cross-modal transfer of text-LLM capabilities into speech LLMs is important.
- **② Method & contribution**: Cross-modal token-level KL, with the text LLM as teacher, is used to align speech-LLM capabilities.
- **③ Task / dataset / model**: Speech-LLM tasks, with student rollout.
- **④ Limitations & future work**: Speech-domain specific. Future: more languages and downstream speech tasks.

</details>

<details>
<summary><b>CORD — Reasoning: Text ➡️ Audio</b></summary>

`arXiv 2026` · 📅 2026-01-23 · [arXiv](https://arxiv.org/abs/2601.16547) · cited 4 · `OPD`

- **① Problem & importance**: Text reasoning ability is hard to transfer to audio; cross-model reasoning alignment matters.
- **② Method & contribution**: Token-level reverse-KL + sequence-level KL + GRPO, with its own text, aligning cross-model reasoning.
- **③ Task / dataset / model**: For text-to-audio reasoning, along the student rollout.
- **④ Limitations & future work**: Alignment quality depends on the text side; future work: broader audio tasks.

</details>

<details>
<summary><b>Data-Efficient On-Policy Distillation for Automatic Speech Recognition</b></summary>

`arXiv 2026` · 📅 2026-05-27 · [arXiv](https://arxiv.org/abs/2605.28139) · cited 0 · `OPD`

- **① Problem & importance**: Addressing the problem that building competitive automatic speech recognition (ASR) models typically requires large-scale audio supervision and incurs high reproduction and specialization costs, this work explores whether a strong teacher can transfer additional recognition capability via On-Policy distillation.
- **② Method & contribution**: The authors study Ark-ASR, a 0.6B-parameter audio-conditioned language model trained on 100k hours of speech, using On-Policy distillation to let the strong Qwen-ASR teacher provide supervision on student-generated transcripts, and analyze teacher-student local compatibility via support-overlap diagnostics.
- **③ Task / dataset / model**: On Chinese-English ASR benchmarks, the proposed training recipe consistently outperforms pure SFT and surpasses the same-size Qwen3-ASR-0.6B baseline on four of five evaluation sets, using only 100k hours of speech (versus the 20M hours reported for the Qwen3-Omni AuT encoder), while the larger Qwen3-ASR-1.7B remains stronger.
- **④ Limitations & future work**: A gap remains between the compact student and the larger teacher; the method's potential to further close this gap on more languages, noisy/accented scenarios, and smaller audio budgets remains to be explored.

</details>

<details>
<summary><b>OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing</b></summary>

`arXiv 2026` · 📅 2026-06-14 · [arXiv](https://arxiv.org/abs/2606.15920) · cited 0 · `OPD`

- **① Problem & importance**: Reinforcement learning for multimodal large models often suffers from sparse rewards in complex reasoning, especially in human-centric scenarios involving state, emotion, intention, and behavior; high-quality CoT annotations are expensive and scarce, while directly SFT-ing on ground-truth labels induces perception shortcuts and lacks transparency for safety-critical human-machine interaction.
- **② Method & contribution**: The authors propose OmniOPSD (rationale-privileged on-policy self-distillation), which uses evidence-aware rationales generated by a frontier model only as training-time teacher-side privileged evidence context rather than as a student imitation target; the student samples its own rollout from the raw multimodal input, and the rationale-privileged teacher scores the same tokens to provide dense supervision.
- **③ Task / dataset / model**: Targeting affective computing / human-centric multimodal reasoning tasks; the summary does not specify the datasets and models, see the original paper.
- **④ Limitations & future work**: It relies on a frontier model to generate high-quality rationales, and rationale quality affects supervision; future work could reduce dependence on frontier models and extend to more human-centric multimodal scenarios.

</details>


## 🎨 Image / Video Generation (Diffusion · Flow)

OPD / self-distillation for diffusion and flow-matching generative models (few-step generation, trajectory self-distillation, adversarial distillation).

| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| π-Flow — Image / Flow OPD | [link](https://arxiv.org/abs/2510.14974) | 2025-10-16 | [GitHub](https://github.com/Lakonik/piFlow) | 440 | 18 | OPD |
| Di$\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator | [link](https://arxiv.org/abs/2503.15457) | 2025-03-19 | — | — | 5 | OPD |
| LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation | [link](https://arxiv.org/abs/2512.23576) | 2025-12-29 | — | — | 5 | OPD |
| Flow-OPD: On-Policy Distillation for Flow Matching Models | [link](https://arxiv.org/abs/2605.08063) | 2026-05-08 | — | — | 3 | OPD |
| D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models | [link](https://arxiv.org/abs/2605.05204) | 2026-05-06 | — | — | 3 | OPD |
| DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models | [link](https://arxiv.org/abs/2605.15055) | 2026-05-14 | — | — | 1 | OPD |
| AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation | [link](https://arxiv.org/abs/2605.13724) | 2026-05-13 | — | — | 1 | OPD |
| TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM | [link](https://arxiv.org/abs/2605.09536) | 2026-05-10 | [GitHub](https://github.com/BHmingyang/TAD) | 2 | 0 | OPD |
| GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models | [link](https://arxiv.org/abs/2605.29398) | 2026-05-28 | — | — | 0 | OPD |
| CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation | [link](https://arxiv.org/abs/2605.25378) | 2026-05-25 | — | — | 0 | OPD |
| Adversarial Dual On-Policy Distillation from Expressive Teacher | [link](https://arxiv.org/abs/2605.27095) | 2026-05-26 | — | — | 0 | OPD |
| Knowledge Distillation for Visual Autoregressive Models | [link](https://arxiv.org/abs/2606.06078) | 2026-06-04 | — | — | 0 | OPD |

<details>
<summary><b>π-Flow — Image / Flow OPD</b></summary>

`ICLR 2026` · 📅 2025-10-16 · [arXiv](https://arxiv.org/abs/2510.14974) · [code](https://github.com/Lakonik/piFlow) · ⭐ 440 · cited 18 · `OPD`

- **① Problem & importance**: Multi-step sampling in flow/diffusion models is slow, and distillation often departs from the student's own trajectory; strict OPD on diffusion is valuable.
- **② Method & contribution**: The student predicts a policy at each time step along its own trajectory and distills via L2 imitation of the teacher velocity field (a diffusion-version strict OPD).
- **③ Task / dataset / model**: For image generation (flow models), along the student trajectory.
- **④ Limitations & future work**: Limited to the flow/diffusion framework; future work: fewer steps, broader text-to-image benchmarks.

</details>

<details>
<summary><b>Di$\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator</b></summary>

`arXiv 2025` · 📅 2025-03-19 · [arXiv](https://arxiv.org/abs/2503.15457) · cited 5 · `OPD`

- **① Problem & importance**: The paper addresses the problem that masked diffusion models (MDMs) require multi-step inference and are slow.
- **② Method & contribution**: The authors propose Di[M]O, which distills an MDM into a one-step generator: it optimizes output logits via token-level distribution matching in an on-policy framework with an auxiliary model, and uses a token initialization strategy to inject randomness, solving the lack of entropy in the initial distribution.
- **③ Task / dataset / model**: Experiments on class-conditional and text-conditional image generation achieve performance comparable to the multi-step teacher while greatly reducing inference time; the summary does not give specific dataset names, and it is the first to achieve one-step MDM distillation and discrete text-to-image distillation.
- **④ Limitations & future work**: The limitation is its focus on image generation; future work could generalize to more modalities and higher-resolution generation.

</details>

<details>
<summary><b>LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation</b></summary>

`arXiv.org` · 📅 2025-12-29 · [arXiv](https://arxiv.org/abs/2512.23576) · cited 5 · `OPD`

- **① Problem & importance**: Real-time video generation with diffusion models is crucial for building general multimodal interactive AI systems, but iterative denoising of all frames under bidirectional attention hinders real-time interaction, and existing distillation methods mostly focus on text-to-video with unnatural human-machine interaction.
- **② Method & contribution**: Targeting real-time interactive video diffusion under multimodal context (text, image, audio), the authors find that the leading on-policy distillation method Self Forcing suffers from flickering, black frames, and quality degradation under multimodal conditions, and propose an improved distillation recipe emphasizing conditioning input quality and the initialization and scheduling of on-policy optimization.
- **③ Task / dataset / model**: Experiments on multimodal-conditioned (audio, image, text) avatar video generation, using the HDTF, AVSpeech, and CelebV-HQ benchmarks, see the original paper.
- **④ Limitations & future work**: The method focuses on avatar video, and its stability in more open scenarios or longer-horizon generation remains to be verified; future work could extend to more general real-time multimodal generation.

</details>

<details>
<summary><b>Flow-OPD: On-Policy Distillation for Flow Matching Models</b></summary>

`arXiv 2026` · 📅 2026-05-08 · [arXiv](https://arxiv.org/abs/2605.08063) · cited 3 · `OPD`

- **① Problem & importance**: Existing Flow Matching text-to-image models face sparse scalar rewards and gradient interference from jointly optimizing heterogeneous objectives under multi-task alignment, leading to a metric 'seesaw effect' and reward hacking.
- **② Method & contribution**: The paper proposes Flow-OPD, the first unified post-training framework integrating on-policy distillation into Flow Matching: it first trains single-reward GRPO domain-expert teachers, then establishes an initial policy via Flow cold-start, integrates heterogeneous expertise into a single student through on-policy sampling, task-routing annotation, and dense trajectory supervision, and introduces Manifold Anchor Regularization for anchoring.
- **③ Task / dataset / model**: Experiments on text-to-image (multi-task alignment); the summary does not specify exact datasets and model names, see the original paper.
- **④ Limitations & future work**: The two-stage pipeline relies on training multiple expert teachers, is costly, and is sensitive to task-routing accuracy; future work could extend to more generative modalities and more efficient expert integration.

</details>

<details>
<summary><b>D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models</b></summary>

`arXiv 2026` · 📅 2026-05-06 · [arXiv](https://arxiv.org/abs/2605.05204) · cited 3 · `OPD`

- **① Problem & importance**: High-performance image generation is shifting from inefficient multi-step models to efficient few-step models (e.g., Z-Image-Turbo, FLUX.2-klein), but directly applying continual SFT to these models harms their few-step inference ability, so addressing continual fine-tuning is important.
- **② Method & contribution**: The authors propose D-OPSD, which leverages the contextual ability inherited by modern diffusion models (with LLM/VLM as encoders) and formulates training as on-policy self-distillation: the same model serves as both teacher and student, the student is conditioned only on text features while the teacher is conditioned on multimodal features of text + target image, minimizing the two predicted distributions on the student's own rollout.
- **③ Task / dataset / model**: For image-generation fine-tuning of step-distilled diffusion models, involving few-step models such as Z-Image-Turbo and FLUX.2-klein; specific benchmarks are in the original paper (the summary is truncated).
- **④ Limitations & future work**: The method relies on the encoder's multimodal contextual ability and is limited in scope by model architecture; future work could generalize to more few-step generative models and tasks.

</details>

<details>
<summary><b>DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models</b></summary>

`arXiv 2026` · 📅 2026-05-14 · [arXiv](https://arxiv.org/abs/2605.15055) · cited 1 · `OPD`

- **① Problem & importance**: Although RL can improve diffusion text-to-image models, existing methods are mostly limited to single-task optimization; extending to multi-task suffers from cross-task interference and imbalance in joint optimization, while cascaded RL is cumbersome and prone to catastrophic forgetting.
- **② Method & contribution**: The authors propose DiffusionOPD, which first trains task-specific teachers independently and then distills them into a unified student along the student's own rollout trajectory, decoupling single-task exploration from multi-task integration; theoretically it lifts OPD from discrete tokens to a continuous-state Markov process, derives a closed-form step-wise KL objective unifying SDE and ODE, and proves this analytic gradient has lower variance and better generalization than PPO-style policy gradients.
- **③ Task / dataset / model**: For multi-task training of diffusion text-to-image models (the summary is truncated; specific datasets and base models are in the original paper).
- **④ Limitations & future work**: The method needs to first train multiple task-specific teachers, and the effect of teacher quality and quantity on the final student, along with scalability to more tasks and larger models, are potential limitations.

</details>

<details>
<summary><b>AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation</b></summary>

`arXiv 2026` · 📅 2026-05-13 · [arXiv](https://arxiv.org/abs/2605.13724) · cited 1 · `OPD`

- **① Problem & importance**: Few-step video generation has progressed via consistency distillation, but consistency-distilled models degrade when allocated more sampling steps at test time, limiting 'any-step' video diffusion; the root cause is that consistency sampling trajectories replace the original probability-flow ODE trajectory, weakening test-time scaling behavior.
- **② Method & contribution**: The authors propose AnyFlow, the first flow-map-based any-step video diffusion distillation framework that changes the distillation target from endpoint consistency mapping to flow-map transfer over arbitrary time intervals, and proposes 'flow-map reverse simulation' to decompose the full Euler rollout into shortcut flow-map transfers, enabling efficient on-policy distillation to reduce test-time discretization error and exposure bias.
- **③ Task / dataset / model**: Targeting few-step / any-step video diffusion generation (the summary does not give specific datasets and base model names, see the original paper).
- **④ Limitations & future work**: The summary gives no quantitative results, and the method's performance across different video backbones, higher resolution, and longer videos, as well as its training cost, remain to be evaluated.

</details>

<details>
<summary><b>TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM</b></summary>

`arXiv 2026` · 📅 2026-05-10 · [arXiv](https://arxiv.org/abs/2605.09536) · [code](https://github.com/BHmingyang/TAD) · ⭐ 2 · cited 0 · `OPD`

- **① Problem & importance**: Diffusion large language models (dLLMs) offer parallel text generation potential but face an accuracy-parallelism trade-off, where increasing tokens per forward (TPF) often degrades generation quality, and existing acceleration methods mostly trade accuracy for speed.
- **② Method & contribution**: The paper proposes TAD (Temporal-Aware trajectory self-Distillation): the teacher generates a decoding trajectory conditioned on the prompt and ground-truth response and records intermediate masked states, partitions masked positions into near/far subsets by remaining steps to reveal, supervises near tokens with hard cross-entropy and far tokens with soft KL, naturally forming a temporal-aware partition and two deployment configurations.
- **③ Task / dataset / model**: Experiments on parallel text generation of diffusion large language models; the summary does not specify exact datasets and base models, see the original paper (repo BHmingyang/TAD).
- **④ Limitations & future work**: It relies on constructing teacher trajectories under ground-truth conditions, requires setting near/far partition thresholds, and its generalization to unseen distributions remains to be verified; future work could extend to more dLLMs and longer generation tasks.

</details>

<details>
<summary><b>GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models</b></summary>

`arXiv 2026` · 📅 2026-05-28 · [arXiv](https://arxiv.org/abs/2605.29398) · cited 0 · `OPD`

- **① Problem & importance**: While RL can improve the denoiser policy of diffusion large language models (dLLMs), the policy likelihood is intractable, and mainstream methods substitute an ELBO for the likelihood, which introduces bias from training-inference mismatch and harms performance.
- **② Method & contribution**: The authors propose Guided Denoiser Self-Distillation (GDSD), which directly distills the dLLM denoiser from an advantage-guided self-teacher (derived from the closed-form optimal solution of reverse-KL-regularized RL), matching denoiser logits to the teacher with an unnormalized objective, turning RL into likelihood-free self-distillation to bypass training-inference mismatch bias, and shows recent ELBO methods are a special case under a different distillation divergence.
- **③ Task / dataset / model**: Evaluated on planning, math, and code benchmarks with LLaDA-8B and Dream-7B, GDSD consistently outperforms prior state-of-the-art methods.
- **④ Limitations & future work**: The method targets the specific paradigm of diffusion language models, and its advantages and scalability on larger dLLMs, more tasks, and against RL on autoregressive models remain to be further verified.

</details>

<details>
<summary><b>CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation</b></summary>

`arXiv 2026` · 📅 2026-05-25 · [arXiv](https://arxiv.org/abs/2605.25378) · cited 0 · `OPD`

- **① Problem & importance**: In customized image editing, as the number of desired effects grows, storing and dynamically loading many effect LoRAs incurs deployment overhead, and cascading with acceleration modules causes parameter interference, concept crosstalk, and style degradation.
- **② Method & contribution**: The authors propose CollectionLoRA, a multi-teacher on-policy distillation framework that distills the concepts of up to 50 effect LoRAs together with few-step generation ability into a single LoRA, and introduces mechanisms such as probabilistic dual-stream routing, asymmetric orthogonal prompts, and coarse-to-fine distillation to resolve feature interference.
- **③ Task / dataset / model**: Targeting customized image editing / visual effects for diffusion models, distilling 50 effects into a single LoRA; specific diffusion models and datasets are not fully detailed in the summary, see the original paper.
- **④ Limitations & future work**: The method targets a preset set of effects, and its generalization and quality ceiling for further scaling the number of effects, unseen effect combinations, and different diffusion backbones remain to be examined.

</details>

<details>
<summary><b>Adversarial Dual On-Policy Distillation from Expressive Teacher</b></summary>

`arXiv 2026` · 📅 2026-05-26 · [arXiv](https://arxiv.org/abs/2605.27095) · cited 0 · `OPD`

- **① Problem & importance**: In embodied control, learning from demonstrations is often modeled as behavior cloning; although diffusion/flow-matching policies model multimodal expert actions, they remain offline supervised learners that get no corrective signal on actually visited states, while standard OPD assumes an unavailable strong fixed teacher.
- **② Method & contribution**: The authors propose FA-OPD, an adversarial dual on-policy distillation method: a flow-matching (FM) teacher learned from demonstrations is co-trained with a lightweight MLP student, where the teacher provides two complementary signals on the student's rollout: a reward channel (an expert-similarity objective driving online exploration) and an action channel (dense local targets at student-visited states to stabilize exploitation).
- **③ Task / dataset / model**: Targeting embodied control / learning-from-demonstration agent tasks; specific simulation environments and datasets are not fully detailed in the summary, see the original paper.
- **④ Limitations & future work**: The teacher itself is learned from limited demonstrations rather than being a strong fixed teacher, so its quality is bounded by demonstration coverage, and the method's stability on real robots, long-horizon complex tasks, and higher-dimensional action spaces remains to be verified.

</details>

<details>
<summary><b>Knowledge Distillation for Visual Autoregressive Models</b></summary>

`arXiv 2026` · 📅 2026-06-04 · [arXiv](https://arxiv.org/abs/2606.06078) · cited 0 · `OPD`

- **① Problem & importance**: Autoregressive image generation models are highly expressive but computationally expensive and need effective compression, yet the behavior of knowledge distillation in visual autoregressive generation has not been well studied.
- **② Method & contribution**: The authors first systematically study distillation strategies for AR image models, finding that language-domain methods do not transfer directly (long decoding horizons and visual token ambiguity make teacher supervision unreliable), and propose VarKD, which distills on student samples, selectively applies teacher supervision, and reduces token-level ambiguity.
- **③ Task / dataset / model**: On ImageNet across multiple AR backbones for image generation, VarKD consistently outperforms prior distillation baselines and narrows the gap to large-scale models.
- **④ Limitations & future work**: The method is designed for image token ambiguity, and its applicability across other generative modalities (e.g., video) is not verified; future work could extend to larger-scale or multimodal autoregressive generation.

</details>


## ⚡ Multimodal Speculative-Decoding Distillation

Training on-policy draft models for vision-language models to speed up inference.

| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding | [link](https://arxiv.org/abs/2509.15235) | 2025-09-17 | — | — | 15 | OPD |
| Speculative Decoding Reimagined for Multimodal Large Language Models | [link](https://arxiv.org/abs/2505.14260) | 2025-05-20 | — | — | 6 | OPD |
| SpecVLM: Fast Speculative Decoding in Vision-Language Models | [link](https://arxiv.org/abs/2509.11815) | 2025-09-15 | — | — | 4 | OPD |
| MASSV — Multimodal SD Draft | [link](https://arxiv.org/abs/2505.10526) | 2025-05-15 | — | — | 0 | OPD |

<details>
<summary><b>ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding</b></summary>

`arXiv.org` · 📅 2025-09-17 · [arXiv](https://arxiv.org/abs/2509.15235) · cited 15 · `OPD`

- **① Problem & importance**: Speculative decoding is widely used on LLMs but underexplored on VLMs, where existing methods achieve limited speedups (under 1.5x); closing this gap is important as multimodal capabilities become increasingly central.
- **② Method & contribution**: The authors propose ViSpec, vision-aware speculative decoding, which uses a lightweight vision adapter to compress image tokens into compact representations integrated into the draft model's attention while preserving positional information, and extracts a global feature vector per image to enhance multimodal coherence of subsequent text tokens.
- **③ Task / dataset / model**: Experiments on vision-language model inference acceleration, with a dedicated training set containing long assistant responses built by adapting existing datasets; the summary does not specify the VLM names, see the original paper.
- **④ Limitations & future work**: It relies on the assumption that vision tokens can be effectively filtered layer-by-layer, and constructing the dedicated long-response dataset has some cost; future work could extend to video and draft-model design for more modalities.

</details>

<details>
<summary><b>Speculative Decoding Reimagined for Multimodal Large Language Models</b></summary>

`arXiv.org` · 📅 2025-05-20 · [arXiv](https://arxiv.org/abs/2505.14260) · cited 6 · `OPD`

- **① Problem & importance**: Speculative decoding can accelerate LLM inference without loss of accuracy, but existing methods cannot achieve comparable speedups on multimodal large language models (MLLMs); how to redesign speculative decoding for MLLMs is important.
- **② Method & contribution**: The authors propose multimodal speculative decoding (MSD) based on two principles: text and vision tokens have different characteristics and should be processed separately in the draft stage, and the draft model needs both language modeling and visual perception capabilities; they adopt two-stage training (first text instruction tuning, then progressively introducing multimodal data).
- **③ Task / dataset / model**: Experiments on multimodal large language model (MLLM) inference acceleration; the summary does not specify the datasets and model names, see the original paper.
- **④ Limitations & future work**: The method centers on draft-model design, and two-stage training with text/vision decoupling may add training complexity; future work could explore more modalities and more general draft architectures.

</details>

<details>
<summary><b>SpecVLM: Fast Speculative Decoding in Vision-Language Models</b></summary>

`arXiv.org` · 📅 2025-09-15 · [arXiv](https://arxiv.org/abs/2509.11815) · cited 4 · `OPD`

- **① Problem & importance**: Speculative decoding can accelerate autoregressive LLMs, but porting it directly to vision-language models (VLMs) faces system constraints such as vision tokens dominating prefill and KV-cache bloat, requiring designs tailored to VLMs.
- **② Method & contribution**: The authors propose the SpecVLM system, which establishes an EAGLE-2-style strong baseline EagleVLM, introduces an elastic visual compressor that adaptively selects pruning/pooling/convolution/resampling primitives, and proposes an online logit distillation protocol that trains the draft model with real-time teacher logits and penultimate-layer features using a cross-entropy plus Smooth L1 objective, avoiding offline distillation corpora.
- **③ Task / dataset / model**: Experiments on vision-language model inference acceleration achieve 1.5-2.3x end-to-end speedup over full autoregressive inference; the summary does not specify the VLM benchmark names, see the original paper.
- **④ Limitations & future work**: The training-time scaling effect of online distillation requires longer training, and the elastic compressor's primitive-selection strategy may add system complexity; future work could extend to video and longer-context scenarios.

</details>

<details>
<summary><b>MASSV — Multimodal SD Draft</b></summary>

`arXiv 2025` · 📅 2025-05-15 · [arXiv](https://arxiv.org/abs/2505.10526) · cited 0 · `OPD`

- **① Problem & importance**: Multimodal models lack adapted draft models for speculative decoding; multimodal SD drafting is valuable.
- **② Method & contribution**: KD CE on a multimodal draft model, with on-policy draft sampling.
- **③ Task / dataset / model**: Multimodal inference acceleration, with draft sampling.
- **④ Limitations & future work**: Multimodal alignment is difficult. Future: more modalities and larger targets.

</details>


## 🤖 Embodied / VLA / GUI Visual Agents

The student is a visual agent or VLA policy supervised on its own visual trajectories.

| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| Refined Policy Distillation (RPD) | [link](https://arxiv.org/abs/2503.05833) | 2025-03-06 | [GitHub](https://github.com/Refined-Policy-Distillation/RPD) | 20 | 17 | OPD |
| HY-Embodied-0.5 | [link](https://arxiv.org/abs/2604.07430) | 2026-04-08 | [GitHub](https://github.com/Tencent-Hunyuan/HY-Embodied) | 749 | 4 | OPD |
| VLA-OPD | [link](https://arxiv.org/abs/2603.26666) | 2026-03-27 | — | — | 3 | OPD |
| HyperEyes — Parallel Multimodal Search Agent | [link](https://arxiv.org/abs/2605.07177) | 2026-05-08 | [GitHub](https://github.com/DeepExperience/HyperEyes) | 62 | 1 | OPD |
| CoPD — Co-Evolving Policy Distillation | [link](https://arxiv.org/abs/2604.27083) | 2026-04-29 | — | — | 1 | OPD |
| Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding | [link](https://arxiv.org/abs/2605.00642) | 2026-05-01 | — | — | 1 | OPD |
| GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving | [link](https://arxiv.org/abs/2606.02774) | 2026-06-01 | — | — | 0 | OPD |
| LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning | [link](https://arxiv.org/abs/2605.07505) | 2026-05-08 | — | — | 0 | OPD |

<details>
<summary><b>Refined Policy Distillation (RPD)</b></summary>

`IROS 2026` · 📅 2025-03-06 · [arXiv](https://arxiv.org/abs/2503.05833) · [code](https://github.com/Refined-Policy-Distillation/RPD) · ⭐ 20 · cited 17 · `OPD`

- **① Problem & importance**: RL rewards for VLA / robotic manipulation are sparse, and imitation easily drifts off the student distribution; a clean VLA-OPD recipe is valuable.
- **② Method & contribution**: Teacher VLA actions + PPO on student rollouts + behavior cloning, described as the cleanest VLA-OPD recipe.
- **③ Task / dataset / model**: VLA / robotic manipulation tasks, with student rollout.
- **④ Limitations & future work**: Relies on a teacher VLA; real-robot transfer needs verification. Future: more robot platforms.

</details>

<details>
<summary><b>HY-Embodied-0.5</b></summary>

`arXiv 2026` · 📅 2026-04-08 · [arXiv](https://arxiv.org/abs/2604.07430) · [code](https://github.com/Tencent-Hunyuan/HY-Embodied) · ⭐ 749 · cited 4 · `OPD`

- **① Problem & importance**: Distilling a 32B embodied model down to a 2B edge model while preserving capability is difficult; embodied strong-to-weak OPD is important.
- **② Method & contribution**: Forward-KL on-policy distillation from 32B to a MoT-2B edge version, where the student generates embodied reasoning trajectories and the teacher provides the FKL target; uses a MoT architecture + visual latent tokens.
- **③ Task / dataset / model**: Embodied: 22 embodied benchmarks, with downstream VLA real-robot dual-arm control (Xtrainer).
- **④ Limitations & future work**: Edge compute is limited. Future: more real-robot tasks and smaller models.

</details>

<details>
<summary><b>VLA-OPD</b></summary>

`arXiv 2026` · 📅 2026-03-27 · [arXiv](https://arxiv.org/abs/2603.26666) · cited 3 · `OPD`

- **① Problem & importance**: There is a gap between offline SFT and online RL for VLA, and RL rewards are sparse; using OPD to bridge them is valuable.
- **② Method & contribution**: An expert VLA teacher provides dense token-level supervision on student trajectories, using reverse-KL (avoiding FKL entropy explosion and hard-CE collapse) in place of sparse RL, preserving the generalist prior and mitigating catastrophic forgetting.
- **③ Task / dataset / model**: VLA / robotic manipulation: LIBERO, RoboTwin2.0, with student trajectories.
- **④ Limitations & future work**: Code to be released; real-robot generalization to be demonstrated. Future: larger-scale real-robot experiments.

</details>

<details>
<summary><b>HyperEyes — Parallel Multimodal Search Agent</b></summary>

`arXiv 2026` · 📅 2026-05-08 · [arXiv](https://arxiv.org/abs/2605.07177) · [code](https://github.com/DeepExperience/HyperEyes) · ⭐ 62 · cited 1 · `OPD`

- **① Problem & importance**: Multimodal search agents struggle to balance efficiency and quality; macro-micro dual-granularity optimization is valuable.
- **② Method & contribution**: TRACE (trajectory-level adaptive cost efficiency) + OPD (token-level) + GRPO, with an external teacher, combining macro (trajectory) and micro (token) dual granularity.
- **③ Task / dataset / model**: Parallel multimodal search agent tasks, with student rollout.
- **④ Limitations & future work**: Many components and complex tuning. Future: a more unified efficiency-quality objective.

</details>

<details>
<summary><b>CoPD — Co-Evolving Policy Distillation</b></summary>

`arXiv 2026` · 📅 2026-04-29 · [arXiv](https://arxiv.org/abs/2604.27083) · cited 1 · `OPD`

- **① Problem & importance**: When integrating multiple expert capabilities into a single model, mixed RLVR suffers from cross-capability divergence costs, while training experts first and then doing OPD avoids divergence but absorbs insufficiently due to the large teacher-student behavior-pattern gap; solving capability integration is important.
- **② Method & contribution**: The authors propose co-evolving policy distillation (CoPD), training experts in parallel and introducing OPD during each expert's ongoing RLVR process (rather than after training completes), letting experts serve as teachers for one another for bidirectional OPD co-evolution, making behavior patterns more consistent while preserving complementary knowledge.
- **③ Task / dataset / model**: Validated on the integrated unification of text, image, and video reasoning capabilities, significantly outperforming strong baselines such as mixed RLVR and MOPD, and even surpassing domain expert models; specific models see the original paper.
- **④ Limitations & future work**: Parallel multi-expert training brings higher compute overhead; future work could generalize to more modalities and larger sets of experts.

</details>

<details>
<summary><b>Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding</b></summary>

`arXiv 2026` · 📅 2026-05-01 · [arXiv](https://arxiv.org/abs/2605.00642) · cited 1 · `OPD`

- **① Problem & importance**: GUI grounding maps instructions to the visual coordinates of target elements and is a core capability of autonomous GUI agents; existing RL methods (e.g., GRPO) rely on expensive multiple rollouts and give sparse signals on hard samples, so finding a better alternative is important.
- **② Method & contribution**: The authors propose GUI-SD, the first OPSD framework for GUI grounding, which uses target boxes and Gaussian soft masks to construct vision-enhanced privileged context for the teacher (without leaking exact coordinates), and adopts entropy-guided distillation based on digit importance and teacher confidence.
- **③ Task / dataset / model**: Experiments on six representative GUI grounding benchmarks consistently outperform GRPO-based methods and naive distillation; specific models see the original paper (summary truncated).
- **④ Limitations & future work**: The privileged-context construction (Gaussian masks, box information) is tailored to GUI tasks and its transferability remains to be verified; future work could extend to more complex multi-step GUI agent tasks.

</details>

<details>
<summary><b>GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving</b></summary>

`arXiv 2026` · 📅 2026-06-01 · [arXiv](https://arxiv.org/abs/2606.02774) · cited 0 · `OPD`

- **① Problem & importance**: This paper addresses the underexplored ability of autonomous-driving VLMs to handle region-specific traffic rules, which concerns their safe deployment across diverse global scenarios.
- **② Method & contribution**: The authors build the GeoDrive-Bench benchmark (5053 human-verified multiple-choice QA covering driving cultures of six countries, with four task types: perception, prediction, planning, and regional reasoning) and design a distillation algorithm that injects region-specific traffic-rule knowledge into the VLM's internal representations.
- **③ Task / dataset / model**: Experiments on nine SOTA VLMs show significant performance gaps across geographic driving cultures for each task, and the proposed baseline model exhibits better geo-culturally aligned reasoning.
- **④ Limitations & future work**: The dataset focuses on six countries and a multiple-choice QA format, with limited coverage and generalization to real open driving scenarios; future work could extend to more countries, open-ended QA, and real driving decisions. This distillation is for knowledge injection rather than student-sampled on-policy distillation.

</details>

<details>
<summary><b>LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning</b></summary>

`arXiv 2026` · 📅 2026-05-08 · [arXiv](https://arxiv.org/abs/2605.07505) · cited 0 · `OPD`

- **① Problem & importance**: Addressing the problem that on-device lightweight vision-language GUI agents have limited capacity and that conventional SFT easily overfits and causes catastrophic forgetting, while efficient cross-platform automated interaction urgently needs to improve small-model capability, this problem is important.
- **② Method & contribution**: The authors propose an SFT-free training paradigm: systematically introducing general knowledge distillation to the GUI domain for the first time, performing Guided On-policy Distillation via oracle reference trajectories and a dynamic retrieval mechanism to reduce hallucination, and designing a Multi-solution Dual-level GRPO framework to jointly align macro subtask planning with micro execution matching.
- **③ Task / dataset / model**: Validated on GUI agent tasks (cross-platform automated interaction, long-horizon operation); the summary does not specify the datasets and base model names, see the original paper.
- **④ Limitations & future work**: The method relies on oracle reference trajectories and a retrieval mechanism, with potentially limited construction cost and generalization to multi-solution tasks; future work could extend to more on-device scenarios and longer-horizon tasks and verify the robustness of the retrieval mechanism.

</details>


## 🙏 Acknowledgments & Notes

- Paper sources and four-point summaries are compiled from the three source awesome lists, the papers' arXiv abstracts, and public materials; errors are possible — **please refer to the original papers**.
- 🔎 Web-added entries: [AoTD](https://arxiv.org/abs/2412.01694) · [VITAL / Thinking With Videos](https://arxiv.org/abs/2508.04416) · [β-KD (Uncertainty-Aware KD, CVPR 2026)](https://arxiv.org/abs/2603.21426).
- ⭐ stars and citations auto-update daily via GitHub Actions; numbers are a snapshot and change over time.
- To add a paper: edit [`papers.json`](papers.json) and the table/HTML regenerate automatically.

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) Released under CC0 (public-domain dedication).
