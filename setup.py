from setuptools import setup

setup(
    name='postit',
    packages=['postit'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-login',
    ],
)
