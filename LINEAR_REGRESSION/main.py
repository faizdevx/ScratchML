# install library pandas numpy matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# intro reading and visualizing

data=pd.read_csv('cgpa.csv')
"""
plt.scatter(data['CGPA'], data['Package_LPA'])
plt.xlabel('CGPA')
plt.ylabel('Salary')
plt.title('CGPA vs Salary')
plt.show()
"""
# functions 

def loss_function(m,b,points):
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].CGPA
        y=points.iloc[i].Package_LPA
       
        total_error += (y - (m*x + b))**2

    return total_error / float(len(points))

# not gonna use it though as we have to minimize it 

def gradient_descent(m_now,b_now,points,learning_rate):
    m_gradient = 0
    b_gradient = 0
    N = float(len(points))

    for i in range(len(points)):
        x = points.iloc[i].CGPA
        y = points.iloc[i].Package_LPA

        m_gradient += -(2/N) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/N) * (y - (m_now * x + b_now))

    new_m = m_now - (learning_rate * m_gradient)
    new_b = b_now - (learning_rate * b_gradient)

    return new_m, new_b

# here n is the number of iterations we want to run epoche

m=0
b=0
learning_rate = 0.0001
epoche = 1000

for i in range(epoche):
    if i % 100 == 0:
        print(f"Epoch {i}: Loss = {loss_function(m, b, data)}")
    m, b = gradient_descent(m, b, data, learning_rate)
   
print(m,b)

plt.scatter(data['CGPA'], data['Package_LPA'],color='blue')

plt.plot(list(range(15)), [m*x + b for x in range(15)], color='red')


plt.show()

# use are not using the loss function here but it is just to show how it works