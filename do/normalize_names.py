
import os
import re

bs = 'bookshelf/'
for fname in os.listdir('bookshelf/'):
    print(fname)
    os.rename(bs+fname, bs+re.sub(r'[\',\(\)\s]', '_', fname))

print("\nDone with normalization\n")
