from setuptools import find_packages, setup
import os

package_name = 'robot_app'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), ['config/compensation.yaml', 'config/projection.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pritor',
    maintainer_email='petya.podstavkin@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lane_finder=robot_app.lane_finder:main',
            'lane_follower=robot_app.lane_follower:main',
            'image_projector=robot_app.image_projector:main',
            'image_compensation=robot_app.image_compensation:main'
        ],
    },
)
