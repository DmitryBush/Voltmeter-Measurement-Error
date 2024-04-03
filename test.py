import math

import numpy as np


def Calculate_Koef(Error_R, R1, R2, R3, R4):
    return (1 / (Error_R ** 2)) / (1 / (R1 ** 2) + 1 / (R2 ** 2) + 1 / (R3 ** 2) + 1 / (R4 ** 2))


def Calculate_Resistance_Error(dU_HAst, U, dIck, I, R):
    return R * math.sqrt((dU_HAst / U) ** 2 + (dIck / I) ** 2)


def Calculate_Result_Resistance(resistor_num):
    R = 0.0
    for i in range(4):
        R += middle_coefficient.get(f'middle_R{resistor_num}')[i] * resistors.get(f'resistors{resistor_num}')[i]
    return R


def Calculate_Result_ResistanseError(R1, R2, R3, R4):
    return 1 / math.sqrt(1 / (R1 ** 2) + 1 / (R2 ** 2) + 1 / (R3 ** 2) + 1 / (R4 ** 2))


persons = {'Data_Person1': np.array([[5.1, 0.2], [2.3, 0.05], [1.1, 0.05], [1.7, 0.05], [193, 5]]),
           'Data_Person2': np.array([[11.8, 0.2], [5.3, 0.20], [2.6, 0.05], [4.0, 0.20], [475, 50]]),
           'Data_Person3': np.array([[21.8, 0.5], [9.7, 0.20], [4.8, 0.20], [7.5, 0.20], [825, 50]]),
           'Data_Person4': np.array([[28.8, 0.5], [13, 0.5], [6.1, 0.2], [9.8, 0.2], [1100, 50]])}

resistors = {'resistors1': np.array([], float),
             'resistors2': np.array([], float),
             'resistors3': np.array([], float)}

error_resistors = {'resistors1': np.array([], float),
                   'resistors2': np.array([], float),
                   'resistors3': np.array([], float)}

middle_coefficient = {'middle_R1': np.array([], float),
                      'middle_R2': np.array([], float),
                      'middle_R3': np.array([], float)}


def calc_resistor():
    global resistors, error_resistors
    for i in range(1, 5):
        R = persons.get(f'Data_Person{i}')[1][0] / (persons.get(f'Data_Person{i}')[4][0] * (10 ** -6))
        resistors['resistors1'] = np.append(resistors.get('resistors1'), R)
        error_resistors['resistors1'] = np.append(error_resistors.get('resistors1'),
                                                  Calculate_Resistance_Error(persons.get(f'Data_Person{i}')[1][1],
                                                                             persons.get(f'Data_Person{i}')[1][0],
                                                                             persons.get(f'Data_Person{i}')[4][1],
                                                                             persons.get(f'Data_Person{i}')[4][0],
                                                                             R))


def calc_coeff():
    global middle_coefficient, error_resistors
    for i in range(4):
        middle_coefficient['middle_R1'] = np.append(middle_coefficient.get('middle_R1'),
                                                    Calculate_Koef(error_resistors.get('resistors1')[i],
                                                                   error_resistors.get('resistors1')[0],
                                                                   error_resistors.get('resistors1')[1],
                                                                   error_resistors.get('resistors1')[2],
                                                                   error_resistors.get('resistors1')[3]))


calc_resistor()
calc_coeff()
TrueResistance = Calculate_Result_Resistance(1)
TrueResistanceError = Calculate_Result_ResistanseError(error_resistors.get('resistors1')[0],
                                                       error_resistors.get('resistors1')[1],
                                                       error_resistors.get('resistors1')[2],
                                                       error_resistors.get('resistors1')[3])

print(resistors.get('resistors1'))
print(error_resistors.get('resistors1'))
print(middle_coefficient.get('middle_R1'))
print(TrueResistance)
print(TrueResistanceError)
