#!/usr/bin/env python3
"""
Dark Moody Amethyst — FilterBlade Save File Fixer
Run this on any save file before loading it into FilterBlade.

Usage:
  python3 fix_savefile.py input.filterBladeSaveFile
  python3 fix_savefile.py input.filterBladeSaveFile output.filterBladeSaveFile
"""

import json
import sys
import os

def fix_savefile(input_path, output_path=None):
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_fixed{ext}"

    with open(input_path, 'r') as f:
        data = json.load(f)

    save_state = json.loads(data['saveStateContent'])
    changes = save_state['changeGroups'][0]['groupChanges']
    before = len(changes)

    # Properties that crash FilterBlade when set to null/false
    bad_props = {
        'SetBackgroundColor', 'SetTextColor', 'SetBorderColor',
        'PlayEffect', 'PlayAlertSound', 'MinimapIcon',
        'UsedEntryStyleCombi'
    }

    filtered = []
    fixed_hex = 0
    fixed_null = 0

    for c in changes:
        cv = c.get('changeValue', {})
        if isinstance(cv, dict):
            nv = cv.get('newValue')
            ident = cv.get('identifier', {})
            if isinstance(ident, dict):
                ident_name = ident.get('identifier', '')
            else:
                ident_name = str(ident)

            # Remove null/false no-ops on known crash-prone properties
            if (nv is None or nv is False) and ident_name in bad_props:
                fixed_null += 1
                continue

            # Fix hex colors to rgb strings
            if isinstance(nv, str) and nv.startswith('#'):
                hex_str = nv.lstrip('#')
                if len(hex_str) == 6:
                    r = int(hex_str[0:2], 16)
                    g = int(hex_str[2:4], 16)
                    b = int(hex_str[4:6], 16)
                    cv['newValue'] = f"rgb({r}, {g}, {b})"
                    fixed_hex += 1

        filtered.append(c)

    after = len(filtered)
    save_state['changeGroups'][0]['groupChanges'] = filtered
    data['saveStateContent'] = json.dumps(save_state)

    with open(output_path, 'w') as f:
        json.dump(data, f)

    print(f"Input:  {input_path} ({before} changes)")
    print(f"Output: {output_path} ({after} changes)")
    print(f"Fixed:  {fixed_hex} hex colors → rgb, {fixed_null} null/false no-ops removed")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    fix_savefile(input_path, output_path)
