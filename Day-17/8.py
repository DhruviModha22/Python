class HighTemperatureError(Exception):
    pass

def convert_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number.")
    
    assert -273 <= temp <= 10000, "Temperature is out of valid range."
    
    if temp > 1000:
        raise HighTemperatureError("Temperature too high for common use.")

    print(f"Temperature is valid: {temp}°C")

convert_temperature(25)  # Valid
# convert_temperature("hot")  # Raises TypeError
# convert_temperature(-500)  # Raises AssertionError
# convert_temperature(5000)  # Raises HighTemperatureError
