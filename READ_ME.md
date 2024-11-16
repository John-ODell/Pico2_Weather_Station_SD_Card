Pi Pico 2 Weather Station Data Collection

Items needed

- Pi Pico 2
- DHT 11 Temperature and Humitidy Sensor
- DS18B20 Digital Temperature Sensor
- LDR/Photoresister Sensor
- TF Micro SD Adapter Module
- Micro SD Card 32 gb or less (fat32 format)
- Thonny IDE
- Circuit Python 9x Libraries

Download "adafruit-circuit-python-bundle-9.x" (do not unzip) https://circuitpython.org/libraries

Flash the Pi Pico 2 with Circuit Python (there are two ways)

First hold the boot button on the Pi, connect it to your computer and let go of the boot button.
    - you should see RP1/RP2 in your folders

Option 1, download the .UF2 from the Ciruit Python Website and drag into the Pi Pico 2 folder.
    - navigate to this page and download the UF2 
    - from your downloads, drag the UF2 into the RP1/RP2 (Pi Pico 2 Foler)
    - it will reconnect after flashing, and will have new folders
    - Go to the next section

Option 2, Download Thonny IDE, hold the boot button on the pi, connect it to your computer, and let go of the boot button.
    - Navigate to Run
    - Configure Interpreter
        - Which Kind of Interpreter
            - CircuitPython (generic)
        - Install
        - Target Volume (Should Auto Detect otherwise RP1/RP2)
        - Family - RP2
        - Pico 2
        - Version - Most Recent

Installing Libraries From "adafruit-circuit-python-bundle-9.x"

Navigate to the Pi Pico 2 in your folders and open the "lib" folder, this is where we will put all of our dependicies 
Inside the "adafruit-circuit-python-bundle-9.x" drag into the lib folder
    - adafruit_bus_debice (folder)
    - adafruit_regist (folder)
    - adafruit_dht.mpy
    - adafruit_sdcard.mpy

Reconizing Circuit Python on the Pi Pico 2 in Thonny
    - Circuit Python must be flashed to the device before Thonny will reconize the board
    - Navigate to run
    - Conifgure Interpreter
        - Which Kind of Interpreter
            - CircuitPython (generic)
        - Port or WebREPL
            - (This Should Say COM(number))
        -Press OK
    - Press the Red Stop Sign to See the Board Information

Wiring - 
TF Micro SD Adapter Module has Dedicated Power and Ground, recommend F->M jumper wires from SD module
to Pi Pico for best connection.

Modules use 3.3v VCC (Pin 36) and Ground (Pin 38) into a bread board

TF Micro SD Adapter Module
(Dedicated 5v VCC and GND)
CS ->  GPIO 13
SCK -> GPIO 10
MOSI -> GPIO 11
MISO -> GPIO 12
VCC -> VBUS (5v)
GND -> GND (Pin 13)

DHT 11 Temperature and Humitidy Sensor 
Signal -> GPIO 14
VCC -> 3.3v
GND -> GND

DS18B20 Digital Temperature Sensor 
AO -> GPIO 26 (Analog Out)
DO -> GPIO 15 (Digital OUt)
VCC -> 3.3v
GND -> GND

LDR/Photoresister Sensor
AO -> GPIO 27
VCC -> 3.3v
GND -> GND

Initializtion SD Card and Test Examples
YOU MUST USE A PI PICO 2 FOR THE SD CARD TO BE RECONIZED, RP2040 WILL NOT WORK

On your board you will find a SD folder with a place holder, this is standard for
circuit python and does not indicate your board is reconizing an sd card. We need 
to Initialize the sd card and make sure we can write to it first.

The first example we will use is "sdcard_init". This will write a sample text file to
the sd card. After running the example and pressing stop, the sd folder may not be able 
to open or show the file just created in Thonny IDE, that is ok. Remove the sd card from the Module 
and read its contents. There will be the test file.

If an error arises make sure you added the correct libraries, the pin connections are to
the correct GPIO ports, VCC is connnect to VBUS (5v), and the sd card is in a fat32 format. 
Larger SD cards can be harder to read as well.

**If you are not having success, see the Contact me for help. 

DHT11 Example

Open the file "dht11.py" and press run. It returns the temperature in Celsius, Fahrenheit and Humidity.

Digital Thermometer Example 

Open digital_therm.py and press run. It returns the temperature in Celsius, Fahrenheit and a
True or False value.
The temperature is read as an analog level and an equation is used to calculate the temperautre,
the True or False value confirms a correct reading to the board or not, not a correct calculation.

The current Calculation is exact, but set to be devided by 2 after collection. For the most accurate
Collection, Collect the Data raw and perform an equation afterwards. A standard can be set at
voltage = ((analog_value / 655535) * 3.3)
return voltage

**for information or to update this equation please see the Contact Me section

LDR/Photoresister Sensor

Open the "light_level.py" and press run. It will return the "Light Level" in voltage.
The higher the reading, the more light there is and the lower, the darker the environment is.

The readings can be hard to understand and need to be placed to scale for analysis.

Pi Pico 2 Weather Station

Open the file "boot.py" and save it to the device along with the examples. 

This time we are writing again to the micro SD card, this time in CSV format.
Once again, the file might disappear when working with Thonny, but when removed
the examined the file will be there. 

Every 10 minutes We are collecting Data of the
    - Temperature 
        - Digitally and Analog for accuracy comparison
    -Humidity Percentage
    -Light Level

This can help give us an understanding of how accurate our local/internet forcast are.
How humidity Plays a role in Temperautre
The speed of changes in Temperauter and humidity
How light effects Temperature

First Log 
    - 35.5 Hours Sat
    - Multiple NAN values from DHT11 
    - LED from Modules and Board LED were not accounted for in LDR code
    - Add timestamps in CSV write

--------------VERSION 1------------------------


