---
title: "Package 1: Psycholinguistics"
layout: page
---

<div style="text-align: center; margin: 30px 0;">
  <a href="{{ '/Package1_Psycholinguistics_Sequence.pdf' | relative_url }}" class="pdf-download-btn">📄 Download Complete Package (PDF)</a>
</div>

---


# Package 1: Experimental Psycholinguistics Sequence
**Instructor:** Utku Turk (utkuturk@umd.edu)
**Format:** Quarter System (10 weeks per course)
**Level Progression:** Undergraduate → Mixed → Advanced Graduate

---

## Package Vision

This three-course sequence trains students in experimental psycholinguistics, from foundational methods through computational modeling to specialized research in morphological planning. Students learn by doing: formulating questions, designing experiments, implementing models, collecting data, and presenting findings. Each course integrates programming (R, Stan, PCIbex), statistical analysis, and theoretical linguistics, preparing students for modern psycholinguistics research.

---

## Course Summaries

### Course 1: Introduction to Psycholinguistics (Undergraduate, Fall Quarter)
**Prerequisites:** Introduction to Linguistics or permission

Students learn psycholinguistics through the complete experimental process. Rather than just reading about experiments, they design them, collect data, analyze results, and present findings. The course covers speech perception, lexical access, syntactic parsing, and language production. By the end of the quarter, students have hands-on experience with self-paced reading, eye-tracking, acceptability judgments, and online experimentation (PCIbex, Gorilla). They learn R programming, mixed-effects models, and APA-format research writing. No prior experimental experience required—skills build from scratch.

**Key outputs:** 4 QALMRI paper summaries, 3 stage projects (question formation, experimental design, data analysis), final experimental proposal.

### Course 2: Bayesian Cognitive Modeling for Linguistics (Mixed Level, Winter Quarter)
**Prerequisites:** Introduction to programming (R or Python) and basic statistics

This course teaches students to formalize theories of cognition computationally using Bayesian modeling. Unlike traditional statistics ("is there an effect?"), cognitive modeling asks "what underlying process generated this data?" Students learn probabilistic programming in **Stan**, implementing models from Signal Detection Theory to hierarchical memory models. The workflow covers theory formalization, Stan implementation, parameter recovery through simulation, application to real data, and robustness evaluation. Mathematical intuition builds through visualization and analogy, not calculus.

**Key outputs:** 7 weekly lab implementations, midterm model replication (SDT or GCM), final project implementing a novel Bayesian cognitive model.

### Course 3: Morphological Planning in Production (Advanced Graduate, Spring Quarter)
**Prerequisites:** Background in psycholinguistics or permission

This advanced seminar investigates when and how speakers plan inflectional morphology during sentence production. Students evaluate competing theoretical accounts (Levelt, Dell, Caramazza), design experiments that test explicit predictions, and build practical skills in PCIbex implementation, production timing analysis, and cross-linguistic design. The course runs as a **studio/maker space**—half our time is spent building experiments and debugging analyses together. Students develop original research proposals suitable for conference submission (HSP, LSA, CUNY) or publication in psycholinguistics journals.

**Key outputs:** 3 problem sets (PCIbex build, R analysis pipeline, cross-linguistic design), article-format final project (10-15 pages) with preregistered analysis plan.

---

## Learning Philosophy

This sequence embodies three core principles. **First, learning by doing:** students conduct research, not just read about it. **Second, acting as colleagues:** the instructor's role shifts from guide (Course 1) to mentor (Course 2) to collaborator (Course 3). **Third, computational literacy:** programming is embedded throughout as a tool for answering linguistic questions. Students completing all three courses can design rigorous experiments, implement computational models, and contribute original findings to the field.

---

**Progression:** Course 1 provides experimental foundations → Course 2 adds computational modeling → Course 3 integrates both in specialized research. Skills build cumulatively: R programming (all courses), experimental design (Courses 1 & 3), Bayesian modeling (Courses 2 & 3), production methods (Course 3).


---
---


# Introduction to Psycholinguistics
### Learning Through the Experimental Process

**LING 2XXX -- Fall Quarter 2026**

**Time:** TBD (meets 4 hours/week: 2 sessions of 2 hours each)

**Location:** TBD

**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))

**Office hours:** By appointment

**Course site:** Canvas

**Prerequisites:** Introduction to linguistics or permission. No prior experimental experience required.

**Format:** Quarter system (10 weeks)

---

## 1. Course Description

How do we study language in the mind? How do psycholinguists design experiments to test linguistic theories? What does it take to go from a theoretical question to publishable experimental results?

