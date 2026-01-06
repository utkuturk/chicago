# Machine Learning for Language
### Neural Networks, Linguistic Structure, and NLP Applications
**LING 3XXX -- Fall Quarter 2026**

**Time:** TBD (meets 4 hours/week: 2 sessions of 2 hours each)

**Location:** TBD

**Instructor:** Utku Turk ([utkuturk@umd.edu](mailto:utkuturk@umd.edu))

**Office hours:** By appointment

**Course site:** Canvas

**Prerequisites:** None. No prior programming or math experience required.

**Format:** Quarter system (10 weeks)

---

## 1. Course Description

How do neural networks learn to process language? Can they acquire grammatical knowledge from text alone? What can machine learning tell us about linguistic structure?

This course introduces neural networks and their applications to language, balancing technical foundations with linguistic questions. You will learn how to build text classifiers, train language models, and implement modern NLP systems. But you will also investigate what these models learn: Do they capture syntactic dependencies? Can they generalize across languages? How do their representations compare to human linguistic knowledge? I am excited to explore the intersection of these two fields with you as we build the technology of the future.

By the end of the quarter, you will be able to implement neural models in Python, design experiments to probe what they've learned, and critically evaluate claims about AI and language. This is a hands-on course that combines practical ML skills with linguistic analysis.

**No prior programming experience required**—we build skills from scratch.

---

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

---

## 3. Course Structure

### Weekly Rhythm

| Component | What it looks like |
| :--- | :--- |
| **Lecture** | Concepts, math intuition, and how things work (Session 1). |
| **Coding lab** | Hands-on Python work: implementing models, debugging (Session 2). |
| **Homework** | Four problem sets with coding + conceptual questions. |
| **Model of the Week** | Each week, we spotlight one influential model or paper. You'll interact with it hands-on—not just read about it, but run it, break it, and understand what makes it tick. |

### The Three Questions

Every model we study will be interrogated through three lenses:

1. **What can it do?** (Capabilities: tasks it solves, benchmarks it passes)
2. **What can't it do?** (Limitations: where it fails, what it doesn't learn)
3. **What does that tell us about language?** (Implications: what this reveals about linguistic structure and cognition)

This isn't just a coding class or just a linguistics class—it's both. You'll build the models AND use them as scientific instruments to investigate language.

### Your Learning Arc

