"""Write the one-word entry to entry.txt in the output directory.

Standard library only. The output directory is MAKEFUN_OUTPUT_DIR when set
and non-empty, otherwise /output. Output is deterministic UTF-8.
"""

import os

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_TEXT = "Bottleneck\n"

output_dir = os.environ.get(OUTPUT_DIR_ENV) or DEFAULT_OUTPUT_DIR
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY_TEXT)
