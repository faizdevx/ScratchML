# theory 

so why logistic regression came in place eventually there is a datset that came in classification form which is not considered and compatible for linear regression hence that  was drawback of lr or mlr so that why we came with concept of logistic regression 

logistic regrression is type of regression model in which we use sigmoid function 

which gives output between 0 and 1 

we input linear equation only 

but its under 

1/(1-e**(mx+c))

here also going to find best m and c such that it fits best the data 

hence we need an loss function for that also therefore we go for a binary entropy loss function 

as if we take a example 

like classifing if a particular mail is ai generated or not 

so its like 

mail ai generated is x feature where

y is output which is yes or no (0,1)

hence we first input the dataset then plot them on graph then normalise if lot of features in it 

then we use the sigmoid function 

for example 

we randomly take m,c as 3,4 

and then it will got the input 

for first data x1 and find y predicted 

y between 0 and 1 

then if 0.5> then yes if <0.5 then no 

for imporoving and making it regression model we use 

loss entropy function 

j=1/nsum of all (yreallogypred + (1-yreal)log(1-ypred))

then we differentiate it and get the best m,c for it 
m=m-learing*(derivate of it )

c=c-learning*(deri of it)

then we got best function and if 0.5> and 0.5< then accd to

we do it 


