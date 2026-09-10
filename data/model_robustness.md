# Model robustness test: interface recurrence across 5 AlphaFold2-multimer models

## Method
scripts/interface_contacts.py (Biopython NeighborSearch, 4.5 A cutoff) was run
on all five relaxed rank models from the ColabFold run (September 2026).
Raw output: data/robustness_test.txt

## Recurrence of phosphosite-containing interface residues

| Site (real numbering) | PDB num | r1 | r2 | r3 | r4 | r5 | direct contacts |
|---|---|---|---|---|---|---|---|
| PBL30 Thr253 | 253 | Y | Y | Y | Y | Y | 5/5 |
| PBL30 Tyr266 | 266 | Y | Y | Y | Y | adj | 4/5 |
| SOBIR1 Thr529 | 224 | Y | Y | Y | Y | adj | 4/5 |
| PBL30 Thr258 | 258 | adj | Y | Y | Y | adj | 3/5 |

Y = direct contact (<4.5 A); adj = not a direct contact but an immediate
neighbour residue is in contact (same interface region).

## Interpretation
- The PBL30 activation-loop region (251-273) contacts SOBIR1 in all five
  models: the interface core is reproducible, not a single-model artifact.
- PBL30 Thr253 is the most robust contact (5/5) and is the top candidate for
  experimental mutagenesis.
- rank_005 shows the fewest contacts (38) and weakest inter-chain signal,
  consistent with its high inter-chain PAE; excluding it from the primary
  analysis was justified.
- Sporadic contacts involving disordered N-terminal tails (e.g. residues
  1, 77-99, 127-164 in some models) are treated as noise, not signal.

## Conclusion
The predicted phosphosite-at-interface hypothesis is internally consistent
across independent models. Experimental validation remains required.
