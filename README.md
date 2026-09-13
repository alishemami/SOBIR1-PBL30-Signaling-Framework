# Structural Basis of SOBIR1–PBL30 Signaling in Arabidopsis
### A computational framework to explore specificity between immunity and development

> **Status:** Work in progress. All protein–protein interaction models in this repository are computational predictions (putative) and require experimental validation.

## Background

Leucine-rich repeat receptor-like proteins (LRR-RLPs) lack cytoplasmic kinase domains and depend on the adaptor kinase **SOBIR1**, an atypical single-pass LRR receptor-like kinase (RLK; UniProt Q9SKB2), for stability and signaling. **PBL30** (CAST AWAY/CST; UniProt P27450) is a membrane-anchored receptor-like cytoplasmic kinase (RLCK) of the PBS1-like (BIK1/PBL) family (VII-7 clade together with PBL31 and PBL32), tethered to the inner plasma-membrane leaflet by N-myristoylation (Gly2) and S-palmitoylation (Cys4).

Both kinases contribute to pattern-triggered immunity downstream of LRR-RLPs (e.g., RLP23, RLP30) **and** to floral organ abscission, raising the central question of this project: how can the same signaling module steer two different outcomes?

## Questions

1. What are the domain architectures of SOBIR1 and PBL30, and how do they differ (RLK vs RLCK)?
2. What is the putative structural interface between the cytoplasmic kinase module of SOBIR1 and PBL30?
3. Which documented phosphorylation sites are structurally positioned in regulatory regions (activation segment, interface), and are they conserved within the PBL30/31/32 clade?
4. If those sites are conserved (i.e., not the specificity switch), where does PBL30 actually diverge from its clade relatives, and could that region explain the dual role?
5. Which residues are candidate targets for future site-directed mutagenesis to dissect immunity vs abscission signaling? (hypotheses only)

## Completed work

### Phase 1 — Protein architecture (UniProt / InterPro / AlphaFold DB)
- **SOBIR1 (Q9SKB2, 641 aa):** signal peptide 1–31; extracellular LRR region 32–284 (LRRs at 112–228); transmembrane helix 285–305; cytoplasmic kinase domain 347–641 (ATP binding 353–361, 377; catalytic Asp489).
- **PBL30 (P27450, 419 aa):** disordered N-terminus 8–48 carrying lipid anchors; kinase domain 86–368 (ATP binding 92–100, Lys124; catalytic Asp218); disordered C-terminus 378–419.
- CATH domain assignment on AlphaFold models: LRR solenoid (3.80.10.10); kinase N-lobe (3.30.200.200); kinase C-lobe (1.10.510.10).

### Phase 2 — Putative complex prediction (ColabFold / AlphaFold2-Multimer v3)
- Input: SOBIR1 cytoplasmic region (306–641) + full-length PBL30 (1–419).
- Settings: `msa_mode=mmseqs2_uniref_env`, `pair_mode=unpaired_paired`, 5 models, top-5 relaxed.
- Result (rank-1 relaxed model): 56 putative inter-chain residue contacts (<4.5 Å), enriched in the activation-segment regions of both kinases (SOBIR1 565–577; PBL30 251–273) and including SOBIR1 P-loop residue 357.
- Confidence assessment: intra-chain pLDDT high (>80) in both kinase cores; inter-chain PAE moderate; rank-5 model discarded (high inter-chain PAE). The interface is therefore reported as a hypothesis-generating model, not as an established structure.
- **Robustness check:** the same contact-extraction script was rerun on all five relaxed models (`data/model_robustness.md`, `data/robustness_test.txt`). The core interface — especially PBL30 Thr253 — recurs in 4–5 of 5 models, so it isn't an artifact of a single prediction.

