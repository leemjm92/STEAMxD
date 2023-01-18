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
* [Key Field Items](#chapter3)
* [Scoring Metrics](#chapter5)
    * [Accessibility](#section5-1)
    * [Object Detection](#section5-2)

## STEAMxD - AI Rescue Operation Challenge 2023 <a id="chapter1"></a>

In this challenge, your team will need to combine all elements of STEAM x D to carry out the mission of rescuing victims from a disaster area using robots equipped with AI image recognition technology. Using state of the art AI-powered robots, your team will first need to modify and retrofit the robot to carry an onboard camera. This will be achieved using computer-aided design (CAD) and 3D printing technologies.

Your team will be tasked to explore a region of (120m x 50m). Given that it is a search and rescue mission, your team will have to navigate the terrain and successfully ‘rescue’ the injured/trapped ‘victim’/’pets’. A successful ‘rescue’ is accomplished when you’ve correctly identified the ‘civilians’/’pets’ for a minimum of 1 second.

In a single arena, a total of 15 minutes has been allocated for you to compete. You can attempt as many rescues as you need within the allocated time. Of all the attempts, the best attempt will be the score awarded to your team. Do note that another team will also be operating in the same 5 x 2.5m terrain area and you will need to communicate and negotiate the arena to ensure that no collisions take place.

There will be a total of 2 different arenas, outdoor and indoor, for which you will get 15 min on each terrain for your team to attempt. The overall score will be the sum of both mission scores.

## Game Fields <a id="chapter2"></a>

<p align="center">
    <hx><b>Outdoor Arena&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &nbsp; &nbsp; &nbsp; Indoor Arena</b></hx>
</p>

<p align="center">
    <img src="/.github/images/outdoor-arena-label.jpg" width="45%" title='Outdoor' />
<!--     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -->
    <img src="/.github/images/indoor-arena-label.jpg" width="45%" title='Indoor' />
</p>

<p align="center">
    <img src="/.github/images/outdoor-arena-box.jpg" width="45%" title='Outdoor' />
<!--     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -->
    <img src="/.github/images/indoor-arena-box.jpg" width="45%" title='Indoor' />
</p>

1. The <span style="color:blue">blue arrow tape</span> (<span style="color:green">green circle</span> in the image above) indicates the starting position for your robot.
2. The <span style="color:blue">solid blue tape</span> (<span style="color:orange">orange rectangle</span> in the image above) in the middle defines the 1st half and 2nd half of the zone. 
3. The <span style="color:blue">blue</span>/<span style="color:silver">silver</span>/black dotted tape (<span style="color:red">red rectangle</span> in the image above) near the exit defines that you’re no long able to reverse into the field. 
4. If your robot is out of bounds (100% of the robot is out of the mat) your run will be stopped, and you will have to start from the beginning of the arena again as indicated by the <span style="color:blue">blue arrow tape</span> (<span style="color:green">green circle</span> in the image above).
5.If your robot is unable to move, you will be allowed to reset the robot to an upright position without penalty. This will be done by the judge in-charge of your arena.
5. Teams are only allowed to be within the red and silver box at the respective arena. **You're not allowed to move out of the red or silver box once you've entered the arena**

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

## Scoring Metrics <a id="chapter5"></a>

### Object Detection Challenge (80% of total score)<a id="section5-1"></a>
Object detection challenge will test the team's ability to train a model that is capable of detecting humans and animals. 

Scoring  

| Class     | Points |
| :-:       | :-:    |
| Humans    | 5      |
| Animals (Cats, Dogs, Rabbits) | 3      |
<!--- | Valuables | 3      | --->

1. For a detection to be counted as successful, the confidence score must be above 30% and the object should be detected for a minimal of 1 second.
2. Every unique object that the team successfully detects accurately will be awarded the corresponding points based on the table above.  Below is an example for illustration purpose. 
    * __Example 1__: Team A successfully detects 15 out of 15 of the humans and 18 out of 18 of the animals \
    Total possible points = $15 \times 5 + 18 \times 3 = 129$ \
    Team A points = $15 \times 5 + 18 \times 3 = 129$ \
    Score as a weightage = $129 \div 129 \times 100 = 80$% 
    * __Example 2__: Team B successfully detects 10 out of 15 of the humans and 15 out of 18 of the animals \
    Total possible points = $15 \times 5 + 18 \times 3 = 129$ \
    Team A points = $10 \times 5 + 15 \times 3 = 95$ \
    Score as a weightage = $95 \div 129 \times 80 = 58.9$% 

### Achievements (20% of total score)<a id="section5-2"></a>
Each achievement is worth 3% the maximum points for achievements will be capped at 20%.

* Example Team A manages to get 8 achievements the maximum you can score for this component is only 20%. \
Team A points = $8 \times 3 = 24$ (capped at 20%)

1. Hidden achievement #1 (outdoor arena) 
2. Hidden achievement #2 (indoor arena)
3. Most humans detected 
4. Most pets detected 
5. Fastest time completion per arena (outdoor/indoor)  
6. Most accurate detection model overall (all 2 classes) 
7. Most accurate detection model for humans 
8. Most accurate detection model for pets 
