#exercise goal
# use numpy functions and numpy matrix/vector operations
#Understand the concept of "broadcasting"
#Be able to vectorize code

#Exercise: Build a function that returns the sigmoid of a real number x. Use math.exp(x) for the exponential function.

#Graded function: basic_sigmoid
import math
import numpy as np

def basic_sigmoid(x):
    """
    compute the sigmoid of x 
    arguments:
    x -- a scalar
    return:
    s==sigmoid(x)
    """
    s=1/(1+math.exp(-x))
    return s

#print("using math:"basic_sigmoid(3))

#array can be used as a vector
#x=np.array([1,2,3])
#print(np.exp(x))
#y=np.array([1,2,3])
#print(y+3)

def sigmoid(x):
    s=1/(1+np.exp(-x))
    return s

def sigmoid_derivative(x):
    s=sigmoid(x)
    ds=s*(1-s)
    return ds
#x=np.array([1,2,3])
#print("sigmoid_derivative(x)="+str(sigmoid_derivative(x)))
#x=np.array([1,2,3])
#print(sigmoid(x))

def image2vector(image):
    v=image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1)
    return v
#get the image data in a matrix and reshape it into a list
image=np.array([
    [
        [ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]
    ],

    [
        [ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]
    ],
    [
        [ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]
    ]
    ])
#print("image2vector(image)="+str(image2vector(image)))
def normalizeRows(x):
#
    x_norm=np.linalg.norm(x,axis=1,keepdims=True)
    print("norm is :"+str(x_norm))
    x=np.divide(x,x_norm)
    return x
x=np.array([
    [0,3,4],
    [1,6,4]
    ])
print("normalizeRows(x)= " +str(normalizeRows(x)))
