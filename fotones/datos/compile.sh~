cd $1
echo "En..."
pwd

ls  > tmp.txt

wc -l tmp.txt > data.txt
cat tmp.txt >> data.txt

gfortran -c  ../GetNames.f90
gfortran ../practica.f90 ../GetNames.o -o ../programa.exe

rm  tmp.txt
cd ..
