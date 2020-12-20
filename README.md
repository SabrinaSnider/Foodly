# Foodly

Foodly is a grocery list web application that automatically gets product aisles for grocery items at Publix and organizes the list accordingly.
![image](https://user-images.githubusercontent.com/10712922/86698390-41276580-bfdd-11ea-9ecb-b4bd13fe1bdd.png)

# Table of Contents

- [Getting Started](#getting-started)
- [Built With](#built-with)

# Getting Started

## Dependencies

### Client

To install the latest LTS version of Node.js, visit the link [here](https://nodejs.org/en/). After installing Node, `cd` into the client folder and run `npm install` to download the client dependencies. 

### Server

To install the latest version of Flask, visit the link [here](https://flask.palletsprojects.com/en/1.1.x/installation/). After installing Flask, `cd` into the server folder and run `pip install -e .` to download the server dependencies.

## Running the project

1. Start the client by running `npm run serve` in the client folder.
2. Start the server by running `flask run` in the server folder.

# Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The server framework
* [Vue](https://vuejs.org/) - The frontend framework
* [sqlite](https://www.sqlite.org/index.html) - SQL database language
* [SQLalchemy](https://www.sqlalchemy.org/) - SQL database library for python
* [Pandas](https://pandas.pydata.org/) - Data processing and organizaiton
