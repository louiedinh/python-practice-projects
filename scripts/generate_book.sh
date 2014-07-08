#!/bin/bash

# -f for from, -s for smart, -o for out, --chapters to set top level headers to chapters, -V to set equal margins.
cat book/*.md content/pages/*.md | pandoc -s -f markdown_mmd -o book-output/book.pdf --chapters --toc -V geometry:margin=1.5in
