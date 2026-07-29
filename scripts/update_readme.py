#!/usr/bin/env python3
"""
update_readme.py

Automated script for Computer Networks Lab repository:
1. Scans root directory for experiment folders (e.g. Exp-01_..., Exp-02_...).
2. Extracts .pkt file and creates direct download button.
3. Automatically removes any accidental sub-README or report files inside experiment folders.
4. Updates README.md table with experiments and direct download buttons only.
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

# Known Titles for nicer formatting (fallback to folder name)
KNOWN_TITLES = {
    "1": "Basic Local Network Setup & PC Configuration",
    "01": "Basic Local Network Setup & PC Configuration",
    "2": "Network Topologies (Bus, Star, Ring & Mesh)",
    "02": "Network Topologies (Bus, Star, Ring & Mesh)",
}


def natural_sort_key(s):
    """Sort strings containing numbers naturally (e.g. Exp-01, Exp-02, Exp-10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", str(s))]


def clean_title_from_folder(folder_name: str, item_num: str) -> str:
    """Format folder name into a clean title (e.g. Exp-01_Basic_Local_Network -> Basic Local Network)."""
    if item_num in KNOWN_TITLES:
        return KNOWN_TITLES[item_num]
    
    cleaned = re.sub(r"^(Exp|Experiment|Lab)[\s\-_]*\d+[\s\-_]*", "", folder_name, flags=re.IGNORECASE)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned if cleaned else folder_name


def scan_experiments(root_dir: Path):
    """Scan root directory for experiment folders containing .pkt files."""
    experiments = []

    # Ignored directories
    ignored = {".git", ".github", "scripts", "__pycache__"}

    for entry in root_dir.iterdir():
        if not entry.is_dir() or entry.name in ignored or entry.name.startswith("."):
            continue

        # Look for .pkt file
        pkt_file = next((f.name for f in entry.iterdir() if f.is_file() and f.suffix.lower() == ".pkt"), None)
        
        # Clean up any sub-README.md or unwanted report/image files in experiment folders
        for unwanted in entry.iterdir():
            if unwanted.is_file() and unwanted.suffix.lower() != ".pkt":
                try:
                    unwanted.unlink()
                    print(f"[-] Removed extraneous file: {entry.name}/{unwanted.name}")
                except Exception as e:
                    print(f"[!] Warning: could not delete {unwanted}: {e}")

        # Check if folder starts with Exp or contains .pkt
        is_exp = bool(re.match(r"^(Exp|Experiment)", entry.name, re.IGNORECASE)) or (pkt_file is not None)
        if not is_exp:
            continue

        folder_name = entry.name
        match = re.search(r"(\d+)", folder_name)
        item_num = match.group(1) if match else "0"
        item_code = f"Exp-{int(item_num):02d}" if item_num.isdigit() else folder_name
        num_display = f"{int(item_num):02d}" if item_num.isdigit() else item_num

        title = clean_title_from_folder(folder_name, item_num)
        raw_pkt_url = f"{RAW_BASE_URL}/{folder_name}/{pkt_file}" if pkt_file else None

        experiments.append({
            "num": num_display,
            "code": item_code,
            "folder_name": folder_name,
            "title": title,
            "pkt_file": pkt_file,
            "raw_pkt_url": raw_pkt_url,
        })

    experiments.sort(key=lambda x: natural_sort_key(x["code"]))
    return experiments


def generate_table(experiments) -> str:
    """Generate simple markdown table with experiment and download button."""
    if not experiments:
        return "*No experiments found. Add folders like `Exp-01_Title` containing a `.pkt` file.*"

    table_lines = [
        "| # | Experiment | Download |",
        "| :---: | :--- | :---: |"
    ]

    for exp in experiments:
        num = exp["num"]
        title = exp["title"]
        raw_pkt_url = exp["raw_pkt_url"]

        if raw_pkt_url:
            download_btn = f"[![Download .pkt](https://img.shields.io/badge/📥_Download-.pkt-005073?style=for-the-badge&logo=cisco&logoColor=white)]({raw_pkt_url})"
        else:
            download_btn = "*(No .pkt file)*"

        table_lines.append(f"| **{num}** | **{title}** | {download_btn} |")

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
        # If marker not found, append
        content += f"\n<!-- EXPERIMENTS_TABLE_START -->\n{table_block}\n<!-- EXPERIMENTS_TABLE_END -->\n"

    # Also update count badge if present
    badge_pattern = r"(https://img\.shields\.io/badge/Experiments-)(\d+)(_Completed-success\?style=for-the-badge)"
    content = re.sub(badge_pattern, f"\\g<1>{exp_count}\\g<3>", content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated README.md with {exp_count} experiments.")


if __name__ == "__main__":
    update_readme()
