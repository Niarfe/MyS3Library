default:
	cat makefile


convert:
	audioconvert --verbose convert yt_music_shelf yt_music_shelf_mp4 --output-format .mp4

update:
	git pull
	do/get_downloads
	do/sync
	do/update_library
	git diff library
	wc -l library

clean_fluff:
	rm -rf `find . -name __pycache__`
	find . -name __pycache__ || true

full: clean_fluff auto_update
