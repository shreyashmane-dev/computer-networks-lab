#!/usr/bin/env python3
"""
update_readme.py

Automated script for Computer Networks Lab repository:
1. Scans root directory for experiment folders (Exp-01 to Exp-10).
2. Generates direct download links for .pkt, sender/receiver .cpp, and case study files.
3. Formats table using official experiment names and dates.
4. Updates README.md automatically.
"""

import os
import re
import sys
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
README_PATH = REPO_ROOT / "README.md"

# Official Experiment Index (Names & Dates)
EXPERIMENT_INDEX = {
    "01": {
        "name": "Design and Configure a Simple Network Topology using Cisco Packet Tracer",
        "date": "28-07-2026",
    },
    "02": {
        "name": "Configure Different Network Topologies using Cisco Packet Tracer",
        "date": "04-08-2026",
    },
    "03": {
        "name": "Case Study of Networking Devices",
        "date": "11-08-2026",
    },
    "04": {
        "name": "Implementation of Framing Methods – Bit Stuffing",
        "date": "17-08-2026",
    },
    "05": {
        "name": "Implementation of Error Correction Code",
        "date": "24-08-2026",
    },
    "06": {
        "name": "Implementation of Stop-and-Wait Protocol",
        "date": "31-08-2026",
    },
    "07": {
        "name": "Implementation of Error Detection Code",
        "date": "07-09-2026",
    },
    "08": {
        "name": "Implementation of C Program for IP Address Calculation",
        "date": "22-09-2026",
    },
    "09": {
        "name": "Configuration of DHCP Server using Cisco Packet Tracer",
        "date": "28-09-2026",
    },
    "10": {
        "name": "Simulation of FTP Working using Cisco Packet Tracer",
        "date": "29-09-2026",
    },
}


