# Curation notes (internal checklist before external submission)
- [ ] Verify primary citation for PBL30/PBL31 association with SOBIR1 and
      RLP23-mediated PTI (Huang 2024 vs an earlier report).
- [ ] Confirm journal name/volume for Wei et al. 2022 (PMC9073325).
- [ ] Check availability of PhosPhAt (Arabidopsis phosphosite DB); if live,
      add cross-reference table for SOBIR1/PBL30 sites.
- [ ] Verify source for the SOBIR1 transmembrane GxxxG dimerization motif.
- [ ] Re-check PBL30 clade naming (VII-7) against current literature.
- [ ] Re-verify average pLDDT (~81.06) quoted from AlphaFold DB entry AF-Q9SKB2-F1.
- [ ] `data/divergence_analysis.md` refers to a sliding-window divergence
      script that was never committed to `scripts/`. Either add it (with
      the exact window/step/threshold used) or keep the current honest
      "not committed" note — don't leave a dangling path reference.
- [x] Nomenclature resolved (2026-09-10): PBL30 = CST/CAST AWAY = At4g35600 = P27450 (Rao et al. 2018 RLCK-VII nomenclature; UniProt Araport xref). PBL31 = At1g76360 = F4I2C7. PBL32 = At2g17220 = Q9SII6 (PIX13).
- [x] Wrong accessions discarded: Q9ZU46 (= ZAR1) and Q9M9C5 (= At1g68400) were initially mistaken for PBL32/PBL31.
- [x] Trap recorded: At5g08720 = HCF145, NOT CST; never reuse this locus for PBL30.
