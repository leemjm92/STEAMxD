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
* [Scoring Metrics](#chapter5)
    * [Accessibility](#section5-1)
    * [Object Detection](#section5-2)

## STEAMxD Competition 2022 <a id="chapter1"></a>
STEAMxD is a competition where undergraduate student groups would learn the basics of object detection algorithms, AI model training and ethics. They would be using robots to navigate through a game arena and making ethical decisions along the way, scoring points for determining the winner for the competition.

## Game Fields <a id="chapter2"></a>
### Competition Zone (Outdoor) <a id="section-2-1"></a>
<p align="center">
    <img src="/.github/images/outdoor-arena.jpg" width="55%" title='Outdoor Arena' />
</p>

### Competition Zone (Indoor) <a id="section-2-2"></a>
<p align="center">
    <img src="/.github/images/indoor-arena.jpg" width="55%" title='Indoor Arena' />
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
4. Most cats detected 
5. Most dogs detected 
6. Most rabbits detected 
7. Fastest time completion per arena (outdoor/indoor)  
8. Most accurate detection model overall (all 4 classes) 
9. Most accurate detection model for humans 
10. Most accurate detection model for cats 
11. Most accurate detection model for dogs 
12. Most accurate detection model for rabbits 