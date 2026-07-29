# Contributing to Computer Networks Lab

Contributing to this lab directly on **GitHub.com (Web UI)** is designed to be **100% automated and effortless**! You don't even need to use Git on your computer. ⚡

---

## 🌐 How to Upload Experiments & Cisco Work Directly on GitHub.com

When you finish an experiment or custom Cisco Packet Tracer lab:

### 1. Go to your GitHub Repository
Open [`github.com/shreyashmane-dev/computer-networks-lab`](https://github.com/shreyashmane-dev/computer-networks-lab) in your web browser.

### 2. Upload Your File
1. Click **Add file** ➔ **Upload files** (top right of the repository view).
2. Drag and drop your `.pkt` file.
3. Path it to the appropriate section folder:

   - **For Syllabus Experiments**:
     ```text
     Experiments/Exp-05_OSPF_Routing/topology.pkt
     ```

   - **For Additional Cisco Labs & Projects**:
     ```text
     Cisco_Labs/Lab-01_Multi_Area_OSPF/topology.pkt
     ```

4. Click **Commit changes**.

---

## 🤖 What Happens Automatically in the Cloud

As soon as you click **Commit changes** on GitHub.com:

1. **GitHub Actions Triggered**: The automated workflow (`.github/workflows/update-readme.yml`) starts running automatically in the background.
2. **Auto-Generated Experiment/Lab README**: If you didn't include a `README.md`, GitHub Actions automatically generates a clean `README.md` inside your lab folder (`Cisco_Labs/Lab-01_.../README.md`) with objectives, direct download `.pkt` links, and an addressing table.
3. **Auto-Updated Main README**: The completed experiment count, visual progress bar, and summary tables in the root `README.md` are updated automatically within seconds!

---

## 🖼️ Optional Files You Can Upload
- `topology.png`: Network diagram screenshot to visually embed in the lab notes.
- `report.pdf`: Assignment report or observation sheet.
