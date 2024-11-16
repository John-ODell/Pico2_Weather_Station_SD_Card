from board import *
from time import sleep
import busio
import sdcardio
import storage

sleep(1)

# Initialize SPI and SD Card
spi = busio.SPI(GP10, MOSI=GP11, MISO=GP12)
cs = GP13
sd = sdcardio.SDCard(spi, cs)

# Mount the filesystem
vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')

# Create a file and write something to it
with open("/sd/pico.txt", "w") as file:
    file.write("1. Hello, world!\r\n")

# Open the file we just created and append a line
with open("/sd/pico.txt", "a") as file:
    file.write("2. This is another line!\r\n")

# Append another line to the file
with open("/sd/pico.txt", "a") as file:
    file.write("3. Last but not least!")

# Open the file in read mode and print its content
with open("/sd/pico.txt", "r") as file:
    print("Printing lines in file:")
    for line in file:
        print(line, end='')
