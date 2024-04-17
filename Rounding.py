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
    
    if 1 <= int(str(error)[0]) <= 2:
        zero_count = (len(str(error)) - 2)
        rounded_error = str(round(float(str(error)[0:2] + '.' + str(error)[2:]), 0))[:-2] + '0' * zero_count
    elif 3 <= int(str(error)[0]) <= 9:
        zero_count = (len(str(error)) - 1)
        rounded_error = str(round(float(str(error)[0:1] + '.' + str(error)[2:]), 0))[:-2] + '0' * zero_count
    else:
        raise "Zero error"

    rounded_value = str(round(float(str(value)[:-zero_count] + '.'
                                    + str(value)[-zero_count]), 0))[:-2] + '0' * zero_count
    return rounded_value, rounded_error


if __name__ == '__main__':
    print(round_error(33081.0, 432.702))
