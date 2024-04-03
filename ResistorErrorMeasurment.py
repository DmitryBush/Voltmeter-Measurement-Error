import math

import numpy as np

# 1 - Напряжение с генератора и погрешность; 2, 3, 4 - Напряжения на разисторах и погрешность; 5 - Сила тока и погрешность

Data_Person1 = np.array([[5.1, 0.2], [2.3, 0.05], [1.1, 0.05], [1.7,0.05], [193, 5]])  #Черемин Д.
Data_Person2 = np.array([[11.8, 0.2], [5.3, 0.20], [2.6, 0.05], [4.0,0.20], [475, 50]])  #Голубев А.
Data_Person3 = np.array([[21.8, 0.5], [9.7, 0.20], [4.8, 0.20], [7.5,0.20], [825, 50]])                                                 #Бушуев Д.

All_Data_Person = [Data_Person1, Data_Person2, Data_Person3]




All_Resistors1 = np.array([])
All_Resistors2 = np.array([])
All_Resistors3 = np.array([])


All_Resistors1_Error = np.array([])
All_Resistors2_Error = np.array([])
All_Resistors3_Error = np.array([])

All_Middle_Koef_For_R1 = np.array([])
All_Middle_Koef_For_R2 = np.array([])
All_Middle_Koef_For_R3 = np.array([])

True_Error1 = 0
True_Error2 = 0
True_Error3 = 0



def Calculate_Resistance_R():
    for i in range(1,4,1):
        All_Resistors1.np.append(Data_Person1[i][0]/(Data_Person1[4][0] * (10**-6)))
        R = Data_Person1[i][0]/(Data_Person1[4][0] * (10**-6))
        All_Resistors1_Error.np.array(Calculate_Resistance_Error(Data_Person1[i][1],Data_Person1[i][0], Data_Person1[4][1], Data_Person1[4][0], R))
        All_Resistors2.np.append(Data_Person2[i][0]/(Data_Person2[4][0] * (10**-6)))
        R = Data_Person2[i][0]/(Data_Person2[4][0] * (10**-6))
        All_Resistors2_Error.np.array(
            Calculate_Resistance_Error(Data_Person2[i][1], Data_Person2[i][0], Data_Person2[4][1], Data_Person2[4][0],
                                       R))
        All_Resistors.np.append(Data_Person3[i][0]/(Data_Person3[4][0] * (10**-6)))
        R = Data_Person3[i][0]/(Data_Person3[4][0] * (10**-6))
        All_Resistors3_Error.np.array(
            Calculate_Resistance_Error(Data_Person3[i][1], Data_Person3[i][0], Data_Person3[4][1], Data_Person3[4][0],
                                       R))


def Koefficient_Calcul():
        All_Middle_Koef_For_R1.np.array(Calculate_Koef(All_Resistors1_Error[0], All_Resistors1_Error[0], All_Resistors2_Error[0],All_Resistors3_Error[0]))
        All_Middle_Koef_For_R2.np.array(Calculate_Koef(All_Resistors1_Error[1], All_Resistors1_Error[1], All_Resistors2_Error[1],All_Resistors3_Error[1]))
        All_Middle_Koef_For_R3.np.array(Calculate_Koef(All_Resistors1_Error[2], All_Resistors1_Error[2], All_Resistors2_Error[2],All_Resistors3_Error[2]))


def Calculate_Resistance_Error(dU_HAst, U, dIck, I, R):

    return R*math.sqrt((dU_HAst/U)**2 + (dIck/I)**2)

def Calculate_Koef(Error_R, R1, R2, R3 ):

    return (1/(Error_R**2))/(1/(R1**2) + 1/(R2**2) + 1/(R3**2))



Calculate_Resistance_R()
Koefficient_Calcul()
True_Error1 = Calculate_Koef(1,All_Middle_Koef_For_R1[0],All_Middle_Koef_For_R1[1],All_Middle_Koef_For_R1[2])
True_Error2 = Calculate_Koef(1, All_Middle_Koef_For_R2[0], All_Middle_Koef_For_R2[1], All_Middle_Koef_For_R2[2])
True_Error3 = Calculate_Koef(1, All_Middle_Koef_For_R3[0], All_Middle_Koef_For_R3[1], All_Middle_Koef_For_R3[2])


print("User 1:")
print("Resistor 1 = ", All_Resistors1[0],"Resistor 2 = ",All_Resistors1[1], "Resistor 3 = ",All_Resistors1[2])
print("Resistor1 Error  = ", All_Resistors1_Error[0], "Resistor2 Error  = ",  All_Resistors1_Error[1], "Resistor3 Error = ", All_Resistors1_Error[2])
print("Koef_Resistor1 = ", All_Middle_Koef_For_R1[0],"Koef_Resistor2 = ", All_Middle_Koef_For_R2[0],"Koef_Resistor3 = ", All_Middle_Koef_For_R3[0])

print("User 2:")
print("Resistor 1 = ", All_Resistors2[0],"Resistor 2 = ",All_Resistors2[1], "Resistor 3 = ",All_Resistors2[2])
print("Resistor Error 1 = ", All_Resistors2_Error[0], "Resistor Error 2 = ",  All_Resistors2_Error[1], "Resistor Error 3 = ", All_Resistors2_Error[2])
print("Koef_Resistor1 = ", All_Middle_Koef_For_R1[1],"Koef_Resistor2 = ", All_Middle_Koef_For_R2[1],"Koef_Resistor3 = ", All_Middle_Koef_For_R3[1])

print("User 3:")
print("Resistor 1 = ", All_Resistors3[0],"Resistor 2 = ",All_Resistors3[1], "Resistor 3 = ",All_Resistors3[2])
print("Resistor Error 1 = ", All_Resistors3_Error[0], "Resistor Error 2 = ",  All_Resistors3_Error[1], "Resistor Error 3 = ", All_Resistors3_Error[2])
print("Koef_Resistor1 = ", All_Middle_Koef_For_R1[2],"Koef_Resistor2 = ", All_Middle_Koef_For_R2[2],"Koef_Resistor3 = ", All_Middle_Koef_For_R3[2])

