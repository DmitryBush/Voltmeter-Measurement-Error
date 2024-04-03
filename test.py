import math

import numpy as np


def Calculate_Koef(Error_R, R1, R2, R3, R4):
    return (1 / (Error_R ** 2)) / (1 / (R1 ** 2) + 1 / (R2 ** 2) + 1 / (R3 ** 2) + 1 / (R4 ** 2))


def Calculate_Resistance_Error(dU_HAst, U, dIck, I, R):
    return R * math.sqrt((dU_HAst / U) ** 2 + (dIck / I) ** 2)

def Calculate_Result_Resistance():
    R = 0.0
    for i in range(4):
        R += All_Middle_R1[i] * Resistors1[i]
    return R

def Calculate_Result_ResistanseError(R1, R2, R3, R4):
    return 1 / math.sqrt(1 / (R1 ** 2) + 1 / (R2 ** 2) + 1 / (R3 ** 2) + 1 / (R4 ** 2))


persons = {'Data_Person1': np.array([[5.1, 0.2], [2.3, 0.05], [1.1, 0.05], [1.7, 0.05], [193, 5]]),
           'Data_Person2': np.array([[11.8, 0.2], [5.3, 0.20], [2.6, 0.05], [4.0, 0.20], [475, 50]]),
           'Data_Person3': np.array([[21.8, 0.5], [9.7, 0.20], [4.8, 0.20], [7.5, 0.20], [825, 50]]),
           'Data_Person4': np.array([[28.8, 0.5], [13, 0.5], [6.1, 0.2], [9.8, 0.2], [1100, 50]])}

Resistors1 = np.array([], float)
Resistors1_Error = np.array([], float)
All_Middle_R1 = np.array([], float)


def calc_resistor():
    global Resistors1, Resistors1_Error
    for i in range(1, 5):
        R = persons.get("Data_Person%d" % i)[1][0] / (persons.get("Data_Person%d" % i)[4][0] * (10 ** -6))
        Resistors1 = np.append(Resistors1, R)
        Resistors1_Error = np.append(Resistors1_Error,
                                     Calculate_Resistance_Error(persons.get("Data_Person%d" % i)[1][1],
                                                                persons.get("Data_Person%d" % i)[1][0],
                                                                persons.get("Data_Person%d" % i)[4][1],
                                                                persons.get("Data_Person%d" % i)[4][0],
                                                                R))


def calc_coeff():
    global All_Middle_R1, Resistors1_Error
    for i in range(4):
        All_Middle_R1 = np.append(All_Middle_R1,
                                  Calculate_Koef(Resistors1_Error[i], Resistors1_Error[0],
                                                 Resistors1_Error[1], Resistors1_Error[2],
                                                 Resistors1_Error[3]))


calc_resistor()
calc_coeff()
TrueResistance = Calculate_Result_Resistance()
TrueResistanceError = Calculate_Result_ResistanseError(Resistors1_Error[0], Resistors1_Error[1],
                                                       Resistors1_Error[2], Resistors1_Error[3])

print(Resistors1)
print(Resistors1_Error)
print(All_Middle_R1)
print(TrueResistance)
print(TrueResistanceError)
