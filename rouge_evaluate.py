import sys
from glob import glob
import os
import math

from rouge import Rouge

def get_evaluator():
    """Get the Rouge evaluator mimicing 1.55"""
    return Rouge(
        metrics=["rouge-n", "rouge-l"],
        max_n=2,
        limit_length=False,
        apply_avg=True,
        alpha=0.5,  # Default F1_score
        stemming=True,
    )


def print_scores(scores):
    """
    Pretty print rouge scores to stdout

    :param scores: the scores output by `Rouge().get_scores`

    :returns: None
    """
    rouge_types = ["rouge-1", "rouge-2", "rouge-l"]
    for rouge in rouge_types:
        precision = scores[rouge]["p"] * 100
        recall = scores[rouge]["r"] * 100
        f1 = scores[rouge]["f"] * 100
        print(rouge.upper() + ":")
        print("\t Precision: %.2f" % precision)
        print("\t Recall: %.2f" % recall)
        print("\t F1: %.2f" % f1)


def rouge_evaluate(ref_folder, hyp_folder, limit=math.inf):
    """Return rouge scores for the given `ref_folder` and `hyp_folder`"""
    ref_paths = glob(os.path.join(ref_folder, "*reference.txt"))
    references = []
    hypothesis = []
    for ref_path in ref_paths[:limit]:
        hyp_path = ref_path.replace(ref_folder, hyp_folder)
        hyp_path = hyp_path.replace("reference.txt", "decoded.txt")
        with open(ref_path) as ref_file, open(hyp_path) as hyp_file:
            ref = ref_file.read()
            hyp = hyp_file.read()
            if ref and hyp:
                references.append(ref)
                hypothesis.append(hyp)

    rouge = get_evaluator()
    return rouge.get_scores(hypothesis, references)


def main():
    """Run evaluation given <ref_folder> <hyp_folder> (<limit>)"""
    ref_folder = sys.argv[1]
    hyp_folder = sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) == 4 else math.inf
    scores = rouge_evaluate(ref_folder, hyp_folder, limit)
    print_scores(scores)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Expected exactly 2-3 args. <ref_folder> <hyp_folder> (<limit>)")
        exit(1)

    main()
