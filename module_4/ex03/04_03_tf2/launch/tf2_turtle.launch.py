from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='04_03_tf2',
            executable='tf2_turtle_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.'
        ),
        DeclareLaunchArgument(
            'delay', default_value='5.0',
            description='Time travel delay'
        ),
        Node(
            package='04_03_tf2',
            executable='tf2_turtle_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='04_03_tf2',
            executable='tf2_turtle_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame'),
                 'delay': LaunchConfiguration('delay')}
            ]
        )
    ])

