# Photo Changes & Revert Guide

This document describes the Highlight photos added to the website and how to revert if needed.

---

## Step 1: Add Your Photos (Required)

**The new images will not display until you run the copy script.**

1. Place your Highlight photos in: `~/Downloads/Highlights/` or `~/Desktop/Highlights/`
2. Run from project root:
   ```bash
   ./scripts/copy-highlights-photos.sh
   ```
   Or with a custom path:
   ```bash
   ./scripts/copy-highlights-photos.sh /path/to/your/Highlights
   ```

---

## What Was Added & Where

### CSR Section (about.php.html #csr)

| Slot | NEW Photo | Replaced | Description |
|------|-----------|----------|-------------|
| Main image 1 | `csr-sewing-machine.jpg` | `csr-uniforms.png` | Sewing machine donation (man featured) |
| Main image 2 | `csr-children-man.jpg` | `csr-sports-kits.png` | Team member with students |
| Grid image 1 | `csr-children-packages.jpg` | `csr-photocopier-1.png` | Students with packages |
| Grid image 2 | `csr-handshake.jpg` | `csr-photocopier-2.png` | Mentorship handshake |
| Grid image 3 | `csr-school-children.jpg` | `csr-photocopier-3.png` | School children at event |
| New row | `csr-celebration.jpg` | (added, not replaced) | Community celebration |

### Women Empowerment Section (about.php.html #women-empowerment)

**Needs Assessment (replaced all 3):**

| Slot | NEW Photo | Replaced |
|------|-----------|----------|
| 1 | `needs-assessment-whiteboard.jpg` | `stakeholders-women-1.png` |
| 2 | `needs-assessment-table.jpg` | `stakeholders-women-2.png` |
| 3 | `empowerment-outdoor-session.jpg` | `stakeholders-women-3.png` |

**Education Sessions (replaced all 6):**

| Slot | NEW Photo | Replaced |
|------|-----------|----------|
| 1 | `education-man-presenting.jpg` | `women-empowerment-1.png` |
| 2 | `education-man-standing.jpg` | `women-empowerment-2.png` |
| 3 | `education-panel.jpg` | `women-empowerment-3.png` |
| 4 | `education-woman-teaching.jpg` | `women-empowerment-4.png` |
| 5 | `education-classroom-group.jpg` | `women-empowerment-5.png` |
| 6 | `education-woman-smartphone.jpg` | `women-empowerment-6.png` |

### Loan Program Section (about.php.html #loan-program)

**Step 1 - Education:**
| Slot | NEW Photo | Replaced |
|------|-----------|----------|
| 1 | `education-man-presenting.jpg` | `women-empowerment-7.png` |
| 2 | `education-panel.jpg` | `women-empowerment-8.png` |
| 3 | `education-classroom-group.jpg` | `women-empowerment-9.png` |

**Step 2 - Groups:**
| Slot | NEW Photo | Replaced |
|------|-----------|----------|
| 1 | `loan-groups-community.jpg` | `community-engagement-1.png` |
| 2 | `empowerment-outdoor-session.jpg` | `community-engagement-2.png` |
| 3 | `loan-groups-celebration.jpg` | `community-engagement-3.png` |

### Community Leaders Section (about.php.html #community-leaders)

| What | NEW | Replaced |
|------|-----|----------|
| Image | `community-group-portrait.jpg` | (was placeholder only) |

### Team Page (team.html)

| What | NEW | Replaced |
|------|-----|----------|
| "Our Team in the Field" | Added `team-man-children.jpg` alongside `team-photo.png` | (added second image, kept original) |

---

## How to Revert

To restore the previous images, run:

```bash
git revert HEAD --no-edit
```

Or manually restore the paths in `about.php.html` and `team.html`:

- Change all `assets/img/highlights/*.jpg` back to the original `assets/img/impact/*.png` paths listed in the tables above.
- On team.html, remove the row with `team-man-children.jpg` and restore the single `team-photo.png` block.

---

## Source Files (from Pixieset Highlights)

- 0Y5H6490, 6491, 6493, 6507, 6479, 6575 (CSR)
- 0Y5H6557, 6543, 6565 (Needs assessment)
- 1C6B6439, 1C6B6441, 0Y5H6464, 6447, 6396, 6371, 6380 (Education)
- 0Y5H6511, 6518 (Loan groups)
- 0Y5H6502, 6524 (Team/community)
