
import os

bs = 'bookshelf/'
for fname in os.listdir('bookshelf/'):
    print(fname)
    os.rename(bs+fname, bs+fname.replace(' ', '_'))

print("\nDone with normalization\n")
