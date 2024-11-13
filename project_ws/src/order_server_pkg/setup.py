from setuptools import find_packages, setup

package_name = 'order_server_pkg'

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
    maintainer='somyeong',
    maintainer_email='ksm001220@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'order_server = order_server_pkg.order_server:main',
            'order_client = order_server_pkg.order_client:main',
            'action_server = order_server_pkg.action_server:main',
        ],
    },
)
