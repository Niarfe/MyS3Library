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
import pandas as pd
csv.field_size_limit(sys.maxsize)


def create_nodes(path_content, ndic, back):
    df = pd.read_csv(path_content)

    for idx, row in enumerate(df.itertuples()):
        words = str(row.content).split()
        print(words[:10])
        ndic[idx] = Node([words], row.name)
        back.merge(ndic[idx])
    return df

def generate_keywords(df, ndic, back):
    #df['keywords'] = ''
    print(df.columns)
    df['keywords'] = df.apply(lambda row: " ".join(ndic[row['id']].create_profile(back, ratio=0.2)), axis=1)
    #for idx, row in enumerate(df.itertuples()):
    #    profile = ndic[idx].create_profile(back, ratio=0.2)
    #    print(profile[:5])
    #    row['keywords'] = " ".join(profile)

    #print(df['keywords'].head(10))
    return df

if __name__ == "__main__":

    _source_file = 'output/content.csv'
    _ratio = 0.2
    print("load_both from background and nodes from {}".format(_source_file))
    ndic = {}
    back = Node()
    df = create_nodes(_source_file, ndic, back)
    print("done loading, start keyword extraction for {} nodes".format(len(ndic)))
   
    df = generate_keywords(df, ndic, back)
    df.to_csv('output/keywords_listing.csv')
    #with open('output/keywords_listing.csv', 'w') as target:
    #    target.write("id,name,keywords\n")
    #    for idx, node in ndic.items():
    #        print(idx, node.name)
    #        target.write("{},{},{}\n".format(
    #            idx, node.name, " ".join(node.create_profile(back, ratio=_ratio))
    #            )
    #        )
