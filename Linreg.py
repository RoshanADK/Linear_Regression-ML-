# THIS IS PERFECTLY WORKING LINEAR REGRESSION Example , You may modify the Table content and find out !
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#inporting the numpy library
from numpy import *

def error_computation(b,m,points):
    #initize it at 0
    totalError = 0 #(COST FUNCTION ho kya)
    #for every point from in the excel files
    for i in range(0, len(points)):
        # get the x values from table
        x = points[i,0]
        #get the y values from table i.e second column
        y = points[i,1]
        #get the difference, square it and add it to the total
        totalError += (y - (m * x + b)) **2  #Squaring the differences
    #get the Average
    return totalError / float(len(points))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def gradient_descent_runner(points,starting_b,starting_m,learning_rate,num_iterations):
    #starting b and m
    b = starting_b
    m = starting_m

    #Gradient Descent
    for i in range(num_iterations):
        #update b and m with new more accurate b and m by performing this gradient descent
        b, m = step_gradient(b, m, array(points),learning_rate)
    return [b,m]


# Brace Yourselves -->> THE  Gradient Descent comes here
def step_gradient(b_current,m_current,points,learningRate):

    #start points for our gradients
    b_gradient= 0    
    m_gradient= 0

    N  = float(len(points))
    for i in range(0, len(points)):
        x= points[i,0]
        y= points[i,1]
        #direction WRT b and m
        #computing partial derivatives of our error function  with respect to x and y (That's calculus if you don't know)
        m_gradient += - x * (y - (m_current * x + b_current))
        b_gradient += - (y - (m_current * x + b_current))
    #update our b and m values using partial derivatives
    new_b = b_current - (learningRate * (2 / N * b_gradient))
    new_m = m_current - (learningRate * (2 / N * m_gradient))
    return [new_b, new_m]



def start_execution():

    #step1 - collecting data
    points = genfromtxt('data.csv',delimiter=',')        #comma separated values
    #step2 - define our hyper-parameters(alpha,m(slope)etc.)
    #Alpha is learning rate i.e how fast should  model converge ?
    learning_rate = 0.0001
    #slope haru y = mx+b assign garne
    init_b = 0
    init_m = 0  # SLOPE
    num_iterations = 100 # How many time you wanna run ; depends on dataSize


    #step 3 - Lets train our model
    print('Starting GD\nb ={0}\nm ={1}\nerror ={2}\n'.format(init_b,init_m, error_computation(init_b,init_m,points)))
    print("Running...")
    [b, m] = gradient_descent_runner(points,init_b,init_m,learning_rate,num_iterations)
    print("After {0} iterations\nb = {1}\nm = {2}\nerror = {3}\n".format(num_iterations, b, m, error_computation(b, m, points)))
    x = int(input("Enter the value of X ?\n"))
    answer = m*x + b
    print(answer)
    
# Python suru ma jaile main khojchha tei vara lekheko ho hai 
if __name__ == '__main__':
    start_execution()
