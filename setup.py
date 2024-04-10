from setuptools import setup, find_packages
from datetime import datetime

setup(
    name='django_analytics',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'maxminddb>=2.0.1',
        'user-agents>=2.2.0'
    ],
    package_data={
        'analytics': ['data/GeoLite2-City.mmdb']
    },
    include_package_data=True,
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License',
    author='Santiago Nestor Britos',
    author_email='s.britos@hotmail.com',
    description='Django Analytics is a package designed to facilitate tracking and analysis of data in Django web applications. It provides middleware that records information about users, including details such as browser, operating system, device, geographical location, and more. The collected data is stored in a new database table, enabling detailed analytics to improve user experience and make informed decisions in application development and maintenance.',
    date=datetime.today().strftime('%Y-%m-%d'),
)