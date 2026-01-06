# Bayesian Cognitive Modeling for Linguistics
### From Theory to Implementation
**LING 4XXX -- Fall 2026**

**Time:** TBD  
**Location:** TBD  
**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))  
**Office hours:** By appointment  
**Course site:** Canvas

**Prerequisites:** Introduction to programming (R or Python) and basic statistics.

---

## 1. Course Description

How do we test theories of cognition? How can we formalize our hypotheses about how the mind works? This course introduces computational modeling as a tool for understanding cognitive processes, with a specific focus on **Bayesian Cognitive Modeling**.

Unlike data analysis, which asks "is there an effect?", cognitive modeling asks "what underlying process generated this data?". We will use the probabilistic programming language **Stan** to build, fit, and evaluate generative models of cognition. We will cover the full workflow: from defining a mathematical model of a cognitive process, to implementing it in code, to recovering parameters from simulated data, and finally applying it to real human behavioral data.

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:
1.  Explain the purpose of quantitative modeling in cognitive science and distinguish among descriptive, predictive, and explanatory models.
2.  Critically evaluate and implement simulations of cognitive models.
3.  Implement Bayesian cognitive models using **Stan** and interpret their structure.
4.  Evaluate the robustness of Bayesian cognitive models (parameter recovery, replication).
5.  Clearly communicate the structure and performance of a Bayesian cognitive model.

## 3. Course Content & Structure

The course is divided into five main modules:
1.  **Foundations:** Role of computational modeling; Simulation; Generative stance.
2.  **Probability:** Probability theory and Bayes rule; Generative processes.
3.  **Tools:** Bayesian models in **Stan**.
4.  **Modeling:** Cognitive modeling in a Bayesian framework (SDT, Categorization, Memory).
5.  **Evaluation:** Model comparison, parameter recovery, and robustness checks.

### The Generative Stance
This course teaches you to think like a **theoretician**. Instead of asking "what pattern is in the data?", you'll ask "if my theory is true, what data would I see?" This flips statistics on its head.

**Weekly Mathematical Intuition Building:**
Each week begins with a conceptual question before we touch code:
- Week 2: "If you flip a coin 10 times and get 7 heads, what can you infer about the coin's bias?"
- Week 5: "How does Signal Detection Theory formalize the difference between sensitivity and bias?"
- Week 7: "What does it mean for a model to 'pool' information across participants?"
- Week 9: "Why do we need model comparison when all models are wrong?"

We'll build mathematical intuition through simulation, visualization, and analogy—not calculus proofs.

### From Theory to Implementation
Each model follows the same workflow:
1. **Formalize the theory** (What are we claiming about cognition?)
2. **Specify the generative process** (How would a god generate this data?)
3. **Implement in Stan** (Translate the theory into code)
4. **Simulate fake data** (Can we recover our parameters?)
5. **Apply to real data** (Does the theory fit human behavior?)
6. **Evaluate robustness** (Where does the model break?)

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 10 | Active engagement in labs. |
| Weekly Labs (10x) | 40 | Coding assignments in R/Stan (4% each). |
| Midterm Project | 20 | Replicating a simple cognitive model. |
| Final Project | 30 | Implementing and testing a novel/extended model. |

### 4.2 Labs & Projects
*   **Labs:** Weekly implementation tasks in R and Stan.
*   **Midterm:** Replicate a standard model (e.g., SDT, GCM). Focus on implementation.
*   **Final:** Choose a phenomenon, implement a Bayesian model, simulate data, and fit/evaluate it.

## 5. Course Schedule

*Readings based on Vasishth et al. (Bayesian Cognitive Modeling) and Lee & Wagenmakers.*

| Wk | Topic | Readings / Concepts | Lab / Assignment |
| :-- | :--- | :--- | :--- |
| **MODULE 1** | **Foundations** | | |
| 1 | Intro to Cognitive Modeling | Generative stance; Descriptive vs Explanatory | Lab 1: Simulating processes |
| 2 | Probability & Bayes Rule | Joint/Conditional probability; Bayes Theorem | Lab 2: Probability math |
| 3 | Intro to Stan | Probabilistic programming; Stan syntax | Lab 3: Hello World in Stan |
| **MODULE 2** | **Basic Models** | **(Lee & Wagenmakers)** | |
| 4 | Parameter Estimation | Binomial rate; Gaussian parameters | Lab 4: Inferring parameters |
| 5 | Signal Detection Theory (SDT) | Equal variance SDT; d' and c | Lab 5: Implementing SDT |
| 6 | Latent Variables | GCM; Change detection; Exemplar theory | Lab 6: GCM implementation |
| **MODULE 3** | **Hierarchical Structures** | | |
| 7 | Hierarchical Models I | Pooling; Shrinkage; Hyperparameters | Lab 7: Hierarchical Binomial |
| 8 | Hierarchical Models II | Individual differences; Log-normal RTs | **Due:** Midterm Project |
| 9 | Model Comparison | Bayes Factors; CV; WAIC; LOO | Lab 8: Comparing models |
| **MODULE 4** | **Advanced Architectures** | **(Vasishth et al.)** | |
| 10 | Multinomial Processing Trees | MPTs; Categorical responses | Lab 9: MPTs for Aphasia |
| 11 | Mixture Models | Fast-guess; Speed-accuracy trade-off | Lab 10: Mixture modeling |
| 12 | Accumulator Models (LBA) | Log-normal race model; Lexical decision | |
| **MODULE 5** | **Evaluation & Project** | | |
| 13 | Robustness | Posterior predictive checks; Recovery | |
| 14 | Final Project Workshop I | Troubleshooting Stan code | |
| 15 | Final Project Workshop II | Peer review of preliminary results | |
| 16 | Final Presentations | Student presentations | **Due:** Final Project Report |

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)
**Coding in Stan:** Stan can be challenging because it is declarative (you declare the model) rather than imperative. But don't worry—we will tackle this together, starting simple and building up complexity line by line.
*   **Start simple:** Build the simplest possible model that compiles.
*   **Use the manual:** The Stan User Guide is excellent.
*   **Simulate first:** Always check if you can recover parameters from simulated data.

**Bayesian concepts:**
*   Focus on the **generative process**: "How would a god generate this data?"
*   Focus on interpreting the posterior distribution, not the integrals.

### 6.2 Academic Integrity
You may collaborate on code, but you must write your own write-ups and understand every line of code you submit.

### 6.3 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me early in the semester. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

## 7. Resources
1.  Lee, M. D., & Wagenmakers, E. J. (2014). *Bayesian Cognitive Modeling*.
2.  Vasishth et al. (2024). *Introduction to Bayesian Data Analysis for Cognitive Science*. [Online Book](https://bruno.nicenboim.me/bayescogsci/)
3.  [Stan User Guide](https://mc-stan.org/users/documentation/)
