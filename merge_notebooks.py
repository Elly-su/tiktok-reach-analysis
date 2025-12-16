"""
Merge Jupyter Notebooks into one comprehensive analysis notebook
"""
import json
import os

# Paths
notebook_dir = r'c:\Users\ellio\Tiktok Reach Analysis Project\notebooks'
part_files = [
    'tiktok_analysis_part1.ipynb',
    'tiktok_analysis_part2.ipynb',
    'tiktok_analysis_part3.ipynb'
]
output_file = os.path.join(notebook_dir, 'tiktok_reach_analysis.ipynb')

# Initialize merged notebook
merged_notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.11.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

# Merge notebooks
for part_file in part_files:
    part_path = os.path.join(notebook_dir, part_file)
    if os.path.exists(part_path):
        with open(part_path, 'r', encoding='utf-8') as f:
            part_notebook = json.load(f)
            merged_notebook["cells"].extend(part_notebook["cells"])
        print(f'Merged: {part_file}')

# Save merged notebook
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_notebook, f, indent=1)

print(f'\nMerged notebook saved to: {output_file}')
print(f'Total cells: {len(merged_notebook["cells"])}')
