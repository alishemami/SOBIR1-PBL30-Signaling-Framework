# Phosphorylation sites at/near the predicted SOBIR1-PBL30 interface

## Summary
- Documented phosphosites examined: SOBIR1 = 2, PBL30 = 6
- Direct interface contacts: 3
  - SOBIR1 Thr529
  - PBL30 Thr253
  - PBL30 Tyr266
- Interface-adjacent (within 1 residue of a contact residue): 1
  - PBL30 Thr258 (contacts at 259-260)
- Not at the interface: SOBIR1 Thr390; PBL30 Ser117, Tyr169, Ser222

## Evidence levels
| Protein | Site | Evidence | Interface status |
|---|---|---|---|
| SOBIR1 | Thr390 | PhosPhAt (plant phosphoproteomics) | not at interface |
| SOBIR1 | Thr529 | RLIMS-P, PMID 35529948 | direct contact |
| PBL30 | Ser117 | experimental MS (3 studies) | not at interface |
| PBL30 | Tyr169 | by similarity (inferred) | not at interface |
| PBL30 | Ser222 | by similarity (inferred) | not at interface |
| PBL30 | Thr253 | by similarity (inferred) | direct contact |
| PBL30 | Thr258 | by similarity (inferred) | interface-adjacent |
| PBL30 | Tyr266 | by similarity (inferred) | direct contact |

Note: PBL30 activation-loop sites are inferred "by similarity" in UniProt,
not directly measured on PBL30; experimental confirmation is therefore
especially valuable.

## Hypothesis
Phosphosites located at (or immediately next to) the predicted contact
surface may couple phosphorylation state to complex stability, and could
contribute to pathway specificity (immunity vs floral organ abscission).
This is a hypothesis for experimental testing, not a result.

## Validation plan (computational, in this repo)
1. Model robustness: run scripts/interface_contacts.py on rank 2-4 models;
   check whether Thr529 / Thr253 / Tyr266 recur as contacts.
2. Conservation: Clustal Omega alignment of PBL30/PBL31/PBL32; check whether
   the four sites are conserved within the clade.

## Validation plan (experimental, proposed for wet lab)
1. Phospho-null (Ala) and phospho-mimetic (Asp/Glu) versions of PBL30 at
   Thr253/Thr258/Tyr266.
2. Dual readout in complementation lines: immune output (ROS/ethylene after
   nlp20) vs floral organ abscission scoring.
3. A mutant that breaks only one of the two outputs would identify a
   specificity switch.

## Data sources
- SOBIR1 sites: iPTMnet entry Q9SKB2 (PhosPhAt, RLIMS-P)
- PBL30 sites: UniProt P27450 MOD_RES
- Interface: AlphaFold2-multimer rank-1 relaxed model, <4.5 A cutoff
  (see data/interface_residues_rank1.txt)
