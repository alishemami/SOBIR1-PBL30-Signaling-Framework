# Divergence Analysis: Hunting the Dual-Role Specificity Switch

## Objective
Identify regions of PBL30 that differ from PBL31/PBL32, which may explain
why PBL30 has dual roles (immunity + abscission) while PBL31/PBL32 only
participate in immunity.

## Method
- Sliding-window divergence score using scripts/divergence_map.py
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

## Top 3 Candidates for the "Dual-Role Switch"

### 1. C-terminal tail (376-419) — TOP CANDIDATE
**Why:**
- Longest divergent region (44 residues)
- Disordered → likely mediates protein-protein interactions
- Outside kinase domain → can evolve independently of catalytic function
- Multiple fully divergent runs (376-379, 390-393, 404-407, 410-419)

**Hypothesis:** C-tail recruits abscission-specific partners while kinase
domain handles immunity signaling.

**Testable predictions:**
- PBL30-ΔC (truncation) should lose abscission function but retain immunity
- PBL31+Ctail chimera should gain abscission function
- C-tail should interact with abscission-zone proteins (HAESA, IDA pathway)

### 2. Region 245-248 (near Thr253) — HIGH INTEREST
**Why:**
- Immediately adjacent to Thr253 (key phosphosite in SOBIR1 interface)
- 4 consecutive fully divergent residues
- May affect phosphorylation dynamics or accessibility

**Hypothesis:** Divergence near Thr253 modulates how PBL30 is phosphorylated
or how it interacts with SOBIR1 in different tissues.

**Testable predictions:**
- Phospho-mimetic (T253D/E) may have different effects in PBL30 vs PBL31
- Region 245-248 may affect kinase conformation near activation loop

### 3. N-terminus (6-70) — SECONDARY CANDIDATE
**Why:**
- Very divergent (mean 1.6-1.87)
- Contains membrane anchors

**Hypothesis:** Different membrane targeting or recruitment kinetics between
PBL30 and PBL31/32.

**Testable predictions:**
- N-terminal swaps may alter subcellular localization
- May affect complex formation kinetics

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
1. Map divergent regions onto AlphaFold structure (pLDDT, surface exposure)
2. Check if divergent regions overlap with known interaction partners
3. Prioritize C-tail truncation mutants for experimental testing
4. Investigate phosphosites in C-terminal tail (Ser/Thr clusters)

## Data Sources
- Alignment: data/pbl_family_clustal_aligned.aln (Clustal Omega)
- Script: scripts/divergence_map.py
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
