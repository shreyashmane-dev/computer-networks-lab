#!/usr/bin/env python3
"""
update_readme.py

Automated script for Computer Networks Lab repository:
1. Scans `Experiments/` and `Cisco_Labs/` for lab folders.
2. Automatically generates an experiment/lab-specific `README.md` inside any folder
   if only a `.pkt` file is uploaded by the user.
3. Updates the root `README.md` statistics and both summary tables with direct 📥 Download .pkt links
   and 📁 View Details shortcuts.
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Ensure UTF-8 output encoding for standard output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Repository Metadata
REPO_OWNER = "shreyashmane-dev"
REPO_NAME = "computer-networks-lab"
BRANCH = "main"
RAW_BASE_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/raw/{BRANCH}"

# Paths
REPO_ROOT = Path(__file__).parent.parent.resolve()
EXPERIMENTS_DIR = REPO_ROOT / "Experiments"
CISCO_LABS_DIR = REPO_ROOT / "Cisco_Labs"
README_PATH = REPO_ROOT / "README.md"

# Target number of experiments for progress calculation
TARGET_EXPERIMENTS = 10


def natural_sort_key(s):
    """Sort strings containing numbers naturally (e.g. Exp-01, Exp-02, Exp-10, Lab-01)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", str(s))]


def clean_title_from_folder(folder_name: str) -> str:
    """Format folder name into a clean title (e.g. Lab-01_Multi_Area_OSPF -> Multi Area OSPF)."""
    cleaned = re.sub(r"^(Exp|Lab|Proj|Project)-?\d+_?", "", folder_name, flags=re.IGNORECASE)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned if cleaned else folder_name


