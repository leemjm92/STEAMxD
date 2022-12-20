# :robot: STEAMxD :robot:
Robotics Challenge

Repository for STEAMxD :robot:

# Table of Contents
* [Overview](#chapter1)
* [Assembly](#chapter2)
    * [How to assemble the picamera module](#chapter2-1)
    * [How to access your picamera stream](#chapter2-2)
* [Technical Rules](technical-rules.md)
* [Terrain](terrain.md)
* [Robot](robot.md)
* [AI](ai.md)


## Overview <a id="chapter1"></a>

This markdown will be updated with the instructions on how to assemble the robot along with the provided raspberry pi camera unit for the purpose of the 6 Sept demo this is not the focus.

## Tools

Two tools are provided in the kit. A screwdriver that can be used for both cross head bolts and allen key head bolts. A spanner for nuts. 

<p align="center">
    <img src="/.github/images/tools0001.jpg" width="90%" title='screwdriver' />
</p>

<p align="center">
    <font size="5">Screwdriver</font>
</p>

<p align="center">
    <img src="/.github/images/tools0002.jpg" width="90%" title='screwdriver' />
</p>

<p align="center">
    <font size="5">Spanner</font>
</p>

## Bolts, nuts and etc
<!--- remember to edit the image to the same size using paint using windows ---> 
<p align="center">
    <img src="/.github/images/bolt0001.jpg" width="20%" title='Insert' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/bolt0002.jpg" width="20%" title='Spacer' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/bolt0003.jpg" width="20%" title='Brass Spacer' />
</p>

<p align="center">
    <img src="/.github/images/bolt0004.jpg" width="20%" title='M2.5 x 12mm' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/bolt0005.jpg" width="20%" title='M4 x 8mm' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/bolt0006.jpg" width="20%" title='M4 x 10mm' />
</p>

<p align="center">
    <img src="/.github/images/bolt0007.jpg" width="20%" title='M4 x 14mm' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/bolt0008.jpg" width="20%" title='M4 x 25mm' />
</p>

<p align="center">
    <img src="/.github/images/bolt0009.jpg" width="20%" title='M4 Nut Flat' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/bolt0010.jpg" width="20%" title='M4 Nut w/ext' />
</p>

## Assembly <a id="chapter2"></a>

Follow the instructions of the mBot instruction set from page 19 onwards. After reaching step 15 (page 23) please proceed to skip step 16 and step 17 and complete step 18. Once step 18 is completed please proceed to the next section on [How to assemble the picamera module](#chapter2-1)

### Assembly of mBot ranger and camera module

<p align="center">
    <img src="/.github/images/ranger0001.jpg" width="90%" title='step 1-3' />
</p>

<p align="center">
    <img src="/.github/images/ranger0002.jpg" width="90%" title='step 4-7' />
</p>

<p align="center">
    <img src="/.github/images/ranger0003.jpg" width="90%" title='step 8-11' />
</p>

<p align="center">
    <font size="5">For steps 9 and 10 please replace with the 3D printed battery holder and the provided battery powerbank</font>
</p>

<p align="center">
    <img src="/.github/images/ranger0003-01.jpg" width="35%" title='3D printed battery holder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/ranger0003-02.jpg" width="35%" title='Battery powerbank' />
</p>

<p align="center">
    <img src="/.github/images/ranger0004.jpg" width="90%" title='step 12-15' />
</p>

<p align="center">
    <img src="/.github/images/ranger0005.jpg" width="90%" title='step 16-18' />
</p>

<p align="center">
    <img src="/.github/images/ranger0006.jpg" width="90%" title='step 4' />
</p>

<!--- 
To be updated with instructions on how to assemble the esp32cam to the mBot 

When ESP32Cam is powered on, wait for 10-15sec then access the image via the link in [How to access your camera stream](#chapter2-2)

--->



<!---

### How to assemble the picamera module  <a id="chapter2-1"></a>

<p align="center">
    <b>Step 1</b>: Attached the picamera housing to the robot frame
</p>

<p align="center">
    <img src="/.github/images/picam-step1.jpg" width="45%" title='step 1' />
</p>

<p align="center">
    <b>Step 2</b>: Once the picamera is attached to the frame, loop the ribbon cable and insert the ribbon cable into the raspberry pi 4. Follow the steps below to ensure that you've attached the ribbon cable correctly to the raspberry pi 4.
</p>

<p align="center">
    <img src="/.github/images/picam-step2.jpg" width="45%" title='step 2' />
</p>

<p align="center">
    <img src="/.github/images/picam-step3.jpg" width="45%" title='step 3' />
</p>

<p align="center">
    <img src="/.github/images/picam-step4.jpg" width="45%" title='step 4' />
</p>

<p align="center">
    <img src="/.github/images/picam-step5.jpg" width="45%" title='step 5' />
</p>

<p align="center">
    <img src="/.github/images/picam-step6.jpg" width="45%" title='step 6' />
</p>

<p align="center">
    <b>Step 3</b>: Place the raspberry pi 4 into the holder and proceed to mBot instruction set step 16 (page 24)
</p>

<p align="center">
    <img src="/.github/images/picam-step7.jpg" width="45%" title='step 7' />
</p>

<p align="center">
    <b>Step 4</b>: Secure the housing to the robot frame 
</p>

<p align="center">
    <img src="/.github/images/picam-step8.jpg" width="45%" title='step 8' />
</p>

<p align="center">
    <b>Step 5</b>: Place the provided powerbank and power on your raspberry pi 4
</p>

<p align="center">
    <img src="/.github/images/picam-step9.jpg" width="45%" title='step 9' />
</p>

--->

### How to access your camera stream <a id="chapter2-2"></a>

Group 21 (camera1) - [link](http://10.21.135.99:9000) \
Group 22 (camera2) - [link](http://10.21.140.11:9000) \
Group 23 (camera3) - [link]() \
Group 24 (camera4) - [link]() \
Group 25 (camera5) - [link]() \
Group 26 (camera6) - [link]() \
Group 27 (camera7) - [link]() \
Group 28 (camera8) - [link]() \
Group 29 (camera9) - [link]()