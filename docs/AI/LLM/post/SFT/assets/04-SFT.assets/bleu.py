"""
@author : Hyunwoong
@when : 2019-12-22
@homepage : https://github.com/gusdnd852
"""

import math
from collections import Counter

import numpy as np


def bleu_stats(hypothesis, reference):
    """Compute statistics for BLEU."""
    stats = []
    stats.append(len(hypothesis))
    stats.append(len(reference))
    for n in range(1, 5):
        s_ngrams = Counter([tuple(hypothesis[i : i + n]) for i in range(len(hypothesis) + 1 - n)])
        r_ngrams = Counter([tuple(reference[i : i + n]) for i in range(len(reference) + 1 - n)])

        stats.append(max(sum((s_ngrams & r_ngrams).values()), 0))
        stats.append(max(len(hypothesis) + 1 - n, 0))
    return stats


def bleu(stats):
    """Compute BLEU given n-gram statistics."""
    if any(x == 0 for x in stats):
        return 0
    (c, r) = stats[:2]
    log_bleu_prec = sum(math.log(float(x) / y) for x, y in zip(stats[2::2], stats[3::2])) / 4.0
    return math.exp(min(0, 1 - float(r) / c) + log_bleu_prec)


def get_bleu(hypotheses, reference):
    """Get validation BLEU score for dev set."""
    stats = np.zeros(10)
    for hyp, ref in zip(hypotheses, reference):
        stats += np.array(bleu_stats(hyp, ref))
    return 100 * bleu(stats)


def idx_to_word(x, vocab):
    # 这里假设 vocab 是 dict: word -> idx
    # 先构造 idx -> word 的反转字典
    idx2word = {idx: word for word, idx in vocab.items()}

    words = []
    for i in x:
        # i 可能是 tensor，需要转成 int
        idx = i.item() if hasattr(i, "item") else i
        word = idx2word.get(idx, "<unk>")
        if "<" not in word:
            words.append(word)
    return " ".join(words)
