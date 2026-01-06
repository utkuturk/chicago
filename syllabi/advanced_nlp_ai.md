# Advanced NLP & AI for Linguistics
### Attention Probing, Causality, and Interpretability
**LING 7XXX -- Winter Quarter 2027**

**Time:** Wednesday 1:30pm--4:20pm (3 hours/week)

**Location:** TBD

**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))

**Office hours:** By appointment

**Course site:** Canvas

**Prerequisites:** Background in neural networks (intro ML for language) or permission.

**Format:** Quarter system (10 weeks)

---

## 1. Course Description

What do neural language models actually learn? How can we probe their internal representations? Can we establish causal relationships between model components and linguistic behavior?

Neural networks are often treated as black boxes. In this seminar, we will open them up together. This advanced seminar explores cutting-edge methods for interpreting and analyzing neural networks through a linguistic lens. We focus on three core areas: (i) **attention probing**—analyzing attention patterns to understand how models process syntactic dependencies, (ii) **causality and intervention**—using counterfactual methods to establish causal relationships, and (iii) **representation analysis**—extracting and interpreting hidden representations for linguistic knowledge.

Students will learn to design rigorous probing experiments, implement causal intervention methods, analyze attention entropy and head specialization, and critically evaluate interpretability claims. This is a research-oriented seminar where students develop original proposals for investigating what neural models learn about language.

---

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:
1.  Design and implement probing classifiers to test for linguistic knowledge.
2.  Analyze attention patterns for syntactic dependencies and semantic roles.
3.  Apply causal intervention methods (counterfactuals, interchange interventions).
4.  Compute and interpret attention entropy and head specialization metrics.
5.  Extract and visualize hidden representations using dimensionality reduction.
6.  Critically evaluate interpretability claims and methodological choices.
7.  Propose original research investigating model representations.

---

## 3. Course Structure

### Weekly Rhythm
| Component | What it looks like |
| :--- | :--- |
| **Paper discussion** | Student-led presentation + group discussion of 1--2 papers (45 min). |
| **Methods tutorial** | Hands-on coding session implementing the week's method (90 min). |
| **Research clinic** | Workshopping student project ideas, designs, and analyses (30 min). |

### Research Seminar Format
This is a **research-level** course. You'll read cutting-edge papers (many from 2024-2025), implement state-of-the-art methods, and develop original research proposals. I expect you to engage critically, propose extensions, and identify flaws in published work.

**Paper Presentation Rotation:**
You will lead discussion twice over the quarter. Your job:
1. **Situate the work** (2 min): What problem does this solve? Why does it matter?
2. **Explain the method** (3 min): Walk us through the key technical contribution
3. **Evaluate the claims** (3 min): What did they show? What did they NOT show?
4. **Propose extensions** (2 min): How would you improve or extend this work?

Prepare 3-5 discussion questions that get at the core tensions in the paper.

**Method Implementation Showcase:**
After implementing each method, you'll demonstrate it on a linguistic phenomenon of your choice:
- Week 3: "Here's what my probing classifier found about verb transitivity..."
- Week 5: "I discovered that attention head 7-3 specializes in..."
- Week 7: "When I intervene on this representation, the model's predictions change because..."

This builds your portfolio of interpretability tools AND helps you discover research questions.

### Tools and Methods
*   **Probing:** Linear probes, control tasks, diagnostic classifiers.
*   **Attention analysis:** Attention weights, entropy, rollout, head pruning.
*   **Causality:** Counterfactual data, causal mediation, interchange interventions.
*   **Representation:** PCA, t-SNE, UMAP, CKA similarity.
*   **Frameworks:** Hugging Face Transformers, AllenNLP Interpret, Captum.

---

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 15 | Active discussion; constructive feedback. |
| Paper presentations (2x) | 20 | Lead discussion on 2 papers (10% each). |
| Method implementations (3x) | 30 | Implement and document 3 methods (10% each). |
| Final project | 35 | Full implementation: paper, code, presentation. |

### 4.2 Paper Presentations
Lead discussion on 2 papers over the quarter. Summarize question/method/findings, critique methodology, propose extensions, and prepare discussion questions.

