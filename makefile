default:
	cat makefile


convert:
	audioconvert --verbose convert yt_music_shelf yt_music_shelf_mp4 --output-format .mp4

audo_update:
	git pull
	do/get_downloads
	do/sync
	do/update_library
	git diff library
	wc -l library
