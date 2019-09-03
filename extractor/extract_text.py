"""
Extract text from a pdf.  Pass in the name of a file and text content
will be sent to console

NOTE: looks like linux' pdftotxt does a better job
"""
import json
import re
import os


def flatten_text(page_text):
    return re.sub(r'\s+', ' ', page_text)


def write_to_json_file(d_pages, filename):
    with open(filename.replace('.pdf', '.json'), 'w') as target:
        for page, text in d_pages.items():
            target.write(json.dumps({page:text}))
            target.write("\n")


def pdf_to_text(source_file_path):
    cmd = "pdftotext {}".format(source_file_path)
    os.system(cmd)

def get_list_of_extracted_files():
    os.system("aws s3 ls s3://eolibrary/extractedbooks/ > extracted.txt")
    with open('extracted.txt', 'r') as source:
        extracted = [line.replace('.txt', '.pdf').split(' ')[-1].strip() for line in source]
    return extracted

def main(file_list):
    extracted = get_list_of_extracted_files()
    with open(file_list, 'r') as source:
        for idx, fname_raw in enumerate(source):
            fname = fname_raw.strip()
            if not fname.endswith(".pdf"):
                print("\tNOT PDF, skipping: {}".format(fname))
                continue
            if fname in extracted:
                print("\tDEJA_VU {}".format(fname))
                continue
#            deja_vu = os.system("aws s3 ls s3://eolibrary/extractedbooks/{}".format(fname.replace('.pdf', '.txt')))
#            if deja_vu == 0:
#                print("\tDEJA_VU {}".format(fname))
#                continue
            cmds = [
                    "echo == STARTING # {} ===".format(idx),
                    "aws s3 cp s3://eolibrary/books/{} .".format(fname),
                    "pdftotext {}".format(fname),
                    "aws s3 mv {}.txt s3://eolibrary/extractedbooks/".format(fname.replace(".pdf", "")),
                    "rm {}".format(fname),
                    ]
            for cmd in cmds:
                print(cmd)
                os.system(cmd)
            

if __name__ == "__main__":
    import argparse as arg
    parser = arg.ArgumentParser(description='Pdf text extractor')
    parser.add_argument('--source', dest="source", type=str, required=True)
    args = parser.parse_args()

    main(args.source)

    print("Done converting {}".format(args.source))


