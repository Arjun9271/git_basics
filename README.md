quora question pair similarity

basically we are trying to solve the duplicate questions >>>

for suppose quora already having a question and their answers also ,,..
some other user came and posted a question which was very similar to previous in sach case <>>
we can map those answers to this...instead of again the users answering same kind of one ...we merge it >


we will map this problem into a binary classification problem>

where if q1 and q2 are similar then we classify it as 1
      if q1 and q3 are disimilar we classify it as 0

but there was a problem in this cases,we were not sure how much confidence questions are these similar <> we cannot make decisions how much sure the model predicting just based on class1 and class0,so to simply that we go with the probability scores ><> according to business cases instead of going always with the model,we can have a visibility by changing the threshold we can achieve good scores


and since we were using probability scores here ,the log-loss going to be best metric <>>> high probability values will have lower log-logss

if we have been given the time, we would have done the time based splitting ,,,in real world we do like that only,the questions getting changes over period of time.


we will do some feature engineering stuff,where we can create some features based on the research, we featurize the vectors by using methods like tfidf -weigheted word2vec this for text data,there are some feature ratios created by research


then we going to start with modelling ....before starting with our real ml models,we starts with a random model ,where to check the worst case in log-loss.
we know in the log-loss the minimum value is zero and maximum is inf,with the help of this dumb model we gets to know whats the worst case.

for example our random model given a value of 0.88

then the interpretation was like follows :  if any trained ml models log-loss was more than 0.88 or near to it ,its an worst model
the more it was was nearer to zero,it was a good model

When you use SGDClassifier(loss='hinge'), you cannot directly call .predict_proba(). To get probabilities and calculate Log-Loss, you have to wrap it in CalibratedClassifierCV. This calibrates the outputs into probabilities, allowing you to compute the Log-Loss.


so we tried the models : sgd classifier with the log-loss : basically a logistic regression 
then sgd classifier with the hinge loss its a linear svm 
then finally we tried with the xgboost <> since its ensemble based where its differ from sgd implementation than previous

comparing to all these 3 ,the xgboost the log-loss came almost near to 0.35 



