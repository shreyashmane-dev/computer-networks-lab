#!/usr/bin/env python3
"""
update_readme.py

Automated script for Computer Networks Lab repository:
1. Scans `Experiments/` for experiment folders.
2. Automatically generates an experiment-specific `README.md` inside any experiment
   folder if only a `.pkt` file is uploaded by the user.
3. Updates the root `README.md` statistics and summary table.
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent.resolve()
EXPERIMENTS_DIR = REPO_ROOT / "Experiments"
README_PATH = REPO_ROOT / "README.md"

# Target number of experiments for progress calculation
TARGET_EXPERIMENTS = 10


def natural_sort_key(s):
    """Sort strings containing numbers naturally (e.g. Exp-01, Exp-02, Exp-10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", str(s))]


def clean_title_from_folder(folder_name: str) -> str:
    """Format folder name into a clean title (e.g. Exp-04_Static_Routing -> Static Routing)."""
    cleaned = re.sub(r"^Exp-?\d+_?", "", folder_name, flags=re.IGNORECASE)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned if cleaned else folder_name


def get_title_from_readme(exp_readme: Path, folder_name: str) -> str:
    """Attempt to extract the title from an existing experiment README.md."""
    if exp_readme.is_file():
        try:
            with open(exp_readme, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#"):
                        title = line.lstrip("#").strip()
                        title = re.sub(r"^Exp(eriment)?[\s\-_]*\d+[\s\-_:]*", "", title, flags=re.IGNORECASE).strip()
                        if title:
                            return title
        except Exception:
            pass
    return clean_title_from_folder(folder_name)


def generate_experiment_readme_content(exp_code: str, title: str, folder_name: str, pkt_file: str = None) -> str:
    """Generate default README.md content for an experiment folder."""
    pkt_info = f"`{pkt_file}`" if pkt_file else "Cisco Packet Tracer (`.pkt`)"
    
    content = f"""# {exp_code}: {title}

## 🎯 Objectives
- Build and configure the network topology in Cisco Packet Tracer.
- Verify node connectivity and analyze network protocol behavior.

---

## 💾 Topology File
- **Packet Tracer File**: {pkt_info}
- Open this file in **Cisco Packet Tracer v8.x+** to inspect the configuration and simulate traffic.

---

## 📐 Network Topology & Configuration

> *Upload a `topology.png` screenshot to this experiment folder to visually display the diagram here.*

### Device Addressing Table Template

| Device Name | Interface | IP Address | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Router1** | GigabitEthernet0/0/0 | `192.168.1.1` | `255.255.255.0` | N/A |
| **PC1** | FastEthernet0 | `192.168.1.10` | `255.255.255.0` | `192.168.1.1` |

---

## 🔍 Verification Steps
1. Open `{pkt_file if pkt_file else 'topology.pkt'}` in Cisco Packet Tracer.
2. Enter Desktop > Command Prompt on end devices.
3. Test connectivity using `ping <destination-ip>`.
"""
    return content


import sys

# Ensure UTF-8 output encoding for standard output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def ensure_experiment_readme(exp_dir: Path, exp_code: str, title: str, pkt_file: str = None) -> bool:
    """Ensure an experiment folder has a README.md file. Creates one if missing."""
    exp_readme = exp_dir / "README.md"
    if not exp_readme.exists():
        content = generate_experiment_readme_content(exp_code, title, exp_dir.name, pkt_file)
        with open(exp_readme, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Auto-generated experiment README: {exp_dir.name}/README.md")
        return True
    return False


def scan_experiments():
    """Scan the Experiments directory, auto-generate missing experiment READMEs, and build dataset."""
    if not EXPERIMENTS_DIR.exists():
        return []

    exp_folders = [
        d for d in EXPERIMENTS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    ]
    exp_folders.sort(key=lambda d: natural_sort_key(d.name))

    experiments = []
    for exp_dir in exp_folders:
        folder_name = exp_dir.name
        
        # Match Exp number
        match = re.match(r"^Exp-?(\d+)", folder_name, re.IGNORECASE)
        exp_num = match.group(1) if match else "N/A"
        exp_code = f"Exp-{exp_num}" if exp_num != "N/A" else folder_name

        exp_readme = exp_dir / "README.md"
        title = get_title_from_readme(exp_readme, folder_name)

        # Detect files
        pkt_file = next((f.name for f in exp_dir.iterdir() if f.is_file() and f.suffix.lower() == ".pkt"), None)
        png_file = next((f.name for f in exp_dir.iterdir() if f.is_file() and f.suffix.lower() in [".png", ".jpg", ".jpeg", ".svg"]), None)
        pdf_file = next((f.name for f in exp_dir.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"), None)

        # Auto-create experiment README if missing
        ensure_experiment_readme(exp_dir, exp_code, title, pkt_file)

        has_readme = (exp_dir / "README.md").is_file()
        rel_path = f"Experiments/{folder_name}".replace("\\", "/")

        experiments.append({
            "code": exp_code,
            "folder_name": folder_name,
            "title": title,
            "rel_path": rel_path,
            "pkt_file": pkt_file,
            "png_file": png_file,
            "pdf_file": pdf_file,
            "has_readme": has_readme,
        })

    return experiments


def generate_text_progress_bar(percentage: int, width: int = 20) -> str:
    """Generate a Unicode progress bar string."""
    filled = int(round(width * percentage / 100))
    bar = "█" * filled + "░" * (width - filled)
    return bar


def generate_stats_block(experiments_count: int, target_count: int, last_updated: str) -> str:
    """Generate statistics section markdown."""
    percentage = int((experiments_count / target_count) * 100) if target_count > 0 else 0
    percentage = min(percentage, 100)
    bar = generate_text_progress_bar(percentage, width=20)

    stats_md = f"""| Metric | Value |
| :--- | :--- |
| 🧪 **Completed Experiments** | **{experiments_count} / {target_count}** |
| 📊 **Completion Rate** | `[{bar}] {percentage}%` |
| 📅 **Last Updated** | `{last_updated}` |
| ⚡ **Status** | ![Active Development](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square) |"""
    return stats_md


def generate_table_block(experiments) -> str:
    """Generate the experiments markdown table."""
    if not experiments:
        return "*No experiments found yet. Add folders under `Experiments/Exp-XX_...` to populate this table.*"

    table_lines = [
        "| Exp # | Experiment Title | Assets & Topology | Status | Folder Link |",
        "| :---: | :--- | :--- | :---: | :---: |"
    ]

    for exp in experiments:
        code = exp["code"]
        title = exp["title"]
        rel_path = exp["rel_path"]

        # Build assets list
        assets = []
        if exp["pkt_file"]:
            assets.append(f"[`💾 Topology (.pkt)`]({rel_path}/{exp['pkt_file']})")
        else:
            assets.append("*(No .pkt file)*")

        if exp["png_file"]:
            assets.append(f"[`🖼️ Diagram`]({rel_path}/{exp['png_file']})")
        
        if exp["pdf_file"]:
            assets.append(f"[`📄 Report`]({rel_path}/{exp['pdf_file']})")

        if exp["has_readme"]:
            assets.append(f"[`📝 Notes`]({rel_path}/README.md)")

        assets_str = " • ".join(assets)
        status_badge = "![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github)"
        folder_link = f"[`📁 {exp['folder_name']}`]({rel_path})"

        table_lines.append(f"| **{code}** | {title} | {assets_str} | {status_badge} | {folder_link} |")

    return "\n".join(table_lines)


def update_readme():
    """Main function to update README.md and experiment READMEs."""
    if not README_PATH.exists():
        print(f"Error: {README_PATH} does not exist.")
        return

    experiments = scan_experiments()
    count = len(experiments)
    target = max(TARGET_EXPERIMENTS, count)
    today_str = datetime.now().strftime("%Y-%m-%d")

    stats_block = generate_stats_block(count, target, today_str)
    table_block = generate_table_block(experiments)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace STATS section
    stats_pattern = r"(<!-- EXPERIMENTS_STATS_START -->)(.*?)(<!-- EXPERIMENTS_STATS_END -->)"
    if re.search(stats_pattern, content, flags=re.DOTALL):
        content = re.sub(
            stats_pattern,
            f"\\1\n{stats_block}\n\\3",
            content,
            flags=re.DOTALL
        )

    # Replace TABLE section
    table_pattern = r"(<!-- EXPERIMENTS_TABLE_START -->)(.*?)(<!-- EXPERIMENTS_TABLE_END -->)"
    if re.search(table_pattern, content, flags=re.DOTALL):
        content = re.sub(
            table_pattern,
            f"\\1\n{table_block}\n\\3",
            content,
            flags=re.DOTALL
        )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated README.md with {count} experiments.")


if __name__ == "__main__":
    update_readme()
