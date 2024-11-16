import time
import board
import adafruit_dht

# Initialize the DHT11 sensor
dht11 = adafruit_dht.DHT11(board.GP14)

while True:
    try:
        # Read temperature and humidity
        temperature = dht11.temperature
        humidity = dht11.humidity

        # Print the values
        print(f"Temperature: {temperature}°C / {temperature * 9/5 + 32}°F")
        print(f"Humidity: {humidity}%")

    except RuntimeError as error:
        # Errors happen fairly often with DHT sensors, just keep going
        print(error.args[0])

    time.sleep(2)
