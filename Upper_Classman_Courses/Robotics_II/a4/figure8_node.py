from setuptools import find_packages, setup

package_name = 'turtlesim_play_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Caleb Young: author name',
    maintainer_email='cyoung24@cub.uca.edu: email address',
    description='Package description: This package allows user to use ROS to simulate a robot going in a figure 8. Using given code and running your terminal the turtle will do a figure 8. You can customize the values to make the figure 8 larger, smaller, or pretty much do whatever you want. This package is a good example of building a workspace in ROS and using it to run simulations.',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'figure8_node = turtlesim_play_pkg.figure8_node:main'
        ],
    },
)
