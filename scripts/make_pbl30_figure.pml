# PyMOL script v2: one color = one message
# Usage: pymol -cq scripts/make_pbl30_figure.pml

load data/AF-P27450-F1-model_v6.pdb, pbl30
hide everything
show cartoon

# Message 1: model confidence (AlphaFold palette, NO red here)
color orange, pbl30        # pLDDT < 50  : disordered
color yellow, b > 50       # pLDDT 50-70 : low
color marine, b > 70       # pLDDT 70-90 : confident
color blue,   b > 90       # pLDDT > 90  : very confident

# Message 2: OUR region of interest (the ONLY red thing)
color red, resi 376-419
show sticks, resi 376-419
set stick_radius, 0.25

# Publication look
bg_color white
set ray_opaque_background, 1
set antialias, 2
set ray_shadow, 0

# Camera: frame the whole protein with some breathing room
orient
zoom pbl30, 15

ray 1600, 1200
png figures/pbl30_ctail_highlight.png, dpi=300
quit
