# Machine Learning for Language
### Neural Networks, Linguistic Structure, and NLP Applications
**LING 2XXX -- Fall 2026**

**Time:** TBD  
**Location:** TBD  
**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))  
**Office hours:** By appointment  
**Course site:** Canvas

**Prerequisites:** None. No prior programming or math experience required.

---

## 1. Course Description

How do neural networks learn to process language? Can they acquire grammatical knowledge from text alone? What can machine learning tell us about linguistic structure?

This course introduces neural networks and their applications to language, balancing technical foundations with linguistic questions. You will learn how to build text classifiers, train language models, and implement modern NLP systems. But you will also investigate what these models learn: Do they capture syntactic dependencies? Can they generalize across languages? How do their representations compare to human linguistic knowledge? I am excited to explore the intersection of these two fields with you as we build the technology of the future.

By the end of the semester, you will be able to implement neural models in Python, design experiments to probe what they've learned, and critically evaluate claims about AI and language. This is a hands-on course that combines practical ML skills with linguistic analysis.

**No prior programming experience required**—we build skills from scratch.

## 2. Learning Objectives

Upon successful completion of this course, students will be able to:
1.  Implement neural networks for text classification and language modeling in Python/PyTorch.
2.  Understand word embeddings and how meaning is represented in vector space.
3.  Build and train RNNs, LSTMs, and transformer models.
4.  Design probing experiments to test what models learn about linguistic structure.
5.  Analyze attention patterns and model representations.
6.  Evaluate whether models learn syntax, semantics, or surface heuristics.
7.  Apply neural models to practical NLP tasks (sentiment, translation, generation).
8.  Critically evaluate claims about AI capabilities and limitations.

## 3. Course Structure

### Weekly Rhythm
| Component | What it looks like |
| :--- | :--- |
| **Lecture** | Concepts, math intuition, and how things work (Tue/Thu first half). |
| **Coding lab** | Hands-on Python work: implementing models, debugging (Tue/Thu second half). |
| **Homework** | Biweekly problem sets with coding + conceptual questions. |
| **Model of the Week** | Each week, we spotlight one influential model or paper. You'll interact with it hands-on—not just read about it, but run it, break it, and understand what makes it tick. |

### The Three Questions
Every model we study will be interrogated through three lenses:
1. **What can it do?** (Capabilities: tasks it solves, benchmarks it passes)
2. **What can't it do?** (Limitations: where it fails, what it doesn't learn)
3. **What does that tell us about language?** (Implications: what this reveals about linguistic structure and cognition)

This isn't just a coding class or just a linguistics class—it's both. You'll build the models AND use them as scientific instruments to investigate language.

### Your Learning Arc
- **Weeks 1-5**: Build your own neural networks from scratch (no magic libraries—you'll implement backprop by hand!)
- **Weeks 6-9**: Explore what models learn about language structure (syntax, semantics, pragmatics)
- **Weeks 10-14**: Work with state-of-the-art transformers and LLMs
- **Weeks 15-17**: Critical evaluation—when do models succeed for the wrong reasons?

### Tools We Use
*   **Python:** primary programming language.
*   **PyTorch:** neural network framework.
*   **Google Colab:** cloud-based coding environment.
*   **Hugging Face:** pretrained models and datasets.

## 4. Course Requirements

### 4.1 Grading
| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 15 | Active engagement in labs. |
| Homework (5x) | 40 | Coding + concepts (8% each). |
| Midterm project | 10 | Classifier proposal. |
| Final project | 35 | Detailed research proposal. |

### 4.2 Projects
*   **Midterm (Week 9):** Propose a neural classifier for a linguistic phenomenon (e.g., modal reading, genericity). 2-3 page proposal.
*   **Final (Finals week):** Detailed research proposal investigating a linguistic question using neural networks. 8-10 page proposal in ACL format + presentation.

## 5. Course Schedule

| Wk | Topic | Readings (Selected) | Lab / Due |
| :-- | :--- | :--- | :--- |
| 1 | Intro; NNs and Language | Newell (1973); Marr (1982) | Python basics I |
| 2 | Representing words | Jurafsky & Martin Ch. 6 | Python basics II |
| 3 | Perceptrons; Gradient Descent | Goodfellow et al. Ch. 6 | Perceptron from scratch |
| 4 | MLP; Backprop | Goodfellow et al. Ch. 6; Olah | PyTorch; **Due:** HW1 |
| 5 | Word Embeddings | Jurafsky & Martin Ch. 6; Ettinger | Probing structure |
| 6 | RNNs; Language Modeling | Jurafsky & Martin Ch. 9; Karpathy | Character LM |
| 7 | Evaluating Linguistic Knowledge | Marvin & Linzen (2018); BLiMP | Minimal pairs; **Due:** HW2 |
| 8 | LSTMs | Olah (2015); Hochreiter & Schmidhuber | LSTM implementation |
| 9 | **Midterm Presentations** | | **Due:** Midterm Project |
| 10 | Attention Mechanisms | Bahdanau et al. (2015); Vig & Belinkov | Visualizing attention; **Due:** HW3 |
| 11 | Transformers I | Vaswani et al. (2017); Illustrated Transformer | Self-attention |
| 12 | Transformers II (BERT/GPT) | Devlin et al.; Radford et al. | Fine-tuning BERT |
| 13 | LLMs \& Prompting | GPT-3 paper; Chain-of-thought | GPT prompts; **Due:** HW4 |
| 14 | Counterfactual Evaluation | Kaushik et al. (2020); Gardner et al. | Minimal pair testing |
| 15 | Model Evaluation (Surprisal) | Futrell et al. (2019); Wilcox et al. | Computing surprisal |
| 16 | Limitations \& Ethics | Bender & Koller (2020); Stochastic Parrots | Bias detection; **Due:** HW5 |
| 17 | **Final Presentations** | | Peer feedback |
| Final | | | **Due:** Final Report |

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)
*   **Time management:** Expect 8--10 hours/week. Start homework early.
*   **Computer use:** Laptops for labs only.
*   **Reading papers:** Read strategically. Take notes by hand.
*   **Coding:** Debug systematically. Pair program.

### 6.2 Academic Integrity
Do your own work. You may collaborate on homework, but must write your own code and answers. Cite sources.

### 6.3 Use of LLMs
LLMs may be used for **support** (debugging, learning syntax) but not to generate solutions. Document any use.

### 6.4 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me early in the semester. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

## 7. Resources
*   **Textbooks:** Jurafsky & Martin (3rd ed.); Goodfellow et al. (Deep Learning).
*   **Frameworks:** PyTorch, Hugging Face.
