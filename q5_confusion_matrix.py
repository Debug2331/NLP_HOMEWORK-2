"""
CS5760 NLP - Homework 2, Part I, Q5.3
Computes per-class precision/recall and macro/micro averages
from a multi-class confusion matrix.
"""

# Rows = System (predicted), Columns = Gold (actual)
labels = ["Cat", "Dog", "Rabbit"]
matrix = {
    "Cat":    {"Cat": 5,  "Dog": 10, "Rabbit": 5},
    "Dog":    {"Cat": 15, "Dog": 20, "Rabbit": 10},
    "Rabbit": {"Cat": 0,  "Dog": 15, "Rabbit": 10},
}

def precision_recall(matrix, labels):
    results = {}
    for c in labels:
        tp = matrix[c][c]
        predicted_total = sum(matrix[c][g] for g in labels)          # row sum
        actual_total = sum(matrix[p][c] for p in labels)             # column sum
        precision = tp / predicted_total if predicted_total else 0.0
        recall = tp / actual_total if actual_total else 0.0
        results[c] = {"TP": tp, "predicted_total": predicted_total,
                       "actual_total": actual_total,
                       "precision": precision, "recall": recall}
    return results

def macro_average(results, labels):
    macro_p = sum(results[c]["precision"] for c in labels) / len(labels)
    macro_r = sum(results[c]["recall"] for c in labels) / len(labels)
    return macro_p, macro_r

def micro_average(results, labels):
    total_tp = sum(results[c]["TP"] for c in labels)
    total_predicted = sum(results[c]["predicted_total"] for c in labels)
    total_actual = sum(results[c]["actual_total"] for c in labels)
    micro_p = total_tp / total_predicted
    micro_r = total_tp / total_actual
    return micro_p, micro_r

if __name__ == "__main__":
    results = precision_recall(matrix, labels)
    print("Per-class metrics:")
    for c in labels:
        r = results[c]
        print(f"  {c:7s} TP={r['TP']:2d}  Precision={r['precision']:.4f}  Recall={r['recall']:.4f}")

    macro_p, macro_r = macro_average(results, labels)
    micro_p, micro_r = micro_average(results, labels)

    print("\nMacro-averaged Precision: {:.4f}".format(macro_p))
    print("Macro-averaged Recall:    {:.4f}".format(macro_r))
    print("Micro-averaged Precision: {:.4f}".format(micro_p))
    print("Micro-averaged Recall:    {:.4f}".format(micro_r))