### Phase 3 — Phosphorylation and conservation mapping
- Curated documented phosphosites: UniProt MOD_RES (PBL30: Ser117 experimental; Tyr169, Ser222, Thr253, Thr258, Tyr266 by similarity) and literature (SOBIR1 phospho-regulation; reciprocal phosphorylation with SOAK1, Chen et al. 2025). Three sites sit directly at the modeled interface: PBL30 Thr253/Tyr266 and SOBIR1 Thr529, with Thr258 immediately adjacent (`data/phosphosites.md`).
- Aligned PBL30 against PBL31 and PBL32 with two independent methods — Biopython pairwise alignment and a Clustal Omega MSA (EBI, job ID `clustalo-I20260911-122535-0316-68070521`) — to test whether these interface phosphosites could be the immunity-vs-abscission switch (`data/conservation_analysis.md`).
- **Result: all three sites are 100% conserved across PBL30/31/32.** Since PBL31 and PBL32 only support immunity (not abscission), a fully conserved site can't be what makes PBL30 special — these residues more likely handle catalytic regulation shared across the whole clade. The switch has to be somewhere else.

### Phase 4 — Divergence mapping and hypothesis generation
- Ran a sliding-window divergence scan of PBL30 against PBL31/PBL32 on the same alignment to find where PBL30 actually differs from its relatives (`data/divergence_analysis.md`).
- The clearest candidate is the disordered **C-terminal tail (376–419)**: it's the longest fully-divergent stretch, it sits well outside the modeled SOBIR1 interface (last contact residue = 353), and a PyMOL rendering (`scripts/make_pbl30_figure.pml`, `figures/pbl30_ctail_highlight.png`) shows it as a solvent-exposed extended chain rather than a folded binding patch — consistent with a flexible partner-recruitment module.
- Working model: the conserved activation loop/interface handles immunity signaling common to the clade, while the divergent C-tail is what lets PBL30 additionally recruit abscission-specific partners.
- Translated this into a concrete mutant panel — truncations, a tail-swap chimera, and phospho-null/mimetic controls — designed so that each construct isolates one part of the model (`docs/mutant_design.md`). The decisive test is grafting the PBL30 tail onto PBL31: if that's sufficient to confer abscission behavior, the tail-sequence hypothesis holds.

## Next steps
- Internal QC before this goes into any external submission: a few citations and details still need re-checking (see `docs/curation_notes.md`) — e.g. the primary source for PBL30/PBL31–SOBIR1 association, current VII-7 clade nomenclature, and the quoted AlphaFold DB average pLDDT for SOBIR1.
- Everything above is computational. The actual test of the model is wet-lab: expressing the Phase 4 constructs in a `pbl30 pbl31 pbl2` background and scoring immunity (ROS/ethylene, bacterial growth) and abscission (floral organ shedding) separately, as laid out in `docs/mutant_design.md`.

## Limitations
- AlphaFold-Multimer confidence for the transient kinase–kinase interface is moderate; atomic details must not be over-interpreted.
- No membrane environment is modeled; lipid anchors are not represented.
- Plant phosphoproteomics coverage is sparse; several PBL30 sites are annotated by similarity only, not direct measurement.
- Conservation of the interface sites argues against them being the specificity switch, but it doesn't prove the C-tail is — that's a hypothesis waiting on the constructs above.

## Reproducibility
- Complex prediction: ColabFold notebook (AlphaFold2.ipynb), parameters as above; input sequences in `data/sequences.fasta`.
- Interface extraction: `scripts/interface_contacts.py` (Biopython NeighborSearch, 4.5 Å cutoff); output in `data/interface_residues_rank1.txt` (rank-1) and `data/robustness_test.txt` (all 5 models).
- Conservation: `scripts/conservation_check.py` plus the Clustal Omega alignment in `data/pbl_family_clustal_aligned.aln`.
- Figure: `scripts/make_pbl30_figure.pml`, run against AlphaFold model AF-P27450-F1-model_v6.pdb.

## References
1. Burr CA, et al. (2011) Plant Physiol 156:1837–1850.
2. Liebrand TWH, et al. (2013) PNAS 110:11011–11016.
3. Zhang W, et al. (2013) Plant Cell 25:4227–4241.
4. Gust AA, Felix G (2014) Curr Opin Plant Biol 21:104–111.
5. Albert I, et al. (2015) Nat Plants 1:15140.
6. Wei X, et al. (2022) Structural analysis of receptor-like kinase SOBIR1 (PMC9073325).
7. Huang WRH, et al. (2024) Nat Commun, receptor-like cytoplasmic kinases in SOBIR1/BAK1-mediated immunity.
8. Chen Y, et al. (2025) Sci Adv 11:eadt2315.

## Author
Ali EmamiPour — [@alishemami](https://github.com/alishemami)
