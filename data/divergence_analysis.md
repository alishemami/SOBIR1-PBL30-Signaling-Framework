# Divergence Analysis: Hunting the Dual-Role Specificity Switch

## Objective
Identify regions of PBL30 that differ from PBL31/PBL32, which may explain
why PBL30 has dual roles (immunity + abscission) while PBL31/PBL32 only
participate in immunity.

## Method
- Sliding-window divergence score over the Clustal Omega alignment
  (`data/pbl_family_clustal_aligned.aln`). **Note:** this was run ad hoc
  and the script was not committed to this repo — see the open item in
  `docs/curation_notes.md`.
- Parameters: window=15 residues, step=5, threshold=1.5 (out of max 2.0)
- Fully divergent runs: consecutive residues where PBL30 differs from BOTH
  PBL31 and PBL32 (score=2), minimum length=4

## Results

### Divergent Windows (mean score ≥ 1.5)

**N-terminal region (residues 6-70):**
Multiple overlapping windows with mean divergence 1.60-1.87
- Contains lipid anchors: Gly2 (myristoylation), Cys4 (palmitoylation)
- Highly disordered in AlphaFold model (low pLDDT)
- Likely role: membrane targeting and recruitment

**C-terminal region (residues 326-415):**
Multiple overlapping windows with mean divergence 1.53-1.80
- 326-340: C-lobe of kinase domain (ends at 368)
- 366-419: disordered C-terminal tail
- Likely role: partner-specific protein interactions

### Fully Divergent Runs (score=2, length≥4)

| Run | Residues | Location | Potential function |
|---|---|---|---|
| 5-8 | 4 aa | N-terminus | Lipid anchor region |
| 20-25 | 6 aa | N-terminus | Disordered region |
| 27-31 | 5 aa | N-terminus | Disordered region |
| 39-42 | 4 aa | N-terminus | Disordered region |
| 44-48 | 5 aa | N-terminus | Disordered region |
| 56-62 | 7 aa | N-terminus | Disordered region |
| 73-78 | 6 aa | N-terminus | Disordered region |
| 209-213 | 5 aa | Kinase N-lobe | Unknown |
| **245-248** | **4 aa** | **Near activation loop** | **Near Thr253 phosphosite!** |
| 295-298 | 4 aa | Kinase C-lobe | Near Tyr266 phosphosite |
| 326-329 | 4 aa | Kinase C-lobe | Structured region |
| 376-379 | 4 aa | C-terminal tail | Disordered, partner binding? |
| 390-393 | 4 aa | C-terminal tail | Disordered, partner binding? |
| 404-407 | 4 aa | C-terminal tail | Disordered, partner binding? |
| 410-419 | 10 aa | C-terminal tail | Long divergent run! |

## Ranking the candidates for the dual-role switch

**1. C-terminal tail (376-419) — the leading candidate.** It's the longest
divergent stretch (44 residues), it's disordered (which usually means
protein-protein interaction surface rather than a folded domain), and it
sits outside the kinase domain, so it can evolve without touching catalytic
function. Working hypothesis: the tail recruits abscission-specific
partners while the kinase domain itself handles immunity. This predicts
that a C-tail truncation (PBL30-ΔC) should lose abscission function but
keep immunity, and that grafting the tail onto PBL31 should be enough to
confer abscission behavior — ideally by binding into the known abscission
machinery (HAESA, IDA pathway), though that link is still speculative.

**2. Region 245-248, right next to Thr253 — worth a look.** Four
consecutive fully divergent residues sitting immediately beside the key
interface phosphosite. This could plausibly shift phosphorylation dynamics
or SOBIR1 accessibility in a tissue-specific way, and predicts that a
phospho-mimetic (T253D/E) might behave differently in PBL30 than in PBL31.

**3. N-terminus (6-70) — a weaker, secondary candidate.** Also strongly
divergent and carries the membrane anchors, so a plausible (if less direct)
hypothesis is that it changes membrane targeting or recruitment kinetics
between PBL30 and its relatives. N-terminal swap constructs could test
this via localization and complex-formation assays.

## Integration with Previous Findings

**What we learned:**
- Interface phosphosites (T253/T258/Y266) are conserved → shared catalytic
  regulation, NOT the switch
- Therefore the switch must be in divergent regions → C-tail and N-term

**New model:**
- Kinase domain + activation loop: shared immunity function (conserved)
- C-terminal tail: recruits abscission-specific partners (divergent)
- N-terminus: may fine-tune membrane recruitment (divergent)

## Next Steps
1. ~~Map divergent regions onto AlphaFold structure~~ — done, see
   "Visual Confirmation" below.
2. Check whether divergent regions overlap with known interaction partners
   (HAESA/IDA pathway) — still open, no direct evidence yet.
3. ~~Prioritize C-tail truncation mutants for experimental testing~~ — done,
   see `docs/mutant_design.md`.
4. Investigate phosphosites within the C-terminal tail itself (Ser/Thr
   clusters) — still open, not yet analyzed.

## Data Sources
- Alignment: data/pbl_family_clustal_aligned.aln (Clustal Omega)
- Script: not yet committed (see Method note above)
- Structure: AlphaFold AF-P27450-F1 (PBL30)

## Visual Confirmation (Reproducible Figure)

Generated using scripts/make_pbl30_figure.pml on 2026-09-12:
- Structure: AlphaFold model AF-P27450-F1-model_v6.pdb (v6, 2025-08-01)
- Coloring: pLDDT confidence (blue=high, orange=low)
- Highlight: C-terminal residues 376-419 (red sticks)

**Observation:** The divergent C-tail (376-419) is a disordered, solvent-exposed
extended chain that projects away from the folded kinase core — consistent
with a flexible partner-recruitment module rather than a structured binding patch.

See: figures/pbl30_ctail_highlight.png

**Methodological note:** Figure is fully reproducible from the script; no
manual editing was performed. This ensures scientific rigor and allows
others to regenerate the exact same visualization.
