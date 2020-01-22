import math
import random
import pandas as pd
import csv
import statistics

# read the train and test dataset
train_data = pd.read_csv('pro-train-data.csv')
test_data = pd.read_csv('pro-test-data.csv')

class0 = []  # 0 Class
class1 = []  # 1 Class

sum0 = 0
sum1 = 0

# seperate class : 0 or 1
for row in range(0, len(train_data)):
    if (train_data['Pass'][row] == 0):
        class0.append(train_data['IQ'][row])
        sum0 += train_data['IQ'][row]
    else:
        class1.append(train_data['IQ'][row])
        sum1 += train_data['IQ'][row]

# Avrage
Avg0 = sum0 / len(class0)
Avg1 = sum1 / len(class1)

# STandard DEViation
std0 = statistics.stdev(class0)
std1 = statistics.stdev(class1)


c0 = len(class0)/len(train_data)    # Not Passed
c1 = len(class1)/len(train_data)    # Pessed


label = []
guess = []

for i in range(len(test_data)):
    test = test_data['IQ'][i]
    label.append(test_data['Pass'][i])

    p_X_c0 = (1/(math.sqrt(2*math.pi)*std0))*math.pow(math.e,
                                                      (-1/2)*(math.pow(((test - Avg0)/std0), 2)))*c0
    p_X_c1 = (1/(math.sqrt(2*math.pi)*std1))*math.pow(math.e,
                                                      (-1/2)*(math.pow(((test - Avg1)/std1), 2)))*c1

    if(p_X_c0 > p_X_c1):
        guess.append(0)
    elif(p_X_c0 < p_X_c1):
        guess.append(1)
    else:
        guess.append(random.randint(0, 1))


# Calculation of Accuracy :
sum_true_positive = 0
sum_true_negative = 0
sum_accuracy = 0
for i in range(0, len(test_data)):
    print("IQ: ", test_data['IQ'][i], " --- Guess: ",
          guess[i], " --- Label: ", label[i])
    if guess[i] == label[i]:
        sum_accuracy += 1

print("\nAccuracy: ", sum_accuracy/len(test_data)*100, "%")
