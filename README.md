# SecretSanta
A Secret Santa selection program written to take advantage of GPIO for embedding in a toy. Uses GPIOZero and a generic thermal receipt printer. Requires Raspberry Pi 2 to work.


### Dependencies
To run the thermal printer, you will need to be using a RPi2.
Make sure you have gpiozero (for the switches/LEDs) and pygame (for sound) installed. 

The printer relies on the CUPS packages being installed to work:
  ```
  sudo apt-get install libcups2-dev libcupsimage2-dev git
  ```
  Once that’s done, download and install this CUPS filter for the thermal printer:
 ```
 git clone https://github.com/adafruit/zj-58
cd zj-58
make
sudo ./install
```

### Setup
You'll need a .jpg picture of everyone participating saved into /home/pi/SSanta
You will also need to add all the names of the participants into the list on line 17 as strings separated by commas.
Ensure that the name strings match EXACTLY with the filename for the photo of that person. Case senstitive! (Including the file extensions!!)


