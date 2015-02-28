import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__),
                       'VERSION')) as f:
    version = f.read().strip()


setup(
    name='maxminddb-geolite2',
    author='Arnout van Meer',
    author_email='rr2do2@gmail.com',
    version=version,
    url='http://github.com/rr2do2/maxminddb-geolite2',
    packages=['_maxminddb_geolite2'],
    description='Provides access to the geolite2 database.  This product '
        'includes GeoLite2 data created by MaxMind, available from '
        'http://www.maxmind.com/',
    install_requires=['maxminddb'],
    py_modules=['geolite2'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
    ],
)
