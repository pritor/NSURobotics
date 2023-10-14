from setuptools import find_packages, setup
import os
from glob import glob
package_name = '04_02_tf2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
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
        	'tf2_turtle_broadcaster = 04_02_tf2.tf2_turtle_broadcaster:main',
        	'tf2_turtle_listener = 04_02_tf2.tf2_turtle_listener:main',
            'tf2_turtle_ff_broadcaster = 04_02_tf2.tf2_turtle_ff_broadcaster:main',
            'tf2_turtle_df_broadcaster = 04_02_tf2.tf2_turtle_df_broadcaster:main'
        ],
    },
)
