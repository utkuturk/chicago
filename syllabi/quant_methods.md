# Quantitative Methods for Linguistics
### R, Bayesian Statistics, and Reproducible Research
**LING 3XXX -- Fall 2026**

**Time:** TBD  
**Location:** TBD  
**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))  
**Office hours:** By appointment  
**Course site:** Canvas

**Prerequisites:** Basic statistics. No prior programming experience required.

**[📄 Download PDF Version](quant_methods.pdf)**

---

## 1. Course Description

How do we understand what statistical models actually do? How can we test whether our models are appropriate for our data? What does it mean for a model to "learn" from data?

This course takes a **simulation-first approach** to quantitative methods in linguistics. I know statistics can be intimidating—I've been there! My goal is to make it approachable by peeling back the math and showing you what's really happening under the hood. Rather than treating statistical models as black boxes that magically produce p-values, we'll build models from the ground up by simulating data. This approach makes abstract statistical concepts concrete: you'll see exactly how regression works, what mixed-effects models assume, and why Bayesian inference is powerful.

Following the approach of McElreath's *Statistical Rethinking*, we emphasize understanding models as generative processes. You'll learn to: (i) simulate data from a specified model, (ii) fit models to recover the parameters you simulated, (iii) check whether your model assumptions are met, and (iv) use simulations for power analysis and model validation.

By the end of the semester, you'll be able to design and execute quantitative studies, analyze complex linguistic datasets, fit appropriate statistical models, and—most importantly—understand what those models are actually doing. I'm excited to work through this journey with you.

**No prior programming or statistics experience required**—we build everything from scratch through simulation.

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:
1.  Program in R for data analysis and simulation.
2.  Simulate data from statistical models (regression, mixed-effects, etc.).
3.  Understand models as generative processes.
4.  Fit and interpret linear and logistic regression models.
5.  Understand and apply mixed-effects models for repeated measures data.
6.  Use simulation to check model assumptions and validate results.
7.  Conduct power analysis through data simulation.
8.  Fit Bayesian models using Stan and brms.
9.  Specify informative priors based on domain knowledge.
10. Create reproducible research documents using Quarto.
11. Critically evaluate statistical claims in linguistic research.

## 3. Course Structure

### Weekly Rhythm
| Component | What it looks like |
| :--- | :--- |
| **Lecture** | Concepts, statistical theory, and when to use which methods (Tue/Thu first half). |
| **Coding lab** | Hands-on R work: data wrangling, visualization, model fitting (Tue/Thu second half). |
| **Homework** | Weekly problem sets with coding + interpretation questions. |
| **Simulation Challenge** | Each week features a "Simulation Challenge"—can you generate data that breaks a model's assumptions? Can you recover parameters from messy data? These challenges build intuition for what models actually do. |

### Why Simulation-First?
Traditional stats courses teach you to run tests on data. This course teaches you to **think like a statistician**: if I believe X about the world, what data would I expect to see? What patterns would surprise me? By simulating data first, you develop deep intuition about what models assume and when they fail.

**Simulation Challenges** (weekly coding puzzles):
- Week 2: Simulate 100 coin flips—how often do you get 5 heads in a row?
- Week 4: How many participants do you need to detect a 50ms difference in reading times?
- Week 6: Can you trick a regression model by adding a correlated predictor?
- Week 8: Simulate crossed random effects—what happens when you ignore them?

### Tools We Use
*   **R:** primary programming language.
*   **RStudio:** integrated development environment.
*   **tidyverse:** data wrangling and visualization.
*   **lme4 & brms:** mixed-effects models.
*   **Stan:** Bayesian inference engine.
*   **Quarto:** reproducible research documents.

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 15 | Active engagement in labs; exercises. |
| Homework (10x) | 50 | Coding + interpretation questions (5% each). |
| Midterm project | 10 | Data analysis report (regression/mixed models). |
| Final project | 25 | Complete analysis with Quarto report + presentation. |

### 4.2 Homework Policy
Homework is due on Canvas by 11:59pm. Late submissions lose 10% per day (up to 3 days). You may collaborate, but must write your own code and answers.

### 4.3 Projects
*   **Midterm (Week 9):** Analyze a dataset using regression or lmer. 3-4 page report.
*   **Final (Finals week):** Complete data analysis project. Clear research question, data collection/curation, analysis, validation, interpretation. 8-10 page reproducible Quarto document.

## 5. Course Schedule

