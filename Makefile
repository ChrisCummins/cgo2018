.PHONY: all, run, help, push, publish

all:
	bundle install
	bundle exec jekyll build --drafts

run:
	sleep 2 && open http://localhost:5000/cgo2018/ &
	bundle exec jekyll serve --drafts --host=0.0.0.0

push publish:
	cd _site && rsync -avh . $$CGO/
	sleep 2 && open http://cgo.org/cgo2018/

help:
	@echo "usage: make {all,run,push}"
	@echo
	@echo "   all                 build site"
	@echo "   run                 build and serve site on http://localhost:5000"
	@echo "   push                deploy built site to cgo.org"