def natural_sort_key(s):
    """Sort strings containing numbers naturally (e.g. Exp-01, Exp-02, Exp-10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", str(s))]


def clean_title_from_folder(folder_name: str, item_num: str) -> str:
    """Format folder name into a clean title, preferring official index."""
    if item_num in EXPERIMENT_INDEX:
        return EXPERIMENT_INDEX[item_num]["name"]
    cleaned = re.sub(r"^(Exp|Experiment|Lab)[\s\-_]*\d+[\s\-_]*", "", folder_name, flags=re.IGNORECASE)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned if cleaned else folder_name


def scan_experiments(root_dir: Path):
    """Scan root directory for experiment folders."""
    experiments = []
    ignored = {".git", ".github", "scripts", "__pycache__"}

    for entry in root_dir.iterdir():
        if not entry.is_dir() or entry.name in ignored or entry.name.startswith("."):
            continue

        # Check if folder starts with Exp
        if not re.match(r"^(Exp|Experiment)", entry.name, re.IGNORECASE):
            continue

        folder_name = entry.name
        match = re.search(r"(\d+)", folder_name)
        item_num = match.group(1) if match else "0"
        num_display = f"{int(item_num):02d}" if item_num.isdigit() else item_num
        item_code = f"Exp-{num_display}"

        # Clean up any accidental sub-README.md
        sub_readme = entry / "README.md"
        if sub_readme.exists():
            try:
                sub_readme.unlink()
                print(f"[-] Removed sub-readme: {entry.name}/README.md")
            except Exception:
                pass

        # Identify files inside folder
        files = [f for f in entry.iterdir() if f.is_file()]
        pkt_files = [f.name for f in files if f.suffix.lower() == ".pkt"]
        cpp_files = [f.name for f in files if f.suffix.lower() == ".cpp"]
        md_files = [f.name for f in files if f.suffix.lower() == ".md" and f.name.lower() != "readme.md"]

        # Date & Title
        info = EXPERIMENT_INDEX.get(num_display, {})
        title = info.get("name", clean_title_from_folder(folder_name, num_display))
        date = info.get("date", "—")

        # Generate action/download badges
        badges = []
        # Packet Tracer
        for pkt in pkt_files:
            url = f"{RAW_BASE_URL}/{folder_name}/{pkt}"
            badges.append(f"[![Download .pkt](https://img.shields.io/badge/📥_Download-.pkt-005073?style=for-the-badge&logo=cisco&logoColor=white)]({url})")

        # Separate Sender and Receiver C++ files
        senders = [c for c in cpp_files if "sender" in c.lower()]
        receivers = [c for c in cpp_files if "receiver" in c.lower()]
        other_cpp = [c for c in cpp_files if c not in senders and c not in receivers]

        for s in senders:
            url = f"{RAW_BASE_URL}/{folder_name}/{s}"
            badges.append(f"[![Sender Code](https://img.shields.io/badge/📤_Sender-.cpp-3776AB?style=for-the-badge&logo=c%2B%2B&logoColor=white)]({url})")

        for r in receivers:
            url = f"{RAW_BASE_URL}/{folder_name}/{r}"
            badges.append(f"[![Receiver Code](https://img.shields.io/badge/📥_Receiver-.cpp-2088FF?style=for-the-badge&logo=c%2B%2B&logoColor=white)]({url})")

        for o in other_cpp:
            url = f"{RAW_BASE_URL}/{folder_name}/{o}"
            badges.append(f"[![Source Code](https://img.shields.io/badge/💻_Code-.cpp-3776AB?style=for-the-badge&logo=c%2B%2B&logoColor=white)]({url})")

        # Case Study / Documentation
        for m in md_files:
            url = f"{folder_name}/{m}"
            badges.append(f"[![View Case Study](https://img.shields.io/badge/📄_Case-Study-2EA44F?style=for-the-badge&logo=markdown&logoColor=white)]({url})")

        experiments.append({
            "num": num_display,
            "code": item_code,
            "folder_name": folder_name,
            "title": title,
            "date": date,
            "badges": " ".join(badges) if badges else "*(In Progress)*",
        })

    experiments.sort(key=lambda x: natural_sort_key(x["code"]))
    return experiments


def generate_table(experiments) -> str:
    """Generate markdown table with experiment name, date, and download buttons."""
    if not experiments:
        return "*No experiments found.*"

    table_lines = [
        "| # | Proper Experiment Name | Date | Direct Download / Source Code |",
        "| :---: | :--- | :---: | :--- |"
    ]

    for exp in experiments:
        num = exp["num"]
        title = exp["title"]
        date = exp["date"]
        badges = exp["badges"]
        table_lines.append(f"| **{num}** | **{title}** | `{date}` | {badges} |")

    return "\n".join(table_lines)


def update_readme():
    """Main function to update README.md."""
    if not README_PATH.exists():
        print(f"Error: {README_PATH} does not exist.")
        return

    experiments = scan_experiments(REPO_ROOT)
    exp_count = len(experiments)
    table_block = generate_table(experiments)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace EXPERIMENTS TABLE section
    exp_table_pattern = r"(<!-- EXPERIMENTS_TABLE_START -->)(.*?)(<!-- EXPERIMENTS_TABLE_END -->)"
    if re.search(exp_table_pattern, content, flags=re.DOTALL):
        content = re.sub(
            exp_table_pattern,
            f"\\1\n{table_block}\n\\3",
            content,
            flags=re.DOTALL
        )
    else:
        content += f"\n<!-- EXPERIMENTS_TABLE_START -->\n{table_block}\n<!-- EXPERIMENTS_TABLE_END -->\n"

    # Also update count badge if present
    badge_pattern = r"(https://img\.shields\.io/badge/Experiments-)(\d+)(_Completed-success\?style=for-the-badge)"
    content = re.sub(badge_pattern, f"\\g<1>{exp_count}\\g<3>", content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated README.md with {exp_count} experiments.")


if __name__ == "__main__":
    update_readme()
