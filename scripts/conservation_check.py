"""Check conservation of key residues across PBL30/31/32 family.

Reads pbl_family.fasta, performs pairwise alignments, and checks whether
key phosphosite residues (Thr253, Thr258, Tyr266 in PBL30) are conserved
in PBL31 and PBL32.
"""
from Bio import pairwise2
from Bio.Seq import Seq
from Bio import SeqIO

# Key residues in PBL30 (1-based indexing)
KEY_RESIDUES = {
    253: "Thr253",
    258: "Thr258", 
    266: "Tyr266"
}

def read_fasta(filepath):
    """Read all sequences from a multi-FASTA file."""
    return {record.id: str(record.seq) for record in SeqIO.parse(filepath, "fasta")}

def align_and_check(seq1, seq2, key_positions):
    """Align two sequences and check conservation at key positions."""
    alignments = pairwise2.align.globalxx(seq1, seq2, score_only=False)
    if not alignments:
        return None
    
    # Take the best alignment
    best = alignments[0]
    aligned1, aligned2, score, begin, end = best
    
    results = {}
    pos_in_aligned = 0
    pos_in_seq1 = 0
    
    for i, (aa1, aa2) in enumerate(zip(aligned1, aligned2)):
        if aa1 != '-':
            pos_in_seq1 += 1
            if pos_in_seq1 in key_positions:
                results[pos_in_seq1] = {
                    'pbl30_residue': aa1,
                    'homolog_residue': aa2,
                    'conserved': aa1 == aa2,
                    'alignment_position': i
                }
    
    return results

def main():
    # Read sequences
    seqs = read_fasta("data/pbl_family.fasta")
    
    # Find PBL30 (CST)
    pbl30_id = [k for k in seqs.keys() if "CST" in k][0]
    pbl30_seq = seqs[pbl30_id]
    
    print("=" * 70)
    print("Conservation Analysis: PBL30 Key Residues")
    print("=" * 70)
    print(f"\nReference: {pbl30_id} (PBL30/CST), length {len(pbl30_seq)} aa\n")
    
    # Check each homolog
    for seq_id, seq in seqs.items():
        if seq_id == pbl30_id:
            continue
        
        print(f"\nAlignment: PBL30 vs {seq_id}")
        print("-" * 70)
        
        results = align_and_check(pbl30_seq, seq, KEY_RESIDUES)
        if results:
            for pos, data in sorted(results.items()):
                status = "✓ CONSERVED" if data['conserved'] else "✗ DIFFERENT"
                print(f"Position {pos:3d} ({KEY_RESIDUES[pos]}): "
                      f"PBL30={data['pbl30_residue']} vs "
                      f"Homolog={data['homolog_residue']} {status}")
        else:
            print("  No alignment found")

if __name__ == "__main__":
    main()
