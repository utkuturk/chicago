# Advanced NLP & AI for Linguistics
### Attention Probing, Causality, and Interpretability
**LING 7XXX -- Spring 2027**

**Time:** TBD  
**Location:** TBD  
**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))  
**Office hours:** By appointment  
**Course site:** Canvas

**Prerequisites:** Background in neural networks (intro ML for language) or permission.

---

## 1. Course Description

What do neural language models actually learn? How can we probe their internal representations? Can we establish causal relationships between model components and linguistic behavior?

Neural networks are often treated as black boxes. In this seminar, we will open them up together. This advanced seminar explores cutting-edge methods for interpreting and analyzing neural networks through a linguistic lens. We focus on three core areas: (i) **attention probing**—analyzing attention patterns to understand how models process syntactic dependencies, (ii) **causality and intervention**—using counterfactual methods to establish causal relationships, and (iii) **representation analysis**—extracting and interpreting hidden representations for linguistic knowledge.

Students will learn to design rigorous probing experiments, implement causal intervention methods, analyze attention entropy and head specialization, and critically evaluate interpretability claims. This is a research-oriented seminar where students develop original proposals for investigating what neural models learn about language.

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:
1.  Design and implement probing classifiers to test for linguistic knowledge.
2.  Analyze attention patterns for syntactic dependencies and semantic roles.
3.  Apply causal intervention methods (counterfactuals, interchange interventions).
4.  Compute and interpret attention entropy and head specialization metrics.
5.  Extract and visualize hidden representations using dimensionality reduction.
6.  Critically evaluate interpretability claims and methodological choices.
7.  Propose original research investigating model representations.

## 3. Course Structure

### Weekly Rhythm
| Component | What it looks like |
| :--- | :--- |
| **Paper discussion** | Student-led presentation + group discussion of 1--2 papers (45 min). |
| **Methods tutorial** | Hands-on coding session implementing the week's method (60 min). |
| **Research clinic** | Workshopping student project ideas, designs, and analyses (30 min). |

### Research Seminar Format
This is a **research-level** course. You'll read cutting-edge papers (many from 2024-2025), implement state-of-the-art methods, and develop original research proposals. I expect you to engage critically, propose extensions, and identify flaws in published work.

**Paper Presentation Rotation:**
You will lead discussion twice. Your job:
1. **Situate the work** (2 min): What problem does this solve? Why does it matter?
2. **Explain the method** (3 min): Walk us through the key technical contribution
3. **Evaluate the claims** (3 min): What did they show? What did they NOT show?
4. **Propose extensions** (2 min): How would you improve or extend this work?

Prepare 3-5 discussion questions that get at the core tensions in the paper.

**Method Implementation Showcase:**
After implementing each method, you'll demonstrate it on a linguistic phenomenon of your choice:
- Week 4: "Here's what my probing classifier found about verb transitivity..."
- Week 5: "I discovered that attention head 7-3 specializes in..."
- Week 7: "When I intervene on this representation, the model's predictions change because..."

This builds your portfolio of interpretability tools AND helps you discover research questions.

### Tools and Methods
*   **Probing:** Linear probes, control tasks, diagnostic classifiers.
*   **Attention analysis:** Attention weights, entropy, rollout, head pruning.
*   **Causality:** Counterfactual data, causal mediation, interchange interventions.
*   **Representation:** PCA, t-SNE, UMAP, CKA similarity.
*   **Frameworks:** Hugging Face Transformers, AllenNLP Interpret, Captum.

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 15 | Active discussion; constructive feedback. |
| Paper presentations (2x) | 20 | Lead discussion on 2 papers (10% each). |
| Method implementations (3x) | 30 | Implement and document 3 methods (10% each). |
| Final project | 35 | Full implementation: paper, code, presentation. |

### 4.2 Paper Presentations
Lead discussion on 2 papers. Summarize question/method/findings, critique methodology, propose extensions, and prepare discussion questions.

### 4.3 Method Implementations
Choose 3 methods to implement. Includes working code (Colab), brief write-up, and demonstration.

### 4.4 Final Project
Conduct an original research project investigating a linguistic question.
*   Research question grounded in linguistic theory (syntax, semantics, phonology, etc.).
*   Implementation of method (probing, intervention, analysis).
*   Systematic evaluation.
*   **Format:** 10--12 page paper (ACL style) + code + presentation.

## 5. Course Schedule

| Wk | Topic | Readings (Selected) | Methods / Due |
| :-- | :--- | :--- | :--- |
| 1 | Intro; Levels of analysis | Newell (1973); Marr (1982); Belinkov & Glass | Setup Hugging Face |
| 2 | Probing I: Methodology | Hewitt & Liang (2019); Conneau et al. | Linear probes |
| 3 | Probing II: Controls | Hewitt & Manning (2019); Pimentel et al. | Control tasks |
| 4 | Attention I: Patterns | Clark et al. (2019); Vig & Belinkov (2019) | Visualizing attention; **Due:** Method 1 |
| 5 | Attention II: Entropy | Voita et al. (2019); Michel et al. (2019) | Head pruning |
| 6 | Causal I: Counterfactuals | Kaushik et al. (2020); Gardner et al. | Data augmentation |
| 7 | Causal II: Mediation | Vig et al. (2020); Finlayson et al. (2021) | Causal mediation; **Due:** Method 2 |
| 8 | Geometry I: Similarity | Saphra & Lopez (2019); Kornblith et al. | CKA similarity |
| 9 | Geometry II: Subspaces | Ravfogel et al. (2020); Bolukbasi et al. | INLP |
| 10 | Cross-linguistic probing | Pires et al. (2019); Chi et al. (2020) | Multilingual models; **Due:** Method 3 |
| 11 | Linguistic Structure | Tenney et al. (2019); Jawahar et al. | Edge probing |
| 12 | Limitations | Belinkov & Glass (2019); Jacovi & Goldberg | Critique workshop |
| 13 | Emergent Abilities | Wei et al. (2022); Schaeffer et al. (2023) | Testing emergence |
| 14 | Mechanistic Interpretability | Olsson et al. (2022); Elhage et al. (2021) | Circuit analysis |
| 15 | Presentations I | | Peer feedback |
| 16 | Presentations II | | Peer feedback |
| Final | | | **Due:** Final Proposal |

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)
*   **Time management:** This is advanced. Budget 10--12 hours/week.
*   **Reading papers:** Read strategically. Take notes by hand.
*   **Implementing methods:** Start with toy examples. Document as you go.

### 6.2 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me early in the semester. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

## 7. Resources
*   **Key Surveys:** Belinkov & Glass (2019); Rogers et al. (2020).
*   **Tools:** [Hugging Face](https://huggingface.co/), [Captum](https://captum.ai/), [BertViz](https://github.com/jessevig/bertviz).
