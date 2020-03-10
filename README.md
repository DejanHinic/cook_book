# Nom Nom cook book

## Milestone Project 3

### [Demo is available here!](https://noom-noom-cookbook.herokuapp.com/)

![Nom Nom cook book](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture-noom-noom-cookbook-herokuapp-com-1583152419684.png?raw=true)

## Overview

### What does it do?
Users will be able to read, add, edit, and delete recipes. 
They will be also able to create their account and log in with it and search the recipes > (THIS 2 FEATURES ARE STILL IN ADAPTATION PROGRES!!!)

### How does it work?

**Nom Nom cook book** is built using the python-based **Flask** micro-framework. 

**PyMongo** is used to connect the application's Python classes and methods to a **MongoDB** database. All data input is handled using **WTForms**.

The site is styled using the **Bootstrap CSS** and **Materialize CSS** front-end framework for responsiveness and enhanced user-experience. **JQuery** are dependencies of Bootstrap. 

The application is hosted on the **Heroku** platform, the database is hosted by **MongoDB Atlas**. 

The **MONGO_URI** and **SECRET_KEY** are hidden in environment variables locally during development and stored as environment variables using Heroku Config Vars in production. 

## UX

### UX Design

In this project I was aiming to achieve a simple and user friendly user design, while providing all required information.

To create cosy design I used the following colors in my project: lightseagreen (`#20b2aa` and '#2aa69a') then default black, red, green and white.

### Target Audience

This application is created for anyone who share passion for tasty food and kitchen tools.


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

#### CSS

CSS code was validated using the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/).

Everything returned as NO ERROR!

#### HTML

HTML code was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

The following issues were captured by the validator:

- The following issue appeared in the all the templates which contains curly brackets {{}}: "Bad value {{url_for('name')}} for attribute href on element a: Illegal character in path segment: { is not allowed."

#### JavaScript

