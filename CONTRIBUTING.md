# Contributing to Computer Networks Lab

Contributing to this lab repository is simple and automated! ⚡

---

## 🌐 How to Add an Experiment

1. Create a folder in the root directory following the naming pattern:
   ```text
   Exp-03_Subnetting/
   ```
2. Place your Cisco Packet Tracer file (`.pkt`) inside that folder:
   ```text
   Exp-03_Subnetting/Exp-03_Subnetting.pkt
   ```
3. Commit and push your changes to GitHub.

---

## 🤖 Automated Updates

- When you push to GitHub, GitHub Actions runs `scripts/update_readme.py` automatically.
- It detects the new experiment folder, extracts the `.pkt` file, and updates the experiments table in `README.md` with a direct download button.
