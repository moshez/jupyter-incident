#!/bin/sh
set -ex
TALK=incident-management
mkdir -p build
jupyter nbconvert $TALK.ipynb --to markdown \
	--TagRemovePreprocessor.remove_cell_tags='{"no_markdown"}'  \
	--TagRemovePreprocessor.remove_all_outputs_tags='{"no_output"}'  \
	--output build/$TALK.md
pandoc --listings -o build/$TALK.tex build/$TALK.md 
mf beamer --input build/$TALK.tex --outdir build
(cd build && pdflatex talk.tex)
(cd build && pdflatex handout.tex)

