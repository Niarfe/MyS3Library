import os

with open('differs', 'r') as source:
    for line in source:
        # remove it from the library (pdf)
        cmd = "aws s3 rm s3://eolibrary/books/{}".format(line.strip())
        os.system(cmd)

        # remove it from the extracted s3 store (txt)
        cmd = "aws s3 rm s3://eolibrary/extractedbooks/{}".format(line.strip().replace('.pdf', '.txt'))
        os.system(cmd)

        # make sure it's gone
        os.system("aws s3 ls s3://eolibrary/books/ | grep {}".format(line.strip().replace('.pdf', '')))
        os.system("aws s3 ls s3://eolibrary/extractedbooks/ | grep {}".format(line.strip().replace('.pdf', '')))

        # remove it from the local copy of extracted
        os.system("rm extractor/content/{}".format(line.strip().replace('.pdf', '.txt')))
