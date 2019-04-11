import os, sys
import glob
import argparse
import numpy as np
import pandas as pd
import math

parser = argparse.ArgumentParser(description="Convert text to features")
parser.add_argument("-P", "--pos", metavar="P", dest="pos", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                                    default=0,
                                                                                    help="What line of the input data file to start from. Default is 0, the first line.")
parser.add_argument("-E", "--end", metavar="E", dest="endline",
                                    type=int, default=None,
                                                                                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
parser.add_argument("inputfile", type=str,
                                    help="The file name containing the text data.")
parser.add_argument("outputfile", type=str,
                                    help="The name of the output file for the feature table.")
parser.add_argument("outputtest", type=str,
                                    help="The name of the output file for the test data.")

args = parser.parse_args()
 
def read_lines(path,l1 = 0,l2 = 1):
    with open(path) as train_file:
        rd = train_file.readlines()
        if l2 == 1:
            l2 = len(rd)
    return rd[l1:l2]

# repeat something mtimes in a list
def mtimes(x,m):
    return [x for i in range(m)]

def ngrams(xs,m):
    xs = mtimes('<start>',m) + xs
    return [xs[(n-(m-1)):(n+1)] for n in range(len(xs))][(m):]

# make a dictionary of all unique words in a corpus
def makeDict(xs):
    newD = []
    for x in xs:
        if x not in newD:
            newD.append(x)
    return newD

# vectorize :: [Str] -> {0,1} -> [Str]
# d = [words with pos]
def vectorize(d,zero_or_one):
    return [x.split('/',1)[zero_or_one] for x in d] 

# dict_map :: [String] -> Dict (String:ndarray)
def dict_map(ds):
    set_ds = set(ds)
    l = len(set_ds)
    values = np.identity(l)
    return dict(zip(set_ds, values))

# foldr :: a -> b -> [a] -> a -> b
def foldr(f,xs,z):
    acc = z
    for x in xs:
        acc = f(acc,x)
    return acc

# basically just rename of np.concatenate
def npc(x,y):
    return np.concatenate((x,y))

# empty array, identity element for fold
ea = np.ndarray([0])

# ngram_to_stuff :: Dict -> N-Gram -> (ndarray,String)
def ngram_to_stuff(d,ng):
    lv = ng[:-1]
    xy = [d[x] if x in d else d['<unk>'] for x in lv]
    w = ng[-1]
    if w not in d:
        w = '<unk>'
    one_hots = foldr(npc,xy,ea).tolist()
    one_hots.append(w)
    return one_hots

def concat_and_pair(d,ngs):
    return [ngram_to_stuff(d,ng) for ng in ngs]

def cc(x,y):
    return x + y


# variable names
# zoo == zeroorone
zoo = args.pos
path0 = args.inputfile
path1 = args.outputfile
test = args.outputtest
param1 = args.startline
param2 = args.endline
ng_param = args.ngram
 
b = read_lines(path0,param1,param2)
a = "<unk>/<unk> <start>/<start> " + foldr(cc,b,"")
# a = "<unk> <start> " + foldr(cc,b,"")
my_dict = makeDict(a.split())
sd2 = vectorize(my_dict,zoo)
vc = dict_map(sd2)

def one_two(xs):
    one = [x[:-1] for x in xs]
    two = [x[-1] for x in xs]
    return one, two

def imperative_data(t1,t2):
    test_lines = read_lines(path0,t1,t2)
    test_lines[0] = "<unk>/<unk> " + test_lines[0]
    # test_lines[0] = "<unk>/<unk> " + test_lines[0]
    test_tokens = [x.split() for x in test_lines]
    del_pos_test_tokens = [vectorize(y,zoo) for y in test_tokens]
    test_ngrams = [ngrams(x,ng_param) for x in del_pos_test_tokens]
    feature_ngram_sents = [concat_and_pair(vc,x) for x in test_ngrams]
    feature_ngram_test_corpus = foldr(cc,feature_ngram_sents,[])
    fl = one_two(feature_ngram_test_corpus)
    return fl[0] , fl[1], feature_ngram_test_corpus


ex_train1 = imperative_data(param1,param2)

ex_train = ex_train1[2]
df1 = pd.DataFrame(ex_train)
df1.to_csv(path1)

param3 = param2 + 1
test_size = math.ceil((param2 - param1) / 5)
param4 = param3 + test_size

eex_train1 = imperative_data(param3,param4)

eex_train = eex_train1[2]
edf1 = pd.DataFrame(eex_train)
edf1.to_csv(test)

print("Loading data from file {}.".format(args.inputfile))
print("Starting from line {}.".format(args.startline))
if args.endline:
    print("Ending at line {}.".format(args.endline))
else:
    print("Ending at last line of file.")
print("Constructing {}-gram model.".format(args.ngram))
print("Writing table to {}.".format(args.outputfile))

