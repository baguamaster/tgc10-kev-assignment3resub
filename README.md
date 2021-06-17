# **Website for**

# **JIA BA BEH\***

**Milestone Project 3 Python &amp; Data Centric Development**

By Kevin Ho | traderkev54@yahoo.com

Welcome to JIA BA BEH – a recipe curation website designed to help members keep track of recipes. The website is meant to be depository of recipes by members, With the pandemic lingering, what better way to spend your time than by challenging, educating and upskilling yourself in learning more recipes.

**\*The name JIA BA BEH is an anglicized Chinese Hokkien dialect word for the question &quot;Have you eaten?&quot;**

**Demo Version of the Website**

Deployment of the website can be found in the heroku URL:

[**https://tgc10-kev-assignment3resub.herokuapp.com**](https://tgc10-kev-assignment3resub.herokuapp.com/)

Github version control may be accessed via:

[**https://github.com/baguamaster/tgc10-kev-assignment3resub**](https://github.com/baguamaster/tgc10-kev-assignment3resub)

![image](images/markdownpics/m1.JPG)

![](RackMultipart20210617-4-4z6swi_html_801d066a3b4be897.jpg)

# **Contents**

**JIA BA BEH**

1. Member Experience

2. Features

3. Database Structure

4. Technologies Applied

5. Other Tools used

6. Deployment

7. Testing, Validation, CRUD, Functionalities

8. Credit &amp; Acknowledgements

**1. Member Experience**

**1.1. Member Stories**

Member Story 1:

&quot;As a organic food member, I would like to be able to see which meals are suitable for me or not.&quot;

Member Story 2:

&quot;As a budding chef, I would like to share recipes with others&quot;

Member Story 3:

&quot;As a foodie, I would like to learn how to cook without hassle.&quot;

Member Story 4:

&quot;As a sufferer of food allergies, I would like to be aware of the ingredients and possible allergenic substances&quot;

Member Story 5:

&quot;As a social foodie, I would like to have a place to curate my inventions and share with friends&quot;

**1.2. Structure**

These member requirements were aligned with the site owner goals of JIA BA BEH to offer a simple-to-use and intuitive member interface.

![image](images/markdownpics/m2.JPG)

![](RackMultipart20210617-4-4z6swi_html_3a7241907c76cd1a.png)

**2. Features**

**2.1. General Features**

The colour theme is mainly warm/browns/green to create an ambience of earthiness and perception of wholesomeness as members peruse the site. The site allows those with food allergies to also monitor possible allergens in the recipes.

Features of the base.html template include:

Favicon:

This icon consists of the simple logo from the JIA BA BEH brand logo.

Background:

JIA BA BEH will curate and showcase food recipes from largely asian members. The colour scheme is earthy and green at the same time, suggesting comfort and down-to-earth homeliness.

**Objective:**

Create a website where enthusiasts can post recipes of their own, and also sample the curated recipes of other members.

The search function helps them to locate key information and display recipes in a digestible and searchable manner.

**Colour**

An maroon, black white theme is used in this instance.

**Fonts**

Monserrat font is used throughout for the website as it is clean, not too common and has nice kerning spaces.

**Images**

Images are chosen for their powerful storytelling ability and whilst some real pictures are used, some stock images were utilized in this demo version. No doubt in the production version, some professional images will need to be shot again.

**Copy**

Copy is written in an easy-going style, and aims to educate the reader on the many aspects of information security.

**Responsiveness**

The site is meant to be responsive to many devices, from desktop and laptop screen to tablets and smart mobile phones. It can be viewed in both portrait and landscape orientation. The breakpoints are usually half of the visual range in this instance.

**Consistency of design and messaging**

All elements on the website are intentioned to carry the same look and feel. The colour scheme and design schema using curved boxes/buttons carry this through.

**Navigation Bar:**

Is a simple bar using a warm / brown colour scheme to frame the page. The JIA BA BEH logo is to the top left corner.

Navigation Menu Items: All Recipes, Login, Register.

For the registered member: View All Recipes, Add Recipe, My Profile, Logout

![image](images/markdownpics/m3.JPG)

![](RackMultipart20210617-4-4z6swi_html_96cfb72231bb6a23.png)

**2.2. CRUD Functionalities**

Create, Read, Update and Delete functions need to be ascribed to the creation of recipes in the website. It gives the member control on being able to search, submit, update and delete their own recipes at their request rather than just the ability to read recipes passively.

![image](images/markdownpics/m4.JPG)

![](RackMultipart20210617-4-4z6swi_html_5a583baa3c080b60.png)

**2.2.1. Create**

**Add Recipe**

This page manifests the &quot;create&quot; functionality. Here, the member is prompted to provide a significant amount of information about the recipe simply by filling the fields requested.

The form inputs are all required entries with the exception of the YouTube video link since this is a totally optional feature.

At the bottom of the page in the Allergens section, I&#39;ve endeavored to educate the member on the 14 common allergenic ingredients to avoid (if one is so pre-disposed)

**2.2.2. Read**

**Search bar:**

The search bar draws on recipe\_name, recipe\_by, cuisine\_type, meal\_time, cooking\_time and description. Members can search for recipes submitted by a certain member through a name search and the function will filter results accordingly. This JIA BA BEH search function uses the default behaviour of a searching index, which is &quot;OR&quot; rather than &quot;AND&quot;.

For example, searching for &quot;minced meat kevin&quot; will filter all recipes and recipe curators that include any of those keywords.

The function uses the GET method and that inadvertently displays the search variable, query and keyword in the address bar as a slug. Adept members may do quick changes to searches by changing or adding keywords in the slug.

There are four buttons underneath the search bar namely the meal times: Breakfast, Lunch, Dinner and Dessert. These are all wired to the search bar.

(img#6search)

**Recipe Cards:**

The .card-reveal and .activator classes from Materialize function will allow members to click on the card and view a summary of the recipe gaining access to the ingredients and steps of cooking. The View buttons are deliberately made available to both members and non-members.

Mealtimes where the recipe may be enjoyed are represented as coloured dots as a visual cue to what type of food it is.

**The View All Recipes Page:**

The cover header addresses the member and can be viewed in full screen modal thanks to the use of the .materialboxed class. This provides allows easy fit of the images used on the page. If the session member views their own recipe, an edit button shows up on the page.

**2.2.3. Update**

**Edit Button:**

For this function, each member is allowed to only see the edit button on receipe that they have curated. This also finds its way to the Full Recipe page and recipe cards on the My Profile page.

All buttons are render the the edit\_recipe template in the following fashion:

**Edit Recipe Page:**

The use of Flask and Jinja allows pages to pull and display recipe data by liking with recipe.\_id found in the app.py function. Upon submission of the data, the member is redirected to the same page to facilitate more edits.

![image](images/markdownpics/m5.JPG)

![](RackMultipart20210617-4-4z6swi_html_d64b6e3cadda76c1.png)

**2.2.4. Delete**

The **delete** button is strategically places at the bottom of the edit\_recipe template marked in red. This type of alert is highly visual and acts to draw attention to this function.

![image](images/markdownpics/m6.jpg)

![](RackMultipart20210617-4-4z6swi_html_648405fe2acfa1d8.png)

**2.3 Special segments**

**Allergens**

A special segment drawing attention to the 14 listed common allergens fulfill a public service by drawing attention to their presence in some recipes. This allows members to have this as one of their search terms.

**3. Database Structure**

**3.1. Recipes Collection**

Data is defined in the following fashion below:

**Data Key Data Type**

cuisine\_type string

recipe\_name string

meal\_time\* array

description string

servings string

is\_vegetarian\*\* string

prep\_time string

cooking\_time string

ingredients object

method object

allergens array

image string

video string

recipe\_by string

\*The meal\_time is defined by the 4 types: Breakfast, Lunch, Dinner and Dessert. It can be noted that members define meal types and we recognize some meals can satisfy more than one option e.g. minced meat rice could be eaten during lunch and dinner.

\*\* is\_vegetarian data is stored as a string.

Exemplary storage of data for Minced Meat Rice:

{

\_id: 8011123616084d23416gd3

cuisine\_type: &quot;Asian&quot;

recipe\_name: &quot;Minced Meat Rice&quot;

meal\_time: Lunch, Dinner

description: &quot;An Asian version of rice bolognaise with mushrooms&quot;

servings: &quot;4&quot;

is\_vegetarian: &quot;No&quot;

prep\_time: &quot;30&quot;

cooking\_time: &quot;30&quot;

ingredients: (Object List with additive function)

method: (Object List with additive function)

allergens: Array List

image: &quot;https://nitrocdn.com/NWTRtZLPBiwunRiGefRPjojVNExYiWXv/assets/static/source/rev-

b0fa5a6/wp-content/uploads/2019/09/1406\_Cantonese-Ground-Beef-And-Eggs\_003.jpg&quot;

video: &quot;https://www.youtube.com/watch?v=QWvuzhrsc8I&quot;

recipe\_by: &quot;kevin&quot;

}

(img#9mincedrice)

**3.2. Members Collection**

**Data Key Data Type**

member\_name string

password string

email string

**4. Technologies Applied**

- HTM5 to structure the webpages and CSS3 to style them.
- JavaScript to run functions
- Python 3.7 via the Flask framework to drive database functions
- MongoDB for non relational noSQL data management
- Git for Versioning Control System and GitHub for repositories.
- Bootstrap 4.5, including its components and utilities for layout. Key elements favoured:
- NavBar is used for the main navigation,
- Distinct images are used as attention grabber
- CSS Stylesheet from w3newbie (https://w3newbie.com/responsive-html5-web-design-tutorial-and-free-template-code/)
- Code Institute&#39;s templates (https://github.com/Code-Institute-Org/gitpod-full-template) to start the coding.
- The template used for Readme.md is also from Code Institute (https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)

**5. Other Tools are also used in the course of development:**

For validating JavaScript:

JShint validator (https://jshint.com/)

For validating markup:

W3 Markup Validator (http://validator.w3.org/)

For validating CSS:

W3 Jigsaw Validator (https://jigsaw.w3.org/css-validator/)

For checking links:

W3C Link Checker (https://validator.w3.org/checklink)

For image editing

Adobe Lightroom (https://lightroom.adobe.com/)

For responsiveness:

Responsive Web Design Checker (https://responsivedesignchecker.com/)

For mindmapping:

Mindup mind mapper (https://www.mindmup.com/)

For UX readability:

Flesch-Kincaid readability test (https://www.webfx.com/tools/read-able/)

For UX viewing on various device formats:

Responsinator: (https://www.responsinator.com/)5. Prototyping

**6. Deployment**

**Preparation**

All major changes were committed on Visual Code Studio as an independent instance and ported over to gitpod and Heroku via github towards deadline.

**Prior to going Live, the following elements are checked gitpod&#39;s native browser preview via open port 8080. This is done by executing command in terminal python3 app.py to run the flask app in app.py:**

Mapping of Learning objectives from &#39;Code Institute&#39;s&#39; Assessment Handbook`

Check code linters and validators are clear

Check that all images sources are unbroken

Test viewport dynamic resizing for android (Samsung S9) and iOS (iPhone X/XS)

Check Create, Read, Display, Update, Delete functions for recipes – add test recipes

Ensure string key-value pair stored in mongoDB document

**Content**

**7. Testing**

**7.1 Website Interactivity**

**Usability**

Website navigation controls are kept simple to be familiar to a web surfer, and a same consistency in design elements permeates throughout the website. 1. Logo that leads back to the home page 2. Main navigation bar at the top 3. Pagination is included to help visitors identify which part of the site they are at 4. Easy to identify buttons

Reader Comprehension

Content are grouped according to subject matter and prose is broken up when long.

The Flesch Readability Test = 54.7, Flesch-Kincaid Grade Level Score = 7, which means the website is easily understood by 13-14 year olds and up.

image

**Operability**

The visitor should be able to easily navigate without trouble.

There is a form function in the &quot;subscribe&quot; page to allow communication

There is sufficient information for an interested party to communicate.

Both search engines follow the familiar search bar and radio buttons format

**Attractiveness**

A responsive design takes into consideration how it looks when on viewed on a desktop browsers as well as smaller screens like mobile phone. The layout will change to cater for different size of the device

Utilisation of white spaces between different sections and components of the page to increase **readability**

Usability compliance

Semantic HTML to enhance code readability

Optimisation of website elements

Compliance to website accessibility guidelines

SEO optimization will be for subsequent steps

![image](img/markdownpics/m12.jpg)

![](RackMultipart20210617-4-4z6swi_html_a2eb081b3a2370cc.png)

**7.2 Code Validation using Code Validators**

1. style.css was validated using the W3C Jigsaw validator ([Link](https://jigsaw.w3.org/css-validator/validator))

No issues were found with style.css

![image](images/markdownpics/m7.JPG)

![](RackMultipart20210617-4-4z6swi_html_77ee3b749b3ec854.jpg)

2. all .html files in templates was validated using the W3 Nu HTML Validator ([Link](https://validator.w3.org/nu/#file))

Many of the Jinja2 syntax were picked up as errors

In order to handle this, each flag was picked out to check if it was truly related to Jinja2 or was an actual error

Post code fix Response from Nu Html Checker: &quot;Document checking completed. No errors or warnings to show.&quot;

**7.3 PEP8 Style guide for Python**

1. Ensure code in app.py complies with PEP8 style guide
2. This is ensured by making sure no callouts from gitpod python linter are present in app.py and that lines of code in app.py to not exceed 79 Characters

![image](images/markdownpics/m8.JPG)

![](RackMultipart20210617-4-4z6swi_html_8320a29d807bad09.jpg)

![image](images/markdownpics/m9.JPG)

![](RackMultipart20210617-4-4z6swi_html_ffb0c5985abf1d76.jpg)

![image](images/markdownpics/m10.JPG)

![](RackMultipart20210617-4-4z6swi_html_2102671f07c1bbbc.jpg)

**7.4 Testing**

7.4.1. Manual Testing of Features

The JIA BA BEH website was designed to give members the ability to find recipes and share them on social media. Members that have registered an account can engage in creating, editing and deleting their own recipes.

In order to demonstrate the full manual testing of these features, a test account &amp; login have been created which allows the manipulation of CRUD functionalities.

**7.4.2 Features Before Registering**

Click View All Recipes (as unregistered user): On first arrival of the JIA BA BEH website, the member will be greeted and referred to as &quot;Guest&quot; on the View All Recipes page. At this point, the member will only be able to find and read recipes via the view buttons:

_ **All\_recipes page for guest** _

Use Search bar: Use the search bar to search for keywords, by typing words and then pressing the search button. In this test, &quot;Minced Rice Kevin&quot; is searched. All recipes containing the keywords will be displayed:

search functionality testing

search functionality testing card reveal

Click on the &quot;Minced Meat Rice&quot; card image: to confirm working of the summary of the recipe:

testing of recipe card preview or reveal

**7.4.3 Register account**

Click Register on the navigation bar:

Confirm that the following page loads correctly:

testing member registration

**Confirmation of Successful Member Creation**

For the purpose of this test, I created an account with a fictitious member name of &quot;foodiekev&quot; as shown in the above image. When successfully registered, &quot;foodiekev&quot; will be redirected to their profile page.

**testing the redirection to member&#39;s profile**

Another member cannot create an account with the same email or membername that has been used before. The system will flash the following message:

**membername exists**

**email exists**

**7.4.4 Login**

If member inputs either an incorrect member\_name or password, the following flash message will be shown:

**incorrect membername (or password)**

Upon successful log in, members will be redirected to their respective profile page.

**7.4.5 Create Recipes (CRUD Functionality)**

Steps: Click Add New Recipe on the navigation bar:

Add Recipe page

Fill in all fields. (The YouTube link is left optional and can be left blank). &quot;foodiekev&quot; will create a new recipe called &quot;Mince Meat Mushroom Rice&quot;:

**Successful: Adding Mince Meat Mushroom Rice recipe**

Once submitted, the following flash message will show:

**Recipe successfully added**

**7.4.6 Read Recipes (CRUD Functionality)**

For viewing of all recipes on the website, msember must click &quot;View All Recipes&quot; on the navigation bar. The menu items will change to display options relevant to a registered member namely: Logout, Add Recipe and My Profile. The page will display as follows:

**View All Recipes page for registered member**

Members can then view their newly created recipes, which will be posted on the View All Recipes page as well as on their Profile page.

To view individual recipes, members need to click on the view button of the desired recipe. For this test, &quot;foodiekev&quot; has chosen to view the recipe for &quot;Lamb Nasi Briyani&quot;:

Full Recipe page

If any member chooses to view their own recipe, there will be an &quot;edit&quot; button available just before the ingredients section.

Own recipe&#39;s full page

![](RackMultipart20210617-4-4z6swi_html_397a0c25925b561.png)

![image](images/markdownpics/m11.JPG)

**7.4.7 Update/Editing Recipes (CRUD Functionality)**

Clicking the &quot;edit&quot; button which can be found on the recipe page allows changes to the recipe details:

**Successful testing for editing recipe**

**7.4.8 Deleting recipes (CRUD Functionality)**

If a member decides that they want to delete their recipe, there will be a two-step process for extra authentication. This provides a failsafe on accidental deletions. If member decides to click &quot;Yes&quot;, then the recipe will be permanently removed from the database and subsequently JIA BA BEH.

**Delete Recipe modal Tested**

The successfully deleted flash message will show.

**8. Credits &amp; Acknowledgements**

MondoDB deployment on Heroku templates – Accime Esterling

CRUD, restful API &amp; Flask guidance – Coders Page

Harry Roberts / CSS-tricks – CSS style templates

UI/UX template ideas – Drew Ryan / W3newbie

**Faculty Acknowledgements**

Mr Alexander Yan – Course Manager and ever-patient advisor

Mr Malcolm Yam - Bootrap instructor

Mr Arif Rawi - HTML and CSS instructor

Mr Paul Kunxin Chor – The master of python, Jinja2, flask, mongoDB, pymongo

Mr Ace Liang - Teaching assistant, who supported this project by holding consultation sessions.

Mr Ng TS – Friend from the IT industry, who gave guidance on last minute coding guidance and py.class templates. (And fantastic saves on short notice on Heroku deployment disaster incidences!)

Deployment of the website can be found in the heroku URL:

[**https://tgc10-kev-assignment3resub.herokuapp.com/**](https://tgc10-kev-assignment3resub.herokuapp.com/)

Github version control may be accessed via:

[**https://github.com/baguamaster/tgc10-kev-assignment3resub**](https://github.com/baguamaster/tgc10-kev-assignment3resub)
