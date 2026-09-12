# Mutant Design: Testing the Two-Pathway Model of PBL30 Dual-Role Signaling

## Model under test
- Immunity arm: PBL30 activation loop (T253/T258/Y266) contacts SOBIR1
  kinase domain; conserved across clade -> shared catalytic regulation.
- Abscission arm: PBL30 C-tail SEQUENCE (376-419) acts as a divergent
  partner-recruitment code; physically separated from the SOBIR1 interface
  (last contact = 353; tail starts = 376).
- All clade members have disordered C-tails; specificity = tail sequence.

## Genetic background
All constructs expressed in pbl30/pbl31/pbl2 triple mutant (complementation)
to remove functional redundancy (Huang et al. 2024).

## Dual readouts (always both)
- Immunity: ROS burst + MAPK activation + ethylene after nlp20/flg22;
  bacterial growth (Pst DC3000).
- Abscission: floral organ shedding score / break-force in AZ.
- Binding: Co-IP with SOBIR1 (is interface intact?).
- Localization: confocal of GFP-tagged construct (is it at the membrane?).

## Construct table

| # | Construct | Change | Question | Immunity | Abscission | SOBIR1 binding | Priority |
|---|---|---|---|---|---|---|---|
| 1 | WT PBL30 | none (positive control) | Does transgene rescue? | + | + | + | control |
| 2 | empty vector | none (negative control) | Baseline of triple mutant | - | - | - | control |
| 3 | Kinase-dead | catalytic Lys->Glu | Is catalysis needed for both arms? | - | - | + | control |
| 4 | Anchor-dead | G2A + C4A | Is membrane targeting needed? | - | - | reduced | control |
| 5 | PBL30-dC | delete 376-419 | Is tail needed for abscission only? | + | - | + | TOP |
| 6 | PBL30body+PBL31tail | tail swap | Is tail sequence the code? (loss) | + | - | + | TOP |
| 7 | PBL31body+PBL30tail | tail swap | Is tail sequence sufficient? (gain) | + | + (GAIN) | + | TOP |
| 8 | T253A | phospho-null | Is interface phospho needed for immunity? | - | + | + | high |
| 9 | T253D/E | phospho-mimic | Does phospho-mimic alter immunity? | altered | + | + | high |

## Key logic
- Constructs 5-7 test the tail-sequence code. Construct 7 is decisive:
  if grafting the PBL30 tail onto PBL31 CONFERS abscission, the tail
  sequence alone is sufficient = the dual-role code is cracked.
- Construct 5 vs 3 separates "tail function" from "catalysis": dC keeps
  catalysis (immunity intact) but loses abscission.
- Constructs 8-9 test the immunity arm independently of the tail.
- Binding column confirms dC and swaps still reach SOBIR1 (so any
  abscission loss is NOT due to lost SOBIR1 contact).

## Interpretation matrix (if model correct)
- dC: immunity OK + abscission lost + binding OK  => tail = abscission module
- swap7: abscission GAINED on PBL31 body         => tail sequence sufficient
- T253A: immunity lost + abscission OK           => interface phospho = immunity arm
- Together: two physically and genetically separable arms = dual-role solved

## Wet-lab feasibility notes
- dC and swaps are simple cloning (restriction/Gibson at tail boundary ~375).
- T253A/D are single-codon changes (site-directed mutagenesis).
- All in same binary vector + same promoter (native PBL30 promoter) to
  keep expression comparable.
