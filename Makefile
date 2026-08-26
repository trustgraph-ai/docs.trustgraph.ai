
BASE_URL="https://docs.trustgraph.ai/"

serve:
	bundle exec jekyll serve --livereload

build:
	bundle exec jekyll build

reset:
	bundle pristine
	bundle update json

