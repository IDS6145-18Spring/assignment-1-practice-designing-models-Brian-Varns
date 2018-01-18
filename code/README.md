## Air Pollution Control System Model

There will be one component, Air Pollution Control, with four sub-components Sensors, Agents, Population, and City Leaders.  Sensors will collect data from the atmosphere around the city block and notify the Population on the EPA pollutants in their area.  If the EPA pollutants are too high the system will notify the population that it is unsafe to conduct specific activities like exercise outside, walk your pet, etc.  The alerts they receive will be determined by the amount of EPA pollutants in their area.

Additionally, I'll look at the impacts these sensors have on city leaders and their decision making for day to day operations of the city.  As data comes in city leaders can make decisions to close certain bridges and reroute traffic to help control the level of pollutants in an area.

![Class Diagram](images/APCSClassDiagram.png)

## Coding Framework
Starting coding framework for the Air Pollution Control System.

[Air Pollution Control](https://github.com/IDS6145-18Spring/assignment-1-practice-designing-models-Brian-Varns/blob/master/code/APC_system/Air_Pollution_Control.py)

This code provides the starting framework for Air Pollution Control, which is the primary hub for the simulation.  This code will "get" the agents and release them into the environment to be detected by the Sensors.

[Agents](https://github.com/IDS6145-18Spring/assignment-1-practice-designing-models-Brian-Varns/blob/master/code/APC_system/Agents.py)

This code provides the starting framework for Agents, which in this case are EPA pollutants.  The primary pollutants that can be dectected by the sensors are given names and values, which will be adjusted based on the level of pollutants released into the environment.

[Sensors](https://github.com/IDS6145-18Spring/assignment-1-practice-designing-models-Brian-Varns/blob/master/code/APC_system/Sensors.py)

This code provides the starting framework for Sensors and the systems that comprise it.  The primary reason for this code is to initialize the many components and their responsibilities, which will be further defined in future code.

[Population](https://github.com/IDS6145-18Spring/assignment-1-practice-designing-models-Brian-Varns/blob/master/code/APC_system/Population.py)

This code provides the starting framwork for the Population.  Here we can see what sort of activities the indiviudal is conducting at the time of the alert and their reaction to it.  Do they stay outside, seek shelter, conduct exercise, walk the dog, etc.

[City Leaders](https://github.com/IDS6145-18Spring/assignment-1-practice-designing-models-Brian-Varns/blob/master/code/APC_system/City_Leaders.py)

This code provides the starting framwork for the City Leaders.  It is similar to that of the Population, but with one main difference, making decisions.  These decisions occur after the alerts are recieved.