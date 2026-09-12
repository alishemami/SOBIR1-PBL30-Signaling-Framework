# PyMOL script: visualize PBL30 with pLDDT coloring and C-tail highlight
# Usage: pymol -cq scripts/make_pbl30_figure.pml

# Load structure
load data/AF-P27450-F1-model_v6.pdb, pbl30

# Hide everything first
hide everything

# Show cartoon representation
show cartoon, pbl30

# Color by pLDDT (stored in B-factor column)
# Blue (high confidence) -> Orange (low confidence)
spectrum b, red_yellow_green_cyan_blue, minimum=50, maximum=90

# Highlight C-terminal tail (376-419) in bright red
color red, resi 376-419

# Make it stand out with thicker sticks
show sticks, resi 376-419
set stick_radius, 0.3, resi 376-419

# Set nice camera angle
set view, \
    0.8, -0.5,  0.3, \
   -0.2,  0.1,  0.9, \
   -0.5, -0.8, -0.0, \
    0.0,  0.0, -60.0, \
  210.0,  0.0,  0.0, \
  -20.0, 140.0, -20.0

# Set background to white
bg_color white

# Improve rendering quality
set antialias, 2
set ray_shadow, 0
set orthoscopic, on

# Ray trace for publication-quality image
ray 1200, 900

# Save image
png figures/pbl30_ctail_highlight.png, dpi=300

# Quit PyMOL
quit
