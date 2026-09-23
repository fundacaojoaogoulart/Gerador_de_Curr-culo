#!/usr/bin/env python3
"""Offline-first lightweight docs validation; optional `mkdocs build --strict`."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

REQUIRED = ['index.md', 'architecture.md', 'data-lineage.md', 'technical-review.md']
LINK = re.compile(r'(?<!!)\[[^]]*\]\(([^)]+)\)')


def validate(repo: Path) -> list[str]:
    issues = []
    docs = repo / 'docs'
    for filename in REQUIRED:
        if not (docs / filename).is_file():
            issues.append(f'missing docs/{filename}')
    if not (repo / 'mkdocs.yml').is_file():
        issues.append('missing mkdocs.yml')
    mapfile = docs / 'documentation-map.json'
    if not mapfile.exists():
        issues.append('missing docs/documentation-map.json')
    else:
        try:
            obj = json.loads(mapfile.read_text(encoding='utf-8'))
            if obj.get('version') != 1 or not isinstance(obj.get('rules'), list) or not obj['rules']:
                issues.append('invalid documentation-map.json version/rules')
        except (ValueError, OSError) as exc:
            issues.append(f'invalid documentation-map.json: {exc}')
    if not docs.is_dir():
        return issues
    for doc in docs.rglob('*.md'):
        if 'site' in doc.relative_to(docs).parts:
            continue
        content = doc.read_text(encoding='utf-8')
        fenced = False
        fence_char = ''
        fence_len = 0
        for lineno, line in enumerate(content.splitlines(), 1):
            match = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', line)
            if match:
                marker = match.group(1)
                if not fenced:
                    fenced, fence_char, fence_len = True, marker[0], len(marker)
                elif marker[0] == fence_char and len(marker) >= fence_len and not match.group(2).strip():
                    fenced = False
            if fenced:
                continue
            for value in LINK.findall(line):
                dest = value.split(' ', 1)[0].strip('<>')
                if not dest or dest.startswith(('https:', 'http:', 'mailto:', '#', 'data:')):
                    continue
                target = (doc.parent / unquote(dest.split('#', 1)[0])).resolve()
                if not target.exists():
                    issues.append(f'{doc.relative_to(repo)}:{lineno}: broken local link {dest}')
        if fenced:
            issues.append(f'{doc.relative_to(repo)}: unclosed code fence')
    return issues


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', default='.')
    ap.add_argument('--build', action='store_true', help='Run mkdocs build --strict (requires mkdocs-material)')
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    issues = validate(repo)
    if args.build:
        if not shutil.which('mkdocs'):
            issues.append('mkdocs executable not installed (install mkdocs-material)')
        elif not issues:
            proc = subprocess.run(['mkdocs', 'build', '--strict'], cwd=repo, capture_output=True, text=True)
            if proc.returncode:
                issues.append(f'mkdocs build failed:\n{proc.stdout}\n{proc.stderr}')
    for issue in issues:
        print('ERROR:', issue)
    print(f"Documentation validation: {'PASS' if not issues else 'FAIL'} ({len(issues)} issue(s))")
    return 1 if issues else 0


if __name__ == '__main__':
    raise SystemExit(main())