This course teaches psycholinguistics **through the experimental process**. Rather than just reading about experiments, we will learn by doing: formulating research questions, designing experiments, collecting data, analyzing results, and presenting findings. I am excited to guide you through this process as we act as colleagues discovering new things about the mind.

You will work through the complete research cycle multiple times, each time with a different linguistic domain: speech perception, lexical access, syntactic parsing, and language production. By the end of the quarter, you will have hands-on experience with every stage of psycholinguistic research and a deep understanding of how experimental methods connect to linguistic theory.

**No prior experimental experience required**—we learn by doing, starting from scratch.

---

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:

1.  Formulate testable research questions from linguistic theories.
2.  Design experiments using appropriate psycholinguistic methods.
3.  Understand and apply methods: self-paced reading, eye-tracking, acceptability judgments, priming.
4.  Collect experimental data using online platforms (PCIbex, Gorilla).
5.  Analyze psycholinguistic data using R and mixed-effects models.
6.  Interpret experimental results in light of linguistic theory.
7.  Write research papers following APA/journal format.
8.  Present experimental findings to both specialist and general audiences.
9.  Critically evaluate published psycholinguistic research.
10. Connect experimental findings to theoretical linguistics.

---

## 3. Course Structure

The course is organized around **five stages of the experimental process**. Each unit focuses on one stage and one linguistic phenomenon:

1.  **Question Formation** (Week 1): Introduction to psycholinguistics & speech perception
2.  **Literature Review** (Weeks 2--3): Lexical access & word recognition
3.  **Experimental Design** (Weeks 4--5): Garden-path effects & parsing
4.  **Data Collection** (Weeks 6--7): Language Production & Planning
5.  **Data Analysis & Presentation** (Weeks 8--10): Analysis methods & final projects

### Weekly Rhythm
| Component | What it looks like |
| :--- | :--- |
| **Lecture** | Linguistic phenomenon + experimental methods (Session 1). |
| **Lab** | Hands-on work with that stage of the process (Session 2). |
| **QALMRI summaries** | Critical reading of experimental papers (4 total). |
| **Stage projects** | Mini-projects at key experimental stages (3 total). |

### Methods We Use
*   **Self-paced reading:** Measuring reading times word-by-word.
*   **Eye-tracking:** Recording eye movements during reading.
*   **Acceptability judgments:** Rating grammaticality and naturalness.
*   **Priming:** Testing facilitation effects.
*   **Online platforms:** PCIbex, Gorilla for data collection.
*   **Analysis:** R, lme4 for mixed-effects models.

### Your Experiment Building Timeline

By the end of the quarter, you will have built multiple mini-experiments:
- **Week 2**: Design your first experiment (speech perception)
- **Week 4**: Conduct a literature review with experimental predictions
- **Week 6**: Full experiment design with materials and analysis plan
- **Week 8**: Analyze and visualize experimental data
- **Week 10**: Present a complete study from question to conclusion

Think of this course as an apprenticeship: you'll do what psycholinguists do, not just read about it.

---

## 4. Course Requirements

### 4.1 Grading

| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 15 | Active engagement in lectures and labs. |
| QALMRI summaries (4x) | 20 | Critical paper summaries (5% each). |
| Stage projects (3x) | 45 | Hands-on work at each experimental stage (15% each). |
| Final project | 20 | Complete experimental study: design, analysis plan, presentation. |

### 4.2 QALMRI Summaries
QALMRI (Question, Alternatives, Logic, Method, Results, Inferences) is a framework for critically reading experimental papers. You will write 4 summaries over the quarter (1-2 pages each), due before the week's second session.

### 4.3 Stage Projects
At key stages, you will complete hands-on assignments:

1.  **Question formation + Literature review** (Week 3): Develop a research question with mini literature review (3-4 pages).
2.  **Experimental design** (Week 6): Design a replication-and-extension experiment that tests competing accounts.
3.  **Data analysis** (Week 8): Analyze provided dataset and visualize results.

### 4.4 Final Project
Design a complete psycholinguistic experiment. Format: 8-10 page proposal in APA style + 10-minute presentation.

---

## 5. Course Schedule (10 Weeks)

