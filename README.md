
# SpaceX First stage Landing Prediction



## Table of Content
- Demo
- Overview
- Motivation
- Technical Aspect
- Installation
- Run
- Deployment on Heroku
- Decission Tree
- Technology Used
- License
## Demo
Link: https://spacexlandingpred.herokuapp.com/
## Screenshots

![App Screenshot]("https://github.com/POTUSAITEJA/SpaceX_App/blob/main/static/screenshot.JPG")


## Overview
This is a simple Flask app created to predict the landing of the first stage of spaceX based on the data from spaceX API some of the data is also taken by web scrapping the SpaceX Wiki page. This trained model(server/artificates/launch_prediction_model.pickle) takes certain parameters(like payloadmass,orbit,..etc) as inputs and predict wheather the first stage will land sucessfully or not.
## Motivation
In recent times space has become a travel destination. Many companies like spaceX and Blue Origin are in the race to offer an affordable space travel to everyone. This can be done by bringing the first stage back to earth. If we predict the landing of the first stage and if the landing is sucessful we can reduce the cost of the travel by 3 times
## Technical Aspect
This project is divided in to two parts

1. Training a Machine learning model using Sk learning
2. Building and hosting a Flask web app on Heroku
    - A user can see all the stastical analysis of the data.
    - USer can choose there desired payload mass and orbit to launch.
    - Based on the users input the Machine Learning algorithm predicts the outcome.
## Installation

The Code is written in Python 3.9. If you don't have Python installed you can install it directly from web. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

```bash
pip install -r requirements.txt
```
    
## Decision tree
Gridsearch cv is performed on various algorithms and based on the accuracy Decision tree is used.

Decision tree hpyerparameters :(best parameters)  {'criterion': 'gini', 'max_depth': 8, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 5, 'splitter': 'random'}
## Technologies used

web Scraping : Beautifulsoup

Implementation: Python, Numpy, Pandas, Sk Learn

Server: Python server, Postman

Frontend: Flask,HTML,CSS,JS



## License

[MIT](https://choosealicense.com/licenses/mit/)

