from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/py_pubsub/launch',['launch/talker_listener.launch.py']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pranit',
    maintainer_email='pranit@example.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
                 'talker = py_pubsub.publisher_member_function:main',
                 'listener = py_pubsub.subscriber_member_function:main',
		 'add_server = py_pubsub.add_service_server:main',
		 'add_client = py_pubsub.add_service_client:main',
        ],
    },
)