| Wk | Topic | Readings (Selected) | Lab / Due |
| :-- | :--- | :--- | :--- |
| **STAGE 1** | **Introduction & Question Formation** | | |
| 1a | What is psycholinguistics? | Lewis & Phillips (2015) | Intro to experimental methods |
| 1b | Categorical perception | Pisoni & Tash (1974) | Formulating research questions |
| **STAGE 2** | **Literature Review (Lexical Access)** | | |
| 2a | Activation & Selection | Dahan (2010) | Literature search strategies |
| 2b | Visual World Paradigm | Tanenhaus et al. (1995) | QALMRI practice; **QALMRI 1 due** |
| 3a | Prediction in lexical access | Staub (2015) | Writing lit reviews |
| 3b | Lexical access wrap-up | Huettig et al. (2011) | **Project 1 due** (Question + Lit Review) |
| **STAGE 3** | **Experimental Design (Syntactic Parsing)** | | |
| 4a | Garden-path effects | van Gompel (2013); Frazier & Rayner (1982) | Designing experiments |
| 4b | Working memory & parsing | Lewis & Vasishth (2005) | **QALMRI 2 due**; Creating materials |
| 5a | Self-paced reading | Just et al. (1982) | Implementing in PCIbex |
| 5b | Parsing theories | Gibson (2000) | Design workshop |
| **STAGE 4** | **Data Collection (Language Production)** | | |
| 6a | Agreement Attraction | Bock & Miller (1991) | **Project 2 due**; Production paradigms |
| 6b | Cross-linguistic Production | Eberhard et al. (2005) | **QALMRI 3 due**; Piloting |
| 7a | Production Planning | Vigliocco & Nicol (1998) | Data collection demo |
| 7b | Production wrap-up | Hartsuiker et al. (2003) | Coding production data |
| **STAGE 5** | **Data Analysis & Presentation** | | |
| 8a | Data Analysis in R | Jaeger (2010); Analysis tutorial | **QALMRI 4 due**; Data wrangling |
| 8b | Mixed Models & Visualization | Barr et al. (2013) | **Project 3 due** (Analysis) |
| 9a | Writing experimental papers | APA Manual; Bem (2003) | Writing results sections |
| 9b | Final presentations I | | Peer feedback |
| 10a | Final presentations II | | Peer feedback |
| 10b | Course synthesis | | Reflection & wrap-up |
| Finals | | | **Due:** Final Project Proposal |

**Note:** Each week has two sessions (a/b). Session (a) is typically lecture-focused; session (b) is lab-focused.

---

## 6. Policies

### 6.1 Quarter System Considerations

This course covers substantial material in 10 weeks. To succeed:

*   **Time management:** Expect 10-12 hours/week outside class. Start assignments early.
*   **Reading strategy:** Use the QALMRI framework. Focus on core readings; optional readings available for depth.
*   **Lab attendance:** Critical—skills build cumulatively. Missing labs puts you behind.
*   **Office hours:** Use them! Especially for R programming and experimental design help.

### 6.2 What you might struggle with (and how to succeed)

*   **Learning R:** Start with small examples. Visualize everything. Use online resources (R for Data Science).
*   **Designing experiments:** Start simple. Pilot everything. Get feedback early.
*   **Reading papers:** Don't read linearly. Use QALMRI. Focus on method and results first.
*   **Quarter pace:** Unlike semesters, there's no "catching up later." Stay current.

### 6.3 Accessibility & Wellness

If you need accommodations, please contact the relevant campus office and talk to me early in the quarter. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

### 6.4 Academic Integrity

Do your own work. You may collaborate on understanding concepts and debugging code, but write your own analyses and summaries. Cite all sources.

### 6.5 Use of LLMs

LLMs (ChatGPT, etc.) may be used for **support** (understanding concepts, debugging R code) but not to generate QALMRI summaries or written assignments. Document any use.

---

## 7. Resources

### Textbooks (Recommended, not required)
*   **Harley, T. A. (2014).** *The Psychology of Language: From Data to Theory* (4th ed.). Psychology Press.
*   **Traxler, M. J. (2012).** *Introduction to Psycholinguistics: Understanding Language Science*. Wiley-Blackwell.
*   **Fernández, E. M., & Cairns, H. S. (2017).** *The Handbook of Psycholinguistics*. Wiley-Blackwell.

