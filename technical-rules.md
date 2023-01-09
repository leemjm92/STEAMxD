# :robot: Technical Rules :robot:

# Table of Contents
* [STEAMxD Competition 2022](#chapter1)
* [Game Fields](#chapter2)
    * [Technical Competition Zone (Outdoor)](#section-2-1)
    * [Technical Competition Zone (Indoor)](#section-2-2)
    * [Technical Competition Zone 3](#section-2-3)
    * [Technical Competition Zone 4](#section-2-4)
* [Key Field Items](#chapter3)
* [Robot Requirements](#chapter4)
* [Scoring Metrics](#chapter5)
    * [Accessibility](#section5-1)
    * [Object Detection](#section5-2)

## STEAMxD Competition 2022 <a id="chapter1"></a>
STEAMxD is a competition where undergraduate student groups would learn the basics of object detection algorithms, AI model training and ethics. They would be using robots to navigate through a game arena and making ethical decisions along the way, scoring points for determining the winner for the competition.

## Game Fields <a id="chapter2"></a>
### Technical Competition Zone (Outdoor) <a id="section-2-1"></a>
<p align="center">
    <img src="/.github/images/outdoor_top_topview.jpeg" width="45%" title='Outdoor (Top Half)' />
<!--     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -->
    <img src="/.github/images/outdoor_btm_topview.jpg" width="45%" title='Outdoor (Bottom Half)' />
</p>

1. Each team should prepare and bring along their own spare parts, equipment, posters and laptops (if necessary). RIC will not provide any of these during the competition.
2. No team should be sharing the same laptop or robot program. It will be deemed as cheating if any team is found to do so, and will be immediately disqualified from the RIC.
3. If a team is found to use solutions identical to external or online resources, or solutions that are clearly designed/made by adults, an investigation will be carried out and the team will be required to justify the originality of their solutions.
    * Logbook, design drafts and/or photos of intermediate prototypes with time stamps may be requested by the organising committee to support the investigation. Hence, we encourage all teams to properly document their work, and treat it as a good learning experience.

### Technical Competition Zone (Indoor) <a id="section-2-2"></a>
<p align="center">
    <img src="/.github/images/indoor_top_topview.jpg" width="45%" title='Indoor (Top Half)' />
<!--     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -->
    <img src="/.github/images/indoor_btm_topview.jpg" width="45%" title='Indoor (Bottom Half)' />
</p>

1. RIC 2021 is for autonomous robots.
    * After the robot has been started (performed any action, e.g. moving, transforming, displaying etc.), the team would no longer be allowed to interfere with or control the robot’s actions (e.g. attempt to communicate with it via radio, wireless/sound control, wired control etc.).
    * The robot must be able to stop by itself, instead of being manually stopped by the team (such as via pressing a button, grabbing the robot etc.).
2. There is no limitation on the brand of hardware/software used. We encourage all participating teams to explore diverse options (even building your own ones!) and adopt the solution they deem to be most suitable for the RIC.

### Technical Competition Zone 3 <a id="section-2-3"></a>
![placeholder-image](terrain/design/top-view.png)

1. There are in total 3 important areas in the venue: the Competition Area, Preparation Area and Audience Area.
    * The Competition Area is where all the graded competitions will take place. Each team can only enter the competition area during their assigned time slot and leave the area upon finishing the challenge.
    * The Preparation Area is a holding area when teams are not currently taking part in the challenge. Each team will have their own designated area where they can have internal discussions, modify their strategy, observe other teams or simply take a rest.
    * The Audience Area is where teachers of various teams should stay during the RIC, to allow them to observe the competition and take photos if they wish to. Participating teams will be permitted to come to the Audience Area and interact with their teachers when it is not their turn to compete. However, they will not be allowed to bring along any part of the robot or the robot in whole, nor can they bring their laptop(s) or any storage device to the Audience Area.

### Technical Competition Zone 4 <a id="section-2-4"></a>
![placeholder-image](terrain/design/top-view.png)

1. Damaging or destroying anything in the venue that the team does not own (e.g. game fields, tables, chairs, venue decorations, robots of other teams etc.).
2. Bringing any medium of communication (both electronic or otherwise) into the competition area or attempting to communicate with anyone outside the competition area when teams are in the middle of completing the challenge.
3. Bringing any food or drinks into the competition area. 
4. Teachers / other teams outside the competition area attempting to communicate with teams in the competition area.
5. Any other behaviours that the organising deem as directly/indirectly interfering with the competition or affecting other teams (e.g. use of dangerous items or inappropriate words, fighting, chasing etc.).


## Key Field Items <a id="chapter3"></a>
![placeholder-image](terrain/design/top-view.png)


Humans, Animals (Rabbits, Dogs, Cats)

## Robot Requirements <a id="chapter4"></a>

## Scoring Metrics <a id="chapter5"></a>

### Object Detection Challenge(80% of total score)<a id="section5-1"></a>
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

### Achievements (20% of total score)<a id="section5-2"></a>
Achievements will test the team's ability across various domains; humanities, engineering, etc.


**Matt: Should there be a limit on the number of achievements each team can achieve? 
How much should each achieve be award this will be weight % so it should be carefully balanced with the object detection scoring or we can give slightly different weightage for different achievement (because we have to balance VIP path)** 
--->

**To be discussed an balanced with Matthew/undergrads on 4-6 Jan** 

1. Saving VIP
2. Most humans detected
3. Most pets detected
4. Most valuables detected
5. Fastest time taken for path
6. Most accurate detection model (separate into individual categories?)
7. Most checkpoints encountered