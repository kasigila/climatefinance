#!/bin/bash
# Copies selected Highlight photos to assets/img/highlights/
# Run from project root: ./scripts/copy-highlights-photos.sh
# Or with custom source: ./scripts/copy-highlights-photos.sh /path/to/Highlights

DEST="assets/img/highlights"

if [ -n "$1" ]; then
    SOURCE="$1"
elif [ -d "$HOME/Downloads/Highlights" ]; then
    SOURCE="$HOME/Downloads/Highlights"
elif [ -d "$HOME/Desktop/Highlights" ]; then
    SOURCE="$HOME/Desktop/Highlights"
else
    echo "ERROR: Source folder not found."
    echo "Place your Highlight photos in ~/Downloads/Highlights or ~/Desktop/Highlights, or run:"
    echo "  $0 /path/to/your/Highlights"
    exit 1
fi

mkdir -p "$DEST"

# CSR photos
cp "$SOURCE/0Y5H6490.JPG" "$DEST/csr-sewing-machine.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6490.jpg" "$DEST/csr-sewing-machine.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6491.JPG" "$DEST/csr-children-man.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6491.jpg" "$DEST/csr-children-man.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6493.JPG" "$DEST/csr-children-packages.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6493.jpg" "$DEST/csr-children-packages.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6507.JPG" "$DEST/csr-handshake.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6507.jpg" "$DEST/csr-handshake.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6479.JPG" "$DEST/csr-school-children.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6479.jpg" "$DEST/csr-school-children.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6575.JPG" "$DEST/csr-celebration.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6575.jpg" "$DEST/csr-celebration.jpg" 2>/dev/null

# Women Empowerment - Needs Assessment
cp "$SOURCE/0Y5H6557.JPG" "$DEST/needs-assessment-whiteboard.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6557.jpg" "$DEST/needs-assessment-whiteboard.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6543.JPG" "$DEST/needs-assessment-table.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6543.jpg" "$DEST/needs-assessment-table.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6565.JPG" "$DEST/empowerment-outdoor-session.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6565.jpg" "$DEST/empowerment-outdoor-session.jpg" 2>/dev/null

# Women Empowerment - Education (man in light blue featured)
cp "$SOURCE/1C6B6439.JPG" "$DEST/education-man-presenting.jpg" 2>/dev/null || cp "$SOURCE/1C6B6439.jpg" "$DEST/education-man-presenting.jpg" 2>/dev/null
cp "$SOURCE/1C6B6441.JPG" "$DEST/education-man-standing.jpg" 2>/dev/null || cp "$SOURCE/1C6B6441.jpg" "$DEST/education-man-standing.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6464.JPG" "$DEST/education-panel.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6464.jpg" "$DEST/education-panel.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6447.JPG" "$DEST/education-woman-teaching.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6447.jpg" "$DEST/education-woman-teaching.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6396.JPG" "$DEST/education-classroom-group.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6396.jpg" "$DEST/education-classroom-group.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6371.JPG" "$DEST/education-woman-smartphone.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6371.jpg" "$DEST/education-woman-smartphone.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6380.JPG" "$DEST/education-woman-portrait.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6380.jpg" "$DEST/education-woman-portrait.jpg" 2>/dev/null

# Loan Program - Groups (man featured)
cp "$SOURCE/0Y5H6511.JPG" "$DEST/loan-groups-community.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6511.jpg" "$DEST/loan-groups-community.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6518.JPG" "$DEST/loan-groups-celebration.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6518.jpg" "$DEST/loan-groups-celebration.jpg" 2>/dev/null

# Team / Community
cp "$SOURCE/0Y5H6502.JPG" "$DEST/team-man-children.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6502.jpg" "$DEST/team-man-children.jpg" 2>/dev/null
cp "$SOURCE/0Y5H6524.JPG" "$DEST/community-group-portrait.jpg" 2>/dev/null || cp "$SOURCE/0Y5H6524.jpg" "$DEST/community-group-portrait.jpg" 2>/dev/null

echo "Done! Copied $(ls -1 "$DEST"/*.jpg 2>/dev/null | wc -l) photos to $DEST"