### Online Resources (Free)
*   **Experimental platforms:** [PCIbex](https://www.pcibex.net/), [Gorilla](https://gorilla.sc/)
*   **R programming:** [R for Data Science](https://r4ds.had.co.nz/), [brms documentation](https://paul-buerkner.github.io/brms/)
*   **Statistics:** [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/), [Learning Statistics with R](https://learningstatisticswithr.com/)

### Tools
*   **R/RStudio:** Statistical analysis and visualization (install both)
*   **PCIbex/IbexFarm:** Web-based experiments (browser-based, no install)
*   **Canvas:** Course materials, submissions, grades

---

## 9. Connection to Course Sequence

This course is **Course 1** in the Experimental Psycholinguistics sequence:

- **Course 1 (this course):** Intro to Psycholinguistics (undergrad) - Fall Quarter
- **Course 2:** Bayesian Cognitive Modeling (mixed) - Winter Quarter
- **Course 3:** Morphological Planning in Production (grad) - Spring Quarter

**Skills that transfer to Course 2:**

- R programming → used for Stan modeling
- Experimental thinking → applied to computational models
- Mixed-effects models → extended to hierarchical Bayesian models

**Not a prerequisite but helpful preparation** for advanced psycholinguistics seminars and research assistantships.

---

## 10. Instructor Note

Welcome to the quarter! Ten weeks is short, but I'm committed to making sure you get the full psycholinguistics research experience. We'll move fast, but we'll move together. Don't hesitate to reach out for help, feedback, or just to talk about language science.

Looking forward to discovering new things about the mind with you.

Best,
Utku Turk


---
---


# Bayesian Cognitive Modeling for Linguistics
### From Theory to Implementation
**LING 4XXX -- Winter Quarter 2027**

**Time:** TBD (meets 4 hours/week: 2 sessions of 2 hours each)

**Location:** TBD

**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))

**Office hours:** By appointment

**Course site:** Canvas

**Prerequisites:** Introduction to programming (R or Python) and basic statistics.

**Format:** Quarter system (10 weeks)

---

## 1. Course Description

How do we test theories of cognition? How can we formalize our hypotheses about how the mind works? This course introduces computational modeling as a tool for understanding cognitive processes, with a specific focus on **Bayesian Cognitive Modeling**.

Unlike data analysis, which asks "is there an effect?", cognitive modeling asks "what underlying process generated this data?". We will use the probabilistic programming language **Stan** to build, fit, and evaluate generative models of cognition. We will cover the full workflow: from defining a mathematical model of a cognitive process, to implementing it in code, to recovering parameters from simulated data, and finally applying it to real human behavioral data.

This course moves quickly through foundational material to give you hands-on experience with the most essential cognitive models.

---

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:

1.  Explain the purpose of quantitative modeling in cognitive science and distinguish among descriptive, predictive, and explanatory models.
2.  Critically evaluate and implement simulations of cognitive models.
3.  Implement Bayesian cognitive models using **Stan** and interpret their structure.
4.  Evaluate the robustness of Bayesian cognitive models (parameter recovery, replication).
5.  Clearly communicate the structure and performance of a Bayesian cognitive model.

---

## 3. Course Content & Structure

The course is divided into four main modules:

1.  **Foundations:** Role of computational modeling; Simulation; Generative stance; Probability & Bayes.
2.  **Basic Models:** Parameter estimation, Signal Detection Theory, Latent variables (Stan implementation).
3.  **Hierarchical Structures:** Pooling, shrinkage, individual differences.
4.  **Advanced Topics & Projects:** Model comparison, mixture models, final projects.

### The Generative Stance
This course teaches you to think like a **theoretician**. Instead of asking "what pattern is in the data?", you'll ask "if my theory is true, what data would I see?" This flips statistics on its head.

**Weekly Mathematical Intuition Building:**

Each week begins with a conceptual question before we touch code:

- Week 1: "If you flip a coin 10 times and get 7 heads, what can you infer about the coin's bias?"
- Week 3: "How does Signal Detection Theory formalize the difference between sensitivity and bias?"
- Week 5: "What does it mean for a model to 'pool' information across participants?"
- Week 7: "Why do we need model comparison when all models are wrong?"

We'll build mathematical intuition through simulation, visualization, and analogy—not calculus proofs.

### From Theory to Implementation

Each model follows the same workflow:

1. **Formalize the theory** (What are we claiming about cognition?)
2. **Specify the generative process** (How would a god generate this data?)
3. **Implement in Stan** (Translate the theory into code)
4. **Simulate fake data** (Can we recover our parameters?)
5. **Apply to real data** (Does the theory fit human behavior?)
6. **Evaluate robustness** (Where does the model break?)

---

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 10 | Active engagement in labs. |
| Weekly Labs (7x) | 42 | Coding assignments in R/Stan (6% each). |
| Midterm Project | 18 | Replicating a simple cognitive model (SDT or GCM). |
| Final Project | 30 | Implementing and testing a novel/extended model. |

### 4.2 Labs & Projects
*   **Labs:** Weekly implementation tasks in R and Stan. Due before the next week's first session.
*   **Midterm (Week 6):** Replicate a standard model (e.g., SDT, GCM). Focus on implementation.
*   **Final (Finals week):** Choose a phenomenon, implement a Bayesian model, simulate data, and fit/evaluate it. 8-10 page report.

---

## 5. Course Schedule (10 Weeks)

*Readings based on Vasishth et al. (Bayesian Cognitive Modeling) and Lee & Wagenmakers.*

| Wk | Topic | Readings / Concepts | Lab / Assignment |
| :-- | :--- | :--- | :--- |
| **MODULE 1** | **Foundations** | | |
| 1a | Intro to Cognitive Modeling | Generative stance; Descriptive vs Explanatory | Conceptual intro |
| 1b | Probability & Bayes Rule | Joint/Conditional probability; Bayes Theorem | Lab 1: Simulating processes + probability |
| 2a | Intro to Stan | Probabilistic programming; Stan syntax | Stan tutorial |
| 2b | Stan Implementation Practice | Binomial rate model | Lab 2: Hello World in Stan |
| **MODULE 2** | **Basic Models** | **(Lee & Wagenmakers)** | |
| 3a | Parameter Estimation | Gaussian parameters; Priors & Posteriors | Lab practice |
| 3b | Signal Detection Theory (SDT) | Equal variance SDT; d' and c | Lab 3: Implementing SDT |
| 4a | Latent Variables I | GCM; Change detection | Theory + simulation |
| 4b | Latent Variables II | Exemplar theory implementation | Lab 4: GCM implementation |
| **MODULE 3** | **Hierarchical Structures** | | |
| 5a | Hierarchical Models I | Pooling; Shrinkage; Hyperparameters | Lab 5: Hierarchical Binomial |
| 5b | Hierarchical Models II | Individual differences; Log-normal RTs | Lab work continues |
| 6a | Review & Midterm Prep | Troubleshooting; Model comparison prep | Office hours intensive |
| 6b | **Midterm Due + Model Comparison** | Bayes Factors; WAIC; LOO | **Midterm due**; Lab 6: Comparing models |
| **MODULE 4** | **Advanced Architectures & Project** | **(Vasishth et al.)** | |
| 7a | Mixture Models | Fast-guess; Speed-accuracy trade-off | Lab 7: Mixture modeling |
| 7b | Multinomial Processing Trees | MPTs; Categorical responses | MPT examples (optional depth) |
| 8a | Robustness & Recovery | Posterior predictive checks | Final project workshop I |
| 8b | Final Project Workshop | Troubleshooting Stan code | Individual consultations |
| 9a | Final Project Workshop II | Peer review of preliminary results | Group feedback session |
| 9b | Advanced Topics (Optional) | Accumulator models (LBA); Future directions | Self-study resources |
| 10a | Final Presentations I | Student presentations | Peer feedback |
| 10b | Final Presentations II | Student presentations | Peer feedback + wrap-up |
| Finals | | | **Due:** Final Project Report |

**Note:** Each week has two sessions (a/b). Sessions blend lecture and lab work, with increasing lab emphasis as the quarter progresses.

---

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)

