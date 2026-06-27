def temp_converter(degree, unit):
    if unit == 'C':
        return degree * 9/5 + 32
    else:
        return (degree - 32) * 5/9

solution = temp_converter(26, 'C')

print("The temperature in fahreinheit is:", solution)

