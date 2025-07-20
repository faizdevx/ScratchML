# mathematical theory 

so what happen in multiple linear regression is that 


we got the dataset with more then features which are independent and one dependent feature we choose so 
first we select x features in  a matrix or called a vector here it is in for it we have not merged weights with bias hence no ones column we gonna add here 

hence we specify x and y both in mxn for x and y is mx1 and weight is also mx1 hence 

we plot initial line on graph 

then the functions we apply 

1) simple prediction based y=mx+c type y=np.dot(m,x)+c


2) cost function (1/(2*m)) * np.sum((y_pred - y)**2)

3) compute gradient by finding derivative of it

    dj_w = (1/m) * np.dot(X.T, error)     
    dj_b = (1/m) * np.sum(error)

    error=ypred-yreal

4) gradient descent takes X,Y,w,b,learning rate,epoches

  w=w-gradient 
  b=b-gradient 

  we do it til some epoches to find best 

5) run the grad function on our data 
  
   w,b,historyof cost=grad

6) final line 

7) thats it dude


here we got many lines and made a hyperplane of it 