| Wk | Topic | Readings / Resources | Lab / due |
| :-- | :--- | :--- | :--- |
| 1 | Intro; Why simulation?; R basics | McElreath Ch. 1-2; R4DS Ch. 1-4 | Installing R/RStudio |
| 2 | Simple simulations; Sampling | McElreath Ch. 3; R4DS Ch. 5 | Coin flips; **Due:** HW1 |
| 3 | Simulations, p-values, NHST | McElreath Ch. 3; Gelman & Hill Ch. 1-2 | Null distributions |
| 4 | Power analysis via simulation | SIMR; DeBruine & Barr (2021) | Sample size planning; **Due:** HW2 |
| 5 | Simple regression | McElreath Ch. 4; Gelman & Hill Ch. 3 | Generative models |
| 6 | Multiple regression; Interactions | McElreath Ch. 5; Gelman & Hill Ch. 4 | Interactions; **Due:** HW3 |
| 7 | GLMs; Logistic regression | McElreath Ch. 10-11; Gelman & Hill Ch. 5 | Binary outcomes |
| 8 | Hierarchical data structures | McElreath Ch. 13; DeBruine & Barr | Nested/Crossed; **Due:** HW4 |
| 9 | LMER I: Random intercepts | McElreath Ch. 13; Winter Ch. 9-10 | Random intercepts; **Due:** Midterm |
| 10 | LMER II: Random slopes | McElreath Ch. 13; Barr et al. (2013) | Maximal models; **Due:** HW5 |
| 11 | Intro to Bayesian Inference | McElreath Ch. 1-3 | Priors/Posteriors |
| 12 | Bayesian regression (brms) | McElreath Ch. 4, 9 | Fitting Bayesian models; **Due:** HW6 |
| 13 | Diagnostics & PPC | McElreath Ch. 9; Gelman Ch. 6 | Validating models |
| 14 | Model comparison | McElreath Ch. 7; Vehtari et al. | WAIC, LOO; **Due:** HW7 |
| 15 | Reproducible research (Quarto) | Quarto docs; Marwick et al. (2018) | Creating Quarto docs |
| 16 | Final presentations | | Peer feedback |
| Final | | | **Due:** Final Project |

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)
*   **Time management:** Expect 8--10 hours/week. Don't cram. Start debugging early.
*   **Learning to code:** Everyone struggles at first. Read error messages. Google is your friend.
*   **Understanding statistics:** Focus on concepts. Visualize everything. Connect to linguistics.

### 6.2 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me as early as possible in the semester. I'm committed to making sure everyone can succeed in this course.

If you're struggling—whether it's with the material, coding, or anything else in life—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together. Your wellbeing matters more than any assignment deadline.

---

## Quarter System (10 Weeks)

For institutions on a quarter system, here's a condensed 10-week version:

| Wk | Topic | Readings (Required) | Lab / Due |
| :-- | :--- | :--- | :--- |
| 1 | R basics; data wrangling | Wickham & Grolemund Ch. 1-5; Winter Ch. 1 | R, RStudio, dplyr basics |
| 2 | Data visualization | Wickham & Grolemund Ch. 3; Healy Ch. 1-3 | ggplot2; publication-quality figures; **Due:** HW1 |
| 3 | Linear regression | Winter Ch. 5-7; Gelman & Hill Ch. 3-4 | Simple and multiple regression |
| 4 | Logistic regression | Winter Ch. 8; Gelman & Hill Ch. 5 | Categorical outcomes; predictions; **Due:** HW2 |
| 5 | Mixed-effects models | Winter Ch. 9-11; Baayen et al. (2008); Barr et al. (2013) | Random intercepts and slopes; **Due:** Midterm project |
| 6 | Data simulation | DeBruine & Barr (2021); Green & MacLeod (2016) | Simulating data; power analysis; **Due:** HW3 |
| 7 | Bayesian inference | McElreath Ch. 1-3; Bürkner (2017) | Priors, posteriors, brms |
| 8 | Model comparison | Gelman et al. Ch. 6-7; Vehtari et al. (2017) | Cross-validation; information criteria; **Due:** HW4 |
| 9 | Reproducible research | Quarto documentation; Marwick et al. (2018) | Quarto documents; final project work |
| 10 | Final presentations | | 10-min presentations; **Due:** Final project |

**Quarter grading:** Participation (15%), Homework 4x (40%, 10% each), Midterm project (15%), Final project (30%).

---

## 7. Resources
*   **Primary Text:** McElreath (2020). *Statistical Rethinking*.
*   **R:** Wickham & Grolemund (2017). *R for Data Science*.
*   **Linguistics:** Winter (2020). *Statistics for Linguists*.
