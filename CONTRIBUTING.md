# Contributing to Computer Networks Lab

Contributing to this lab directly on **GitHub.com (Web UI)** is designed to be **100% automated and effortless**! You don't even need to use Git on your computer. ⚡

---

## 🌐 How to Upload Experiments Directly on GitHub.com

When you finish a new experiment in Cisco Packet Tracer:

### 1. Go to your GitHub Repository
Open [`github.com/shreyashmane-dev/computer-networks-lab`](https://github.com/shreyashmane-dev/computer-networks-lab) in your web browser.

### 2. Upload Your File
1. Click **Add file** ➔ **Upload files** (top right of the repository view).
2. Drag and drop your `.pkt` file.
3. In the filename input or commit message, path it to a folder under `Experiments/`:
   ```text
   Experiments/Exp-05_OSPF_Routing/topology.pkt
   ```
4. Click **Commit changes**.

---

## 🤖 What Happens Automatically in the Cloud

As soon as you click **Commit changes** on GitHub.com:

1. **GitHub Actions Triggered**: The automated workflow (`.github/workflows/update-readme.yml`) starts running automatically in the background.
2. **Auto-Generated Experiment README**: If you didn't include a `README.md`, GitHub Actions automatically generates a clean `README.md` inside your experiment folder (`Experiments/Exp-05_OSPF_Routing/README.md`) with objectives, topology links, and an addressing table.
3. **Auto-Updated Main README**: The completed experiment count, visual progress bar (`[██████████░░░░░░░░░░] 50%`), and summary table in the root `README.md` are updated automatically within seconds!

---

## 🖼️ Optional Files You Can Upload
- `topology.png`: Network diagram screenshot to visually embed in the experiment notes.
- `report.pdf`: Assignment report or observation sheet.
