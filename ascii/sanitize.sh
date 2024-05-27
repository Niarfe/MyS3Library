
for text in $(ls texts/)
do
    dos2unix texts/${text}
    tr -d '^M' < texts/${text} 
done
