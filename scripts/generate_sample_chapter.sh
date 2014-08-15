#!/bin/bash

cat book/working-through-a-side-project.md | grep -i -v "^title:\|^date:\|category:\|^tags:\|^slug:\|^author:\|^summary:"  | pandoc -s -f markdown_mmd --include-before-body=book/title-page.tex -o book-output/sample-chapter.tex -V geometry:margin=1.5in
