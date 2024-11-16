import time
import board
import analogio

# Initialize analog input for the photoresistor
photoresistor = analogio.AnalogIn(board.GP27)

# Function to read analog value
def read_light_level():
    return photoresistor.value

# Main loop
while True:
    light_level = read_light_level()

    # Print the light level
    print(f"Light Level: {light_level}")

    time.sleep(2)
