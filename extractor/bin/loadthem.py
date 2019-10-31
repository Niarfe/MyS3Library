"""
This script takes a file of extracted text and generates the
theseus 'background' then gets the highest frequency words per book
against the background

Input:
    _source_file: string, path to file containing text content.  csv: id, name, full-text
    _ratio:       float, cutoff angle for keyword filter when comparing a source to background

Output:
    keyword_listing.csv:  file containing keyword output of neurons. csv: id, name, keywords (ranked in order left-right)

"""
from theseus.node import Node
import csv
import sys
csv.field_size_limit(sys.maxsize)



def load_both(path_content):
    print("load both {}".format(path_content))
    docs = []
    ndic = {}
    back = Node()
    def _get_next(iter):
        return next(iter)

    with open(path_content, 'r', encoding='ISO-8859-1') as source:

        j_rows = csv.DictReader(source)
        for idx, row in enumerate(j_rows):
            if len(row) == 3:
                words = row['content']
            elif len(row) > 3:
                print("pop")
                continue
            else:
                raise Exception("batafuco!")
            sidx = row['id']
            name = row['name']
            idx = int(sidx)
            words = words.split()
            # print(idx, name, words)
            if idx % 100 == 0:
                print(idx)

            docs.append(words)
            ndic[idx] = Node([words], name)
            back.merge(ndic[idx])

    return back, ndic



if __name__ == "__main__":

    _source_file = 'output/content.csv'
    _ratio = 0.2
    print("load_both from background and nodes from {}".format(_source_file))
    back, ndic = load_both(_source_file)
    print("done loading, start keyword extraction for {} nodes".format(len(ndic)))
    with open('output/keywords_listing.csv', 'w') as target:
        target.write("id,name,keywords\n")
        for idx, node in ndic.items():
            print(idx, node.name)
            target.write("{},{},{}\n".format(
                idx, node.name, " ".join(node.create_profile(back, ratio=_ratio))
                )
            )
