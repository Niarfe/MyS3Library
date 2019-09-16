default:
	cat makefile


extract:
	python extract_text.py --source ../library

content:  output/content.csv
keywords: output/keywords_listing.csv
dupes:    output/dupes.txt
seeit:    output/seeit.csv

######################
output/content.csv:
	bash bin/download_extracted_content.sh
	python bin/create_content_csv.py
	wc -l output/content.csv

output/keywords_listing.csv:
	python bin/loadthem.py # this should take all.csv which has raw text and produce keyword_listings.txt

output/dupes.txt: output/keywords_listing.csv 
	. env/bin/activate; python bin/findupes_with_hydraseq.py output/keywords_listing.csv  10 > output/dupes.txt
	cat output/dupes.txt

output/seeit.csv:  dupes # inspect the contents of keywords arranged, with keywords first, you can sort it to get idea of patterns
	. env/bin/activate; python bin/viewkeys.py output/keywords_listing.csv 100 > output/seeit.csv
	vim output/seeit.csv

clean:
	rm output/*

all: extract content keywords dupes seeit

