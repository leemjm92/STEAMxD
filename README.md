# :robot: STEAMxD :robot:
Robotics Challenge

Repository for STEAMxD :robot: 

## To-Do:
### Overview
- To set-up the overview readme **In-Progress**
- To include other team members into the repository
- To add in the team management timeline at projects

### Terrain
- ~~Folder for terrain/tiles design **OBSOLETE**~~
- ~~Terrain folder to-do **OBSOLETE**~~
- Find the shopee link for the source of the training modular rubber mats
- Matthew actively working on doing the final version of the terrains (mountains / slopes / etc)
 

### Robot
- ~~Adjust the M4 holes to 4.4mm for 3D printed parts of the powerbank and picam holder~~ **DONE**
- ~~The chamfer for the powerbank case can also be taller increase by 2mm in height for more rigidity~~ **DONE**
- ~~Spacer need to be reprinted use 4.5mm for it~~ **DONE**
- Need to also re-design the pi4 top case low profile **In-Progress**
- ~~Picam case to shift the holes to center and extend the L bracket portion accordingly~~ **DONE**
- ~~Shift the documentation for picam set-up from onedrive (STEAMxD -> General -> Proposal -> Documentation) to github~~ **DONE**
- Need to source the cables required for the pi4 -> powerbank (remember to measure length)
- Need to design or find a cable management tool for the 5v-12v cable **In-Progress**
- To measure the output voltage and amphere from remax and xiaomi powerbank and the 6 AA battery see if 18W is doable if not 22.5W USB-C to 12V is the solution. Alternatively, get 18650 Li-Ion batteries and case -> USB plus case -> 5.5 x 2.1 mm barrel plug / Another alternative is purchase DIY power bank UPS 18650 with 12v and USB output (taobao)
- Setup of the remaining pi4 3/4 left **In-Progress**
- Need to buy 5 more pi4 + 1 depending if the existing pi4 4gb can be used for the competition (ep-tech)

### AI
- ~~Decided on using YOLOv5 PyTorch due to ease of use and ability to do various image augmentation via DataLoaders~~ **DONE** 
- Need to explore the albumentation addition in YOLOv5 and add in the code block to test the various augmentation **In-Progress**
- Fork the YOLOv5 repo and remove the augmentation settings links are in my personal laptop to update in this repo 
- Explore the video inference output in google colab and see if I can get it working if unable to do just utilise image
- Need to figure out how to do real-time inference and display into HTML webpage (integrate with the real-time video feed page) - Figure out how to save the real-time video feed and do post-progressing to get score (ranking for actual day competition)
- Scrap the web for the required images of the miniature figurines 
- Decide on the scale of the images (need to check the pixel count and convert to cm from the jpeg image)
- Items are not to scale to ensure decent performance on the model
- For the purpose of the showcase in September, images will be printed out and pasted on foam just for demostration as we have yet to purchase the miniature items

### Rules
- ~~Template for general rules and technical rules~~ **DONE**
- Update the rules markdown to be relevant to the current competition **In-Progress**

## Progress Updates
### 23 Aug 2022 - Melvin
<!--- Template for this portion
#### Overview
#### Terrain
#### Robot
#### AI
#### Rules
--->

#### Overview
- NIL

#### Terrain
- Mountains **done**
- Slope **in-progress**

#### Robot
- Final payload of the mBot Ranger is **done**
    - Powerbank [source](https://s.lazada.sg/s.0mlvQ)
    - 5v to 12v [source](https://shopee.sg/product/161750523/4409642610?smtt=0.23355575-1661240500.10)
    - picamera v2 
    - 3d printed parts (powerbank holder, raspberry pi 4 battery slider case & picamera case) **done** 
- Set-up procedure of the picam is **done**

#### AI
- Decided on YOLOv5 PyTorch for model training (YOLOv5m - Medium model) 
- Labeling (makesense.ai), data augmentation (google colab - YOLOv5 library internal), training (google colab), inference (google colab - images confirm working, to test out video inference in colab for output) 
- For the purpose of the showcase in September, images will be printed out and pasted on foam just for demostration as we have yet to purchase the miniature items

#### Rules
- Current points system is likely to remain

## Meeting (Internal)

### 27 July 2022 - Gordon, Matthew
Ideas
- Replace the scoring system to be base on object detection only (since the goal of the earthquake scenario is to be able to rescue as many people as possible)  
  
|  1        |  2        | Autonomous Zone  |
| :-        | :-        | :-:              |
|1a   \   1b|2a   \   2b|                  |
|1c   \   1d|2c   \   2d|                  |
|  3        |  4        | Manual Zone      |
|3a   \   3b|4a   \   4b|                  |
|3c   \   3d|4c   \   4d|                  |
| Elderly Zone | Young Zone  |             |

- Full exploration of the manual zone will be limited to some % of max zone time (e.g. 80% of 5 mins - 4mins) 
    - therefore, students will have to trade off between exploring the elderly or young zone (this is in line with the scenario where exploration of one area will result in collapse of another area)
    - the **a-d** zones will be inaccessible after some % of max zone time (e.g. 50% of 5 mins - 2.5mins)
        - a zone will collapse at 2.5 mins
        - b zone will collapse at 3 mins
        - c zone will collapse at 3.5 mins
        - d zone will collapse at 4 mins
    - if zone 3 is explored, **a-d** zone that will collapse will be 4 and vice versa
- The same zone scenario will be applicable for autonomous zone

## Meeting (External)

### 21 July 2022 - Franklin (Overall workshop coordinator) and Irene (Overall logistic coordinator)
Franklin 
- selling point of the competition is AI component of it <---- using robotics
- Jeffery will be in the team not Setsuko
- Design instructions 
- When the terrain/play area done this should be informed to provide them with feedback
- Coordinate this 2 workshops 
- Level of difficulty (JC/Poly students) 
- Timing of the activity 
- Dry run of the training materials (August and September)  
- Folder in the OneDrive (part of the Team) do up the daily schedule next week
- **Teach the students how to do AI**
- **Curious above the difficulty of the AI training and actual competition day**
- **How the obstacle course will look like by August/September**

Irene (overall backend)
- Franklin (overall coordinate workshop)
- End July/Early August the requirement
- 2 cohort classroom and 2 capstone rooms for the team (5m x 5m) previous discussion
- 3D printer availibility (tentatively shift to Tuesday)
- Workshop 10am (2 hrs lunch/industry talk/campus tour)
- Schedule: 930-12, 230-430

### 19 July 2022 - Setsuko and Jeffery (HASS)
design opportunities 
- user centric design workshop 
	- influence something (fukushima radiation) 
	- earthquake urban rubbles 
	- tsunami 
- location variation that influence robots 
- ethical issues when judgement is required (incentivising and disincentivizing) 
	- skin colour
	- age 
	- basically no discrimination
- introduce objects/scene trickery 
	- pieces of bodies/body parts instead of humans
- who should the user be centered on
- AI dataset
	- generic dataset
	- variability (new classes)

Setsuko/Jeffrey human arts and social sciences
- walk away with an understanding of an design angle