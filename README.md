# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Warrick Macmillan

## Additional instructions

Note: gendata.py has been renamed to read.py

Included are all the scripts and outputs as originally run, of which the data is summarized in the all* files and below.

Read has an additional boolean parameter, P, indicating whether we are looking at the word or POS.

Hypotheses:  

I took perhaps the most naive perspective with respect to this lab:  

  1. That increasing n-gram size would increase/decrease accuracy and perplexity, respectively
  2. Accurcay and perplexity would be correlated in a bijective way
  3. Increasing corpus training size would decrease/increase perplexity and accuracy, respectively
  4. Training on POS vs. words proper would yield more accurate results 

This naive approach was mostly correct. 

  1. Mostly true: (-P 0 -N 3 -S 0 -E 400) -> (-P 0 -N 3 -S 0 -E 400) saw a decrease in accuracy
  2. Mostly true: (-P [0/1] -N 3 -S 0 -E 800) -> (-P [0/1] -N 4 -S 0 -E 800) saw an increase in both accuracy and perplexity 
  3. We saw monotonic increases in accuracy and decreases perplexity for all results with respect to this hypothesis.
  4. This was the most obviously valid assumption



It is worth noting that while the naive hypothesis was contradicted, the relative changes in accuracy and perplexity were < 5% of the norm of respective values being compared, thus it was nothing drastically noticeable: within a reasonable error bound, I suppose.  

The use of POS yielded significantly better results (around %30 instead of %10) becuase this is a significantly " coarser " view of the language.  However, it is perhaps less informative as well depending on the application, and therefore has less general utility.  

I also found when testing larger corpus sizes (> 3200 lines) that there was some kind of run time error when training the data.  This is something which would need to be inspected and improved as well.

The test data size was 1/5 the training corpus size.  This would be another interesting parameter to investigate for theoretical insight.  

One interesting experiment would be to try this on all types of permutations on the corpus  (with repsect to which lines are included in training) and come up with a distribution of accuracy and perplexity results.  



| -P 0 -N 2 -S 0 -E 400        : | -P 0 -N 2 -S 0 -E 800      : | 
| -----------------------------: | ---------------------------: | 
| Perplexity: 73.44268075795797: | Perplexity: 71.638461700893: | 
| -----------------------------: | ---------------------------: | 
| Accuracy: 0.11524663677130045: | Accuracy: 0.124124124124124: | 
| -----------------------------: | ---------------------------: | 
| -P 0 -N 3 -S 0 -E 400        : | -P 0 -N 3 -S 0 -E 800      : | 
| -----------------------------: | ---------------------------: | 
| Perplexity: 73.56606069442662: | Perplexity: 70.030124258511: | 
| -----------------------------: | ---------------------------: | 
| Accuracy: 0.1210762331838565 : | Accuracy: 0.129129129129129: | 
| -----------------------------: | ---------------------------: | 
| -P 0 -N 4 -S 0 -E 400        : | -P 0 -N 4 -S 0 -E 800      : | 
| -----------------------------: | ---------------------------: | 
| Perplexity: 75.31935736425139: | Perplexity: 70.955276314510: | 
| -----------------------------: | ---------------------------: | 
| Accuracy: 0.11838565022421525: | Accuracy: 0.130130130130130: | 

##

Bonus:


| -P 1 -N 2 -S 0 -E 400          | -P 1 -N 2 -S 0 -E 800          |
| ----------------------------:  | ----------------------------:  |
| Perplexity: 7.74563307397765   | Perplexity: 6.61462930475166   |
| ----------------------------:  | ----------------------------:  |
| Accuracy: 0.284304932735426    | Accuracy: 0.28853853853853856  |
| ----------------------------:  | ----------------------------:  |
| -P 1 -N 3 -S 0 -E 400          | -P 1 -N 3 -S 0 -E 800          |
| ----------------------------:  | ----------------------------:  |
| Perplexity: 7.615118160821453  | Perplexity: 6.37995027623184   |
| ----------------------------:  | ----------------------------:  |
| Accuracy: 0.2905829596412556   | Accuracy: 0.30505505505505504  |
| ----------------------------:  | ----------------------------:  |
| -P 1 -N 4 -S 0 -E 400          | -P 1 -N 4 -S 0 -E 800          |
| ----------------------------:  | ----------------------------:  |
| Perplexity: 7.670867580834537  | Perplexity: 6.4231032697665835 |
| ----------------------------:  | ----------------------------:  |
| Accuracy: 0.29192825112107623  | Accuracy: 0.3123123123123123   |
 
 
 
 



