def convert_temperature(temp, unit="C"):
    """
    Convert temperature between Celsius and Fahrenheit.
    
    Args:
        temp (float): The temperature value to convert.
        unit (str): The unit of the input temperature. "C" for Celsius, "F" for Fahrenheit.
                   Defaults to "C".
    
    Returns:
        float: The converted temperature, rounded to 2 decimal places.
    
    Raises:
        ValueError: If unit is not "C" or "F".
    """
    if unit == "C":
        # Convert Celsius to Fahrenheit: F = C × 9/5 + 32
        fahrenheit = temp * 9 / 5 + 32
        return round(fahrenheit, 2)
    elif unit == "F":
        # Convert Fahrenheit to Celsius: C = (F − 32) × 5/9
        celsius = (temp - 32) * 5 / 9
        return round(celsius, 2)
    else:
        raise ValueError("Unit must be 'C' or 'F'")
