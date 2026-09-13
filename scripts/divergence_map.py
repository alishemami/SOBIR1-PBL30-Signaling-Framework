"""Map sequence-divergent regions of PBL30 relative to PBL31/PBL32.

Reads the CLUSTAL O alignment (data/pbl_family_clustal_aligned.aln) and,
for every PBL30 residue, checks how the two paralogs differ at that
aligned column. Substitution divergence (both paralogs carry a real but
different residue) is now scored separately from indel divergence (a
paralog has a gap there, i.e. PBL30 has an insertion/extension relative
to that paralog) -- the two were conflated in the first version of this
script, which made a purely length-driven stretch at the very C-terminus
look like a run of amino-acid substitutions.

Usage: python scripts/divergence_map.py [window] [step] [threshold]
"""
import sys
from collections import defaultdict

ALN = "data/pbl_family_clustal_aligned.aln"


def parse_clustal(path):
    seqs = defaultdict(str)
    with open(path) as fh:
        for line in fh:
            parts = line.split()
            if parts and (parts[0].startswith("sp|") or parts[0].startswith("tr|")):
                seqs[parts[0]] += parts[1]
    return dict(seqs)


def main():
    window = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    step = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    thr = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5

    seqs = parse_clustal(ALN)
    ref_id = [k for k in seqs if "P27450" in k][0]
    other_ids = [k for k in seqs if k != ref_id]
    ref = seqs[ref_id]

    cols = []
    pos = 0
    for i, aa in enumerate(ref):
        if aa != "-":
            pos += 1
            cols.append((pos, aa, [seqs[k][i] for k in other_ids]))

    scored = []
    for p, aa, o in cols:
        sub = sum(1 for v in o if v != "-" and v != aa)
        gap = sum(1 for v in o if v == "-")
        scored.append((p, aa, sub, gap))

    print(f"PBL30 divergence vs PBL31/PBL32 (window={window}, thr={thr})")
    print(f"{'window':>12} | mean substitution divergence (0-2)")
    print("-" * 42)
    for i in range(0, len(scored) - window + 1, step):
        win = scored[i:i + window]
        mean = sum(sub for _, _, sub, _ in win) / window
        if mean >= thr:
            print(f"{win[0][0]:>5}-{win[-1][0]:<5} | {mean:.2f}")

    print("\nPer-residue fully divergent runs -- TRUE SUBSTITUTIONS ONLY "
          "(sub=2, length>=4):")
    runs, cur = [], []
    for p, aa, sub, gap in scored:
        if sub == 2:
            cur.append(p)
        else:
            if len(cur) >= 4:
                runs.append((cur[0], cur[-1]))
            cur = []
    if len(cur) >= 4:
        runs.append((cur[0], cur[-1]))
    for a, b in runs:
        print(f"  {a}-{b}")

    print("\nIndel-only runs (both paralogs gapped here -- PBL30-specific "
          "extension, not a substitution; length>=4):")
    runs, cur = [], []
    for p, aa, sub, gap in scored:
        if gap == 2:
            cur.append(p)
        else:
            if len(cur) >= 4:
                runs.append((cur[0], cur[-1]))
            cur = []
    if len(cur) >= 4:
        runs.append((cur[0], cur[-1]))
    for a, b in runs:
        print(f"  {a}-{b}")


if __name__ == "__main__":
    main()
