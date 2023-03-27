# Pi in the sky project
By Nathaniel and Thomas

**Project Goal: Launch a Raspberry Pi into the air and have it record data then land safely**

## Project Planning

### Project Outline
  To make a mortar that launches water rockects out of it by throwing one in and it getting punctured through the cap by a nail at the bottom of the mortar to then launch the rocket.
  
### Materials
  + Cvc Pipe
  + Sharp Nail
  + 2L Soda Bottle
  + Nose Cone(3d Printed)
  + Fins(3d Printed)
  + Parachute
  + Casing for Electronice(3d Printed/Lasercut)
  + Electronics
    + Raspberry Pi
    + Altimeter
    + Battery 
    + Circuit Board
    
### Function
  The mechanism for how the mortar is very simple. You throw a pressurized water rocket into the mortar and when it hits the bottom, there is a nail that punctures the cap of the water rocket, releasing the pressure and propelling the rocket upwards. The mortar itself will be a simple cvc pipe that is set at an angle on a stand to send the water rocket in an ark, like a mortar.
  
### What we need to learn
  We need to figure out the ideal size of the cvc pipe to optimize the launch, as well as figure how to design the rocket itself. Specifically we need to design an area to safely hold the raspberry pi and whether we would need a parachute or not. Also, we need to figure out how water pressure works and what the best way to optimize it is for our purposes.
  
### What is success?
  Have a functionioning Mortar that can effectively launch multiple water rockets at a time without flaw and having one of the rockets measure the height it reaches and possibly measure it's arc and the distance it travels as well. Also, try to make the rockets go as high and as far as we can.
  
### Saftey concerns/Risk Mitigation
  The risks of the water rocket is the highly pressurized water that could hurt someone or certainly get someone wet. To mitigate these risks we will make sure everone is using proper PPE and make sure everyone is far enough away at launch. Another risk is the nail in the bottom of the mortar which will be very sharp, we will mitigate this risk by handiling the nail safely and as little as possible. The only other risk is the flight path of the rocket, we will mitigate this risk by making sure everyone is out of the way in the way the mortar is pointing as to not hit anyone.
  
### Iterations 

+ #### Debates about the protection of the components
   + No parachute or substantial protection. Cons: All components would break constant replacement and Mr. Miller angry. Pros: Very light and Easy
   + Substantial protection through securing electronics to wall of the cone. Cons: Components would probably still break, Mr Miller probably angry. Pros: Very light, might provide some protection
   + Peanut Butter protection. Cons: Messy, Ruins the electornics, 3d printed stuff would still break. Pros: Peanut Butter, Electronics wouldn't break?
   + **Parachute. Cons: Heavier, hard to design, might not work. Pros: Should protect electronics and all components.**
+ #### Launching Mechanism
   + Rocket launcher. Cons: Lame, boring, unoriginal. Pros: It would go very high, Very easy to make/use, safe.
   + **Mortar. Cons: Rocket can't get as high, slightly unsafe. Pros: Awesome, goes in a measurable? arc, can launch multiple rockets/shells**
   + Truck Rockets. Cons: Nothing at all, "unsafe". Pros: Awesome, moveable, on a golf cart.
 
### Schedule

T < December 5, Planning and document

December 5 < T < December 25, Onshape design

December 25 < T < January 25, Coding

January 25 < T < March 1, Testing and refineing rocket 

March 1 < T < April 1, Installation and testing of electronics and tracking device, and parachute.

April 1 < T < Spring break, Final testing and tweaking

### Diagrams

#### Rocket Diagram
<img src="images/Rocket%20Sketch.jpg" alt="Left View" width="500" height="500">

#### Mortar Diagram
<img src="images/Mortar%20Sketch.jpg" alt="Left View" width="500" height="500">

#### Block Diagram
<img src="images/Block%20diagram.jpg" alt="Left View" width="500" height="500">

## Project Timeline

### Week 1(Dec. 5th - Dec. 9th)

#### Goals

Start designing the rocket and mortar in onshape and get a good idea of what the project is going to look like.

#### Progress

+ Rough Mortar design in onshape
<img src="images/Mortardesign1.PNG" alt="Left View" width="300" height="300">

+ Brainstorming - Figuring out exact ideas for the shell of the bottle rocket, mortar will be set at 45 degree angle to maximize distance.

### Week 2(Dec. 12th - Dec. 16th)

#### Goals

