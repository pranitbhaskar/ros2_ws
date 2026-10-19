from setuptools import find_packages, setup

package_name = 'my_new_package'

setup(       
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pranit',
    maintainer_email='pranit@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'example_node_executable = my_new_package.node_example:main',
            'example_custom_move_turtle = my_new_package.move_turtle:main'
        ],
    },
)
