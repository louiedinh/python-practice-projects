#!/bin/bash

input_filenames=""
for chapter in `cat book/chapters.txt`
do
    input_filenames+="book/$chapter "
done

# -f for from, -s for smart, -o for out, --chapters to set top level headers to chapters, -V to set equal margins.
cat $input_filenames \
    | grep -i -v "^title:\|^date:\|category:\|^tags:\|^slug:\|^author:\|^summary:" \
    | pandoc -s -f markdown_mmd -o book-output/book.pdf --chapters --toc -V geometry:margin=1.5in
