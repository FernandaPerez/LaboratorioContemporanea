ls  > tmp.txt
echo "path = $1"
wc -l tmp.txt > ../data.txt
cat tmp.txt >> ../data.txt
