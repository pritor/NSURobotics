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
            package='04_02_tf2',
            executable='tf2_turtle_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),
        DeclareLaunchArgument(
            'target_frame', default_value='carrot1',
            description='Target frame name.'
        ),
        DeclareLaunchArgument(
            'radius', default_value='4.0',
            description='radius of carrot1 rotation'
        ),
        DeclareLaunchArgument(
          'direction_of_rotation', default_value='1',
          description='direction of carrot1 rotation'
        ),
        Node(
            package='04_02_tf2',
            executable='tf2_turtle_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='04_02_tf2',
            executable='tf2_turtle_listener',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
        Node(
            package='04_02_tf2',
            executable='tf2_turtle_df_broadcaster',
            name='dynamic_broadcaster',
            parameters=[
                {'radius': LaunchConfiguration('radius'),
                 'direction_of_rotation': LaunchConfiguration('direction_of_rotation')}
            ]
        ),
    ])
