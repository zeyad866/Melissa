#!/usr/bin/env python3
import argparse
import sys
from typing import Dict, List, Sequence, Set, Union

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def calculate_precision_recall_f1(tp: int, fp: int, fn: int) -> Dict[str, Union[int, float]]:
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    return {
        "true_positives": tp,
        "false_positives": fp,
        "false_negatives": fn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def calculate_precision_at_k(
    ranked_items: Sequence[Union[str, int]],
    relevant_set: Set[Union[str, int]],
    k: int
) -> float:
    if k <= 0 or not ranked_items:
        return 0.0
    top_k = ranked_items[:k]
    hits = sum(1 for item in top_k if item in relevant_set)
    return round(hits / k, 4)


def calculate_mae(predicted: Sequence[float], ground_truth: Sequence[float]) -> float:
    if len(predicted) != len(ground_truth) or not predicted:
        raise ValueError("Inputs must have identical non-zero lengths.")
    total_abs_error = sum(abs(p - g) for p, g in zip(predicted, ground_truth))
    return round(total_abs_error / len(predicted), 4)


def calculate_spearman_correlation(ranks_a: Sequence[float], ranks_b: Sequence[float]) -> float:
    n = len(ranks_a)
    if n != len(ranks_b) or n < 2:
        return 0.0
    sum_d_squared = sum((a - b) ** 2 for a, b in zip(ranks_a, ranks_b))
    rho = 1.0 - (6.0 * sum_d_squared) / (n * (n**2 - 1))
    return round(rho, 4)


def run_self_tests():
    # 1. P/R/F1 check
    prf1 = calculate_precision_recall_f1(tp=8, fp=2, fn=2)
    assert prf1["precision"] == 0.8
    assert prf1["recall"] == 0.8
    assert prf1["f1"] == 0.8

    # 2. Precision@K check
    ranked_jobs = ["job_1", "job_2", "job_3", "job_4", "job_5"]
    relevant_jobs = {"job_1", "job_3", "job_5"}
    assert calculate_precision_at_k(ranked_jobs, relevant_jobs, k=3) == 0.6667

    # 3. MAE check
    assert calculate_mae([90.0, 80.0, 70.0], [85.0, 80.0, 75.0]) == 3.3333

    # 4. Spearman correlation check
    assert calculate_spearman_correlation([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 1.0

    print("[PASS] calculate_metrics.py: All metric formulas verified successfully.")


def main():
    parser = argparse.ArgumentParser(description="AIE314 Evaluation Metric Calculator")
    parser.add_argument("--test", action="store_true", help="Run metric sanity checks")
    args = parser.parse_args()

    if args.test:
        run_self_tests()
    else:
        print("Run with --test to verify calculations or import functions into your evaluation scripts.")


if __name__ == "__main__":
    main()
