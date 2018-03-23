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

    git clone
    cd body-mass-index
    pyenv virtualenv 2.7.14 bmi27 | pyenv virtualenv 3.6.3 bmi36
    pyenv activate bmi27 | pyenv activate bmi36
    pip install -r requirements.txt
    cd application/static
    yarn install
    yarn build
    cd ../..
    ./start

## Testing
For testing the Python/Flask part, please do as follows:

    cd body-mass-index
    pytest test

As per testing the React part:

    cd application/static
    yarn test
