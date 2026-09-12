# Next steps: hunting the true specificity switch (Phase 4 plan)

## What we know (2026-09-11)
- Interface phosphosites (PBL30 T253/T258/Y266; SOBIR1 T529) are conserved
  in PBL31/PBL32 -> shared catalytic regulation, NOT the dual-role switch.
- Therefore the immunity-vs-abscission determinant must lie in regions that
  DIFFER between PBL30 and PBL31/PBL32.

## Phase 4 work plan
1. Divergence mapping from the Clustal Omega MSA (sliding-window identity
   of PBL30 vs PBL31/PBL32) -> scripts/divergence_map.py
2. Overlay divergent windows on the AlphaFold model (pLDDT, surface
   exposure) to separate disordered tails from structured surfaces.
3. Cross-check divergent regions against iPTMnet/PhosPhAt phosphosites of
   PBL30 (C-tail Ser/Thr clusters).
4. Produce a ranked candidate list (truncation / swap constructs) for
   experimental testing of abscission vs immunity outputs.