Continue work on rocket shell and refine ideas for assembley and specifics of the mechanisms of the rocket and what it'll be able to do

#### Progress 

+ Intial design of rocket mostly complete, created the casing that will go around the actual bottle. Still need to design the area to hold the electronics and parachute

+ Concept for launch sequence mostly formulated and designed, pvc cap will have a hole drilled through it to hold the nail which will pierce the bottle and launch it. There will also be holes to drain excess water from the bottom of the mortar through the cap

+ Design for mortar holder completed 

+ Brainstorming - Best way to integrate a parachute while also fufilling perameters of the project is to have servos in the top of the rocket casing to spin, releasing the cap of the rocket casing, allowing the parachute to deploy. These servos will activate the parachute at a set height which will be calculated using an altimeter in the rocket.

### Week 3(Jan. 3rd - Jan. 6th)

#### Goals

Finish the onshape design for the project and make sure the rocket casing will be able to hold all electronics that are needed and fully be able to fufill our project goals

#### Progress

+ Completion of the onshape design for the rocket casing
<img src="images/Rocketcasing1.PNG" alt="Left View" width="500" height="500">

+ Completion of holders for electornics inside casing(Circuit board, Servos)

#### Servo Design
<img src="images/Electronic1.PNG" alt="Left View" width="250" height="250">

#### Circuit Board Design
<img src="images/Electronic2.PNG" alt="Left View" width="250" height="250">

### Week 4(Jan. 9th - Jan. 13th)

#### Goals

Starting the coding process and formulating how the parchute will deploy

#### Progress

+ Starting the code for the parachute trigger when the rocket reaches a certain altitude and for the button to reattach the nose cone

+ [Code for the parachute](https://github.com/nmckee78/Piintheskyrocket/blob/main/servo_code).

+ Brainstorming Ideas - What angle do the servos need to be to properly release? - Answer: 180, How to make sure the parachute won't get stuck on the servos? - Answer: Some sort of protective layer or sheet between the two, not fully figured out, Will the servos have enough power to hold the cone on all by themselves - Answer: Need to test to find out

### Week 5(Jan. 17th - Jan. 20th)

#### Goals

Create code for data collection 

#### Progress 

+ Started coding for the data collection, got pretty stuck.

+ [Assembled Code](https://github.com/nmckee78/Piintheskyrocket/blob/main/servo_code).

### Week 6(Jan. 23rd - Jan. 27th)

#### Goals

Continue to work on code, brainstorm ideas to improve the rocket.

#### Progress

+ Continued to try to work out the code, continued to be stuck

+ Brainstormed ideas to improve the rocket(Incl. Smaller nose cone, Weight reducing in bottom of rocket, better threads.

+ 3d printed first part of the rocket, went well

### Week 7(Jan. 30th - Feb. 3rd)

#### Goals

Keep working on code, implement rocket ideas

#### Progress 

+ Started to figure out the code but still not implementing it

+ Discussed more ways to reduce weight and increase efficency in the rocket 

+ Added more slits in bottom of rocket, 3d printed test threads(Did not work)

+ Made new threads 

### Week 8(Feb. 6th - Feb. 10th)

#### Goals

Actually finish the code, get more pieces of the rocket, continue to refine rocket design

#### Progress

+ Finished the code! 

+ [Final code](https://github.com/nmckee78/Piintheskyrocket/blob/main/servo_code).

+ Printed middle part of rocket, might need to redesign, kinda flimsy

+ Printed working threads 

+ Continued to improve cad design

+ Started to think about parachute implemenation


### Week 9(Feb 13- Feb 17th)

#### Goals

-Make the parachute.

#### Progress
- This week I made the parachute. I did this by cutting out a 50 cm radius circle from trash bag. I then put duck tape patchs around the edge for reanforcement, and punched holes for strings. I tied strings to the hols than tied all of those to a main cord and the parachute was done.



### Week 9(Feb 20- Feb 24th)

#### Goals
Fly the paracute successfully.

#### Progress

-We threw the parachute off the hill tied to a 2x4 and it succesfully deployed. At first it was not openning in time and we discoverd that to make it open fast enough we had too shorted the main cord and not fold it as many times. After this innnovation we succeded in makeing it work consistanly.
![tttttttttttttttttttttttttttttttttttttttt](https://user-images.githubusercontent.com/71349802/228027597-664a32d2-6511-4d61-bc7f-eef399ca2184.gif)





