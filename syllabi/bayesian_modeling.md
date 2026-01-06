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
