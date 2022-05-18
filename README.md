# Inverse Kinematics 

The project implements inverse kinematics for a three degree rotational robot arm in order to minimize an objective function in whilst maintaining physical constraints.  

The repository contains code for forward kinematics (fk.py), inverse kinematics (ik-a.py , ik-b.py) and collision functions.

**Output:** 

The first image shows the output of minimizing the objective function from source (green) to destination (red).

![Output 1](https://github.com/vakharia-aarya/Inverse-Kinematics/blob/main/output1.png)


The image below shows the output of running the inverse kinematics program but with an obstacle in the search space. The robot arm finds the shortest path from source to destination while avoiding the obstacle.

![Output 2](https://github.com/vakharia-aarya/Inverse-Kinematics/blob/main/output2.png)