### 4.3 Method Implementations
Choose 3 methods to implement (one from each core area: probing, attention, causality/representation). Includes working code (Colab), brief write-up (2-3 pages), and in-class demonstration.

### 4.4 Final Project
Conduct an original research project investigating a linguistic question.
*   Research question grounded in linguistic theory (syntax, semantics, phonology, etc.).
*   Implementation of interpretability method (probing, intervention, analysis).
*   Systematic evaluation.
*   **Format:** 10--12 page paper (ACL style) + code + presentation.

---

## 5. Course Schedule (10 Weeks)

| Wk | Topic | Readings (Selected) | Methods / Due |
| :-- | :--- | :--- | :--- |
| 1 | Intro & Probing I | Newell (1973); Marr (1982); Belinkov & Glass (2019) | Setup Hugging Face; Linear probes |
| 2 | Probing II: Methodology & Controls | Hewitt & Liang (2019); Hewitt & Manning (2019) | Control tasks |
| 3 | Probing III: Implementation | Conneau et al. (2018); Pimentel et al. (2020) | **Due:** Method 1 (Probing); Showcase |
| 4 | Attention I: Patterns & Visualization | Clark et al. (2019); Vig & Belinkov (2019) | Visualizing attention |
| 5 | Attention II: Entropy & Specialization | Voita et al. (2019); Michel et al. (2019) | **Due:** Method 2 (Attention); Head pruning |
| 6 | Causal I: Counterfactuals | Kaushik et al. (2020); Gardner et al. (2021) | Data augmentation |
| 7 | Causal II & Geometry | Vig et al. (2020); Kornblith et al. (2019) | **Due:** Method 3 (Causality/Geometry); CKA |
| 8 | Cross-linguistic Probing & Limitations | Pires et al. (2019); Belinkov & Glass (2019) | Multilingual models; Critique workshop |
| 9 | Final Project Workshop & Emergent Abilities | Wei et al. (2022); Schaeffer et al. (2023) | Individual consultations |
| 10 | Final Presentations | | Peer feedback; Wrap-up |
| Finals | | | **Due:** Final Project Paper |

**Note:** Each week is a single 3-hour session. Structure: 45 min paper discussion → 90 min methods tutorial → 30 min research clinic.

---

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)
*   **Time management:** This is advanced. Budget 10--12 hours/week outside class.
*   **Reading papers:** Read strategically. Focus on methods and results. Take notes by hand.
*   **Implementing methods:** Start with toy examples. Document as you go. Use Hugging Face extensively.
*   **Quarter pace:** Week 3 (quarter) = Week 4-5 (semester). Very fast progression.
*   **Debugging:** Interpretability code can be tricky. Use office hours. Share code snippets on Slack/Discord.

### 6.2 Academic Integrity
You may collaborate on understanding methods, but must implement your own code and write your own analyses. Cite all sources.

### 6.3 Use of LLMs
LLMs may be used for **debugging** and **understanding** code, but not for generating implementations. You must understand every line. Document any use.

### 6.4 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me early in the quarter. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

---

## 7. Resources

### Key Surveys
*   **Belinkov & Glass (2019).** "Analysis Methods in Neural Language Processing: A Survey." *TACL*.
*   **Rogers et al. (2020).** "A Primer on Neural Network Architectures for Natural Language Processing." *JAIR*.

