#!/usr/bin/env python3

"""
Checks for broken internal links in markdown files.
Skips _site/, .git/, and _includes/ directories.
Skips external URLs, anchors, Liquid tags, and image/HTML file links.

Usage: python3 check-links.py [directory]
  Default directory is the current working directory.
"""

import os
import re
import sys
import glob

def check_links(root_dir="."):
    broken = []
    link_pattern = re.compile(r'(?:\]\(|href=")([^")\s#]+)')
    skip_prefixes = ("http", "mailto:", "{%", "{{", "#")
    skip_extensions = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".html")
    skip_dirs = {"_site", ".git", "_includes"}

    for md in glob.glob(os.path.join(root_dir, "**/*.md"), recursive=True):
        rel = os.path.relpath(md, root_dir)
        if any(rel.startswith(d + os.sep) or rel.startswith(d + "/") for d in skip_dirs):
            continue

        dir_path = os.path.dirname(md)
        with open(md) as f:
            for line_num, line in enumerate(f, 1):
                for m in link_pattern.finditer(line):
                    target = m.group(1)

                    if target.startswith(skip_prefixes):
                        continue
                    if target.endswith(skip_extensions):
                        continue

                    resolved = os.path.normpath(
                        os.path.join(dir_path, target.rstrip("/"))
                    )
                    exists = (
                        os.path.exists(resolved)
                        or os.path.exists(resolved + ".md")
                        or (
                            os.path.isdir(resolved)
                            and os.path.exists(
                                os.path.join(resolved, "index.md")
                            )
                        )
                    )
                    if not exists:
                        broken.append((rel, line_num, target, resolved))

    if broken:
        for rel, line_num, target, resolved in sorted(broken):
            print(f"  {rel}:{line_num}: {target}")
        print(f"\n{len(broken)} broken link(s) found.")
        return 1
    else:
        print("No broken links found.")
        return 0

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(check_links(root))