- **Weeks 1-3**: Build your own neural networks from scratch (no magic libraries—you'll implement backprop by hand!)
- **Weeks 4-6**: Explore what models learn about language structure (syntax, semantics, pragmatics)
- **Weeks 7-9**: Work with state-of-the-art transformers and LLMs
- **Week 10**: Critical evaluation—when do models succeed for the wrong reasons?

### Tools We Use

*   **Python:** primary programming language.
*   **PyTorch:** neural network framework.
*   **Google Colab:** cloud-based coding environment.
*   **Hugging Face:** pretrained models and datasets.

---

## 4. Course Requirements

### 4.1 Grading

| Item | % | What counts |
| :--- | :--: | :--- |
| Participation | 15 | Active engagement in labs. |
| Homework (4x) | 48 | Coding + concepts (12% each). |
| Midterm presentation | 7 | Classifier proposal (Week 5). |
| Final project | 30 | Detailed research proposal (8-10 pages). |

### 4.2 Projects

*   **Midterm (Week 5):** Propose a neural classifier for a linguistic phenomenon (e.g., modal reading, genericity). 2-page proposal + 5-minute presentation.
*   **Final (Finals week):** Detailed research proposal investigating a linguistic question using neural networks. 8-10 page proposal in ACL format + presentation.

---

## 5. Course Schedule (10 Weeks)

| Wk | Topic | Readings (Selected) | Lab / Due |
| :-- | :--- | :--- | :--- |
| 1a | Intro; NNs and Language | Newell (1973); Marr (1982) | Python basics I |
| 1b | Representing words | Jurafsky & Martin Ch. 6 | Python basics II |
| 2a | Perceptrons; Gradient Descent | Goodfellow et al. Ch. 6 | Perceptron from scratch |
| 2b | MLP; Backprop | Goodfellow et al. Ch. 6; Olah | PyTorch basics |
| 3a | Word Embeddings | Jurafsky & Martin Ch. 6 | Training embeddings |
| 3b | Probing Structure | Ettinger (2020) | **Due:** HW1; Probing lab |
| 4a | RNNs; Language Modeling | Jurafsky & Martin Ch. 9; Karpathy | Character LM |
| 4b | Evaluating Linguistic Knowledge | Marvin & Linzen (2018); BLiMP | Minimal pairs testing |
| 5a | LSTMs | Olah (2015); Hochreiter & Schmidhuber | **Midterm presentations** |
| 5b | LSTM implementation | | LSTM coding; **Due:** HW2 |
| 6a | Attention Mechanisms | Bahdanau et al. (2015) | Visualizing attention |
| 6b | Attention & Syntax | Vig & Belinkov (2019) | Attention analysis |
| 7a | Transformers I | Vaswani et al. (2017); Illustrated Transformer | **Due:** HW3; Self-attention |
| 7b | Transformers II (BERT/GPT) | Devlin et al.; Radford et al. | Fine-tuning BERT |
| 8a | LLMs & Prompting | GPT-3 paper; Chain-of-thought | GPT prompts |
| 8b | Counterfactual Evaluation | Kaushik et al. (2020); Gardner et al. | Minimal pair testing |
| 9a | Model Evaluation (Surprisal) | Futrell et al. (2019); Wilcox et al. | **Due:** HW4; Computing surprisal |
| 9b | Limitations & Ethics | Bender & Koller (2020); Stochastic Parrots | Bias detection |
| 10a | Final Presentations I | | Peer feedback |
| 10b | Final Presentations II | | Peer feedback; Wrap-up |
| Finals | | | **Due:** Final Report |

**Note:** Each week has two sessions (a/b). Session (a) focuses on concepts; session (b) focuses on hands-on coding.

---

## 6. Policies

### 6.1 What you might struggle with (and how to succeed)

*   **Time management:** Expect 10-12 hours/week outside class. Start homework early.
*   **Python learning curve:** Week 1-2 will be challenging if you're new to programming. Use office hours!
*   **Math anxiety:** We explain through intuition and visualization, not proofs. Focus on understanding, not memorization.
*   **Reading papers:** Read strategically. Focus on key contributions, not every detail.
*   **Coding:** Debug systematically. Pair program. Use Google Colab so everyone has the same environment.

### 6.2 Quarter System Considerations

This course moves **fast**:

*   **Week 3 (quarter) = Week 5 (semester):** Already implementing backprop by hand
*   **Week 7 (quarter) = Week 11 (semester):** Already working with transformers
*   **No catching up later:** Missing one week = missing 10% of content
*   **Use labs effectively:** Don't skip session (b)—that's where you learn to code

### 6.3 Academic Integrity
Do your own work. You may collaborate on homework, but must write your own code and answers. Cite sources.

### 6.4 Use of LLMs
LLMs may be used for **support** (debugging, learning syntax) but not to generate solutions. Document any use.

**Pedagogical note:** Part of this course is understanding how LLMs work. Using ChatGPT to solve homework defeats the purpose—you're trying to build the thing that ChatGPT is!

### 6.5 Accessibility & Wellness
If you need accommodations, please contact the relevant campus office and talk to me early in the quarter. If you are struggling—academically or personally—please reach out. I really appreciate when students communicate with me, and I'm happy to work with you to make a plan together.

---

## 7. Resources

### Textbooks (Free Online)
*   **Jurafsky & Martin (3rd ed.).** *Speech and Language Processing*. [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)
*   **Goodfellow et al.** *Deep Learning*. [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)

### Online Tutorials
*   **PyTorch Tutorials:** [https://pytorch.org/tutorials/](https://pytorch.org/tutorials/)
*   **The Illustrated Transformer:** [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)
*   **Karpathy's Neural Networks:** [https://karpathy.github.io/](https://karpathy.github.io/)

### Frameworks
*   **PyTorch:** Neural network implementation
*   **Hugging Face:** Pre-trained models ([https://huggingface.co/](https://huggingface.co/))
*   **Google Colab:** Free GPU access ([https://colab.research.google.com/](https://colab.research.google.com/))

---

## 9. Connection to Course Sequence

This course is **Course 1** in the AI/NLP sequence:
- **Course 1 (this course):** Machine Learning for Language (mixed) - Fall Quarter
- **Course 2:** Advanced NLP & AI for Linguistics (grad) - Winter Quarter

**Skills developed here that transfer to Course 2:**
- **PyTorch:** Used for implementing interpretability methods
- **Transformers:** Course 2 probes transformer representations
- **Attention:** Course 2 analyzes attention patterns in depth
- **Critical thinking:** Course 2 evaluates interpretability claims

**Can be taken standalone** if you just want ML/NLP skills without the interpretability focus.

---

## 10. Who Should Take This Course

### Good fit if you:

- Curious about how neural networks process language
- Want to learn Python and PyTorch
- Like hands-on coding (not just theory)
- Interested in linguistics AND computation
- Comfortable with mathematical intuition (no proofs required)

### May struggle if you:

- Uncomfortable with programming (we teach from scratch, but it's fast-paced)
- Prefer lecture-only courses (half the time is coding labs)
- Find 10-week quarters overwhelming

### No Prerequisites

Seriously—we assume zero programming background. Week 1 starts with "what is a variable?"

### For Different Student Populations

- **Linguistics undergrads:** Learn computational skills for NLP career paths
- **CS undergrads:** Gain linguistic perspective on NLP (beyond engineering)
- **Linguistics grad students:** Prepare for computational linguistics research
- **CS grad students:** Understand what NLP systems actually learn about language

---

## 11. What You'll Build

By the end of the quarter, you'll have:

1. **Perceptron from scratch** (Week 2) - no libraries, just NumPy
2. **Multi-layer network with backprop** (Week 3) - understand gradient descent
3. **Word embeddings** (Week 3) - train your own Word2Vec-style model
4. **Character-level language model** (Week 4) - generate text with RNNs
5. **LSTM classifier** (Week 5) - sentiment analysis
6. **Attention mechanism** (Week 6) - visualize what models attend to
7. **Transformer** (Week 7) - self-attention and multi-head attention
8. **BERT fine-tuning** (Week 7) - use pre-trained models
9. **GPT prompting** (Week 8) - in-context learning experiments
10. **Probing classifier** (Week 9) - test what models learn about syntax

Plus: A **final research proposal** investigating a linguistic question with neural networks.

---

## 12. Instructor Note

Welcome! This course moves fast, but we'll move together. My goal is to demystify neural networks—show you that they're not magic, just math and code. By Week 10, you'll be able to read an NLP paper and think "I could implement that."

The linguistics perspective is what makes this course special. We don't just ask "does it work?"—we ask "what does it learn?" and "what does that tell us about language?" This is the future of linguistics: using computational models as scientific instruments.

I'm excited to build models and test theories with you. Let's discover what neural networks can teach us about language.

Best,
Utku Turk
