<div align="center">

# 🌐 Computer Networks Lab

### *A Comprehensive Collection of Computer Networks Experiments, Topologies, & Lab Reports*

[![Cisco Packet Tracer](https://img.shields.io/badge/Cisco_Packet_Tracer-v8.x-005073?style=for-the-badge&logo=cisco&logoColor=white)](https://www.netacad.com/courses/packet-tracer)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Auto_Update-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

[![Repo Size](https://img.shields.io/github/repo-size/shreyashmane-dev/computer-networks-lab?style=flat-square&color=blue)](https://github.com/shreyashmane-dev/computer-networks-lab)
[![Last Commit](https://img.shields.io/github/last-commit/shreyashmane-dev/computer-networks-lab?style=flat-square&color=green)](https://github.com/shreyashmane-dev/computer-networks-lab/commits/main)
[![Stars](https://img.shields.io/github/stars/shreyashmane-dev/computer-networks-lab?style=flat-square&color=gold)](https://github.com/shreyashmane-dev/computer-networks-lab/stargazers)
[![Forks](https://img.shields.io/github/forks/shreyashmane-dev/computer-networks-lab?style=flat-square&color=orange)](https://github.com/shreyashmane-dev/computer-networks-lab/network/members)

</div>

---

## 📌 About The Repository

Welcome to the **Computer Networks (CN) Laboratory** repository! This repository contains practical implementations, network topology files (`.pkt`), high-resolution diagrams (`.png`), and detailed analytical lab reports for university-level Computer Networks experiments.

> 🤖 **Automated README**: This repository features an automated GitHub Actions workflow (`.github/workflows/update-readme.yml`) that scans the `Experiments/` folder on every push, calculates progress metrics, and updates the table below automatically!

---

## 📊 Lab Overview & Progress Statistics

<!-- EXPERIMENTS_STATS_START -->
| Metric | Value |
| :--- | :--- |
| 🧪 **Completed Experiments** | **2 / 10** |
| 📊 **Completion Rate** | `[████░░░░░░░░░░░░░░░░] 20%` |
| 📅 **Last Updated** | `2026-07-29` |
| ⚡ **Status** | ![Active Development](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square) |
<!-- EXPERIMENTS_STATS_END -->

---

## 🧪 Experiments Summary

<!-- EXPERIMENTS_TABLE_START -->
| Exp # | Experiment Title | 📥 Direct Download (.pkt) | 📁 Explore Details | Included Assets | Status |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **Exp-01** | **Basic Local Network Setup & PC Configuration** | [![Download PKT](https://img.shields.io/badge/📥_Download-.pkt-005073?style=for-the-badge&logo=cisco&logoColor=white)](https://github.com/shreyashmane-dev/computer-networks-lab/raw/main/Experiments/Exp-01_Basic_Local_Network/Exp-01_Basic_Local_Network.pkt) | [![View Details](https://img.shields.io/badge/📁_View-Details-2088FF?style=for-the-badge)](Experiments/Exp-01_Basic_Local_Network/) | [`📄 Report`](Experiments/Exp-01_Basic_Local_Network/report.pdf) • [`📝 Notes`](Experiments/Exp-01_Basic_Local_Network/README.md) | ![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github) |
| **Exp-02** | **Network Topologies (Bus, Star, Ring & Mesh)** | [![Download PKT](https://img.shields.io/badge/📥_Download-.pkt-005073?style=for-the-badge&logo=cisco&logoColor=white)](https://github.com/shreyashmane-dev/computer-networks-lab/raw/main/Experiments/Exp-02_Network_Topologies/Exp-02_Network_Topologies.pkt) | [![View Details](https://img.shields.io/badge/📁_View-Details-2088FF?style=for-the-badge)](Experiments/Exp-02_Network_Topologies/) | [`📝 Notes`](Experiments/Exp-02_Network_Topologies/README.md) | ![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github) |
<!-- EXPERIMENTS_TABLE_END -->

---

## 🛠️ Repository Directory Structure

```text
computer-networks-lab/
├── .github/
│   └── workflows/
│       └── update-readme.yml     # 🤖 GitHub Actions workflow for auto updating README
├── Experiments/                  # 🧪 Experiment source folders
│   ├── Exp-01_Basic_Local_Network/
│   │   ├── README.md             # 📝 Experiment objectives & instructions
│   │   ├── topology.pkt          # 💾 Cisco Packet Tracer binary topology
│   │   ├── topology.png          # 🖼️ Network topology screenshot
│   │   └── report.pdf            # 📄 Lab report & observation table
│   ├── Exp-02_Network_Topologies/
│   └── ...
├── Reports/                      # 📄 Global lab reports & docs archive
├── Images/                       # 🖼️ Repository graphics & badges
├── scripts/
│   └── update_readme.py          # ⚙️ Python script for dynamic README updates
├── .gitignore                    # 🙈 Git ignore rules
├── CONTRIBUTING.md               # 🤝 Guidelines for adding experiments
├── LICENSE                       # 📜 MIT License
└── README.md                     # 📖 Main repository overview
```

---

## 🚀 How to Add New Experiments (Directly on GitHub.com)

Adding a new experiment can be done **directly in your web browser** without using terminal commands:

1. Open your repository on **GitHub.com** and click **Add file** ➔ **Upload files**.
2. Drag & drop your `.pkt` file and specify the experiment folder path, e.g.:
   `Experiments/Exp-05_OSPF_Routing/topology.pkt`
3. Click **Commit changes**.
4. 🤖 **GitHub Actions** will automatically run in the background, generate `Experiments/Exp-05_OSPF_Routing/README.md`, update the completed count, progress bar, and summary table above within seconds!

For detailed steps, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 🛠️ Technologies & Tools Used

- **Network Simulation**: [Cisco Packet Tracer v8.x](https://www.netacad.com/courses/packet-tracer)
- **Protocol Analysis**: [Wireshark](https://www.wireshark.org/)
- **Automation**: Python 3.x, GitHub Actions Workflow
- **Documentation**: Markdown, Mermaid, SVG Graphics

---

## 👤 Author

**CN Lab Student / Maintainer**
- 🐙 GitHub: [@shreyashmane-dev](https://github.com/shreyashmane-dev)
- 🏫 Course: Computer Networks Laboratory
- 📧 Contact: `student@example.com`

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.
