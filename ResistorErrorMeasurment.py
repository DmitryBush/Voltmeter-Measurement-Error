import math
import numpy as np

# 1 - Напряжение с генератора и погрешность; 2, 3, 4 - Напряжения на разисторах и погрешность; 5 - Сила тока и погрешность
persons = {'Data_Person1': np.array([[5.1, 0.2], [2.3, 0.05], [1.1, 0.05], [1.7, 0.05], [193, 5]]),  # Черемин Д.
           'Data_Person2': np.array([[11.8, 0.2], [5.3, 0.20], [2.6, 0.05], [4.0, 0.20], [475, 50]]),  # Голубев А.
           'Data_Person3': np.array([[21.8, 0.5], [9.7, 0.20], [4.8, 0.20], [7.5, 0.20], [825, 50]])}  # Бушуев Д.

resistors = {'resistor1': np.array([], float),
             'resistor2': np.array([], float),
             'resistor3': np.array([], float)}

error_resistors = {'resistor1': np.array([], float),
                   'resistor2': np.array([], float),
                   'resistor3': np.array([], float)}

middle_coefficient = {'middle_R1': np.array([], float),
                      'middle_R2': np.array([], float),
                      'middle_R3': np.array([], float)}

true_resistors = {'resistor1': 0.0,
                  'resistor2': 0.0,
                  'resistor3': 0.0}

true_error_resistors = {'resistor1': 0.0,
                        'resistor2': 0.0,
                        'resistor3': 0.0}


def Calculate_Resistance_R():
    global resistors, error_resistors
    for i in range(1, 4, 1):
        R = persons.get(f'Data_Person{i}')[1][0] / (persons.get(f'Data_Person{i}')[4][0] * (10 ** -6))
        resistors['resistor1'] = np.append(resistors.get('resistor1'), R)
        error_resistors['resistor1'] = np.append(error_resistors.get('resistor1'),
                                                 Calculate_Resistance_Error(persons.get(f'Data_Person{i}')[1][1],
                                                                            persons.get(f'Data_Person{i}')[1][0],
                                                                            persons.get(f'Data_Person{i}')[4][1],
                                                                            persons.get(f'Data_Person{i}')[4][0],
                                                                            R))

        R = persons.get(f'Data_Person{i}')[2][0] / (persons.get(f'Data_Person{i}')[4][0] * (10 ** -6))
        resistors['resistor2'] = np.append(resistors.get('resistor2'), R)
        error_resistors['resistor2'] = np.append(error_resistors.get('resistor2'),
                                                 Calculate_Resistance_Error(persons.get(f'Data_Person{i}')[2][1],
                                                                            persons.get(f'Data_Person{i}')[2][0],
                                                                            persons.get(f'Data_Person{i}')[4][1],
                                                                            persons.get(f'Data_Person{i}')[4][0],
                                                                            R))

        R = persons.get(f'Data_Person{i}')[3][0] / (persons.get(f'Data_Person{i}')[4][0] * (10 ** -6))
        resistors['resistor3'] = np.append(resistors.get('resistor3'), R)
        error_resistors['resistor3'] = np.append(error_resistors.get('resistor3'),
                                                 Calculate_Resistance_Error(persons.get(f'Data_Person{i}')[3][1],
                                                                            persons.get(f'Data_Person{i}')[3][0],
                                                                            persons.get(f'Data_Person{i}')[4][1],
                                                                            persons.get(f'Data_Person{i}')[4][0],
                                                                            R))


def Koefficient_Calcul():
    global middle_coefficient
    for i in range(3):
        middle_coefficient['middle_R1'] = np.append(middle_coefficient.get('middle_R1'),
                                                    Calculate_Koef(error_resistors.get('resistor1')[i],
                                                                   error_resistors.get('resistor1')[0],
                                                                   error_resistors.get('resistor1')[1],
                                                                   error_resistors.get('resistor1')[2]))

        middle_coefficient['middle_R2'] = np.append(middle_coefficient.get('middle_R2'),
                                                    Calculate_Koef(error_resistors.get('resistor2')[i],
                                                                   error_resistors.get('resistor2')[0],
                                                                   error_resistors.get('resistor2')[1],
                                                                   error_resistors.get('resistor2')[2]))

        middle_coefficient['middle_R3'] = np.append(middle_coefficient.get('middle_R3'),
                                                    Calculate_Koef(error_resistors.get('resistor3')[i],
                                                                   error_resistors.get('resistor3')[0],
                                                                   error_resistors.get('resistor3')[1],
                                                                   error_resistors.get('resistor3')[2]))


