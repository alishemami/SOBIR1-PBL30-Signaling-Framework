# Status note (2026-09-12)

The Phase 4 plan below (as of 2026-09-11) has since been carried out —
see `data/divergence_analysis.md` for the divergence scan and
`docs/mutant_design.md` for the resulting construct table. Keeping the
original plan here for the record.

## What we knew on 2026-09-11
- Interface phosphosites (PBL30 T253/T258/Y266; SOBIR1 T529) are conserved
  in PBL31/PBL32 → shared catalytic regulation, not the dual-role switch.
- Therefore the immunity-vs-abscission determinant had to lie in regions
  that differ between PBL30 and PBL31/PBL32.

## Phase 4 plan (completed)
1. Divergence mapping from the Clustal Omega MSA (sliding-window identity
   of PBL30 vs PBL31/PBL32) — done, `scripts/divergence_map.py`.
2. Overlay divergent windows on the AlphaFold model (pLDDT, surface
   exposure) — done, `figures/pbl30_ctail_highlight.png`.
3. Cross-check divergent regions against phosphosites of PBL30's C-tail —
   noted as an open question in `data/divergence_analysis.md`.
4. Produce a ranked candidate list and construct table — done,
   `docs/mutant_design.md`.

For what's actually still open, see the "Next steps" section of the
top-level README.
