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
| 🧪 **Completed Experiments** | **4 / 10** |
| 📊 **Completion Rate** | `[████████░░░░░░░░░░░░] 40%` |
| 📅 **Last Updated** | `2026-07-29` |
| ⚡ **Status** | ![Active Development](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square) |
<!-- EXPERIMENTS_STATS_END -->

---

## 🧪 Experiments Summary

<!-- EXPERIMENTS_TABLE_START -->
| Exp # | Experiment Title | Assets & Topology | Status | Folder Link |
| :---: | :--- | :--- | :---: | :---: |
| **Exp-01** | Basic Local Network Setup & PC Configuration | [`💾 Topology (.pkt)`](Experiments/Exp-01_Basic_Local_Network/topology.pkt) • [`🖼️ Diagram`](Experiments/Exp-01_Basic_Local_Network/topology.png) • [`📄 Report`](Experiments/Exp-01_Basic_Local_Network/report.pdf) • [`📝 Notes`](Experiments/Exp-01_Basic_Local_Network/README.md) | ![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github) | [`📁 Exp-01_Basic_Local_Network`](Experiments/Exp-01_Basic_Local_Network) |
| **Exp-02** | Network Topologies (Bus, Star, Ring & Mesh) | [`💾 Topology (.pkt)`](Experiments/Exp-02_Network_Topologies/topology.pkt) • [`🖼️ Diagram`](Experiments/Exp-02_Network_Topologies/topology.png) • [`📝 Notes`](Experiments/Exp-02_Network_Topologies/README.md) | ![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github) | [`📁 Exp-02_Network_Topologies`](Experiments/Exp-02_Network_Topologies) |
| **Exp-03** | Subnetting and VLAN Configuration | *(No .pkt file)* • [`📝 Notes`](Experiments/Exp-03_Subnetting_and_VLANs/README.md) | ![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github) | [`📁 Exp-03_Subnetting_and_VLANs`](Experiments/Exp-03_Subnetting_and_VLANs) |
| **Exp-04** | RIP Routing | [`💾 Topology (.pkt)`](Experiments/Exp-04_RIP_Routing/rip_topology.pkt) • [`📝 Notes`](Experiments/Exp-04_RIP_Routing/README.md) | ![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github) | [`📁 Exp-04_RIP_Routing`](Experiments/Exp-04_RIP_Routing) |
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

## 🚀 How to Add New Experiments

Adding a new experiment is completely automated:

1. Create a new folder under `Experiments/` following the pattern `Exp-XX_Title` (e.g. `Exp-03_Subnetting_VLANs`).
2. Add your Cisco Packet Tracer file (`topology.pkt`), screenshot (`topology.png`), notes (`README.md`), and report (`report.pdf`).
3. Push to GitHub! The GitHub Action will automatically detect the new folder and update this `README.md`.

For detailed instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

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
