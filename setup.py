from setuptools import setup


setup(
    name='pylama-pre-commit',
    description='Pylama pre-commit support',
    url='https://github.com/gvanderest/pylama-pre-commit',
    version='0.2.0',
    author='Guillaume VanderEst',
    author_email='gvanderest@gmail.com',
    install_requires=[
        'pylama[all]',
    ],
)
