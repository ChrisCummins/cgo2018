.PHONY: all, run, help, push, publish

all:
	bundle install
	bundle exec jekyll build --drafts

run:
	bundle exec jekyll serve --drafts --host=0.0.0.0

push publish:
	cd _site && rsync -avh . $$CGO/

help:
	@echo "usage: make {all,run,push}"
	@echo
	@echo "   all                 build site"
	@echo "   run                 build and serve site on http://localhost:5000"
	@echo "   push                deploy built site to cgo.org"
