
echo "| LANG | FILE | TITLE |"
echo "| --   | --   | --    |"
for text in $(ls texts/)
do
    FNAME=${text}
    TITLE=$(head -n 1 texts/${text}  | sed -E 's/The Project Gutenberg eBook of[[:space:]]+/ /g')
    LANGG=$(head -n 30 texts/${text} | grep 'Language:' | sed -E 's/Language://g' | sed 's/[[:space:]]//g')
    echo "| ${LANGG} | ${FNAME} | ${TITLE#[[:space:]]} |"
done