JavaScript code was validated using [JSHint](https://jshint.com/).

Validator has indicated that there are two unknown / undefined variables, namely `$`.

Four unused variable was flagged `Materialize`. The warning was ignored as these functions are activated by onlclick event.

### Features testing

All the features were tested manually throughout the application development process. Table below outlines all features and tests performed on them, as well as all resolved and remaining bugs associated with tested features.

| Feature type                         | Feature                                  | Tests                                                                                                                                                                                                                                                                                                                                                                                                                       | Bugs                                                  |
| :----------------------------------: | :--------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------:|
| Buttons (including anchor links)     | Kitchen Cookware                         | - test if button redirects to store for cookware;<br>- test if cookware store page opens in a new tab                                                                                                                                                                                                                                                                                                                       | No bugs.                                                 |
|                                      | Knives                                   | - test if button redirects to store for knives;<br>- test if cookware store page opens in a new tab                                                                                                                                                                                                                                                                                                                         | No bugs.                                                 |
|                                      | Appliances                               | - test if button redirects to store for appliances;<br>- test if cookware store page opens in a new tab                                                                                                                                                                                                                                                                                                                     | No bugs.                                                 |
| Forms                                | Sign up form                             | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                                                                                   | There is problem with empty fields, it actually allows it to store the blank field as a name(in future it will be fixed with form.py file). <br> If there is same name attempt to register, then we get alert message that user already exist.|
|                                      | Add recipe                               | - test if input text works correctly for each field;<br> - test if there is any field left empty the form can be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                                                                                            | No bugs.                                                 |
|                                      | Delete recipe                            | - test if data is deleted correctly from the database;<br> - test if button delete is working for action;<br>                                                                                                                                                                                                                                                                                                               | No bugs.                                                 |
|                                      | Edit recipe                              | - test if update forms pull data correctly from the database and then send correctly back;<br> - test if input text works correctly for each field;<br> - test if there is any field left empty the form can be submitted;<br>                                                                                                                                                                                              | No bugs.                                                 |
| Structure                            | Navbar                                   | - test if all navbar menu items redirect user to the appropriate page;<br> - test if item that is currently active is highlighted;<br> - test if navbar collapses on smaller devices;                                                                                                                                                                                                                                       | No bugs.                                                 |
|                                      | Footer                                   | - test if footer stays at the bottom of the page;                                                                                                                                                                                                                                                                                                                                                                           | No bugs.                                                 |
| Other                                | Accordion                                | - check if only one element is un-wrapped at the time;<br> test if clicking on the heading un-wraps the correct element;                                                                                                                                                                                                                                                                                                    | No bugs.                                                 |
|                                      | Tabs                                     | - check if tabs change when tab `li` is clicked;<br> test if information displays correctly in the tab;                                                                                                                                                                                                                                                                                                                     | No bugs.                                                 |

### Responsiveness testing

This site was tested across multiple browsers (Google Chrome, Safari, Mozilla Firefox, Opera) and on multiple mobile devices (iPad Mini, iPad, Huawei P20) to ensure compatibility and responsiveness.

Chrome developer tools were used to additionally inspect responsiveness for the following devices:

- iPad Pro / iPad / iPad Mini (portrait & landscape);

- iPhone 5/SE (portrait & landscape);

- iPhone 6/7/8 (portrait & landscape);

- iPhone 6/7/8 Plus (portrait & landscape);

- iPhone X (portrait & landscape);

- Android (Pixel 2) (portrait & landscape).

Furthermore, [Responsinator](https://www.responsinator.com/) was used to test responsiveness of the final version of the project.

The website is fully responsive and working well on mobile devices.


### Features left to be implemented
* Log in feature is still having few details that I need to fix to be in order
* Text search engine to be implemented
* Pagination to be fixed to work properly
* Search recipes. This feature is still left to implement. It will allow user to search recipe by text. 

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
* JavaScript

## Libraries
* JQuery
* Google Fonts

## Deployment

### GitHub

The site was developed using Gitpod. To keep records of different versions of all project files git version control system was used. 

To initialize the local repository the command `$ git init` was used. After adding initial files and committing them `$ git remote add origin 'GitHub repo name'` command was used to add new remote repository. Code was then pushed to the master branch of the remote repository using `$ git push -u origin master`.

In order to track the changes in the local repository the following steps were taken:

- command `$ git add 'filename'` - to update what will be committed;

- command `$ git commit` - to commit the changes.

Using `$ git push` command all changes from the local repository were pushed to the remote one on GitHub.

### Heroku

This project is hosted using Heroku, deployed directly from the `master` branch. 

To deploy my project I followed these steps:

1. Create App: 

     - On Heroku website I logged onto my account and created [noom-noom-cookbook](https://git.heroku.com/noom-noom-cookbook.git);
     - Under the **Settings** tab I clicked button **Reveal Config Vars** and I set the IP to 0.0.0.0 and the PORT to 5000;
     - At the later stage configuration for the MongoDB database were added, namely 'MONGO URI' and 'SECRET KEY';

2. Install the Heroku: 

     - I used option to connect github directly with Heroku so every my push to github from gitpod automatically updates the changes to my app on Heroku; 

3. Git repository:

     - If repository not created already the following commands should be used in order to initialize a git repository in a new or existing directory: 
        ```
        $ cd 'directory-name'/
        $ git init
        $ heroku git:remote -a 'app-name''
        ```
        
    - For existing repositories add the Heroku remote should be used: `$ heroku git:remote -a 'app-name'`;

4. Requirements:

    - In order to run the app Heroku needs to install the required dependencies so make sure that 'requirements.txt' file was created and committed;
    - In order to create 'requirements.txt' file run `$ sudo pip3 freeze --local > requirements.txt` command in the terminal;

5. Procfile:

    - Procfile is a Heroku specific type of file that tells Heroku how to run our project;
    - For the 'Procfile' run `$ echo web: python > Procfile` command in the terminal;
    - In order to start web processes run `heroku ps:scale web=1` command in the terminal;

5. Deployment: Committed code was deployed to Heroku using the following command: `$ git push heroku master`.

6. Connecting MongoDB to gitpod has a trick how to insert mongoDB link

    - cd .. all the way until workspace name folder 
    - then enter: gp open /home/gitpod/.bashrc
    - COPY THE LINK FROM MONGO APP mongodb+srv://root:<password>@myfirstcluster-ol1er.mongodb.net/test?retryWrites=true&w=majority
    - export MONGO_URI="", change the password and change test to your original filename (myTestDB) and add the quotes 
    - export MONGO_URI="mongodb+srv://root:0t0rin0laring0l0gija@myfirstcluster-ol1er.mongodb.net/myTestDB?retryWrites=true&w=majority"
    - then thype in terminal: echo $MONGO_URI ---- is to check is it connected

### Content and Acknowledgements
The recipes were copied from the https://www.delish.com/cooking/ and I've got the inspiration from that page. 

### Media
The photos used in this site were obtained mostly from google