**Coding in Stan:** Stan can be challenging because it is declarative (you declare the model) rather than imperative. But don't worry—we will tackle this together, starting simple and building up complexity line by line.

*   **Start simple:** Build the simplest possible model that compiles.
*   **Use the manual:** The Stan User Guide is excellent.
*   **Simulate first:** Always check if you can recover parameters from simulated data.

**Bayesian concepts:**
*   Focus on the **generative process**: "How would a god generate this data?"
*   Focus on interpreting the posterior distribution, not the integrals.

**Quarter pace:**
*   This course moves **fast**. Week 2 in quarter = Week 3-4 in semester.
*   **Don't fall behind** on labs—each builds on the previous one.
*   **Use office hours** extensively—debugging Stan code is part of learning.

### 6.2 Academic Integrity
You may collaborate on code, but you must write your own write-ups and understand every line of code you submit.

### 6.3 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me early in the quarter. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

### 6.4 Use of LLMs
LLMs may be used for **debugging** (e.g., understanding Stan error messages) but not for generating model code. Document any use.

---

## 7. Resources

### Textbooks
1.  **Lee, M. D., & Wagenmakers, E. J. (2014).** *Bayesian Cognitive Modeling*. Cambridge University Press.
2.  **Vasishth et al. (2024).** *Introduction to Bayesian Data Analysis for Cognitive Science*. [Online Book](https://bruno.nicenboim.me/bayescogsci/)

### Online Resources
3.  [Stan User Guide](https://mc-stan.org/users/documentation/)
4.  [Stan Discourse Forum](https://discourse.mc-stan.org/) - for troubleshooting
5.  [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/) - supplementary Bayesian modeling resource

### Software (All Free)
*   **R/RStudio:** Statistical computing environment
*   **cmdstanr:** R interface to Stan ([installation guide](https://mc-stan.org/cmdstanr/))
*   **brms:** Alternative high-level Bayesian modeling in R (we'll mention but won't focus on)

---

## 9. Connection to Course Sequence

This course is **Course 2** in the Experimental Psycholinguistics sequence:

- **Course 1:** Intro to Psycholinguistics (undergrad) - Fall Quarter
- **Course 2 (this course):** Bayesian Cognitive Modeling (mixed) - Winter Quarter
- **Course 3:** Morphological Planning in Production (grad) - Spring Quarter

**Skills from Course 1 that help here:**

- **R programming:** You already know `dplyr`, `ggplot2`, `lme4` from Course 1
- **Mixed-effects models:** Now extended to full Bayesian hierarchical models
- **Experimental thinking:** Now formalized as generative models

**Skills developed here that transfer to Course 3:**

- **Bayesian analysis:** Used for production latency models in Course 3
- **Hierarchical modeling:** Applied to cross-linguistic experiments
- **Parameter recovery:** Used to validate complex production models

**Can be taken standalone** if you have programming and statistics background.

---

## 10. Who Should Take This Course

### Good fit if you:

- Want to formalize theories of cognition computationally
- Need Bayesian modeling skills for research
- Took Course 1 (Intro Psycholing) and want deeper statistical skills
- Are comfortable with programming and willing to learn Stan
- Like thinking generatively ("what process could generate this data?")

### May struggle if you:

- Have no programming experience (take Course 1 first or learn R basics first)
- Prefer plug-and-play statistics (this course emphasizes understanding over push-button tools)
- Find 10-week quarters overwhelming

### For graduate students:

Especially valuable if your research involves:
- Modeling cognitive processes
- Individual differences
- Cross-linguistic comparisons requiring hierarchical models
- Reaction time or accuracy data needing mixture models

---

## 11. Instructor Note

This quarter moves fast, but the goal is the same: teach you to think like a modeler. By Week 10, you should be able to read a psycholinguistics paper and think "I could formalize that theory in Stan and test whether it recovers the behavioral pattern."

Stan has a learning curve, but it's worth it. Once you learn Stan, you can model anything—not just language, but vision, memory, decision-making, clinical data, and more. This skill is valuable in academia and industry.

I'm committed to helping you succeed. Use office hours, ask questions, debug together. We'll get through it together.

Looking forward to building models with you.

Best,
Utku Turk


---
---


# Seminar in Psycholinguistics
### How Words Are Built: Experimental Approaches to Morphological Planning
**LING 7XXX -- Spring Quarter 2027**

**Time:** Wednesday 1:30pm--4:20pm (3 hours/week)

**Location:** TBD

**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))

**Office hours:** By appointment

**Course site:** ELMS/Canvas

**Methods spine (recurring):** [*Experimentology*](https://experimentology.io)

**Format:** Quarter system (10 weeks)

---

## 1. Course Description

When do we plan inflectional morphology? This seminar connects theory about production and morphological encoding to experiments that can test it. You will evaluate core claims, design studies with explicit predictions, and build practical skills in implementation, analysis, and modeling. Think of us as colleagues working on the same project together—my goal is to help you develop the best possible project, not just evaluate it at the end. The quarter ends with an original proposal or pilot, written in article format.

---

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:
1.  Evaluate competing accounts of morphological planning in production.
2.  Turn theoretical claims into concrete predictions and falsifiable tests.
3.  Design experiments with appropriate controls, counterbalancing, and exclusions.
4.  Implement web-based production tasks in PCIbex (timing + audio).
5.  Analyze timing/error data in R (mixed models).
6.  Design cross-linguistic experiments that test morphological planning.
7.  Conduct power analyses and interpret model comparison metrics.
8.  Present and defend an experimental design.
9.  Write preregistered analysis plans with reproducible workflows.

---

## 3. Course Structure

### Weekly Rhythm
| Component | What it looks like |
| :--- | :--- |
| **Readings** | Short **required** core + **recommended** breadth + a **depth pick** (read fully). |
| **Mini-lecture** | Claim, design logic, and what pattern would change minds. (30 min) |
| **Studio/Lab** | 90 minutes: PCIbex builds, R analysis, or modeling/simulation. |
| **Peer Workshop** | 30 minutes: Share work-in-progress, get feedback, troubleshoot together. |
| **Problem sets** | Three deliverables scaffolding the final project. |
| **Project** | Idea → design → analysis → write-up. |

### The Studio Model
This seminar runs like an **art studio** or **maker space**—not a lecture hall. Half our time is spent building: writing code, designing experiments, debugging analyses. I'll circulate and work with you individually or in small groups.

**Expect to:**
- Show unfinished work and get feedback (that's how we learn!)
- Help each other debug code and brainstorm designs
- Present work-in-progress multiple times, not just at the end
- Iterate based on peer and instructor feedback

**Studio Sessions Include:**
- **Week 3**: PCIbex build-athon—bring your laptop, build a minimal naming experiment
- **Week 5**: Analysis clinic—bring your data, we'll wrangle it together
- **Week 7**: Design workshop—pitch your final project idea, get feedback
- **Week 9**: Cross-linguistic design exchange—pair up and critique each other's designs

### A Collaborative Approach
**Think of us as colleagues working on the same project together.** Reach out anytime with questions about your design, feedback on materials, or coding problems.

---

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 20 | Substantive questions (Weekly) + discussion. |
| Problem set 1 | 10 | PCIbex build (minimal PWI). |
| Problem set 2 | 10 | R analysis pipeline. |
| Problem set 3 | 10 | Cross-linguistic design plan. |
| Final project | 50 | Proposal (5) + Presentation (10) + Final Paper (35). |

### 4.2 Deliverables
*   **Week 4:** Problem Set 1 (PCIbex experiment).
*   **Week 5:** 1-page proposal.
*   **Week 6:** Problem Set 2 (Analysis).
*   **Week 8:** Problem Set 3 (Cross-ling design).
*   **Finals:** Final paper (10--15pp article-format proposal with pilot data or comprehensive preregistered analysis plan).

---

## 5. Course Schedule (10 Weeks)

| Wk | Date | Topic | Readings (Req) | Studio / Due |
| :-- | :--- | :--- | :--- | :--- |
| 1 | | Production architecture & PWI I | Levelt et al. (1999); Schriefers et al. (1990) | Claim → Measure; R Bootcamp |
| 2 | | PWI II & Chronometry | Meyer (1996); Schriefers et al. (2002) | PCIbex scaffold |
| 3 | | Structural constraints | Momma et al. (2016); Experimentology | **PCIbex build-athon** |
| 4 | | Speech Errors & Auxiliaries | Garrett (1975); Miozzo & Caramazza (1997) | **Due:** PS1; Error coding |
| 5 | | Agreement Attraction | Bock & Miller (1991); Eberhard et al. (2005) | **Due:** Proposal; Analysis clinic |
| 6 | | Quant Workflow & Models | Vasishth et al. (2018); Barr et al. (2013) | **Due:** PS2; Power analysis |
| 7 | | Derivational Morph | Janssen & Caramazza (2011); Janssen et al. (2008) | **Design workshop** |
| 8 | | Cross-linguistic Design | Vigliocco & Nicol (1998); Hartsuiker et al. (2003) | **Due:** PS3; Design clinic |
| 9 | | Theory to Predictions | Embick (2015); Bobaljik (2015) | Prereg skeleton; **Presentations I** |
| 10 | | Synthesis & Open Science | Pickering & Garrod (2013); Open Science readings | **Presentations II**; Final Q&A |
| Finals | | | | **Due:** Final Project |

**Note:** Each week is a single 3-hour session. Structure: 30 min lecture → 90 min studio/lab → 30 min peer workshop.

---

## 6. Policies

### 6.1 Attendance
Attendance is expected. Email me if you must miss class. You are responsible for catching up on lab content.

### 6.2 Late Work
*   **Reading questions:** No late submissions (part of participation).
*   **Problem sets:** 10% penalty per day (max 3 days).
*   **Project:** Extensions by arrangement only.

### 6.3 Collaboration
Collaboration is encouraged! Discuss approaches, but write your own code and analysis.

### 6.4 Academic Integrity
Do your own work; cite sources. Plagiarism or fabrication result in failure.

### 6.5 Use of LLMs
LLMs (ChatGPT, etc.) are allowed for **support** (debugging, brainstorming) but not generation. You must document use.

### 6.6 Accessibility & Wellness
If you need accommodations, please register with the relevant accessibility office and talk to me early in the quarter. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

---

## 7. Resources
*   **Experimentology:** [experimentology.io](https://experimentology.io) (primary methods resource)
*   **Technical:** [PCIbex Docs](https://doc.pcibex.net/), [R4DS](https://r4ds.had.co.nz/)
*   **Production literature:** Levelt (1989), Dell (1986), Caramazza (1997)
*   **Analysis:** Vasishth et al. (2018) *Statistical Foundations of Number*

---


## 9. Connection to Course Sequence

This course is **Course 3** (capstone) in the Experimental Psycholinguistics sequence:
- **Course 1:** Intro to Psycholinguistics (undergrad) - Fall Quarter
- **Course 2:** Bayesian Cognitive Modeling (mixed) - Winter Quarter
- **Course 3 (this course):** Morphological Planning in Production (grad) - Spring Quarter

**Skills from previous courses that are essential here:**
- **From Course 1:**
  - R programming (ggplot2, dplyr)
  - Mixed-effects models (lme4)
  - Experimental design logic
  - PCIbex basics (if covered)
- **From Course 2:**
  - Bayesian hierarchical modeling (used for production latencies)
  - Parameter recovery (validating models)
  - Generative thinking (what process generates errors?)

**Integration in Course 3:**
- **Experiments:** Design production tasks (Course 1 skills)
- **Models:** Fit hierarchical Bayesian models to production data (Course 2 skills)
- **Theory:** Connect findings to morphological theory (new in Course 3)

**Can be taken standalone** if you have:
- Background in psycholinguistics (or take Course 1 first)
- R programming skills (or take Course 1/2 first)
- Willingness to learn PCIbex quickly

---

## 10. Who Should Take This Course

### Good fit if you:
- Want to conduct original production research
- Are interested in morphological planning / agreement / speech errors
- Comfortable with R and willing to learn PCIbex
- Like hands-on, studio-style learning (not just reading papers)
- Planning a dissertation or QP on production topics

### May struggle if you:
- No prior psycholinguistics background (take Course 1 first)
- Uncomfortable with programming (Course 1 or 2 will help)
- Prefer lecture-style seminars to studio/lab format
- Find 10-week quarters overwhelming

### For advanced graduate students:
This seminar is ideal if you're:
- Preparing a QP or dissertation on production
- Developing experimental skills for your research program
- Seeking publication-ready proposals for psycholinguistics journals (e.g., *JML*, *Cognition*, *LCP*)

---

## 11. Expected Background

### Assumed Knowledge
You should be comfortable with:
- **Psycholinguistics concepts:** Production architecture, incremental planning, lexical access
- **R programming:** Data wrangling (dplyr), visualization (ggplot2), mixed models (lme4)
- **Statistics:** Mixed-effects models, understanding interactions, model comparison

### Will Learn in This Course
- **PCIbex:** Web-based production experiments (audio recording, timing)
- **Morphological theory:** How production models connect to morphosyntactic theory
- **Cross-linguistic design:** Leveraging typological differences to test theories
- **Preregistration:** Writing analysis plans before seeing data

---

## 12. Final Project Expectations

Your final project should:

1. **Motivate a research question** from production theory (2-3 pages)
2. **Review relevant literature** critically (2-3 pages)
3. **Propose an experiment** with:
   - Explicit predictions from competing theories
   - Materials (example items)
   - Design (conditions, counterbalancing, exclusions)
   - Preregistered analysis plan (models, contrasts)
4. **Include pilot data (optional)** or **detailed power analysis**
5. **Discuss implications** for theory and future directions (1-2 pages)

**Format:** ACL/LSA/Cognition style (10 pages)

**Outcome:** Should be submittable to a conference (HSP, LSA, CUNY) or workshop with minor revisions.

---

## 13. Instructor Note

This seminar is the capstone of the sequence, where you apply everything you've learned to tackle an active research question. The quarter format is intense, but the studio model ensures you get individualized feedback and hands-on support.

By Week 10, you should have a conference-ready proposal that you're excited to continue working on. Many students turn these projects into QPs, dissertation chapters, or first-author publications.

I'm committed to helping you develop the best possible project. Use office hours, ask questions, workshop your ideas with peers. This is a collaborative research environment, not a traditional seminar.

Looking forward to building experiments and testing theories together.

Best,
Utku Turk
