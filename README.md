# SmartHome

## Setup for LED-Strip with with addressable LEDs

Follow setup instructions to install the python library for the ws2811b led strip: 
> <details>
>   <summary>https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/</summary>
  >
  > sudo apt-get update
  >
  > sudo apt-get install gcc make build-essential python-dev git scons swig
  >
  > sudo nano /etc/modprobe.d/snd-blacklist.conf
  >
  >     add following line to the file
  >     > blacklist snd_bcm2835
  >
  > sudo nano /boot/config.txt
  >    
  >    comment follwing line in the file
  >    > \# Enable audio (loads snd_bcm2835)
  >    >
  >    > dtparam=audio=on
  >
  > sudo reboot
  >
  > git clone https://github.com/jgarff/rpi_ws281x
  >
  > cd rpi_ws281x/
  >
  > sudo scons
  >
  > cd python
  >
  > sudo python3 setup.py build
  >
  > sudo python3 setup.py install
  >
  > sudo pip3 install adafruit-circuitpython-neopixel
  >
  > sudo nano examples/strandtest.py
  > </details>

Start server to access the user interface via flask RESTful API from your smartphone/computer.

> sudo python3 index.py

![](/doc/steps.jpg?raw=true)
