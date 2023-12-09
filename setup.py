from setuptools import setup, find_packages

setup(
    name='CompSyRobotics',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'sympy',
    ],
    description="RoboSymPy is a powerful Python library for solving a wide range of robotic problems using symbolic computations with SymPy. Perform tasks like forward and inverse kinematics, trajectory planning, and dynamics analysis. Benefit from the library's support for both symbolic and numeric calculations, making it a versatile tool for robotics research and applications.",
    author='Awais Amjad',
    author_email='amjadawais08@gmail.com',
    url='https://github.com/awaisamjad/CompSyRobotics',
)
