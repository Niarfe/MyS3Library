import pandas as pd
import sys

source_path = 'output/keywords_listing.csv'

df = pd.read_csv(source_path)

base, confidence, signal = None, None, None
if len(sys.argv) < 4:
    print("search_match.py base:word1,word2,word3 confidence:20 signal:5")
    sys.exit(0)
else:
    for arg in sys.argv[1:]:
        print("ARG:", arg)
        key, val = arg.split(':')
        if key == 'confidence': confidence = int(val)
        if key == 'signal': signal = int(val)
        if key == 'base': base = set(val.split(','))

df = df[df['keywords'].apply(
    lambda x: True if len(set(str(x).split()[:confidence]).intersection(base)) >= signal else False)]

print(df.head(20))
