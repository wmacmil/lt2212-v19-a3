import os, sys
# import argparse
import numpy as np
import pandas as pd
import pickle
import argparse
from sklearn.linear_model import LogisticRegression


def one_two(xs):
    one = [x[:-1] for x in xs]
    two = [x[-1] for x in xs]
    return one, two

parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str,
                    help="The file name containing the features in the test data.")
parser.add_argument("modelfile", type=str,
                    help="The name of the saved model file.")


args = parser.parse_args()

test_data = args.datafile
model = args.modelfile

# model = "m"
# test_data = "t.csv"

clf = pickle.load(open(model, 'rb'))
# myLogisticFcn = pickle.load(open(model, 'rb'))


df_input1 = pd.read_csv(test_data, index_col=0)
# 'split' : dict like {'index' -> [index], 'columns' -> [columns]
df_input_split1 = df_input1.to_dict('split')
returned_input_data1 = df_input_split1['data']

# ans3 = myLogisticFcn.predict(returned_input_data1)
# calculate accuracy and perplexity below


# so fdsa needs uknowns
xasdf, fdsa  = one_two(returned_input_data1)

answers = clf.predict(xasdf)
anslp = clf.predict_log_proba(xasdf)
classlogprob = list(zip(fdsa,anslp))
# generate class dictionary from model
classes = clf.classes_
enclas = list(enumerate(classes))
d = {key: value for (value, key) in enclas}
# cool, finally works
# things to change : add unks to both the imperative function and the n_grams_stuff function

# heres the error

logProbs = [classlogprob[i][1][d[classlogprob[i][0]]] for i in range(len(classlogprob))]

# # cool, maybe works?
# # perplexity
perp = 2 ** ((-1)/len(logProbs) * sum(logProbs))

acc = clf.score(xasdf,fdsa)
# acc = clf.score(xasdf,asdf[1])

print("Loading data from file {}.".format(args.datafile))
print("Loading model from file {}.".format(args.modelfile))
print("Testing {}-gram model.".format(args.ngram))
print("Perplexity: " + str(perp))
print("Accuracy: " + str(acc))