### Tools
*   **[Hugging Face](https://huggingface.co/):** Pre-trained models and datasets
*   **[Captum](https://captum.ai/):** Model interpretability for PyTorch
*   **[BertViz](https://github.com/jessevig/bertviz):** Attention visualization

### Papers (Available on Course Site)
All assigned papers available through library access or as preprints on arXiv.

---

## 9. Connection to Course Sequence

This course is **Course 2** (capstone) in the AI/NLP sequence:
- **Course 1:** Machine Learning for Language (mixed) - Fall Quarter
- **Course 2 (this course):** Advanced NLP & AI for Linguistics (grad) - Winter Quarter

**Skills from Course 1 that are essential here:**
- **PyTorch:** Used for all implementations
- **Transformers:** We probe transformer models extensively
- **Attention mechanisms:** Now analyzed in detail
- **Python programming:** Need to be comfortable debugging
- **Hugging Face:** Primary framework for loading models

**Integration in Course 2:**
- **Course 1 question:** "Can transformers learn syntax?"
- **Course 2 answer:** "Here's how to test that with probing classifiers, and here's what we find..."

**Can be taken standalone** if you have:
- Strong Python/PyTorch background
- Familiarity with transformers (BERT, GPT)
- Graduate-level research skills

---

## 10. Who Should Take This Course

### Good fit if you:
- Want to conduct interpretability research
- Comfortable with Python, PyTorch, and transformers
- Interested in what models learn (not just engineering performance)
- Like reading cutting-edge papers (2024-2025 research)
- Enjoy debugging and troubleshooting code

### May struggle if you:
- No neural network background (take Course 1 first)
- Uncomfortable with advanced Python (need strong programming skills)
- Prefer lecture-style seminars to research workshops
- Find 10-week quarters overwhelming

### For Graduate Students
This seminar is ideal if you're:
- Planning dissertation/research on interpretability or computational linguistics
- Preparing for academic jobs requiring computational skills
- Aiming to publish in ACL, EMNLP, *CL*, *Computational Linguistics*
- Interested in AI safety, robustness, and responsible AI development

---

## 11. Expected Background

### Required Knowledge
You should be comfortable with:
- **Neural networks:** MLPs, RNNs, LSTMs, transformers (from Course 1 or equivalent)
- **PyTorch:** Implementing models, loading pre-trained weights, debugging
- **Python:** NumPy, pandas, matplotlib, seaborn
- **Hugging Face:** Loading models, tokenizers, datasets
- **Linguistics:** Basic syntax, semantics, morphology (so you can formulate research questions)

### Will Learn in This Course
- **Probing:** Designing diagnostic classifiers, control tasks
- **Attention analysis:** Head specialization, entropy, pruning
- **Causal methods:** Counterfactuals, interchange interventions
- **Representation geometry:** CKA, SVCCA, PWCCA
- **Critical evaluation:** Methodological pitfalls in interpretability research

---

## 12. Final Project Expectations

Your final project should:
1. **Motivate a linguistic question** (1-2 pages): e.g., "Do models learn binding constraints?"
2. **Review relevant work** (1-2 pages): Existing probing studies, what's unresolved
3. **Implement an interpretability method** (core of paper):
   - Probing classifiers, attention analysis, or causal intervention
   - Clear methodology, controls, evaluation metrics
4. **Analyze results systematically** (2-3 pages): What did you find? What does it mean?
5. **Discuss implications** (1-2 pages): For linguistic theory, for NLP systems, for future work

**Format:** ACL 2-column style (10-12 pages)

**Code:** Publicly available GitHub repository with README

**Outcome:** Should be submittable to *ACL, **BlackboxNLP, *SCiL, or similar venues with minor revisions.

---

## 13. Relationship to Package 1 (Psycholinguistics)

Students who complete both Package 1 (Psycholinguistics) and Package 2 (AI/NLP) can conduct cutting-edge research at their intersection:

### Research Questions You Can Answer
- **Compare neural models with human processing:**
  - Do BERT's surprisal predictions match human reading times?
  - Do neural models show agreement attraction like humans?
  - Do attention patterns align with human garden-path effects?

- **Use models to generate psycholinguistic stimuli:**
  - LLMs generate sentences → human experiments validate → probing checks what models learned

- **Model human errors:**
  - Build Bayesian models (Package 1, Course 2) of human agreement errors
  - Compare with neural model errors (Package 2, Course 2)

### Combined Skills
- **Experiments + Models:** Design human experiments (Package 1) and neural model probes (Package 2) to test the same theory
- **Bayesian + Neural:** Hierarchical Bayesian models (Package 1) compared with neural network models (Package 2)
- **Production + NLP:** Morphological planning (Package 1) tested in both humans and language models

---

## 14. Instructor Note

This seminar is intense but rewarding. By Week 10, you'll have implemented multiple interpretability methods and proposed original research. Many students turn these projects into first-author publications.

The quarter format means we move fast—Week 3 you're already showcasing probing classifiers. But the research clinic format ensures you get individualized feedback and support.

I'm committed to helping you succeed. Use office hours, ask questions, share code on our class Slack. This is a collaborative research environment.

Looking forward to discovering what models learn about language—together.

Best,
Utku Turk
