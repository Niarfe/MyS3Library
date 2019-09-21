import os
import re

content_dir = 'content/'

fnames = os.listdir(content_dir)

with open('output/'+'content.csv', 'w') as target:
    target.write("id,name,content\n")
    for idx, fname in enumerate(fnames):
        text = open(content_dir+fname).read()
        alpha_num = re.sub(r'\W+', ' ', text)
        flat_lowercase_text = re.sub(r'\s+', ' ', alpha_num).lower()
        target.write("{},{},{}\n".format(idx, fname.replace('.txt', '.pdf'), flat_lowercase_text.strip().replace('\x00', '')))
        if idx % 100 == 0:
            print("done through ", idx)
