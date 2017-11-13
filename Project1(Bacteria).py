import numpy as np
import math
import decimal

import matplotlib.pyplot as plt
#---------------------------------FIRST FUNCTION----------------------------------------------------------------------------

def dataLoad(filename):

    with open(filename+".txt") as f:

        new_data=np.array([0,0,0])
        for a_line in f:
            word = a_line.split(' ')
            data = np.array([float(word[0]),float(word[1]),float(word[2])])

            new_data = np.vstack((new_data,data))

    data = new_data

    new_array = np.array([0, 0, 0])
    number_of_rows = data.shape[0]
    for i in range(number_of_rows):
        if data[i][0] < 10 or data[i][0] > 60:
            if  i==0:
                continue

            print("error type: temperature in line", i)
            continue


        if data[i][1] < 0:

            print("error type:  growth rate in line", i)
            continue
        if not (data[i][2]==1 or data[i][2]==2 or data[i][2]==3 or data[i][2]==4):
            print("error type: bacteria type in line",i)
            continue
        else:
            new_array = np.vstack((new_array, data[i]))
    new_array=np.delete(new_array,0,0)
    return new_array
#---------------------------------SECOND FUNCTION----------------------------------------------------------------------------

def dataStatistics(data, statistic):

    if statistic == 'Mean Temperature':

        a = np.mean(data,axis=0)
        result= a[0]


    elif statistic == 'Mean Growth rate':
        a = np.mean(data, axis=0)
        result = a[1]
    elif statistic == 'Std Temperature':
        a = np.std(data, axis=0)
        result = a[0]
    elif statistic == 'Std Growth rate':
        a = np.std(data, axis=0)
        result = a[1]
    elif statistic == 'Rows':
        a = np.shape(data)
        result = a[0]
    elif statistic == 'Mean Cold Growth rate':
        sum=0
        n=0

        for i in range(np.shape(data)[0]):
            if data[i][0]<20:
                sum=sum+data[i][1]
                n=n+1
        result=sum/n
    elif statistic == 'Mean Hot Growth rate':
        sum=0
        n=0

        for i in range(np.shape(data)[0]):
            if data[i][0]>50:
                sum=sum+data[i][1]
                n=n+1
        try:
            result=sum/n
        except ZeroDivisionError:
            print("division by zero!")
            result=None

    return result


#---------------------------------THIRD FUNCTION------------------------------------------------------------------------

def dataPlot(data):
#---------------------------------first part-----bar plot- number of bacteri--------------------------------------------
    counter = 0
    counter2=0
    counter3=0
    counter4=0

    type_1= np.array([0,0,0])
    type_2= np.array([0,0,0])
    type_3= np.array([0,0,0])
    type_4= np.array([0,0,0])

    for i in range(len(data[:,2])):
        if data[i,2]==1:
            counter=counter+1
            type_1 = np.vstack((type_1, data[i]))
        if data[i,2]==2:
            type_2 = np.vstack((type_2, data[i]))
            counter2=counter2+1
        if data[i,2]==3:
            type_3 = np.vstack((type_3, data[i]))
            counter3=counter3+1

        if data[i,2]==4:
            type_4 = np.vstack((type_4, data[i]))
            counter4=counter4+1




    plt.bar([1 ], [counter],  label="Type 1", color='g')
    plt.bar([2 ], [counter2], label="Type 2", color='r')
    plt.bar([3 ], [counter3], label="Type 3", color='b')
    plt.bar([4 ], [counter4], label="Type 4", color='y')

    plt.legend()
    plt.xlabel('Bacteria Types')
    plt.ylabel('Number of Bacteria')

    plt.title('Bacteria Type Frequency Graph')

    plt.show()





#---------------------------------second PART-----------Growth rate by temperature--------------------------------------

    plt.scatter(type_1[:,0], type_1[:,1], label="Salmonella enterica", color='g', s=25, marker="*" )

    plt.scatter(type_2[:, 0], type_2[:, 1], color='r', s=25, marker="x", label="Bacillus cereus")
    plt.scatter(type_3[:, 0], type_3[:, 1], color='b', s=25, marker="^", label="Listeria")
    plt.scatter(type_4[:, 0], type_4[:, 1], color='y', s=25, marker="o", label="Brochothrix thermosphacta")





    plt.title("Growth Rate by Temperature")  # Set the title of the graph
    plt.xlabel("Temperature")  # Set the x-axis label
    plt.ylabel("Growth Rate")  # Set the y-axis label
    plt.axis([10, 60, 0, 1])
    plt.legend()
    plt.show()





def main():
    button= ''
    while not button=='quit':

        print(" L for loading data\n F for filter data\n D for Display Statistic\n G for Generating plots")
        button = input("What would you like to do? ")

        if button=="L":
            filename= input("The name of the file name is necessary :")
            dataLoad(filename)



main()