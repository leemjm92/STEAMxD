# Raspberry Pi FPV Camera Set-up
credit: [PyShine](https://pyshine.com) and [Sam Westby Tech](https://www.youtube.com/watch?v=QzVYnG-WaM4)

## Hardware
1. Raspberry Pi (Zero W/Zero 2 W/3A/3B/4A/4B)
2. MicroSD card 16gb and above
3. USB card reader
4. Raspberry Pi Camera (ver 1/ver 2)
5. Raspberry Pi Flex Camera
6. Powerbank

## Flash OS
1. Insert the SD card (better > 8GB size) into an USB card reader and plug it to your Computer (any of Mac OS, Windows and Ubuntu/Linux).
2. Go to the official link to download the Raspberry Pi Imager https://www.raspberrypi.org/software/
3. It is really quick and easy to install. You can watch the 3-steps here: [link](https://www.youtube.com/watch?v=J024soVgEeM)
<!--
you can define your username and password here when using the Imager if you've done so then
-->
4. Take out and again insert the USB card reader to your PC. This time you will see that the USB device name has changed to Boot. **If you've a HDMI cable and monitor available you can skip to [Set-up with monitor](#chapter3) alternatively if you've no access to a monitor you can proceed to the [Headless Set-up](#chapter2)** 

### Headless Set-up (without monitor) <a id="chapter2"></a>
<!-- 
to insert the relevant pictures for each step do this while I setup another sd card 
instead of using pictures some of the steps can be inlcuded within a short gif/webm/video
-->
 
**For Windows:**  
4. Open the device and find the config.txt file, open it in a text editor, go to the last line, press enter and add this dtoverlay=dwc2 after the last line, and save it.
<!-- to insert picture of how the config file should look like -->
5. In the device find the cmdline.txt file and add between two spaces this modules-load=dwc2,g_ether, right after the rootwait, then save and close this .txt as well.
<!-- to insert picture of how the cmdline.txt file should look like -->
7. Make an empty file in notepad and save it as ssh and remove the .txt in the name. This fill should exist in the same place as config.txt and cmdline.txt.
<!--
use cmdline cd boot directory -> touch ssh 
-->
8. Thats it! now remove the SD card and insert it into the Rasbperry Pi SD card slot properly. Simply plug the USB data cable to your Raspberry Pi card and connect it to the computer. The computer will also provide the power to your card, so no need to insert the power cable.
9. Upon connection the Windows OS will detect a new LAN device, wait for it to be installed and then we need Bonjour.
10. Go to this link, download and install Bonjour https://support.apple.com/kb/dl999?locale=en_GB
11. In the Device Properties of Windows OS, find the USB Serial Port and provide it the drivers from this link USB Ethernet Drivers: https://wiki.moddevices.com/wiki/Troubleshooting_Windows_Connection
12. After that you can view in the device in the Network and Sharing connections. The device is ready to SSH!
13. Next, install Bitvise client software: https://www.bitvise.com/ssh-client-download
14. We require the Host, Port, Username and the Password to access the Pi.
15. By default: Host is raspberrypi.local, Port is 22, Username is pi, and Password is raspberry, enter these values in the GUI and hit Login.
16. Once login, you can now visualize pi@raspberrypi:~ $ in the Command or Terminal window, enter ls to view your files. Now that we are able to access the PI, the next step is to enable its wifi so that we can download the opencv using a pip installer.
17. After the ```pi@raspberrypi:~ $``` in the Terminal window, we can write ```sudo raspi-config``` and hit enter to open the configuration window.
<!--
steps 14 to step xx single gif
-->
18. Select ```1 System Options``` using the arrow keys and press Enter.
19. Now select ```S1 Wireless LAN```, and Enter the Wifi SSID and the Password and press Enter.
<!--
need to check if the steps are correct from 17 to 19
-->
20. Select ```3 Interface Options``` using the arrow keys and press Enter.
21. Now select ```Enable legacy camera``` using the arrows keys and press Enter.
22. Repeat steps 16 and 17 but select ```Enable VNC``` using the arrows keys and press Enter.
<!--
end of not confirmed steps
-->
23. Once the wifi access is enable, after the ```pi@raspberrypi:~ $``` in the Terminal window, we need to update the system by using following commands: ```sudo apt-get update && sudo apt-get upgrade```.
24. Once the update has been done proceed to [How to install OpenCV](#chapter5).

<!--
[Link](https://pyshine.com/How-to-install-OpenCV-in-Rasspberry-Pi/) \
Step 1: Fresh installation of RPI OS steps till Step 9 \
Step 2: Connect to my acer laptop and SSH in following Access RPI OS using SSH Step 4 to 5 \
Step 3: Update raspi-config (wifi SSID “SUTD_LAB” password = none), enable legacy camera & enable VNC as well \
Step 4: ```sudo nano /etc/wpa_supplicant/wpa_supplicant.conf``` (if no connection)
-->

### Set-up with monitor <a id="chapter3"></a>
Straightaway boot into raspberry pi GUI and record the steps to update later

<!--
this steps are only relevant for me because I'm cloning the image
## change pi to new user 
Step 1: ```sudo passwd``` # set root password \
Step 2: ```sudo nano /etc/ssh/sshd_config```  # set PermitRootLogin yes \
Step 3: raspi-config # (1) system -> (5) auto login -> (B1) 1st option \
Step 4: ```sudo reboot``` \
Step 5: ssh with user/pw root; sutd \
Step 6: ```usermod -l picam1 pi``` \
Step 7: ```usermod -m -d /home/picam1 picam1``` \
Step 8: remove PermitRootLogin go back to step 2 - 3
-->

## How to install OpenCV <a id="chapter5"></a>
[Link](https://www.youtube.com/watch?v=QzVYnG-WaM4) \
Step 1: ```df -h```If you're not using most of it, ```run sudo raspi-config advanced``` # expand filesystem reboot your pi \
Step 2: ```sudo apt-get update && sudo apt-get upgrade``` \
Step 3: ```python3 -V``` \
Step 4: ```sudo apt-get install python3-pip python3-virtualenv``` \
Step 5: ```mkdir picam``` \
Step 6: ```cd picam``` \
Step 7: ```python3 -m pip install virtualenv``` \
Step 8: ```python3 -m virtualenv env``` \
Step 9: ```source env/bin/activate``` \
Step 10: ```sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev``` \
Step 11: ```pip install "picamera[array]"``` \
Step 12: ```pip install opencv-python``` \
Step 13: ```python3``` ```import cv2``` ```cv2.__version__``` \
Step 14: If there is error importing cv2 ```pip install –U numpy``` \
```pip install opencv-contrib-python``` (much longer full version) 

## How to set-up VNC 
If you prefer to work with a GUI interface you can set-up VNC so that you can access Raspberry Pi OS via GUI interface on boot. \
1. Need to refer to the github.io site that I saved for the steps to do so in onedrive under the campusx word document
Step 1: ```sudo apt-get install tightvncserver``` \
Step 2: name should be picam1; 2; etc ```vncserver :1 -name picam# -depth 16 -geometry 1280x768``` password: , view only password: no \
VNC-Viewer user: 

## Running the picam as a service 
Step 1: Copy the picam.service file into ```cd /lib/systemd/system``` and put the picam.service file in 
remember to edit the paths and might have to change to ```/usr/bin/python``` for python PATH \
Step 2: ```sudo chmod 644 /lib/systemd/system/picam.service``` \
Step 3: ```sudo systemctl daemon-reload``` \
Step 4: ```sudo systemctl enable picam.service``` \
Step 5: ```sudo reboot``` \
Step 6: Check status of service ```sudo systemctl status picam.service``` \
Step 7: picam.py is to be place in picam folder 

## Change the IP address to static 
#home

interface wlan0 \
static ip_address=192.168.1.11 \
static routers=192.168.1.254 \
static domain_name_servers=8.8.8.8 8.8.4.4

#sutd_lab

interface wlan0 \
static ip_address=10.21.135.11 \
static routers=10.21.132.1 \
static domain_name_servers=8.8.8.8 8.8.4.4

static IP address for picam1-10 10.21.135.11-20

commands to change ip address to static \
```sudo route -n``` # get the gateway ip \
```sudo nano /etc/dhcpcd.conf``` # add in the interface portion \
```sudo reboot``` \
```ifconfig``` # to check the ip address has change  