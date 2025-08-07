from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            namespace= "turtleg", package='turtlesim', executable='turtlesim_node', output='screen'),
        launch_ros.actions.Node(
            namespace= "turtlej", package='turtlesim', executable='turtlesim_node', output='screen'),
            launch_ros.actions.Node(
            namespace= "turtlem", package='turtlesim', executable='turtlesim_node', output='screen'),
        launch_ros.actions.Node(
            namespace= "turtlep", package='turtlesim', executable='turtlesim_node', output='screen'),
    ])
