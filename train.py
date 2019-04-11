import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

def one_two(xs):
    one = [x[:-1] for x in xs]
    two = [x[-1] for x in xs]
    return one, two

parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                            help="The file name containing the features.")
parser.add_argument("modelfile", type=str,
                            help="The name of the file to which you write the trained model.")

args = parser.parse_args()

in_path = args.datafile
ng = args.ngram
out_path = args.modelfile

df_input1 = pd.read_csv(in_path, index_col=0)
df_input_split1 = df_input1.to_dict('split')
returned_input_data1 = df_input_split1['data']

X, Y = one_two(returned_input_data1)

clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X,Y)

with open(out_path, 'wb') as file:
    model = pickle.dump(clf, file)
                        
print("Loading data from file {}.".format(args.datafile))
print("Training {}-gram model.".format(args.ngram))
print("Writing table to {}.".format(args.modelfile))

# # testing
# tparam1 = 0
# tparam2 = 10
# asdf = imperative_data(111,113)
# xasdf = asdf[0]
# so it predicts on just the one hot representations
# ans2 = clf.predict(xasdf[:10])
