# Nom Nom cook book

## Milestone Project 3

### [Depoyment on Heroku](https://noom-noom-cookbook.herokuapp.com/)

![Nom Nom cook book](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture-noom-noom-cookbook-herokuapp-com-1583152419684.png?raw=true)

## Overview

### What is this application for?
This application is created for anyone who share passion for tasty food and kitchen tools.

### What does it do?
Users will be able to read, add, edit, and delete recipes. 
They will be also able to create their account and log in with it and search the recipes > (THIS 2 FEATURES ARE STILL IN ADAPTATION PROGRES!!!)

### How does it work?
**Nim Nom cook book** is built using the python-based **Flask** micro-framework. 
**PyMongo** is used to connect the application's Python classes and methods to a **MongoDB** database. All data input is handled using **WTForms**.
The site is styled using the **Bootstrap CSS** and **Materialize CSS** front-end framework for responsiveness and enhanced user-experience. **JQuery** are dependencies of Bootstrap. 
The application is hosted on the **Heroku** platform, the database is hosted by **MongoDB Atlas**. 
The **MONGO_URI** and **SECRET_KEY** are hidden in environment variables locally during development and stored as environment variables using Heroku Config Vars in production. 

 