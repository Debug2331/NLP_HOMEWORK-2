"""
CS5760 NLP - Homework 2, Part II, Q1
Bigram Language Model built from a small training corpus.
"""

from collections import defaultdict

corpus = [
    "<s> I love NLP </s>",
    "<s> I love deep learning </s>",
    "<s> deep learning is fun </s>",
]

tokenized = [sentence.split() for sentence in corpus]

# --- Unigram counts ---
unigram_counts = defaultdict(int)
for sent in tokenized:
    for word in sent:
        unigram_counts[word] += 1

# --- Bigram counts ---
bigram_counts = defaultdict(int)
for sent in tokenized:
    for i in range(len(sent) - 1):
        bigram_counts[(sent[i], sent[i + 1])] += 1

# --- MLE bigram probabilities: P(w_i | w_{i-1}) = count(w_{i-1}, w_i) / count(w_{i-1}) ---
def bigram_prob(w_prev, w_curr):
    denom = unigram_counts[w_prev]
    if denom == 0:
        return 0.0
    return bigram_counts[(w_prev, w_curr)] / denom

def sentence_probability(sentence, verbose=True):
    words = sentence.split()
    prob = 1.0
    if verbose:
        print(f"\nSentence: {sentence}")
    for i in range(len(words) - 1):
        p = bigram_prob(words[i], words[i + 1])
        if verbose:
            print(f"  P({words[i+1]:9s}| {words[i]:9s}) = {p:.4f}")
        prob *= p
    if verbose:
        print(f"  => P(sentence) = {prob:.6f}")
    return prob

if __name__ == "__main__":
    print("Unigram counts:")
    for w, c in unigram_counts.items():
        print(f"  {w}: {c}")

    print("\nBigram counts:")
    for (w1, w2), c in bigram_counts.items():
        print(f"  ({w1}, {w2}): {c}")

    s1 = "<s> I love NLP </s>"
    s2 = "<s> I love deep learning </s>"

    p1 = sentence_probability(s1)
    p2 = sentence_probability(s2)

    print("\n--- Result ---")
    if p1 > p2:
        print(f"The model prefers S1: \"{s1}\" (P={p1:.6f} > P={p2:.6f})")
        print("Reason: it reuses higher-frequency bigrams (I->love, love->NLP, NLP->end)")
        print("observed more consistently relative to their context counts in the corpus.")
    elif p2 > p1:
        print(f"The model prefers S2: \"{s2}\" (P={p2:.6f} > P={p1:.6f})")
    else:
        print("Both sentences are equally probable under the model.")