def get_title_from_readme(exp_readme: Path, folder_name: str) -> str:
    """Attempt to extract the title from an existing README.md."""
    if exp_readme.is_file():
        try:
            with open(exp_readme, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#"):
                        title = line.lstrip("#").strip()
                        title = re.sub(r"^(Exp|Experiment|Lab|Proj|Project)[\s\-_]*\d+[\s\-_:]*", "", title, flags=re.IGNORECASE).strip()
                        if title:
                            return title
        except Exception:
            pass
    return clean_title_from_folder(folder_name)


def generate_lab_readme_content(item_code: str, title: str, section_dir_name: str, folder_name: str, pkt_file: str = None) -> str:
    """Generate default README.md content for a lab/experiment folder."""
    pkt_info = f"`{pkt_file}`" if pkt_file else "Cisco Packet Tracer (`.pkt`)"
    pkt_download = f"[📥 **Download {pkt_file}**]({RAW_BASE_URL}/{section_dir_name}/{folder_name}/{pkt_file})" if pkt_file else ""
    
    content = f"""# {item_code}: {title}

## 🎯 Objectives
- Build and configure the network topology in Cisco Packet Tracer.
- Verify node connectivity and analyze network protocol behavior.

---

## 💾 Topology File & Direct Download
- **Packet Tracer File**: {pkt_info}
- {pkt_download}
- Open this file in **Cisco Packet Tracer v8.x+** to inspect the configuration and simulate traffic.

---

## 📐 Network Topology & Configuration

> *Upload a `topology.png` screenshot to this lab folder to visually display the diagram here.*

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


def ensure_lab_readme(lab_dir: Path, section_dir_name: str, item_code: str, title: str, pkt_file: str = None) -> bool:
    """Ensure a lab folder has a README.md file. Creates one if missing."""
    lab_readme = lab_dir / "README.md"
    if not lab_readme.exists():
        content = generate_lab_readme_content(item_code, title, section_dir_name, lab_dir.name, pkt_file)
        with open(lab_readme, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Auto-generated lab README: {section_dir_name}/{lab_dir.name}/README.md")
        return True
    return False


def scan_directory(target_dir: Path, default_prefix: str = "Exp"):
    """Scan a directory for folders, auto-generate missing READMEs, and build dataset."""
    if not target_dir.exists():
        return []

    section_name = target_dir.name
    folders = [
        d for d in target_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    ]
    folders.sort(key=lambda d: natural_sort_key(d.name))

    items = []
    for lab_dir in folders:
        folder_name = lab_dir.name
        
        # Match number
        match = re.search(r"(\d+)", folder_name)
        item_num = match.group(1) if match else "N/A"
        
        # Match prefix or use default
        prefix_match = re.match(r"^(Exp|Lab|Proj|Project)", folder_name, re.IGNORECASE)
        prefix = prefix_match.group(1).capitalize() if prefix_match else default_prefix
        item_code = f"{prefix}-{item_num}" if item_num != "N/A" else folder_name

        lab_readme = lab_dir / "README.md"
        title = get_title_from_readme(lab_readme, folder_name)

        # Detect files
        pkt_file = next((f.name for f in lab_dir.iterdir() if f.is_file() and f.suffix.lower() == ".pkt"), None)
        png_file = next((f.name for f in lab_dir.iterdir() if f.is_file() and f.suffix.lower() in [".png", ".jpg", ".jpeg", ".svg"]), None)
        pdf_file = next((f.name for f in lab_dir.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"), None)

        # Auto-create README if missing
        ensure_lab_readme(lab_dir, section_name, item_code, title, pkt_file)

        has_readme = (lab_dir / "README.md").is_file()
        rel_path = f"{section_name}/{folder_name}".replace("\\", "/")

        # Build direct raw download link for .pkt file
        raw_pkt_url = f"{RAW_BASE_URL}/{rel_path}/{pkt_file}" if pkt_file else None

        items.append({
            "code": item_code,
            "folder_name": folder_name,
            "title": title,
            "rel_path": rel_path,
            "pkt_file": pkt_file,
            "raw_pkt_url": raw_pkt_url,
            "png_file": png_file,
            "pdf_file": pdf_file,
            "has_readme": has_readme,
        })

    return items


def generate_text_progress_bar(percentage: int, width: int = 20) -> str:
    """Generate a Unicode progress bar string."""
    filled = int(round(width * percentage / 100))
    bar = "█" * filled + "░" * (width - filled)
    return bar


def generate_stats_block(experiments_count: int, target_count: int, cisco_labs_count: int, last_updated: str) -> str:
    """Generate statistics section markdown."""
    percentage = int((experiments_count / target_count) * 100) if target_count > 0 else 0
    percentage = min(percentage, 100)
    bar = generate_text_progress_bar(percentage, width=20)

    stats_md = f"""| Metric | Value |
| :--- | :--- |
| 🧪 **Completed Core Experiments** | **{experiments_count} / {target_count}** |
| 📡 **Additional Cisco Labs & Projects** | **{cisco_labs_count} Total** |
| 📊 **Completion Rate** | `[{bar}] {percentage}%` |
| 📅 **Last Updated** | `{last_updated}` |
| ⚡ **Status** | ![Active Development](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square) |"""
    return stats_md


def generate_table_block(items, empty_message: str) -> str:
    """Generate markdown table with direct download buttons and folder links."""
    if not items:
        return f"*{empty_message}*"

    table_lines = [
        "| ID # | Title / Topic | 📥 Direct Download (.pkt) | 📁 Explore Details | Included Assets | Status |",
        "| :---: | :--- | :---: | :---: | :--- | :---: |"
    ]

    for item in items:
        code = item["code"]
        title = item["title"]
        rel_path = item["rel_path"]
        raw_pkt_url = item["raw_pkt_url"]

        # Download button/link
        if raw_pkt_url:
            download_btn = f"[![Download PKT](https://img.shields.io/badge/📥_Download-.pkt-005073?style=for-the-badge&logo=cisco&logoColor=white)]({raw_pkt_url})"
        else:
            download_btn = "*(No .pkt file)*"

        # Explore details / folder link button
        folder_btn = f"[![View Details](https://img.shields.io/badge/📁_View-Details-2088FF?style=for-the-badge)]({rel_path}/)"

        # Additional assets indicator
        assets = []
        if item["png_file"]:
            assets.append(f"[`🖼️ Diagram`]({rel_path}/{item['png_file']})")
        if item["pdf_file"]:
            assets.append(f"[`📄 Report`]({rel_path}/{item['pdf_file']})")
        if item["has_readme"]:
            assets.append(f"[`📝 Notes`]({rel_path}/README.md)")

        assets_str = " • ".join(assets) if assets else "*(Notes Auto-Generated)*"
        status_badge = "![Completed](https://img.shields.io/badge/Completed-success?style=flat-square&logo=github)"

        table_lines.append(f"| **{code}** | **{title}** | {download_btn} | {folder_btn} | {assets_str} | {status_badge} |")

    return "\n".join(table_lines)


def update_readme():
    """Main function to update README.md and experiment READMEs."""
    if not README_PATH.exists():
        print(f"Error: {README_PATH} does not exist.")
        return

    # Ensure directories exist
    EXPERIMENTS_DIR.mkdir(exist_ok=True)
    CISCO_LABS_DIR.mkdir(exist_ok=True)

    experiments = scan_directory(EXPERIMENTS_DIR, default_prefix="Exp")
    cisco_labs = scan_directory(CISCO_LABS_DIR, default_prefix="Lab")

    exp_count = len(experiments)
    cisco_count = len(cisco_labs)
    target = max(TARGET_EXPERIMENTS, exp_count)
    today_str = datetime.now().strftime("%Y-%m-%d")

    stats_block = generate_stats_block(exp_count, target, cisco_count, today_str)
    exp_table_block = generate_table_block(experiments, "No experiments found yet. Add folders under `Experiments/Exp-XX_...` to populate this table.")
    cisco_table_block = generate_table_block(cisco_labs, "No additional Cisco labs uploaded yet. Upload folders under `Cisco_Labs/Lab-XX_...` to populate this table.")

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

    # Replace EXPERIMENTS TABLE section
    exp_table_pattern = r"(<!-- EXPERIMENTS_TABLE_START -->)(.*?)(<!-- EXPERIMENTS_TABLE_END -->)"
    if re.search(exp_table_pattern, content, flags=re.DOTALL):
        content = re.sub(
            exp_table_pattern,
            f"\\1\n{exp_table_block}\n\\3",
            content,
            flags=re.DOTALL
        )

    # Replace CISCO LABS TABLE section
    cisco_table_pattern = r"(<!-- CISCO_LABS_TABLE_START -->)(.*?)(<!-- CISCO_LABS_TABLE_END -->)"
    if re.search(cisco_table_pattern, content, flags=re.DOTALL):
        content = re.sub(
            cisco_table_pattern,
            f"\\1\n{cisco_table_block}\n\\3",
            content,
            flags=re.DOTALL
        )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated README.md with {exp_count} experiments and {cisco_count} Cisco labs.")


if __name__ == "__main__":
    update_readme()
