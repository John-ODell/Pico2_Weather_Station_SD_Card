import time
import board
import analogio
import digitalio
import adafruit_dht
import busio as io
import storage
import adafruit_sdcard

# Initialize DHT11 sensor
dht11 = adafruit_dht.DHT11(board.GP14)

# Initialize analog input for the photoresistor
photoresistor = analogio.AnalogIn(board.GP27)

# Initialize analog input for AO
analog_input = analogio.AnalogIn(board.GP26)

# Initialize digital input for DO
digital_input = digitalio.DigitalInOut(board.GP15)
digital_input.direction = digitalio.Direction.INPUT

# Initialize SD card
SD_CS = board.GP13
spi = io.SPI(board.GP10, board.GP11, board.GP12)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Function to read temperature and humidity from DHT11
def read_dht11():
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        return temperature, humidity
    except RuntimeError as error:
        print(error.args[0])
        return None, None

# Function to read light level from photoresistor
def read_light_level():
    return photoresistor.value

# Function to read temperature from digital thermometer
def read_temperature():
    analog_value = analog_input.value
    voltage = (analog_value / 65535) * 4.7
    temperature_c = (voltage - 0.5) * 100
    return temperature_c

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to read digital value from digital thermometer
def read_digital():
    return digital_input.value

# Function to save data to a CSV file
def save_to_csv(data):
    with open("/sd/sensor_data.csv", "a") as file:
        file.write(",".join(map(str, data)) + "\n")

# Main loop
while True:
    # Read data from sensors
    dht11_temp_c, dht11_humidity = read_dht11()
    dht11_temp_f = celsius_to_fahrenheit(dht11_temp_c) if dht11_temp_c is not None else None
    light_level = read_light_level()
    temperature_c = read_temperature()
    temperature_f = celsius_to_fahrenheit(temperature_c)
    digital_value = read_digital()

    # Print the values
    print(f"DHT11 Temperature (Celsius): {dht11_temp_c}°C")
    print(f"DHT11 Temperature (Fahrenheit): {dht11_temp_f}°F")
    print(f"DHT11 Humidity: {dht11_humidity}%")
    print(f"Light Level: {light_level}")
    print(f"Digital Thermometer Temperature (Celsius): {temperature_c:.2f}°C")
    print(f"Digital Thermometer Temperature (Fahrenheit): {temperature_f:.2f}°F")
    print(f"Digital Value: {digital_value}")

    # Save data to CSV every 10 minutes
    save_to_csv([dht11_temp_c, dht11_temp_f, dht11_humidity, light_level, temperature_c, temperature_f, digital_value])
    time.sleep(600)  # 10 minutes
