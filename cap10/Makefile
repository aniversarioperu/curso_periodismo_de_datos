SRC = $(wildcard *.md)

DOCS = $(SRC:.md=.docx)
PDFS = $(SRC:.md=.pdf)

doc: clean $(DOCS)

pdf: clean $(PDFS)

%.docx: %.md refs.bib
	pandoc -f markdown -V geometry:margin=1in -t docx $< --bibliography=refs.bib -o $@

%.pdf: %.md header.latex refs.bib
	pandoc --latex-engine=xelatex -s -S --template header.latex -f markdown -V geometry:margin=1in $< --bibliography=refs.bib -o $@

	

clean:
	rm -rf *pdf *docx
