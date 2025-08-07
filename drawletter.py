import subprocess
import threading
import time

def publish_twist_command(topic, linear, angular):
    cmd = [
        "ros2", "topic", "pub", "--once", topic, "geometry_msgs/msg/Twist",
        f"{{linear: {{x: {linear['x']}, y: {linear['y']}, z: {linear['z']}}}, "
        f"angular: {{x: {angular['x']}, y: {angular['y']}, z: {angular['z']}}}}}"
    ]
    subprocess.run(cmd)

def execute_commands(commands):
    for cmd in commands:
        publish_twist_command(*cmd)
        time.sleep(1)

turtle1_cmd = [
    ("/turtleg/turtle1/cmd_vel", {"x": 1.3, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": 0.2, "y": -0.2, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": 0.0, "y": -1.5, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": -0.2, "y": -0.2, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": -2.2, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": -0.4, "y": 0.4, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": 0.0, "y": 3.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": 0.4, "y": 0.4, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": 2.2, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtleg/turtle1/cmd_vel", {"x": 0.4, "y": -0.4, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
]

turtle2_cmd = [
    ("/turtlej/turtle1/cmd_vel", {"x": 1.0, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlej/turtle1/cmd_vel", {"x": -2.0, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlej/turtle1/cmd_vel", {"x": 1.0, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlej/turtle1/cmd_vel", {"x": 0.0, "y": -3.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlej/turtle1/cmd_vel", {"x": -0.2, "y": -0.2, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlej/turtle1/cmd_vel", {"x": -0.7, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlej/turtle1/cmd_vel", {"x": -0.4, "y": 0.4, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
]

turtle3_cmd = [
    ("/turtlem/turtle1/cmd_vel", {"x": 0, "y": 3.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlem/turtle1/cmd_vel", {"x": 1.5, "y": -1.5, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlem/turtle1/cmd_vel", {"x": 1.5, "y": 1.5, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlem/turtle1/cmd_vel", {"x": 0, "y": -3.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
]

turtle4_cmd = [
    ("/turtlep/turtle1/cmd_vel", {"x": 0.0, "y": 4.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlep/turtle1/cmd_vel", {"x": 2.0, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlep/turtle1/cmd_vel", {"x": 0.2, "y": -0.2, "z": 3.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlep/turtle1/cmd_vel", {"x": 0.0, "y": -1.5, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlep/turtle1/cmd_vel", {"x": -0.2, "y": -0.2, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
    ("/turtlep/turtle1/cmd_vel", {"x": -2.0, "y": 0.0, "z": 0.0}, {"x": 0.0, "y": 0.0, "z": 0.0}),
]

threads = []
for cmd_list in [turtle1_cmd, turtle2_cmd, turtle3_cmd]:
    thread = threading.Thread(target=execute_commands, args=(cmd_list,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

execute_commands(turtle4_cmd)

