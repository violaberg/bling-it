# **Bling It**

## **Overview**

<img scr><br>

Deployed project can be found here: [Bling It]()

## **Table of Contents**
* [**Overview**](#overview)
* [**User experience**](#user-experience-ux)
    + [**Strategy plane**](#strategy-plane)
        - [**Site goals**](#site-goals)
        - [**Opportunities**](#opportunities)
    + [**Scope plane**](#scope-plane)
    + [**Structure plane**](#structure-plane)
        - [**Developer Tasks & User Stories**](#developer-tasks--user-stories)
        - [**Flowchart**](#flowchart)
    + [**Skeleton plane**](#skeleton-plane)
        - [**Wireframes**](#wireframes)
    + [**Surface plane**](#surface-plane)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
* [**Agile Development**](#agile-development)
* [**Features & Future Development**](#features--future-development)
* [**Technologies used**](#technologies-used)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Acknowledgement & Credits**](#acknowledgement--credits)
* [**Media**](#media)

# **User experience (UX)**

During the planning phase I revisited UX videos provided on the course and used 5 planes to create my design.

## **Strategy plane**

### **Site goals**

* Offer a fully responsive user-friendly site to browse through.
* Implement fully functional features.

### **Opportunities**

Opportunity | Importance | Viability/Feasibility
---|---|---
Age verification | 5 | 5
Newsletter list | 3 | 5
User register/login | 5 | 5
User profile | 3 | 1
User ability to add photos to gallery | 2 | 3
User ability to delete previously added photos | 2 | 3
User reviews | 5 | 5
Full CRUD funcionality for user | 5 | 5
Full CRUD funcionality for admin | 5 | 5
Admin login via front end | 5 | 5
Password recovery | 5 | 5
Reservation management system for admin | 5 | 3
User ability to book a tour online | 5 | 5
User ability to edit/cancel booking online | 3 | 3
Booking confirmation on site | 5 | 5
Booking confirmation by email | 5 | 5
Booking reminder by email | 3 | 3
Visible booking for logged-in user | 3 | 2
Option to pay for booking online | 3 | 1
About page | 5 | 5
Contact form | 5 | 5
Social media links | 3 | 5
Terms & conditions | 3 | 3
Wine blog | 2 | 2
---|---|---
Total |95|96

## **Scope plane**

Due to a incredible amount of new knowledge and deadline for this project as for anything in life and to avoid scope creep, I used MoSCoW method to keep project on track and concentrate on delivering fully functional site. Unfortunately, since beginning of the project I knew I won't have time to implement everything I would like so decided to leave some features for future development.

* Must Have:
    + 

* Should Have:
    + 

* Could Have:
    + 

* Won't Have:
    + Bling It blog

## **Structure plane**

### **Developer Tasks & User Stories**

|   EPIC                    |ID|    Task        |
|:--------------------------|--|:---------------|
|SET UP & DEPLOYMENT        |  ||
|                           |  | As a developer, I can create a new Github repository to store my project files online|
|                           |  | As a developer, I can create a new workspace on Gitpod, install Django and add required libraries to have access to cloudbased images and postgress database|
|                           |  | As a developer, I can create a Heroku app and deploy project early to confirm funcionality|
|                           |  ||

<br>

|   EPIC                    |ID|    User Story  |
|:--------------------------|--|:---------------|
|NAVIGATION AND CONTENT     |  ||
|                           |  | As a user, I can navigate through website easily|
|                           |  | As a user, I can clearly understand the purpose of the site|
|                           |  | As a user, I can read relevant content|
|USER REGISTRATION & LOGIN  |  ||
|                           |  | As a user, I can register on the site|
|                           |  | As a user, I can login using USERNAME and password|
|                           |  | As a user, I can logout|
|BOOKING                    |  ||
|                           |  | As a user, I can book a tour|
|                           |  | As a logged-in user, I can see my booking|
|                           |  | As a logged-in user, I can edit my booking|
|                           |  | As a logged-in user, I can cancel my booking|
|REVIEWS                    |  ||
|                           |  | As a user, I can read reviews from other visitors|
|                           |  | As a logged-in user, I can leave a review|
|                           |  | As a logged-in user, I can add my photo taken at wine cellar when leaving a review|
|                           |  | As a logged-in user, I can delete my previously added photo to review|
|                           |  | As a logged-in user, I can edit my review|
|                           |  | As a logged-in user, I can delete my review|
|BLOG                       |  ||
|                           |  | As a user, I can see a paginated list of posts|
|                           |  | As a user, I can click on a post to see full text|
|COMMENTS                   |  ||
|                           |  | As a logged-in user, I can write a comment on post|
|                           |  | As a logged-in user, I can edit my comment|
|                           |  | As a logged-in user, I can delete my comment|
|                           |  | As a user, I can read other people comments|
|GALLERY                    |  ||
|                           |  | As a user, I explore images in gallery|
|CONTACT                    |  ||
|                           |  | As a user, I can find wine cellar's opening hours|
|                           |  | As a user, I can find wine cellar's location|
|                           |  | As a user, I can contact someone at wine cellar|
|ADMIN                      |  ||
|                           |  | As an admin, I can login to access admin panel|
|                           |  | As an admin, I can add/edit content|
|                           |  | As an admin, I can create draft posts|
|                           |  | As an admin, I can create, read, update and delete posts|
|                           |  | As an admin, I can delete inappropriate reviews/photos|
|                           |  | As an admin, I can approve comments|
|                           |  | As an admin, I can delete inappropriate comments|
|                           |  | As an admin, I can upload/ delete images from gallery|
|                           |  | As an admin, I can add description to images in gallery|
|DEVELOPER                  |  ||
|                           |  | As a developer, I can create wireframes|
|                           |  | As a developer, I can create a fully responsive site|
|                           |  | As a developer, I can choose color scheme and style of the website|
|                           |  | As a developer, I can choose fonts|
|                           |  ||

### **Flowchart**

To help with a flow of the website, I created a flowchart using [Draw.io](https://www.drawio.com/)

![Flowchart](static/docs/flowchart.drawio.png)

## **Skeleton plane**

### **Wireframes**

Wireframes for both desktop and mobile were created with [Balsamiq](https://balsamiq.com/) and can be seen below:

#### **Original wireframes:**

#### **Desktop wireframes:**

#### **Mobile wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Gallery Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Gemstone Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Contact Success Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Logout Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Register Page</summary><img src="static/docs/wireframes/"></details>

### **Database schema**

![Database schema]()

## **Surface plane**

### **Color Scheme**

![Color palette]()

To add more depth and interest to design but not make it overwhelming for user to look at, I created a pattern for background using two of my colors - ***:

![Pattern]()

### **Typography**

In planning the visual identity of my website, I meticulously selected two fonts, ***, to convey a harmonious blend of elegance and readability.

# **Agile Development**

I have included details of agile development in a separate file [AGILE.md](AGILE.md).

# **Features & Future Development**

## **Features**

## **Future Development**

In the second half of development I realized what I won't be able to implement due to dealine fast approaching. I decided to leave following features for future development:
* 

# **Technologies used**

* HTML
* CSS
* Javascript
* Python
* Django
* Django allAuth
* Bootstrap
* [Heroku](https://www.heroku.com/)
* Heroku PostreSQL & [ElephantSQL](https://www.elephantsql.com/)
* Jinja
* Whitenoise
* Cloudinary
* Summernote

# **Testing**

I have included details of testing in a separate file [TESTING.md](TESTING.md).

# **Deployment**

I have included details of testing in a separate file [DEPLOYMENT.md](DEPLOYMENT.md).

# **Acknowledgement & Credits**

* [Hero Patterns](https://heropatterns.com/) - background pattern
* [Google Fonts](https://fonts.google.com/) - fonts
* [Font Awesome](https://fontawesome.com/) - icons
* Walkthrough Boutique Ado from Code Institute course used to set up my project, styled and adjusted to suit my own project.

* The biggest thank you as always to my family during this busy time of juggling the biggest project so far, hackathon and life in general.
* Thank you as well to my mentor [David Bowers](https://github.com/dnlbowers) who supported me from the very beginning always giving the best advice and ideas for solutions and more importantly never losing hope in me, even when I did.
* And thank you to [Kim](https://github.com/kimatron) for continuous support during late and long nights and in general for convincing me to take on this course.
* And last but not least, thank you to Code Institute for organising hackathons. They have been a tremendous learning opportunity and therefore a great help during my project struggles.

# **Media**

## **Images**
* []() - image by ***, available at this [link]()