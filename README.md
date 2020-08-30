# OnlineSmoothieRecipe

## Data Centric Development Milestone Project-3

## Description

The OnlineSmoothieRecipe is an online recipe notes, where a user can find recipes or add his/her own recipes. User can create an account
with features of adding, updating and deleting his/her own recipes.

# UX

### Intended Target Audiences

 The target audience of this web page are juice and smoothie lovers who are either in search of good making recipes or they want to save 
 their favourite recipes online and want to share with others. The purpose of this web-page is to provide a platform to juice/smoothie lovers
 so they can share their recipes with others. Besides, the web page owner's goal is to create a smoothie/juice recipes database.

 ### Suitability Of Project

This project is suitable to perform **CRUD** operations.
- Users can create, view and search for recipes in the database.
- Users can edit or delete their own recipes.
- Users can only view other's recipes but don't have the access to edit or delete other's recipes.
- User login system has put in place so that user can manage their recipes.

 ### User Stories

 1. As a user, I want to see a list of recipes.
 2. As a user, I want to search for recipes so that I can find recipes easily and quickly.
 3. As a user, I want to be able to create an account.
 4. As a user, I want to be able to login to my account.
 5. AS a user, I want to store/add  and share my recipes online with others.
 6. As a user, I want to see a list of my own recipes.
 7. As a user, I want to see the details of the recipe.
 8. As a user, I want to update/dlete my existing recipes.

## Design

 The website design is simple and responsive which allows the user to perform easily the CRUD functionality. The design 
 inspiration is taken from the **Code Institute's Task Manager Mini Project**.

#### Fonts

1. Google fonts **Krona One** is used in navbar and footer. 
2. Where as **Balsamiq Sans** is used in the body. 

#### features

1. The target_blank value is given to the social link in the footer so that they will open in a new tab / window on click.
2. The required attribute is used in the **Search bar**, **Log In form**, **Sign Up form**, **Add Recipe form** and **Edit Recipe form** so that user 
fill in all the files before performing the respective actions.
3. Maximum, minimum and character counter attributes are also added in the input fields for better user experience. 

#### Hover Effect

1. Slight changes in background-colors and default cursor changes to the pointer happens when a user hover over a button.
2. Default cursor changes to hand pointer when a user hover over logo and social links.

## Wireframes

