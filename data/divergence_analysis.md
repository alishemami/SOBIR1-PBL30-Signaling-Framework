# Divergence Analysis: Hunting the Dual-Role Specificity Switch

## Objective
Identify regions of PBL30 that differ from PBL31/PBL32, which may explain
why PBL30 has dual roles (immunity + abscission) while PBL31/PBL32 only
participate in immunity.

## Method
Sliding-window divergence score over the Clustal Omega alignment
(`data/pbl_family_clustal_aligned.aln`), computed with `scripts/divergence_map.py`
(window=15 residues, step=5, threshold=1.5 out of max 2.0).

**Update (2026-09-13):** the first version of this script counted a
paralog's alignment gap the same as a real amino-acid substitution. That
conflated two different things — PBL30 having a different residue at a
homologous position (substitution) vs. PBL30 simply having residues that
neither paralog reaches at all (an indel/extension) — so the script now
scores them separately:
- **Substitution divergence**: both paralogs have a real residue there,
  and it differs from PBL30's.
- **Indel divergence**: a paralog has a gap at that column (no residue to
  compare).
"Fully divergent" runs below (score=2, length ≥ 4) are reported per
category rather than combined.

## Results

### Divergent windows (mean substitution score ≥ 1.5)
- N-terminal region, residues 6-70 (several overlapping windows, mean
  1.53-1.73) — contains the lipid anchors (Gly2 myristoylation, Cys4
  palmitoylation) and is disordered in the AlphaFold model.
- Kinase C-lobe / start of the tail, residues 326-405 (several
  overlapping windows, mean 1.53-1.60).

### Fully divergent runs — true substitutions (sub=2, length ≥ 4)

| Run | Length | Location | Note |
|---|---|---|---|
| 20-25 | 6 aa | N-terminus | disordered |
| 39-42 | 4 aa | N-terminus | disordered |
| 44-48 | 5 aa | N-terminus | disordered |
| 56-62 | 7 aa | N-terminus | disordered |
| 73-78 | 6 aa | N-terminus | disordered |
| 209-213 | 5 aa | Kinase N-lobe | — |
| **245-248** | **4 aa** | **Near activation loop** | **adjacent to Thr253 phosphosite** |
| 295-298 | 4 aa | Kinase C-lobe | near Tyr266 phosphosite |
| 326-329 | 4 aa | Kinase C-lobe | — |
| 376-379 | 4 aa | C-terminal tail | — |
| 390-393 | 4 aa | C-terminal tail | — |

### Indel-only run — PBL30-specific extension (both paralogs gapped, length ≥ 4)

| Run | Length | Location | Note |
|---|---|---|---|
| 411-419 | 9 aa | C-terminal tail | see below — this is a real extension, not a substitution artifact |

Three runs from the first pass of this analysis (5-8, 27-31, 404-407) no
longer appear in either table: on closer inspection each one was a mix of
one real mismatch and one paralog gap, which the old scoring counted as
"fully divergent" but which isn't a clean substitution run. They're
dropped rather than force-fit into either category.

**Is the 411-419 extension a real finding or an alignment artifact?**
Checked directly: PBL30's sequence runs all the way to the last column of
the alignment with no trailing gaps, while PBL31 and PBL32 stop 16 and 9
columns earlier, respectively. PBL31 is actually the longest of the three
proteins overall (484 aa vs. PBL30's 419 and PBL32's 414), so its extra
length sits elsewhere in the sequence, not at the C-terminus — it
genuinely does not reach as far as PBL30 does here. So this is a real,
PBL30-specific 9-residue C-terminal extension, not an alignment gap
artifact, even though it isn't a "substitution" in the strict sense.

## Ranking the candidates for the dual-role switch

**1. C-terminal tail (376-419) — the leading candidate.** Two things are
going on in this region: two runs of true substitutions (376-379, 390-393,
8 residues total) and a 9-residue extension (411-419) that neither
paralog has at all. Combined with the region being disordered and sitting
outside the kinase domain (so it can evolve without touching catalytic
function), the working hypothesis is unchanged: the tail recruits
abscission-specific partners while the kinase domain handles immunity.
This predicts that a C-tail truncation (PBL30-ΔC) should lose abscission
function but keep immunity, and that grafting the tail onto PBL31 should
be enough to confer abscission behavior — ideally by binding into the
known abscission machinery (HAESA, IDA pathway), though that link is
still speculative.

**2. Region 245-248, right next to Thr253 — worth a look.** Four
consecutive true-substitution residues sitting immediately beside the key
interface phosphosite. This could plausibly shift phosphorylation dynamics
or SOBIR1 accessibility in a tissue-specific way, and predicts that a
phospho-mimetic (T253D/E) might behave differently in PBL30 than in PBL31.

**3. N-terminus (6-70) — a weaker, secondary candidate.** Several
substitution runs here, and it carries the membrane anchors, so a
plausible (if less direct) hypothesis is that it changes membrane
targeting or recruitment kinetics between PBL30 and its relatives.
N-terminal swap constructs could test this via localization and
complex-formation assays.

## Integration with previous findings

What we learned: interface phosphosites (T253/T258/Y266) are conserved
across the clade, so they're shared catalytic regulation, not the switch.
The switch — if it's encoded in sequence at all — has to be in one of the
regions where PBL30 actually differs from its relatives: the C-tail
(substitutions + a unique extension) or the N-terminus (substitutions).

New model: the conserved kinase domain and activation loop handle the
immunity function shared with PBL31/PBL32, while the divergent C-tail
(and possibly the N-terminus) is what's specific to PBL30.

## Next steps
1. ~~Map divergent regions onto AlphaFold structure~~ — done, see
   "Visual confirmation" below.
2. Check whether divergent regions overlap with known interaction partners
   (HAESA/IDA pathway) — still open, no direct evidence yet.
3. ~~Prioritize C-tail truncation mutants for experimental testing~~ — done,
   see `docs/mutant_design.md`.
4. Investigate phosphosites within the C-terminal tail itself (Ser/Thr
   clusters) — still open, not yet analyzed.

## Data sources
- Alignment: `data/pbl_family_clustal_aligned.aln` (Clustal Omega)
- Script: `scripts/divergence_map.py`
- Structure: AlphaFold AF-P27450-F1 (PBL30)

## Visual confirmation (reproducible figure)

Generated using `scripts/make_pbl30_figure.pml` on 2026-09-12:
- Structure: AlphaFold model AF-P27450-F1-model_v6.pdb (v6, 2025-08-01)
- Coloring: pLDDT confidence (blue=high, orange=low)
- Highlight: C-terminal residues 376-419 (red sticks)

**Observation:** the divergent C-tail (376-419) is a disordered,
solvent-exposed extended chain that projects away from the folded kinase
core — consistent with a flexible partner-recruitment module rather than
a structured binding patch.

See: `figures/pbl30_ctail_highlight.png`

Figure is fully reproducible from the script; no manual editing was
performed.
