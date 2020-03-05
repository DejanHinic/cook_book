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

**Nom Nom cook book** is built using the python-based **Flask** micro-framework. 

**PyMongo** is used to connect the application's Python classes and methods to a **MongoDB** database. All data input is handled using **WTForms**.

The site is styled using the **Bootstrap CSS** and **Materialize CSS** front-end framework for responsiveness and enhanced user-experience. **JQuery** are dependencies of Bootstrap. 

The application is hosted on the **Heroku** platform, the database is hosted by **MongoDB Atlas**. 

The **MONGO_URI** and **SECRET_KEY** are hidden in environment variables locally during development and stored as environment variables using Heroku Config Vars in production. 

### Mockup and Wireframe links
* [Mockups](https://github.com/DejanHinic/cook_book/tree/master/static/Mockups)
* [Wireframes](https://github.com/DejanHinic/cook_book/tree/master/static/Wireframe)

### Features
The following are the features provided in Nom Nom cook book.

#### Basic Features
* Users can add recipe, read info, delete or edit. (In future only registrated users will be able to edit or delete recipes)

### Navbar
* Navbar is responsive on any device and when is showed on smaller screens then navbar transforms as a side navbar

#### User Registration
* Users are able to registrate their account by creating their name and password.

#### Search recipes and recipes collection
* This feature is still left to implement. It will allow user to search recipe by text. 

![Search and all Recipes Data](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture_allrecipes.png?raw=true)

#### Check the recipe 
* User can check the informations about the specific recipes. (steps, ingredients, allergens, prep and cook info, cuisine style)

![Recipe Info Data](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture_recipeinfo.png?raw=true)

#### Add recipe
* Users can store informations (recipe title, short description, steps, ingredients, allergens, prep and cook info, cuisine style).

![Adding Data](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture_addrecipe.png?raw=true)

#### Editing recipe 
* All collected information for any recipe can be edited.

![Editing Data](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture_editrecipe.png?raw=true)

#### Deleting recipe
* Simply just click delete button and recipe will be erased fro MongoDb database.

#### Kitchen Tools section
This section is addition to this project as one of the requirements of the assigment.

There are 3 cards which have short description about Cookware, Appliances and Knives.

All of these cards have a link to a websites which I choose to give an options to buy and infos for user. 


### Testing
The application was tested manually by walking through the features.

* All the pages are responsive on all devices thx to Bootstrap.

* The data is stored correctly in MongoDB. There are 2 collections = Recipes and Users

* Codes were tested with jigsaw.w3.org , validator.w3.org and codebeautify.org validators

* click the 'sign up' link:
the sign up page opens and displays the registration form


### Features Left to Fix
* Log in feature is still having few details that I need to fix to be in order
* Text search engine to be implemented
* Pagination to be fixed to work properly

## Database Organisation
Nom Nom cook book uses a document-oriented database using MongoDB. The chosen structure was developed by progessing through the following steps:

* defining the recipe details and registrating users account stored at Recipes and Users

    * Users: 
         - name
         - password

            ![Users Data](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture_userdata.png?raw=true)

    * Recipe
        - title
        - short description
        - cook time
        - prep time
        - cuisine
        - serves 
        - calories
        - food type
        - steps
        - ingredients
        - allergens

![Recipe Data](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture_recipedata.png?raw=true)

### Technologies Used
* html5 https://www.w3schools.com/html/
* css https://www.w3schools.com/css/css_intro.asp for styling
* bootstrap 4 https://getbootstrap.com/ to build the grid and make it responsive for all devices
* balsamic for wireframe https://balsamiq.com/?gclid=CjwKCAjwndvlBRANEiwABrR32Mzzb1wWuG0slcCQDwB1B2W9OBv8pacL7BzOZ9sGnPggguab1vbt4BoCTewQAvD_BwE
* AdobeXD for mockups
* Materialize for style
* Flask 
* MongoDB
* Python

### Content and Acknowledgements
The recipes were copied from the https://www.delish.com/cooking/ and I've got the inspiration from that page. 

### Media
The photos used in this site were obtained mostly from google
