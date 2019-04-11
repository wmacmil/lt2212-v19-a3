#!/usr/bin/bash

python3 read.py -P 0 -N 4 -S 0 -E 400 brown_rga.txt g0.csv t0.csv
python3 train.py g0.csv m0

python3 read.py -P 1 -N 4 -S 0 -E 400 brown_rga.txt g1.csv t1.csv
python3 train.py g1.csv m1


python3 read.py -P 0 -N 4 -S 0 -E 800 brown_rga.txt g00.csv t00.csv
python3 train.py g00.csv m00

python3 read.py -P 1 -N 4 -S 0 -E 800 brown_rga.txt g11.csv t11.csv
python3 train.py g11.csv m11

python3 test.py t0.csv m0
python3 test.py t1.csv m1
python3 test.py t00.csv m00
python3 test.py t11.csv m11

# echo Hello World!
# ls
# echo You
# ls

