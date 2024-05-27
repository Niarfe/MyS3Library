default:
	@cat default | grep -E "^.*:\s.*#"

get:
	wget --no-clobber https://www.gutenberg.org/cache/epub/${ID}/pg${ID}.txt
	head -n 1 pg${ID}.txt

titles:
	bash get_titles.sh

guten.md:
	bash sanitize.sh
	bash get_titles.sh >> guten.md

