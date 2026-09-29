#!/usr/bin/env python3
"""
update_readme.py

Automated script for Computer Networks Lab repository:
1. Scans root directory for experiment folders (Exp-01 to Exp-10).
2. Generates direct clickable download links for each experiment.
3. Formats table showing only Experiment Number and Experiment Title (clickable for download).
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

# Official Experiment Index (Names)
EXPERIMENT_NAMES = {
    "01": "Design and Configure a Simple Network Topology using Cisco Packet Tracer",
    "02": "Configure Different Network Topologies using Cisco Packet Tracer",
    "03": "Case Study of Networking Devices",
    "04": "Implementation of Framing Methods – Bit Stuffing",
    "05": "Implementation of Error Correction Code",
    "06": "Implementation of Stop-and-Wait Protocol",
    "07": "Implementation of Error Detection Code",
    "08": "Implementation of C Program for IP Address Calculation",
    "09": "Configuration of DHCP Server using Cisco Packet Tracer",
    "10": "Simulation of FTP Working using Cisco Packet Tracer",
    "11": "Simulation of ARP Working using Cisco Packet Tracer",
}


def natural_sort_key(s):
    """Sort strings containing numbers naturally (e.g. Exp-01, Exp-02, Exp-10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", str(s))]


def clean_title_from_folder(folder_name: str, item_num: str) -> str:
    """Format folder name into a clean title, preferring official index."""
    if item_num in EXPERIMENT_NAMES:
        return EXPERIMENT_NAMES[item_num]
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

        title = EXPERIMENT_NAMES.get(num_display, clean_title_from_folder(folder_name, num_display))

        # Check for sender and receiver files
        senders = [c for c in cpp_files if "sender" in c.lower()]
        receivers = [c for c in cpp_files if "receiver" in c.lower()]
        other_cpp = [c for c in cpp_files if c not in senders and c not in receivers]

        # Construct clickable download entry
        if pkt_files:
            download_url = f"{RAW_BASE_URL}/{folder_name}/{pkt_files[0]}"
            exp_entry = f"[{title}]({download_url})"
        elif senders and receivers:
            s_url = f"{RAW_BASE_URL}/{folder_name}/{senders[0]}"
            r_url = f"{RAW_BASE_URL}/{folder_name}/{receivers[0]}"
            exp_entry = f"{title} — [📥 Sender]({s_url}) • [📥 Receiver]({r_url})"
        elif other_cpp:
            c_url = f"{RAW_BASE_URL}/{folder_name}/{other_cpp[0]}"
            exp_entry = f"[{title}]({c_url})"
        elif md_files:
            m_url = f"{folder_name}/{md_files[0]}"
            exp_entry = f"[{title}]({m_url})"
        else:
            exp_entry = title

        experiments.append({
            "num": num_display,
            "code": item_code,
            "folder_name": folder_name,
            "entry": exp_entry,
        })

    experiments.sort(key=lambda x: natural_sort_key(x["code"]))
    return experiments


def generate_table(experiments) -> str:
    """Generate minimal markdown table with experiment number and clickable download link."""
    if not experiments:
        return "*No experiments found.*"

    table_lines = [
        "| # | Experiment |",
        "| :---: | :--- |"
    ]

    for exp in experiments:
        num = exp["num"]
        entry = exp["entry"]
        table_lines.append(f"| **{num}** | {entry} |")

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

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated README.md with {exp_count} experiments.")


if __name__ == "__main__":
    update_readme()
