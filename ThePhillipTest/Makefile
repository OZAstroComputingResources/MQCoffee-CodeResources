#### MAIN EXECUTABLES ####
LATEXBUILD=latexmk -xelatex -shell-escape
LATEXCLEAN=latexmk -xelatex -C
OPEN=xdg-open

MAINTEXFILE=thesis_main.tex
OTHERTEXFILES=abstract.tex achievements.tex acknowledgements.tex code.tex conclusion.tex derivation-appendix.tex frontmatter.tex image-appendix.tex introduction.tex results.tex theory.tex thesis_main.tex

BIBTEXFILESLOCATION=bibliography
IMAGELOCATION=images

BIBTEXFILES=$(foreach bibfile,$(shell ls $(BIBTEXFILESLOCATION)),$(BIBTEXFILESLOCATION)/$(bibfile))
SVGIMAGES=$(shell ls $(IMAGELOCATION)/*.svg)
PGFIMAGES=$(shell ls $(IMAGELOCATION)/*.pgf)
PDFIMAGES=$(shell ls $(IMAGELOCATION)/*.pdf)


PNGIMAGES=$(SVGIMAGES:.svg=.png)

TARGETS=$(MAINTEXFILE:.tex=.pdf)

GENERATEDFILES=$(MAINTEXFILE:.tex=.aux) $(MAINTEXFILE:.tex=.log) $(MAINTEXFILE:.tex=.out) $(MAINTEXFILE:.tex=.toc) $(MAINTEXFILE:.tex=.lof) $(MAINTEXFILE:.tex=.lot) $(BIBTEXFILES:.bib=.bbl) $(MAINTEXFILE:.tex=.bbl) $(MAINTEXFILE:.tex=.bcf) $(MAINTEXFILE:.tex=.blg) $(MAINTEXFILE:.tex=.run.xml) $(MAINTEXFILE:.tex=.nav) $(MAINTEXFILE:.tex=.snm) ${MAINTEXFILE:.tex=.thm} ${MAINTEXFILE:.tex=.pyg}


.PHONY: all clean

all: $(TARGETS)

$(TARGETS): $(MAINTEXFILE) $(BIBTEXFILES) $(OTHERTEXFILES) $(PNGIMAGES) $(PGFIMAGES) $(PDFIMAGES)
	$(LATEXBUILD) $(MAINTEXFILE) 

clean:
	$(LATEXCLEAN) $(MAINTEXFILE)
	rm -f $(GENERATEDFILES) *~ scripts/texput.*

$(PNGIMAGES): $(SVGIMAGES)
	$(foreach image,$(SVGIMAGES),inkscape --export-png=$(image:.svg=.png) $(image);)
	
view: all
	$(OPEN) $(TARGETS) &

