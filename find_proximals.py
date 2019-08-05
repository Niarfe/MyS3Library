import difflib


def distance(_s1, _s2):
    result =  round(difflib.SequenceMatcher(None, _s1, _s2, False).ratio(), 2)
    return str(result) if result > 0.75 else " "


with open('library', 'r') as source:
    books = [book.strip() for book in source] 

books = books[:100]

matrix = [[distance(book1, book2) for book2 in books] for book1 in books]

with open('matrix.csv', 'w') as target:
    for idx, row in enumerate(matrix):
        print(idx)
        target.write(",".join(row)+"\n")
        
    

    
    
    
