#!/bin/bash

pandoc -f markdown_mmd -s -o test.epub --toc --chapters *.md
