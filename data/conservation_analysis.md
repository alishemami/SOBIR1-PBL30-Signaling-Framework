# Conservation Analysis of PBL30 Phosphosites Across PBL Family

## Objective
Test the hypothesis that phosphosites at the predicted SOBIR1-PBL30 interface
(Thr253, Thr258, Tyr266) are responsible for pathway specificity (immunity vs.
floral organ abscission) by checking their conservation in close homologs
PBL31 and PBL32.

## Methods

### Method 1: Pairwise Alignment (Biopython)
- Pairwise global alignment using Biopython `pairwise2.globalxx`
- PBL30 (CST, At4g35600, P27450) aligned separately against:
  - PBL31 (At1g76360, F4I2C7, 484 aa)
  - PBL32 (At2g17220, Q9SII6, 414 aa)
- Key residues mapped from PBL30 numbering to aligned positions
- Script: scripts/conservation_check.py

### Method 2: Multiple Sequence Alignment (Clustal Omega)
- All three sequences aligned simultaneously using Clustal Omega (EBI server)
- Job ID: clustalo-I20260911-122535-0316-68070521
- Alignment file: data/pbl_family_clustal_aligned.aln
- Key positions manually verified from MSA columns

## Results

### Pairwise Alignment (Biopython)

#### PBL30 vs PBL31
| PBL30 Residue | Position | PBL30 | PBL31 | Status |
|---|---|---|---|---|
| Thr253 | 253 | T | T | ✓ CONSERVED |
| Thr258 | 258 | T | T | ✓ CONSERVED |
| Tyr266 | 266 | Y | Y | ✓ CONSERVED |

#### PBL30 vs PBL32
| PBL30 Residue | Position | PBL30 | PBL32 | Status |
|---|---|---|---|---|
| Thr253 | 253 | T | T | ✓ CONSERVED |
| Thr258 | 258 | T | T | ✓ CONSERVED |
| Tyr266 | 266 | Y | Y | ✓ CONSERVED |

### Multiple Sequence Alignment (Clustal Omega)

| PBL30 Residue | Position | PBL30 | PBL31 | PBL32 | Status |
|---|---|---|---|---|---|
| Thr253 | 253 | T | T | T | ✓ CONSERVED |
| Thr258 | 258 | T | T | T | ✓ CONSERVED |
| Tyr266 | 266 | Y | Y | Y | ✓ CONSERVED |

**All 3 key residues are 100% conserved across all three family members,
confirmed by two independent methods.**

## Interpretation

The starting hypothesis was that Thr253/Thr258/Tyr266 might be the
dual-role switch: if they controlled abscission specifically, they should
differ between PBL30 (immunity + abscission; Burr 2011, Huang 2024) and its
immunity-only relatives PBL31/PBL32 (Rao 2018). They don't — all three
sites are identical across all three kinases, so this hypothesis doesn't
hold up.

That's still a useful result. Full conservation across a clade where only
one member has the extra (abscission) role points to a shared, more basic
function rather than a specificity switch — most likely catalytic
regulation and activation-loop stabilization that all three kinases need
to be active at all, rather than something PBL30-specific.

Pairwise Biopython alignment and the independent Clustal Omega MSA agree
on all three positions, so this isn't an artifact of one alignment method.

## Implications for the "Dual-Role" Question
The switch that directs signaling toward immunity vs. abscission must lie
**elsewhere**. Candidate regions to investigate next:
- Divergent segments between PBL30 and PBL31/PBL32 (outside activation loop)
- The disordered C-terminal tail (378-419) unique to PBL30
- Juxtamembrane regions with clade-specific residues
- Partner-recognition surfaces that differ between the three kinases

## Limitations
- Conservation does not prove function
- Post-translational modification patterns may differ even when sequence
  is conserved (different kinases may phosphorylate the same site in
  different contexts)
- Structural context not fully captured by sequence alignment alone

## Data Sources
- PBL30: UniProt P27450 (CST / CAST AWAY)
- PBL31: UniProt F4I2C7 (At1g76360)
- PBL32: UniProt Q9SII6 (PIX13 / At2g17220)
- Nomenclature: Rao et al. 2018 (RLCK-VII classification)
- Clustal Omega: EMBL-EBI (https://www.ebi.ac.uk/Tools/msa/clustalo/)

## Conclusion
The three interface phosphosites are strongly conserved and unlikely to be
the specificity switch. Future work should focus on clade-divergent regions
to identify the true determinants of immunity vs. abscission signaling.
