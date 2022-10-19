# :robot: Technical Rules :robot:

# Table of Contents
* [Challenge Rules](#chapter1)
* [Game Fields](#chapter2)
    * [Technical Competition Zone 1](#section-2-1)
    * [Technical Competition Zone 2](#section-2-2)
    * [Technical Competition Zone 3](#section-2-3)
    * [Technical Competition Zone 4](#section-2-4)
* [Key Field Items](#chapter3)
* [Robot Requirements](#chapter4)
* [Scoring Metrics](#chapter5)
    * [Accessibility](#section5-1)
    * [Object Detection](#section5-2)

## Challenge Rules <a id="chapter1"></a>
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text
Placeholder text 

## Game Fields <a id="chapter2"></a>
### Technical Competition Zone 1 <a id="section-2-1"></a>
![placeholder-image](terrain/design/top-view.png)


1. All teachers and team members must be pre-registered in order to enter the venue.
2. Each team should prepare and bring along their own spare parts, equipment, posters and laptops (if necessary). RIC will not provide any of these during the competition.
3. No team should be sharing the same laptop or robot program. It will be deemed as cheating if any team is found to do so, and will be immediately disqualified from the RIC.
4. If a team is found to use solutions identical to external or online resources, or solutions that are clearly designed/made by adults, an investigation will be carried out and the team will be required to justify the originality of their solutions.
    * Logbook, design drafts and/or photos of intermediate prototypes with time stamps may be requested by the organising committee to support the investigation. Hence, we encourage all teams to properly document their work, and treat it as a good learning experience.

### Technical Competition Zone 2 <a id="section-2-2"></a>
![placeholder-image](terrain/design/top-view.png)

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
Humans, Pets, Valuables

## Robot Requirements <a id="chapter4"></a>

## Scoring Metrics <a id="chapter5"></a>
### Accessibility <a id="section5-1"></a>
1. Every path set that the robot successfully navigates across will be awarded with 1 point (e.g. Successfully navigated across $6 \over 7$ path set; score $6 \over 7$ $\times 50$ = $42.86 \over 50$ points) 

### Object Detection <a id="section5-2"></a>
Scoring  

| Class     | Points |
| :-:       | :-:    |
| Humans    | 5      |
| Pets      | 3      |
| Valuables | 3      |

3. Every unique object that the team successfully detects accurately will be awarded the corresponding points based on the mode of detection (manual or AI), scoring calculation will always be upon total possible points via AI mode. Below is and example for illustration purpose
    * Example for a successful detection of $5 \over 7$ humans, $3 \over 5$ pets and $6 \over 10$ valuables  
    Total possible manual points = $7 \times 5 + 5 \times 3 + 10 \times 1 =  60​$  
    Total possible AI points = $7 \times 15 + 5 \times 9 + 10 \times 3 =  180$  
    If team chooses manual mode, score = $40 \over 180$ = $11.11 \over 50$  
    If team chooses autonomous mode, score = $120 \over 180$ = $33.33 \over 50$
