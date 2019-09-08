#  Salad Book

----
## What is this?

[Click here to see a live version of the website](https://salad-book.herokuapp.com/)

> This is an online cookbook for salads in which you can view, add, edit and delete recipes
----
## Technologies used :
* HTML5
* CSS3
* JS and Chart.js
* Materialize CSS
* Python
* Flask
* Mongo DB

----
## Requirements :
* Design a database schema based on recipes, and any other related properties and entities(e.g. method, votes, ingredients, cuisine etc…).Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
* Create the backend code and frontend form to allow users to add new recipes to the site
* Create the backend code to group and summarise the recipes on the site, based on their attributes (create a chart)
* Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. popularity, type, etc…) and order them based on some reasonable aspect (e.g. number of stars).
* Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
* Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages


## About project:
>This is web app was designed to allow users to view, edit, add and delete reipces. Also to search recipes by different criteria.
The project's structure:
* Back-end: Python and Flask
* Front-end: HTML, CSS, JS, Chart.js and Materialize CSS
* Database: Mongo DB

## Deployment 
I used Heroku for deployment using my master branch as the source.
Create requirements file to ensure all dependencies for heroku to run ---->  sudo pip3 freeze --local > requirements.txt 

Create the Procfile ----> echo web: python run.py > Procfile 

Scale app dynos for heroku ----> heroku ps:scale web=1 

Push to Heroku ----> git push heroku master 



## Testing 
* Testing connection to the database
* Testing adding a recipe in the DB by filling and submitting the right form (post)
* Testing editing a recipe in the DB by filling and submitting the right form (post)
* Testing the back-end code with tests and print statements
* Used html and css validator
* Google Developer Tools (responsive mode)
* Running the website in different browsers 
* Running the website on different devices phones and tablets (apple, android)


## Credits 
### Content  ###
The source for the recipes was https://www.bbcgoodfood.com
### Media  ###
The photos in the site were obtained from Google or from https://www.bbcgoodfood.com
