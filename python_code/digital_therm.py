import time
import board
import analogio
import digitalio

# Initialize analog input for AO
analog_input = analogio.AnalogIn(board.GP26)

# Initialize digital input for DO
digital_input = digitalio.DigitalInOut(board.GP15)
digital_input.direction = digitalio.Direction.INPUT

# Function to read analog value and convert to temperature
def read_temperature():
    # Read the analog value (0-65535)
    analog_value = analog_input.value
    
    # Convert the analog value to a voltage (0-3.3V)
    voltage = (analog_value / 65535) * 4.7
    
    # Adjust the conversion formula based on your sensor's characteristics
    # This is a placeholder conversion; you may need a specific formula for your sensor
    temperature_c = (voltage - 0.5) * 100  # Adjusted conversion
    
    return temperature_c

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to read digital value
def read_digital():
    return digital_input.value

# Main loop
while True:
    temperature_c = read_temperature()
    temperature_f = celsius_to_fahrenheit(temperature_c)
    digital_value = read_digital()

    # Print the values
    print(f"Temperature: {temperature_c:.2f}°C / {temperature_f:.2f}°F")
    print(f"Digital Value: {digital_value}")

    time.sleep(2)
