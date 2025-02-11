from setuptools import find_packages, setup

package_name = 'BlueROV2_description'

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
    maintainer='safrunzi',
    maintainer_email='saf359@drexel.edu',
    description='This package contains description and gazebo files for the UUV BlueROV2 by Blue Robotics. This is based on the following repository: https://github.com/UUVControl/bluerov2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
