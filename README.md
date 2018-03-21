# Body Mass Index Challenge

## Description
Web application to calculate the BMI given the mass and height of the user. The application indicates the category according to the [standard](http://en.wikipedia.org/wiki/Body_mass_index#Categories). You must register in order to use the application. Afterwards, you will be able to calculate your body mass index.

## Setup
PyEnv was used to select the proper Python version to be used along with
VirtualEnv. The React part was setup using Nodeenv integtrated into PyEnv.
For JavaScrip/React, Yarn and Webpack were also installed.

## Prerrequisites
Make sure to install and have a working PyEnv and then with the help of PyEnv
install Python versions 2.7.14 and 3.6.3

## Installation
Please follow the next recommended sequence of general instructions to install
this application:
1) Git clone
2) cd body-mass-index
3) pyenv virtualenv 2.7.14 bmi27 | pyenv virtualenv 3.6.3 bmi36
4) pyenv activate bmi27 | pyenv activate bmi36
5) pip install -r requirements.txt
6) cd application/static
7) yarn install
8) yarn build
9) cd ../..
10) ./start

## Testing
For testing the Python/Flask part, please do as follows:
1) cd body-mass-index
2) pytest test

As per testing the React part:
1) cd application/static
2) yarn test

