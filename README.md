# Nom Nom cook book

## Milestone Project 3

### [Demo is available here!](https://noom-noom-cookbook.herokuapp.com/)

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

| Feature type                         | Feature                                  | Tests                                                                                                                                                                                                                                                                                                                                                                                                                       | Bugs                                                  |
| :----------------------------------: | :--------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------:|
| Buttons (including anchor links)     | Buy online button                        | - test if button redirects to amazon;<br> - test if search of a given book performed correctly;<br> - test if amazon page opens in a new tab                                                                                                                                                                                                                                                                                  | Initially there was an issue<br>with '&' symbol but<br>function was adjusted<br>to replace it with 'and'.<br>Function has to be improved<br>to take into account <br>other scenarios such as<br>e.g. link contains other tag. |
| Forms                                | Sign up form                             | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;<br> - test if password hashing works i.e. password saved to database is hashed;                                                                                                                                       | Initially username was<br>case sensitive but<br>that was fixed by applying<br>python `lower()` method<br>to the username. |
|                                      | Add recipe                               | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                                                                                      | No bugs.                                                  |
|                                      | Delete recipe                            | - test if update forms pull data correctly from the database;<br> - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                     | Bug related to updates<br>in situation when<br>only some fields where update<br>other fields where removed.<br>Bug fixed using `$set`<br>mongoDB operator to only update<br>fields edited by the user. |
|                                      | Edit recipe                              | - test if update forms pull data correctly from the database;<br> - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                     | Bug related to updates<br>in situation when<br>only some fields where update<br>other fields where removed.<br>Bug fixed using `$set`<br>mongoDB operator to only update<br>fields edited by the user. |
| Structure                            | Navbar                                   | - test if all navbar menu items redirect user to the appropriate page;<br> - test if item that is currently active is highlighted;<br> - test if navbar collapses on smaller devices;                                                                                                                                                                                                                                          | No bugs.                                                 |
|                                      | Footer                                   | - test if GitHub link works correctly;<br> - test if footer stays at the bottom of the page;                                                                                                                                                                                                                                                                                                                                  | No bugs.                                                 |
| Alerts                               | Toast messages                           | - test if all flash messages are styled with toastr;<br> - test if no text is cut off;<br> - test if delete button and progress displays correctly;<br> - test if different colors applied to different categories of toast messages;                                                                                                                                                                                           | No unresolved bugs left.                                 |
|                                      | Delete confirmation messages             | - test if confirmation message pops up when trying to delete a review or account;<br> - test if clicking 'delete' button on the message performs deleting;<br> - test if clicking 'cancel' cancels the action;                                                                                                                                                                                                                 | No unresolved bugs left.                                 |
| Other                                | Accordion                                | - check if only one element is un-wrapped at the time;<br> test if clicking on the heading un-wraps the correct element;                                                                                                                                                                                                                                                                                                      | No bugs.                                                 |
|                                      | Tabs                                     | - check if tabs change when tab `li` is clicked;<br> test if information displays correctly in the tab;                                                                                                                                                                                                                                                                                                      | No bugs.                                                 |

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

### Content and Acknowledgements
The recipes were copied from the https://www.delish.com/cooking/ and I've got the inspiration from that page. 

### Media
The photos used in this site were obtained mostly from google
