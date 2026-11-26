#!/usr/bin/env python3
"""One Line, One Laugh entry: writes a single funny line to /output/entry.txt."""
import os

LINE = 'The fridge texted me at 2 a.m.: "You ate the leftovers. I saw everything. The yogurt is next."'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
