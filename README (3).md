# CS5760 Natural Language Processing — Homework 2

**Student name:** Meka Preetam Reddy
**Student ID:** 700794858
**Course:** CS5760 Natural Language Processing, Fall 2026
**University:** University of Central Missouri — Dept. of Computer Science & Cybersecurity

## Contents

| File | Description |
|---|---|
| `Homework_2_Solutions.docx` | Full write-up: all Part I written-calculation answers (Q1–Q5) and the explanations/outputs for the Part II and Q5.3 programs. |
| `q5_confusion_matrix.py` | Part I, Q5.3 — computes per-class precision/recall and macro/micro-averaged precision & recall from the given 3-class (Cat/Dog/Rabbit) confusion matrix. |
| `part2_q1_bigram_model.py` | Part II, Q1 — builds a bigram language model from a 3-sentence training corpus, estimates bigram probabilities with MLE, and scores two test sentences to show which one the model prefers. |

## How to run

Both scripts use only the Python standard library (no dependencies to install).

```bash
python3 q5_confusion_matrix.py
python3 part2_q1_bigram_model.py
```

### q5_confusion_matrix.py
Reads the confusion matrix (System = predicted rows, Gold = actual columns) as a hard-coded dictionary, then prints:
- Per-class true positives, precision, and recall for Cat, Dog, Rabbit
- Macro-averaged precision/recall (simple mean across classes)
- Micro-averaged precision/recall (pooled counts across all classes)

**Expected output:**
```
Per-class metrics:
  Cat     TP= 5  Precision=0.2500  Recall=0.2500
  Dog     TP=20  Precision=0.4444  Recall=0.4444
  Rabbit  TP=10  Precision=0.4000  Recall=0.4000

Macro-averaged Precision: 0.3648
Macro-averaged Recall:    0.3648
Micro-averaged Precision: 0.3889
Micro-averaged Recall:    0.3889
```

### part2_q1_bigram_model.py
Tokenizes the training corpus, builds unigram and bigram counts, computes MLE bigram probabilities P(w_i | w_{i-1}), and evaluates the probability of two candidate sentences using those probabilities, printing which sentence the model prefers and why.

**Expected output (summary):**
```
S1 = <s> I love NLP </s>              -> P(S1) = 0.333333
S2 = <s> I love deep learning </s>    -> P(S2) = 0.166667
Model prefers S1
```

## Notes

- Part I, Q1 (Naive Bayes worked example) uses the standard textbook priors/likelihoods (Jurafsky & Martin movie-review example), since the specific "Q2" slide numbers referenced in the assignment weren't provided with this file — see the note in `Homework_2_Solutions.docx` for details.
- All written calculations (Q1–Q4, and the by-hand portion of Q5) are in `Homework_2_Solutions.docx`, alongside the code and program output for the two programming questions.
