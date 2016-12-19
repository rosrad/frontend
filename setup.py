try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

setup(name='frontend',
      version='0.1',
      description='Python Speech Processing',
      author='rosrad',
      author_email='justnow.ren@gmail.com',
      url='https://github.com/rosrad/frontend',
      packages=['frontend'],
    )
