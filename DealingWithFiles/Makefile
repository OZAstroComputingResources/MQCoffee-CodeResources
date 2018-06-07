OPEN=xdg-open
START_SERVER=python3 -m http.server

OUT_FORMAT=revealjs
IN_FORMAT=markdown+yaml_metadata_block
OUTPUT=talk.html
BEAMER_ARGS=--latex-engine=xelatex
REVEALJS_VERSION=3.6.0
REVEALJS_URL=https://github.com/hakimel/reveal.js/archive/$(REVEALJS_VERSION).tar.gz
REVEALJS_FILE=revealjs.tar.gz
REVEALJS_DIR=reveal.js
REVEALJS_UNTARED_DIR=$(REVEALJS_DIR)-$(REVEALJS_VERSION)
PRES_URL=http://localhost:8000/$(OUTPUT)

.PHONY: all clean download_revealjs

all: $(OUTPUT)

$(OUTPUT): outline.md
	pandoc $< --output=$@ --from=$(IN_FORMAT) --to=$(OUT_FORMAT) --standalone

download_revealjs: remove_revealjs
	wget $(REVEALJS_URL) -O $(REVEALJS_FILE)
	tar -xf $(REVEALJS_FILE)
	mv $(REVEALJS_UNTARED_DIR) $(REVEALJS_DIR)
	rm -f $(REVEALJS_FILE)

remove_revealjs:
	rm -rf $(REVEALJS_DIR)

clean:
	rm -f $(OUTPUT)

start_server:
	$(START_SERVER) &

view: all start_server
	$(OPEN) $(PRES_URL)

