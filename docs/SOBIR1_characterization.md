# In silico characterization of Arabidopsis SOBIR1 (Q9SKB2)

Companion note to the README: sequence- and structure-based characterization
of the SOBIR1 receptor-like kinase, part of the SOBIR1-PBL30 signaling
framework project.

## 1. Protein sequence information
- Name: Leucine-rich repeat receptor-like serine/threonine/tyrosine-protein
  kinase SOBIR1
- Organism: Arabidopsis thaliana
- Gene: SOBIR1
- UniProt accession: Q9SKB2 (reviewed)
- Length: 641 amino acids

## 2. Protein architecture (UniProt + InterProScan)
| Feature | Position (UniProt) | Interpretation |
|---|---|---|
| Signal peptide | 1-31 | Sec/SPI; secretory pathway targeting |
| Extracellular LRR region | 32-284 (LRR repeats 112-228) | ligand/partner interaction |
| Transmembrane helix | 285-305 | single-pass plasma-membrane anchor |
| Cytoplasmic kinase domain | 347-641 | signaling output (ATP binding 353-361 and 377; catalytic Asp489) |

Architecture: extracellular LRR -> transmembrane helix -> cytoplasmic kinase
= a single-pass LRR receptor-like kinase (RLK), not an RLCK.

## 3. Signal peptide analysis (SignalP 6.0, run by author)
- Predicted Sec/SPI signal peptide; cleavage between residues 31 and 32
- Probability: 0.976790
- Consistent with UniProt annotation (SIGNAL 1-31; CHAIN 32-641).

## 4. AlphaFold structural analysis (AlphaFold DB entry AF-Q9SKB2-F1)
- Per-residue pLDDT: high/very-high confidence in the LRR solenoid and the
  kinase core; low confidence in terminal and linker segments (flexible or
  disordered).
- Average pLDDT quoted from the entry summary: ~81.06 (to be re-verified;
  see docs/curation_notes.md).
- CATH domains on the model: LRR solenoid 3.80.10.10; kinase N-lobe
  3.30.200.200; kinase C-lobe 1.10.510.10.

## 5. Conclusion
Sequence- and structure-based evidence supports classification of SOBIR1 as
a single-pass LRR receptor-like kinase with an extracellular sensor region
and a cytoplasmic catalytic module. Phosphorylation-dependent regulation and
the interaction with PBL30 are analyzed in the main project phases (README).