def Calculate_Resistance_Error(dU_HAst, U, dIck, I, R):
    return R * math.sqrt((dU_HAst / U) ** 2 + (dIck / I) ** 2)


def Calculate_Koef(Error_R, R1, R2, R3):
    return (1 / (Error_R ** 2)) / (1 / (R1 ** 2) + 1 / (R2 ** 2) + 1 / (R3 ** 2))


def Calculate_Result_Resistance(resistor_num):
    R = 0.0
    for i in range(3):
        R += middle_coefficient.get(f'middle_R{resistor_num}')[i] * resistors.get(f'resistor{resistor_num}')[i]
    return R


def Calculate_Result_Error_Resistanse(R1, R2, R3):
    return 1 / math.sqrt(1 / (R1 ** 2) + 1 / (R2 ** 2) + 1 / (R3 ** 2))


Calculate_Resistance_R()
Koefficient_Calcul()

for j in range(1, 4):
    true_resistors[f"resistor{j}"] = Calculate_Result_Resistance(j)
    true_error_resistors[f"resistor{j}"] = \
        Calculate_Result_Error_Resistanse(error_resistors.get(f'resistor{j}')[0],
                                          error_resistors.get(f'resistor{j}')[1],
                                          error_resistors.get(f'resistor{j}')[2])

print("Resistor 1:")

print("Measurement:")
print(f'Measurement 1 = {resistors.get("resistor1")[0]}\n'
      f'Measurement 2 = {resistors.get("resistor1")[1]}\n'
      f'Measurement 3 = {resistors.get("resistor1")[2]}\n')

print("Measurement Error:")
print(f'Measurement error 1 = {error_resistors.get("resistor1")[0]}\n'
      f'Measurement error 2 = {error_resistors.get("resistor1")[1]}\n'
      f'Measurement error 3 = {error_resistors.get("resistor1")[2]}\n')

print("Middle Coefficient:")
print(f'Middle coefficient 1 = {middle_coefficient.get("middle_R1")[0]}\n'
      f'Middle coefficient 2 = {middle_coefficient.get("middle_R1")[1]}\n'
      f'Middle coefficient 3 = {middle_coefficient.get("middle_R1")[2]}\n')

print("Results:")
print(f'Result_R1 = {true_resistors.get("resistor1")}\n'
      f'Result error R1 = {true_error_resistors.get("resistor1")}\n')


print("Resistor 2:")

print("Measurement:")
print(f'Measurement 1 = {resistors.get("resistor2")[0]}\n'
      f'Measurement 2 = {resistors.get("resistor2")[1]}\n'
      f'Measurement 3 = {resistors.get("resistor2")[2]}\n')

print("Measurement Error:")
print(f'Measurement error 1 = {error_resistors.get("resistor2")[0]}\n'
      f'Measurement error 2 = {error_resistors.get("resistor2")[1]}\n'
      f'Measurement error 3 = {error_resistors.get("resistor2")[2]}\n')

print("Middle Coefficient:")
print(f'Middle coefficient 1 = {middle_coefficient.get("middle_R2")[0]}\n'
      f'Middle coefficient 2 = {middle_coefficient.get("middle_R2")[1]}\n'
      f'Middle coefficient 3 = {middle_coefficient.get("middle_R2")[2]}\n')

print("Results:")
print(f'Result R2 = {true_resistors.get("resistor2")}\n'
      f'Result error R2 = {true_error_resistors.get("resistor2")}\n')

print("Resistor 3:")

print("Measurement:")
print(f'Measurement 1 = {resistors.get("resistor3")[0]}\n'
      f'Measurement 2 = {resistors.get("resistor3")[1]}\n'
      f'Measurement 3 = {resistors.get("resistor3")[2]}\n')

print("Measurement Error:")
print(f'Measurement error 1 = {error_resistors.get("resistor3")[0]}\n'
      f'Measurement error 2 = {error_resistors.get("resistor3")[1]}\n'
      f'Measurement error 3 = {error_resistors.get("resistor3")[2]}\n')

print("Middle Coefficient:")
print(f'Middle coefficient 1 = {middle_coefficient.get("middle_R3")[0]}\n'
      f'Middle coefficient 2 = {middle_coefficient.get("middle_R3")[1]}\n'
      f'Middle coefficient 3 = {middle_coefficient.get("middle_R3")[2]}\n')

print("Results:")
print(f'Result R3 = {true_resistors.get("resistor3")}\n'
      f'Result error R3 = {true_error_resistors.get("resistor3")}\n')
