# ROS2 Multi-Turtle Letter Drawing

## 🐢 Overview
This project was developed as a final assignment for the Robotic Systems course. It utilizes ROS2 and the turtlesim simulation environment to control multiple turtles that collaboratively draw alphabetic characters. The project demonstrates multi-robot coordination, dynamic spawning, and controlled movement within a simulated space.

## 🎯 Objective
To design and implement a ROS2-based robotic system where multiple turtles work together to draw user-defined letters using precise movement control and pose coordination.


## ⚙️ Tech Stack
- Language: Python 3
- Framework: ROS2 (Foxy or later)
- Simulation: Turtlesim (ROS2 package)
- Platform: Ubuntu (tested on Ubuntu 20.04)


## 🛠️ Implementation
The system is composed of two core scripts:
- createturtle.py: Spawns additional turtles dynamically, assigns them initial positions, and manages orientation.
- drawletter.py: Controls the movement of each turtle to collectively form letters. The path and shape of the letter are predefined using turtle pose commands.


Key features:
- Multi-turtle spawning with distinct roles
- Coordinated linear/angular velocity control
- Real-time drawing of custom shapes and letters
- Logging and graceful shutdown via ROS2 node lifecycle management


## 🧪 How to Run
1. Make sure ROS2 and turtlesim are installed on your system.
2. Launch the turtlesim node:
   ```bash
   ros2 run turtlesim turtlesim_node
   
3. In a new terminal, run the turtle creation script:
   ```bash
   ros2 run <your_package_name> createturtle.py
   
4. Then run the drawing script:
   ```bash
   ros2 run <your_package_name> drawletter.py
   
Replace <your_package_name> with the name of your ROS2 package.

📄 Project Report
For details on system architecture, challenges, and results, see:
- robotics_final_project_report.docx

👤 Author
- Enes Kapsızlar

Project developed individually as part of an academic course.
