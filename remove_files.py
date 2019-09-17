import os

with open('differs', 'r') as source:
    for line in source:
        cmd = "aws s3 rm s3://eolibrary/books/{}".format(line.strip())
        os.system(cmd)
        cmd = "aws s3 rm s3://eolibrary/extractedbooks/{}".format(line.strip().replace('.pdf', '.txt'))
        os.system(cmd)
        os.system("aws s3 ls s3://eolibrary/books/ | grep {}".format(line.strip().replace('.pdf', '')))
        os.system("aws s3 ls s3://eolibrary/extractedbooks/ | grep {}".format(line.strip().replace('.pdf', '')))
