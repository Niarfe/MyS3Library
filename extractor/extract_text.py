"""
Extract text from a pdf.  Pass in the name of a file and text content
will be sent to console
"""
import PyPDF2
import json
import re

def extract_text(filename):
    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    return {idx:pageObj.extractText() for idx,  pageObj in enumerate([pdfReader.getPage(pagenum) for pagenum in range(pdfReader.numPages)])}

def flatten_text(page_text):
    return re.sub(r'\s+', ' ', page_text)


def write_as_json_file(d_pages, filename):
    with open(filename.replace('.pdf', '.json'), 'w') as target:
        for page, text in d_pages.items():
            target.write(json.dumps({page:text}))
            target.write("\n")

def main(source_file_path):
    pages = extract_text(source_file_path)
    write_to_json_file(pages, source_file_path)

if __name__ == "__main__":
    import argparse as arg
    parser = arg.ArgumentParser(description='Pdf text extractor')
    parser.add_argument('--source', dest="source", type=str, required=True)
    args = parser.parse_args()

    main(args.source)

    print("Done converting {}".format(args.source))