I used [Balsamiq](https://balsamiq.com/) to create wireframes which will provide an overview of prototyping a website. 
- [Wireframes in PDF](static/wireframes/wireframe.pdf)

## Database Schema

MONGODB is used for this project to store data at the backend. Database schema is designed for various collections before building the project. 
- [Collections in PDF](static/collections/collections.pdf)

## Existing Features
- **Navbar/Side** Navbar and side navbar links vary, if user is logged in or not. If user is not logged in then (Home,
All Recipes, Log In) buttons are shown. but if loged in, user can see (Home, All Recipes, Add Recipes, My Recipes and Logout).
At login and signup pages all navbar/sidenavbar links will disappear except the logo OnlineSmoothieRecipe. 
- **All recipes** When a user click on the home page and has not logged in yet, he/she can see the list of all recipes in the database
with no possiblities of editing/deleting. User can also see the list of all recipes once the user has logged in with possiblities of edit/delete.
- **Search** User can search for any recipe in the database with logged in/without logged in.
- **Register** User can easily register if does not have an account. Signup form has two fields username and password. 
It is required that a username must be minimum of three character long and password should be minimum 6 character long. 
It is not possible to have two accounts with the same name as before registration username will be checked if it already exist or not. 
If username already exist then user will be notified that username already exist with a flash message. Otherwise, creation will be successful. 
- **Login** If username password does not match user will get a message that invalid username/password.
- **Flash Messages** Flash Messages are shown to the user to keep user inform of user interactivity. Flash messages for 
login and signup will stay untill these pages are refreshed. Where as flash messages on recipe addition, deletion and update will 
disappear after 4 sec.
- **Logout** Logout allows a user to logout of his/her own session and return to the home page.
- **showrecipes/Allrecipies**
- ***View*** It allows a user to see the details of recipes in the database.
- **Add Recipe** When user is logged in, it allows user to add a new recipe in the database. All the fields are required in add recipe form. After 
adding the recipe user will get a flash message that recipe is added successfully and will disappear after few seconds. Then 
user will be redirected to the (all recipes) page.
- **Edit/Delete Recipe** When user is logged in user can edit or delete a recipe which he owns. the buttons will appear only if the user is the owner. 
- **Cancel Button** Cancel button is provied in edit recipe page for user's convenience to cancel the operation which will 
redirect the user back to that particular recipe that user was viewing before.
- **Deletion Confirmation** If a user click on delete button, then a modal will pop up to confirm if user is sure to delete the recipe or not.
If yes is clicked, then deletion will be confirmed but if no is clicked, then user will be redirrected to the recipe that user was before.
- **My Recipe** If user want to see his/her own added recipes then **My Recipe** function will display the list of user's own recipe
But user must be logged in to his/her own session in order to see it.
- **Error handler(404), try and except** If user enters broken url, then for better user experience an errorhandler(404) is added. This will
display a message **Oops! Looks like you entered wrong URL**. It will also provide link to the home page for user convenience.

### Future Implementations

- **Linking Carousles** At the moment **All Recipes** and **My Recipes** pages shows all the recipes. But in 
in future I would like to add links to the carousel images which can redirect users to the spicific recipe of that clicked image.
- **Graphs** possiblities of adding graphs in future to give a statistical overview of the recipes.
- **Reset Password** A reset password feature can be added in the future.
- **Recover Password** Password recovery feature if forgotten can also be added in future.
- **Recipe Image** To make recipe visually appealing, recipe image addition option can also be added in future.
- **Top 10 Recipes** Top 10 recipes feature can also be added in future.

## Technologies Used

- **HTML5**
- **CSS3**  
- **JavaScript** 
- **JQuery** 
- **[Materialize Framework](https://materializecss.com/)**
- **[Python](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**
- **[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)**
- **[Balsamiq](https://balsamiq.com/)**
- **[PyMongo](https://pymongo.readthedocs.io/en/stable/)**
- **[MongoDB](https://www.mongodb.com/)**
- **[Google Fonts](https://fonts.google.com/)**
- **[Git & Github](https://github.com/)**
- **[Heroku](https://www.heroku.com/#)**
- **[HTML Formatter](https://webformatter.com/html)**

## Testing

Google developers tool has been used to test the project constantly from the  beginning to identify any error or to see 
how the changes looks like on different screen sizes. I created my own account and tested all the functions to make sure 
they work properly. In addition, I aslo asked my family, friends and slack community to test the project and give their feedback.

### User Stories

User stories from the UX section were tested to see if they all work as intended. 
- *As a user, I want to see a list / catalogue of recipes.*
1. Go to the **Home** Page.
2. Click on **All Recipes** button in the navbar or on **All Recipes** beside image slider.
3. All the lists of recipes will be displayed.
- *As a user, I want to search for recipes so that I can find easily and quickly.*
1. Go to the **Home** Page
2. Go to the search bar beside the image slider and write any key word to search for the recipe.
3. Click on the **Search** button.
4. It will reidirect you to the recipes.
5. If no recipe found then a **No Recipe Found** will be displayed.
- *As a user, I want to be able to create an account.*
1. Go to the **Home** Page.
2. Click on **log In** button and then **Sign Up** button.
3. Fill in username and password, then click on **Sign Up** button.
4. If username does not exist already then a user account will be created and user will be redirected to **Home** page.
5. If user already exist then user will get a message that **User already exists.**
- *As a user, I want to be able to login to my account.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and click on **Log In** button.
4. If username and password are correct then user will be redirected to the **Home** Page.
5. If username and password does not match then **Invalid username/password** message will be displayed.
- *AS a user, I want to store/add  and share my recipes online with others.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **Add Recipe** and fill out the **Add Recipe** form. All fields are required to fill in.
5. Click on **Add Recipe** button. A confirmation message **Recipe successfully Added** will be displayed and user will 
be redirected to the list of all recipes.
- *As a user, I want to see a list of my own recipes.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **My Recipes** button.
5. User will be redirected to list of user's own recipes. 
- *As a user, I want to see the details of the recipe.*
1. Find the recipe either by using **Search bar** or from list **All Recipes** or from list of **My Recipes**.
2. Click on the **View** button.
3. Recipe details will be shown.
- *As a user, I want to update my existing recipes.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **My Recipes** button and choose the recipe form the list to update.(**User can only update or delete his own recipes**)
5. Click on the **View** button and the recipe details will be displayed.
6. Click on the **Edit** button and recipe details will open in a editable form.
7. Edit the required field and click on update. A conformation message **Recipe successfully updated** will be displayed.
8. If user want to cancel the update and return to the previous page then click on **Cancel** button.
- *As a user, I want to delete my existing recipes.*
1. Go to the **Home** Page.
2. Click on **log In** button.
3. Fill in username, password and **Log In**.
4. Click on **My Recipes** button and choose the recipe form the list to update.(**User can only update or delete his own recipes**)
5. Click on the **View** button and the recipe details will be displayed.
6. Click on the **Delete** button and a pop up window will appear to confirm the deletion.
7. Click **yes** to confirm and a confirmation message **Recipe successfully deleted** will be displayed.
8. Click **No** to get back to same page agian.
- *As a user, I want to end the session.*
1. Click on the **Logout** button to end the session.

### Bugs / Issues

1. **Carousel was not functioning** I encountered a very interesting bug when I copied Carousel from materializecss.com. 
I have coppied and pasted so many times but couldn't find out what exactly the problem is. Then i made an appointment with my mentor
that if he can find out what i am missing. After i shared this issue, with my mentor, he found out that i was copying the carousel from 
meterializecss.com which was the new version of it and i had the links which provided by Code institiute which was the old version.
So, we fixed that issue together but it really took 3 days to troublshoot. 

2. **Not compatiblity of coding** I had a general issue with the links and codes that provided by Code Institute. The links which were
provided is old versions and when i wanted to add new forms and buttons, the links were no longer compatible. It actually took lots of 
time to debug and fixed the issues.

### Code Validation

The code has been validated by using;

- [W3C Markup Validation Service for HTML](https://validator.w3.org/)
- [W3C Markup Validation Service for CSS](https://jigsaw.w3.org/css-validator/)
- [Pep8 Online for Pyhton](http://pep8online.com/)

### Interesting Bugs / Issue

1. **Add Recipe function stopped working** - I encountered a very interesting bug when I made datepicker field a required 
field. I also wanted to show a feedback message to the user. To achieve this, I added a **JavaScript** function which I took from **Stack overflow**. 
But later I realized that **Add Recipe** function is not working. Since I used **Git** version control so I start going back to
the previous versions of my project to find out after which commit **Add Recipe** button stopped working. At last I found out
that its the **JavaScript** function that is causing this issue. So I replaced it with a **JQuery code** and solved this issue.
2. **Recipes can be stolen / Edited** - A very interesting bug that one of my friend **Elliot Redhead** point out was that a user can 
steal someone else's recipe and can edit / delete. Although edit / delete button are ment to display only to recipe owner.
Process of stealing recipe was;
- First view someone else's recipe and copy the recipe ID from the URL.
- Now open your own recipe in edit recipe page.
- Remove your recipe's ID and paste someone else's recipe ID.
- Press Enter now can edit someone els's recipe.
- **Solution** - To overcome this issue I need to update my edit recipe function. I put a check over there that will first see 
if the user who is trying to access the edit recipe page is the owner of the recipe. If **yes** then the function will let user
to proceed to edit recipe page else user will be redirected to the home page.
3. **No Recipe Found** - If a user in session does not have any own recipe then **No Recipe Found** message is displayed but
in the beginning this message has been also displayed in **All recipes**. To overcome this issue I need to amend my **Search Recipe**
function and **My Recipes** function togeather with if statement in recipes.html. Credit goes to Tim who helped me to fix this issue.
4. **Flash Messages** - Flash messages were not appearing after a delay of few seconds on **Adding Recipe**, **Updating Recipe**
and **Deleting Recipe** I realized later that, I need to hide it first then delay and it worked.
5. **Carousel** - I found out that if user keep click on or on touch screen keep pressing the **Carousel (Image Slider)**
then the images starts flashing. I did not tried to fix it and it remains there.
6.  In the **Input form** fields, user can insert content without giving spaces as a single line entry and add the recipe in the
 database. When later this recipe is viewed then it is displayed in a weird way as text will be overlapping out of the text fields.
 To overcome this I need to either add some complex Regular Expressions to the pattern or some keystroke queries using JavaScript,
 that I left for future.

## Deployment to Heroku

- **[OnlineSmoothieRecipe Live Page](http://online-smoothie-recipe.herokuapp.com/index_recipe)**

- **[OnlineSmoothieRecipe Github Repository](https://github.com/asifdanishyar/DCD_Milestone_Project)**

1. Login to **[Heroko](https://www.heroku.com/)** account.
2. Click on **New** at the right top corner and click on **Create new app**.
3. Choose **App name** and a **region**. Then click on **Create app**.
4. Go to terminal window and create **requirements.txt** by running command **pip3 freeze --local > requirements.txt**
5. Then create **Procfile** by running command **echo web: python app.py > Procfile** **Remember P is capital**
6. Add these files to stagging area by running command **git add requirements.txt** & **git add Procfile**.
7. Then commit these file respectively by running command **git commit -m "Added requirements.txt** & **git commit -m "Added Procfile**.
8. Then push these files to **github** by running command **git push**
9. Go back to **Heroku** to your **App** and click on **Deploy** tab. 
10. Then go to **Deployment Method** and click on **Github Connect to Github**.
11. Then make sure your **Github Profile** is displayed and add you **repository name** and click on **Search**.
12. Once it find your repository then click on **Connect**.
13. Now go to **Settings** at the top. Then click on **Reveal Config Vars**.
14. In **Config Vars** add **IP** with value **0.0.0.0** then add **PORT** as **5000** then add **SECRET_KEY** then add **MONGO_URI** and then add **MONGO_DBNAME** which is the name of database.
15. Now go back to **Deploy** tab and click on **Enable Automatic Deploys**.
16. Now click on **Deploy Branch**
17. It will take a minute and display a message that **Your app was successfully deployed**.
18. Click on **View** to launch your deployed app.

## Local Deployment

1. Go to [OnlineSmoothieRecipe Github Repository](https://github.com/asifdanishyar/DCD_Milestone_Project)
2. Click on **Code** beside **Gitpod**. 
3. A drop down menu open then click on **Download Zip**
4. Unzip the downloaded zip file.
5. Open app.py file and install requirements.txt by running comman **pip3 install -r requirements.txt**.
6. Create a database in **MONGODB**
7. Create env.py file and add **MONGO_URI** and **SECRET_KEY**. 
8. Now run the app.py by running code **python3 app.py**

## Credits

All pictures are taken from [Google](https://www.google.com/)
All recipes are taken from [Website](https://www.tasteandtellblog.com/)

### Acknowledgements
1. Code Institute's **Task Manager Application** was great source of inspiration. I follow it to design and develop my **OnlineSmoothieRecipe** website.
2. Code for **Login System** is taken from [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE)
3. Code Institute's tutor support has been a great help during the whole project, a very special thanks to tutor support team, specially Samantha.
4. The project is based on **Materialize**, so the code is taken from [Materialize](https://materializecss.com/)
5. A special thanks to my mentor **Sandeep Aggarwal** for his valuable feedback during mentoring sessions. 
6. Besides tutor support [Stack overflow](https://stackoverflow.com/) was great source of help.
7. [W3Schools](https://www.w3schools.com/)
8. [Flask Error Handler](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

## Disclaimer
Project is created for educational purposes. 
