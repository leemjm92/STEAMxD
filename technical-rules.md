# :robot: Technical Rules :robot:

<p align="center">
    <img src="/.github/images/steamxd-logo.jpg" width="80%"/>
</p>

<div align="center">Organised by </div> 
<p align="center">
    <img src="/.github/images/sutd-logo.jpg" width="18%"/>
</p>

# Table of Contents
* [STEAMxD Competition 2022](#chapter1)
* [Game Fields](#chapter2)
    * [Competition Zone (Outdoor)](#section-2-1)
    * [Competition Zone (Indoor)](#section-2-2)
* [Key Field Items](#chapter3)
* [Robot Requirements](#chapter4)
* [Scoring Metrics](#chapter5)
    * [Accessibility](#section5-1)
    * [Object Detection](#section5-2)

## STEAMxD Competition 2022 <a id="chapter1"></a>
STEAMxD is a competition where undergraduate student groups would learn the basics of object detection algorithms, AI model training and ethics. They would be using robots to navigate through a game arena and making ethical decisions along the way, scoring points for determining the winner for the competition.

## Game Fields <a id="chapter2"></a>
### Competition Zone (Outdoor) <a id="section-2-1"></a>
<p align="center">
    <img src="/.github/images/outdoor_top_topview.jpeg" width="45%" title='Outdoor (Top Half)' />
</p>
<p align="center">
    <img src="/.github/images/outdoor_btm_topview.jpg" width="45%" title='Outdoor (Bottom Half)' />
</p>

### Competition Zone (Indoor) <a id="section-2-2"></a>
<p align="center">
    <img src="/.github/images/indoor_top_topview.jpg" width="45%" title='Indoor (Top Half)' />
</p>
<p align="center">
    <img src="/.github/images/indoor_btm_topview.jpg" width="45%" title='Indoor (Bottom Half)' />
</p>

## Key Field Items <a id="chapter3"></a>

<p align="center">
    <img src="/.github/images/adult0001.jpg" width="20%" title='testing1' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/rabbit0001.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/dog0001.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/cat0001.jpg" width="20%" title='placeholder' />
</p>

<p align="center">
    <hx><b>Human&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;Rabbit&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;Dog&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;Cat</b></hx>
</p>

## Robot Requirements <a id="chapter4"></a>
1. Each team should prepare and bring along their own spare parts, equipment, posters and laptops (if necessary). RIC will not provide any of these during the competition.
2. No team should be sharing the same laptop or robot program. It will be deemed as cheating if any team is found to do so, and will be immediately disqualified from the RIC.
3. If a team is found to use solutions identical to external or online resources, or solutions that are clearly designed/made by adults, an investigation will be carried out and the team will be required to justify the originality of their solutions.
    * Logbook, design drafts and/or photos of intermediate prototypes with time stamps may be requested by the organising committee to support the investigation. Hence, we encourage all teams to properly document their work, and treat it as a good learning experience.
    
1. RIC 2021 is for autonomous robots.
    * After the robot has been started (performed any action, e.g. moving, transforming, displaying etc.), the team would no longer be allowed to interfere with or control the robot’s actions (e.g. attempt to communicate with it via radio, wireless/sound control, wired control etc.).
    * The robot must be able to stop by itself, instead of being manually stopped by the team (such as via pressing a button, grabbing the robot etc.).
2. There is no limitation on the brand of hardware/software used. We encourage all participating teams to explore diverse options (even building your own ones!) and adopt the solution they deem to be most suitable for the RIC.

## Scoring Metrics <a id="chapter5"></a>

### Object Detection Challenge (80% of total score)<a id="section5-1"></a>
Object detection challenge will test the team's ability to train a model that is capable of detecting humans and animals. 

Scoring  

| Class     | Points |
| :-:       | :-:    |
| Humans    | 5      |
| Animal    | 3      |
<!--- | Valuables | 3      | --->

1. In order for a detection to be counted as succesful, the confidence score has to be above 50% (to be adjusted accordingly) and the object should be detected for a minimal of 1 second (to be adjusted accordingly).
**Matt: insert an example of the detection as picture of successful detection or should I use a video instead?** --->
2. Every unique object that the team successfully detects accurately will be awarded the corresponding points based on the table above. Below is an example for illustration purpose
    * Example Team A successfully detects 10 out of 15 of the humans and 15 out of 18 of the animals \
    Total possible points = $15 \times 5 + 18 \times 3 = 129$ \
    Team A points = $10 \times 5 + 15 \times 3 = 95$ \
    Score as a weightage = $95 \div 129 \times 100 = 73.64$% 

Scoring is split into 2 categories: object detection and hidden objectives. 

Object detection will take up a weightage of 80% while the hidden objectives will take up a weightage of 20% 

Under the object detection category, a successful ‘rescue’ is accomplished when you’ve correctly identified the ‘civilians’/’pets’ for a minimum of 1 second. 

For each successful ‘civilians’ ‘rescue’, 5 points is award. For each successful ‘pets’ ‘rescue’ 3 points is award.  

Below is an example of points calculation for object detection category: 
xxxxx

Under the hidden objective category, teams that can successfully complete the hidden objectives will be awarded points up to a maximum weightage of 20%. 

Below is an example of points calculation for the hidden objective category: 
xxxxx

### Achievements (20% of total score)<a id="section5-2"></a>
Each achievement is worth 3% the maximum points for achievements will be capped at 20%.

* Example Team A manages to get 8 achievements the maximum you can score for this component is only 20%. \
Team A points = $8 \times 3 = 24$ (capped at 20%) \

1. Hidden achievement #1 (outdoor arena) 
2. Hidden achievement #2 (indoor arena)
3. Most humans detected 
4. Most cats detected 
5. Most dogs detected 
6. Most rabbits detected 
7. Fastest time completion per arena (outdoor/indoor)  
8. Most accurate detection model overall (all 4 classes) 
9. Most accurate detection model for humans 
10. Most accurate detection model for cats 
11. Most accurate detection model for dogs 
12. Most accurate detection model for rabbits 