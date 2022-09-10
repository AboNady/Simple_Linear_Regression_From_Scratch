#Please refer to the README File for the full formulas and explanation

import time #To Calculate the execution time
import numpy as np #To deal with Math
import pandas as pd #To handle the data's part
import matplotlib.pyplot as plt #To Draw

strt = time.time() #Calculate the time


#------------------------------------------------------------


def costfunc(x,y,m,c):    
    pred = m*x + c
    sm = np.sum(    np.power( (pred-y) , 2 )   )
    c =  sm   /    (2 * (x.shape[0]) ) #x.shape[0] is the same len(x)
    return c



#------------------------------------------------------------


def Gradientdes(x,y, m,c, alpha,iters):

    for i in range(iters):
        pred = m*x + c 

        D_m = ( -2 / len(x) ) *  np.sum(  np.multiply(x, (y-pred) )  ) #I used multiply here to do the Element-wise or Hadarmad product
        D_c = ( -2 / len(x) ) *  np.sum(   y.T-pred.T ) 
        
        c = c - (alpha*D_c)
        m = m - (alpha*D_m)
        
        cosf.append( costfunc(x, y, m, c) )
        
    return m,c


#------------------------------------------------------------


#Import the txt file
datas = pd.read_csv(r'C:\Users\NADY\Desktop\datas1.txt', header = None , names=['Xdata','Ydata'] )

# Define the variables Y_pred = mx + x
#I set it to Zero because it heard that it would be better, I do not know what will happen if I cahnged it how this affect
m = 0 #Slope
c = 0 #Intercept 

cosf = [] #An empty list for the cost function, so I can draw the graph of the Cost Function

#We have the data as 97*2, So, I want to choose specific columns 
x = datas.iloc[: , 0]
y = datas.iloc[: , -1] 

#Convert it into a matrix form, so we can handle and multiply it easily 
#NOTE: if did not multiply the data with 0.1 there will be
x = np.matrix(x.values) 
y = np.matrix(y.values) 


#------------------------------------------------------------


alpha = 0.0001 #Step Size
iters = 2000 # Number of iterations

slope, intersect = Gradientdes(x, y,m,c, alpha, iters)

#Xnew is to draw the fit line values, so find the Max and Min Points to draw the line between them as X values
xnew = np.linspace(x.min(), x.max() , 1600)

#The Y of the predicted fit line
f = slope*xnew + intersect

end = time.time()


cosf = 0.01* np.array(cosf) #I multiplied it to have smaller values for the cost function. However, you can skip this step

#------------------------------------------------------------

#Just print the values
print('\nThe Slope value : ', slope)

print('\nThe Intersect value :', intersect)

print('\nThe Cost Function value : ' , cosf[-1])


#------------------------------------------------------------


#Draw the Dataset and The Fit line in the same Graph 
fig, ax = plt.subplots(figsize=(5,5))
#The Fit line
ax.plot(xnew,f, 'r', label='Prediction')
#The Dataset
ax.scatter(np.array(x) ,np.array(y) , label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')


#------------------------------------------------------------


# draw error graph
fig, ax = plt.subplots(figsize=(5,5))
ax.plot( np.arange(iters) , cosf , 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost Value')
ax.set_title('Error vs. Training Epoch')

#------------------------------------------------------------


print('\nThe Excuation time is : ',end-strt,'Second')

