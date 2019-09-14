"""
Display contents of keywords set by | keywords (up to number passed in) | title |

Inputs:
    $1:  file name of keyword content.  csv: id,name,keywords
    $2:  int, the number of keywords to grab for display

Output:
    console: comma separated | keywords (up to $2 requested) , title |
"""
import sys
import csv

with open(sys.argv[1], 'r') as source:
    csv_file = csv.DictReader(source)
    for row in csv_file:
        words = row['keywords'].split()
        print("{},{}".format(" ".join(words[:int(sys.argv[2])]), row['name'].strip()))

