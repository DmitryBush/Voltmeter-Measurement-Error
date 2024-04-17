def round_error(value: float, error: float):
    if error.is_integer():
        if 1 <= int(str(error)[0]) <= 2:
            zero_count = (len(str(error)) - 2)
            rounded_error = str(round(float(str(error)[0:2] + '.' + str(error)[2:]), 0))[:-2] + '0' * zero_count
        elif 3 <= int(str(error)[0]) <= 9:
            zero_count = (len(str(error)) - 1)
            rounded_error = str(round(float(str(error)[0:1] + '.' + str(error)[2:]), 0))[:-2] + '0' * zero_count
        else:
            raise "Zero error"
    else:
        error_list = str(error).replace('.', ' ').split()
        if error_list[0][0] == '0':
            found_val = False
            for i in range(len(error_list[1])):
                if 1 <= int(error_list[1][i]) <= 2:
                    zero_count = (len(str(error_list[1]))[i:] - 2) + i
                    rounded_error = str(round(float(str(error_list[1])[i: i + 2]
                                                    + '.'
                                                    + str(error_list[1])[i + 2:]),
                                              0))[:-2] + '0' * zero_count
                    found_val = True
                    break
                elif 3 <= int(str(error_list[1][i])[0]) <= 9:
                    zero_count = (len(str(error_list[1]))[i:] - 1) + i
                    rounded_error = str(round(float(str(error_list[1])[i: i + 1]
                                                    + '.'
                                                    + str(error_list[1])[i + 2:]),
                                              0))[:-2] + '0' * zero_count
                    found_val = True
                    break
            if found_val is False:
                raise "None meaning value"
        else:
            if 1 <= int(str(error_list[0][0])[0]) <= 2:
                zero_count = (len(str(error_list[0])) - 2)
                rounded_error = str(round(float(str(error_list[0])[0:2]
                                                + '.'
                                                + str(error_list[0])[2:]),
                                          0))[:-2] + '0' * zero_count
            elif 3 <= int(str(error_list[0][0])[0]) <= 9:
                zero_count = (len(str(error_list[0])) - 1)
                rounded_error = str(round(float(str(error_list[0])[0:1]
                                                + '.'
                                                + str(error_list[0])[2:]),
                                          0))[:-2] + '0' * zero_count
            else:
                raise "Zero error"
    
    rounded_value = str(round(float(str(value)[:-zero_count] + '.'
                                    + str(value)[-zero_count]), 0))[:-2] + '0' * zero_count
    return rounded_value, rounded_error


if __name__ == '__main__':
    print(round_error(33081.0, 432.702))
