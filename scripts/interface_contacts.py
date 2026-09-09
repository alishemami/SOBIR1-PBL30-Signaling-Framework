"""Extract putative inter-chain contacts from an AlphaFold-Multimer PDB.

Usage:
    python interface_contacts.py path/to/model.pdb [cutoff]

Prints residue IDs of chain A and chain B with any heavy-atom distance
below cutoff (default 4.5 A). Requires Biopython.
"""
import sys
from Bio.PDB import PDBParser
from Bio.PDB.NeighborSearch import NeighborSearch


def main(pdb_path, cutoff=4.5):
    structure = PDBParser(QUIET=True).get_structure("model", pdb_path)[0]
    atoms = [a for a in structure.get_atoms() if a.element != "H"]
    search = NeighborSearch(atoms)

    pairs = set()
    for atom in atoms:
        if atom.get_parent().get_parent().id != "A":
            continue
        for other in search.search(atom.coord, cutoff):
            if other.get_parent().get_parent().id == "B":
                pairs.add((atom.get_parent().id, other.get_parent().id))

    print("Chain A interface residues:", sorted({i for i, _ in pairs}))
    print("Chain B interface residues:", sorted({j for _, j in pairs}))
    print("Total contact pairs:", len(pairs))


if __name__ == "__main__":
    path = sys.argv[1]
    cut = float(sys.argv[2]) if len(sys.argv) > 2 else 4.5
    main(path, cut)
