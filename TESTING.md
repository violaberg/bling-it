# **TESTING**

## **Table of Contents**
* [**User Story Testing**](#user-story-testing)
* [**Code Validation**](#code-validation)
    + [**HTML**](#html)
    + [**CSS**](#css)
    + [**JavaScript**](#javascript)
    + [**Python**](#python)
* [**Automated Testing**](#automated-testing)
* [**Browser Testing**](#browser-testing)
* [**Device Testing**](#device-testing)
* [**Lighthouse**](#lighthouse)
    + [**Desktop**](#desktop)
    + [**Mobile**](#mobile)
* [**Manual Testing**](#manual-testing)
    + [**Navigation**](#navigation)
    + [**Home Page**](#home-page)
    + [**All Gemstone Page**](#all-gemstones-page)
    + [**Gemstone's Detail Page**](#gemstones-detail-page)
    + [**Reviews Page**](#reviews-page)
    + [**Contact Page**](#contact-page)
    + [**FAQ Page**](#faq-page)
    + [**Privacy Policy Page**](#privacy-policy-page)
    + [**Sign Up Page**](#sign-up-page)
    + [**Login Page**](#login-page)
    + [**Log out Page**](#log-out-page)
    + [**Shopping Bag Page**](#shopping-bag-page)
    + [**Checkout Page**](#checkout-page)
    + [**Profile Page**](#profile-page)
    + [**Add Gemstone Page for Admin**](#add-gemstone-page-for-admin)
    + [**Edit Gemstone Page for Admin**](#log-out-page)
* [**Responsiveness**]()
* [**Bugs & Fixes**]()

## **User Story Testing**

For the following, I will leave out the type of user, ***As a developer/admin/user, I can…***, and only list the latter part of the story as a heading.

### **EPIC 1 - Planning:**

**...create wireframes so that I can clearly see the planned site layout** |passed |
|:---:|:---|
Wireframes created for desktop |&check;|
Wireframes created for mobile |&check;|
|||

**...choose fonts so that I can create a sophisticated site** |passed |
|:---:|:---|
Main, easy to read, Google font chosen |&check;|
Heading and special text Google font chosen |&check;|
Both fonts suit the style of app |&check;|
|||

**...choose color palette and style of the site so that I can have a clear vision of end result** |passed |
|:---:|:---|
Colours chosen keeping in mind project style |&check;|
Colours are pleasant to an eye and create a good contrast |&check;|
Logo and background chosen to suit the style and colors |&check;|
Color palette created once colors have been chosen |&check;|
|||

**... create ERD so that I can clearly see my project's schema** |passed |
|:---:|:---|
ERD created and uploaded to project's folder |&check;|
|||

### **EPIC 2 - Setup and Deployment:**

**...create Github repository so that I can store my project's files online** |passed |
|:---:|:---|
Github repository created |&check;|
Kanban board using MoSCoW method created |&check;|
Project set to Public |&check;|
|||

**...create new workspace so that I can start working on project** |passed |
|:---:|:---|
Workspace on Gitpod using CI Gitpod full template created |&check;|
Django installed |&check;|
README, TESTING, DEPLOYMENT and AGILE |&check;|
New Heroku app created and deployed early so to can confirm functionality |&check;|
Databse connected |&check;|
|||

**...design a responsive app so that I can ensure it's easy to use on any device** |passed |
|:---:|:---|
Project designed and developed with mobile first approach |&check;|
Bootstrap and media queries used for responsiveness |&check;|
|||

**... create user-friendly error pages so that I can guide user safely back to home page** |passed |
|:---:|:---|
403, 404, 500 error pages created |&check;|
Customize to project's style |&check;|
'Back to home page' button added |&check;|
|||

### **EPIC 3 - Admin and Store Management:**

**...easily login so that I can update site when needed** |passed |
|:---:|:---|
Access to only authenticated admin |&check;|
User friendly admin panel |&check;|
|||

**...add a product so that I can add new items to store** |passed |
|:---:|:---|
User friendly form in admin panel to add products |&check;|
|||

**...edit/ update a product so that I can change product prices, descriptions, images and other product criteria** |passed |
|:---:|:---|
User friendly form in admin panel to edit/ update products |&check;|
|||

**... create ERD so that I can clearly see my project's schema** |passed |
|:---:|:---|
delete a product so that I can remove items that are no longer for sale |&check;|
User friendly form on admin panel to delete a product |&check;|
Alert message confirming deletion |left for future dev|
|||

### **EPIC 4 - Viewing and Navigating:**

**...view a list of products so that I can select some to purchase if I like** |passed |
|:---:|:---|
User friendly product list with images (or default image) and price |&check;|
|||

**...check individual product detail page so that I can identify price, description, product image and any other additional information** |passed |
|:---:|:---|
User friendly product page created |&check;|
Easy to read description written |&check;|
All necessary information clearly visible |&check;|
|||

**...choose a gemstone so that I can quickly find products I'm interested in and don't have to search through all** |passed |
|:---:|:---|
Option to choose a certain gemstone type |&check;|
|||

**...easily view the total of my purchase at any time so that I can avoid spending too much** |passed |
|:---:|:---|
Clearly visible total at the top of the page beside cart icon |&check;|
|||

**...add items I like to my wishlist so that I can find them easily if I decide to purchase later** |passed |
|:---:|:---|
Easily visible 'heart' for option to add item to wishlist |&check;|
Wishlist accessible on top of the page |&check;|
|||

### **EPIC 5 - Sorting and Searching:**

**...search for a product by name or a description so that I can find a specific product I'd like to purchase** |passed |
|:---:|:---|
Clearly visible search bar at the top of the page |&check;|
|||

**...easily see what I've searched for and the number of results so that I can quickly see whether the product I want is available and decide if I want to purchase it** |passed |
|:---:|:---|
Clearly visible search results |&check;|
|||

**...sort the list of available products so that I can easily identify the best priced products** |passed |
|:---:|:---|
Easy to sort items |&check;|
Option to sort A-Z/ Z-A |&check;|
By price |&check;|
By carat size |&check;|
|||

### **EPIC 6 - Registration and User Accounts:**

**...register on site so that I can save my personal information and wishlist** |passed |
|:---:|:---|
User friendly sign up form |&check;|
User data stored and processed securely |&check;|
Validation for user input |&check;|
|||

**...login/ logout so that I can access my personal account information** |passed |
|:---:|:---|
User friendly form for login |&check;|
Clearly visible logout button |&check;|
Confirmation before and after logging out |&check;|
|||

**...receive an email confirmation after registration so that I can verify that my account registration has been successful** |passed |
|:---:|:---|
Email confirmation sent successfully |&check;|
|||

**...easily recover my password in case I forget it so that I can recover access to my account** |passed |
|:---:|:---|
Easily visible and user friendly way to recover password |&check;|
|||

**...have a personalized user profile so that I can view my personal order history and order confirmation, and save my payment information** |passed |
|:---:|:---|
User friendly profile with personal information easily accessible |&check;|
|||

### **EPIC 7 - Purchasing and Checkout:**

**...view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive** |passed |
|:---:|:---|
User friendly checkout bag |&check;|
Clearly visible items in bag with prices beside each |&check;|
Clearly visible total amount of purchase |&check;|
|||

**...remove individual items from my bag so that I can easily make changes to my purchase before checkout** |passed |
|:---:|:---|
Easy to remove items before checkout |&check;|
Immediate changes in bag after removal |&check;|
|||

**...feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase** |passed |
|:---:|:---|
All safety features implemented |&check;|
|||

**...easily enter my payment information so that I can check out quickly and with no hassle** |passed |
|:---:|:---|
User friendly form to fill in payment details |&check;|
Payment detail verification |&check;|
|||

**... view an order confirmation after checkout so that I can verify that I haven't made any mistakes** |passed |
|:---:|:---|
Clearly visible order confirmation with items and total included |&check;|
|||

**...receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records** |passed |
|:---:|:---|
Email sent successfully |&check;|
|||

**...check my order status so that I can know when to expect it** |passed |
|:---:|:---|
Clearly visible order status in user profile |&check;|
Order stages - In Progress, Delivered, Cancelled |&check;|
|||

### **EPIC 8 - Contact:**

**...easily locate contact details so that I can contact shop if I need** |passed |
|:---:|:---|
Easily visible contact details in footer visible on every page |&check;|
|||

**...contact someone at Bling It so that I can receive any additional information needed** |passed |
|:---:|:---|
Responsive and easy to use contact form with necessary fields |&check;|
Site should prominently display contact information, including phone number, a contact form and/or email address |&check;|
Email confirmation page after message has been sent successfully |&check;|
|||

**...subscribe to newsletters so that I can receive the latest news, special offers and sales notifications** |passed |
|:---:|:---|
Clearly visible subscription form on home page |&check;|
|||

### **EPIC 9 - FAQ and Privacy Policy:**

**...create/edit a list of FAQ so that I can offer users instant answers to their questions** |passed |
|:---:|:---|
User friendly option to write FAQ through admin panel |&check;|
Option to edit questions |&check;|
|||

**...read through FAQ so that I can find answers to my questions without contacting shop** |passed |
|:---:|:---|
Easy to locate FAQ page |&check;|
Clearly written questions and answers |&check;|
|||

**...read Privacy Policy so that I can see how my personal information, data will be used and what rights I have** |passed |
|:---:|:---|
Clearly written policy |&check;|
Easy to access Policy page |&check;|
|||


### **EPIC 10 - Reviews and Ratings:**

**...leave a review so that I can contribute to the community and help others to make informed decisions** |passed |
|:---:|:---|
The review submission form should include fields for the user to enter a title and written content |&check;|
User friendly form |&check;|
Character limit should be set |&check;|
|||

**...leave a rating for the site so that I can let others know of my experience with shop** |passed |
|:---:|:---|
Clearly visible location to leave a rating for site |&check;|
|||

**...delete review so that I can ensure appropriate content on app** |passed |
|:---:|:---|
Delete button/ link |&check;|
Modal to confirm deletion |&check;|
|||

## **Code Validation**

### **HTML**

All HTML pages were validated using [W3C HTML Validator](https://validator.w3.org/)

|   PAGE                                     |  VALIDATOR SCREENSHOT                                     |   RESULT    |
|--------------------------------------------|-----------------------------------------------------------|-------------|
| Home Page                                  |<details><summary>Home Page</summary><img src="static/docs/validators/home-page-w3.png"></details>| <mark>PASS</mark> |
| About Page                                 |<details><summary>About Page</summary><img src="static/docs/validators/about-page-w3.png"></details>| <mark>PASS</mark> |
| All Gemstones Page                         |<details><summary>All Gemstones Page</summary><img src="static/docs/validators/all-gemstones-w3.png"></details>| <mark>PASS</mark> |
| Gemstones Detail Page                      |<details><summary>Gemstones Detail Page</summary><img src="static/docs/validators/gemstone-detail-w3.png"></details>| <mark>PASS</mark> |
| Reviews Page                               |<details><summary>Reviews Page</summary><img src="static/docs/validators/reviews-page-w3.png"></details>| <mark></mark> |
| Contact Page                               |<details><summary>Contact Page</summary><img src="static/docs/validators/contact-page-w3.png"></details>| <mark>PASS</mark> |
| FAQ Page                                   |<details><summary>FAQ Page</summary><img src="static/docs/validators/faq-page-w3.png"></details>| <mark>PASS</mark> |
| Privacy Policy Page                        |<details><summary>Privacy Policy Page</summary><img src="static/docs/validators/privacy-policy-w3.png"></details>| <mark>PASS</mark> |
| Bag Page                                   |<details><summary>Bag Page</summary><img src="static/docs/validators/bag-w3.png"></details>| <mark>PASS</mark> |
| Checkout Page                              |<details><summary>Checkout Page</summary><img src="static/docs/validators/checkout-w3.png"></details>| <mark>PASS</mark> |
| Checkout Success Page                      |<details><summary>Checkout Success Page</summary><img src="static/docs/validators/checkout-success-w3.png"></details>| <mark>PASS</mark> |
| Profile Page                               |<details><summary>Profile Page</summary><img src="static/docs/validators/profile-w3.png"></details>| <mark>PASS</mark> |
| Login Page                                 |<details><summary>Login Page</summary><img src="static/docs/validators/"></details>| <mark>PASS</mark> |
| Logout Page                                |<details><summary>Logout Page</summary><img src="static/docs/validators"></details>| <mark>PASS</mark> |
| Error 403 Page                             |<details><summary>Error 403 Page</summary><img src="static/docs/validators/error-403-w3.PNG"></details>| <mark>PASS</mark> |
| Error 404 Page                             |<details><summary>Error 404 Page</summary><img src="static/docs/validators/error-404-w3.PNG"></details>| <mark>PASS</mark> |

### **CSS**

All CSS pages were validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

|   PAGE                                     |  VALIDATOR SCREENSHOT                                     |   RESULT    |
|--------------------------------------------|-----------------------------------------------------------|-------------|
| base.css                                   |<details><summary>base.css</summary><img src="static/docs/validators/base.css-w3.png"></details>| <mark>PASS</mark> |
| checkout.css                               |<details><summary>checkout.css</summary><img src="static/docs/validators/checkout.css-w3.png"></details>| <mark>PASS</mark> |
| profile.css                                |<details><summary>profile.css</summary><img src="static/docs/validators/profile.css-w3.png"></details>| <mark>PASS</mark> |

### **JavaScript**

All JavaScript was validated using (JS Hint)[https://jshint.com/]

|   PAGE                                     |  VALIDATOR SCREENSHOT                                     |   RESULT    |
|--------------------------------------------|-----------------------------------------------------------|-------------|
| gemstones.html                             |<details><summary>gemstones.html</summary><img src="static/docs/validators/gemstones-jshint.PNG"></details>| <mark>PASS</mark> |
| scroll-to-top btn                          |<details><summary>reviews.html</summary><img src="static/docs/validators/scroll-to-top-jshint.PNG"></details>| <mark>PASS</mark> |
| profile.js                                 |<details><summary>profile.js</summary><img src="static/docs/validators/profiles-jshint.png"></details>| <mark>PASS</mark> |

### **Python**

All Python was validated using (CI Python Linter)[https://pep8ci.herokuapp.com/]

| FILE     | VALIDATOR SCREENSHOT                                                                                    | RESULT            |
| -------- | ------------------------------------------------------------------------------------------------------- | ----------------- |
| ***blingit*** |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/project-views-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/project-urls-plinter.png"></details> | <mark>PASS</mark> |
| settings.py | <details><summary>Settings</summary><img src="static/docs/validators/settings-plinter.png"></details> | <mark>few errors but these can't be split for better functionality</mark> |
| ***home*** |
| models.py   | <details><summary>Models</summary><img src="static/docs/validators/home-models-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/home-views-plinter.png"></details> | <mark>PASS</mark> |
| forms.py    | <details><summary>Forms</summary><img src="static/docs/validators/home-forms-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/home-urls-plinter.png"></details> | <mark>PASS</mark> |
| admin.py    | <details><summary>Admin</summary><img src="static/docs/validators/home-admin-plinter.png"></details> | <mark>PASS</mark> |
| apps.py     | <details><summary>Apps</summary><img src="static/docs/validators/home-apps-plinter.png"></details> | <mark>PASS</mark> |
| tests.py    | <details><summary>Tests</summary><img src="static/docs/validators/home-tests-plinter.png"></details> | <mark>PASS</mark> |
| ***bag*** |
| apps.py     | <details><summary>Models</summary><img src="static/docs/validators/bag-apps-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/bag-views-plinter.png"></details> | <mark>PASS</mark> |
| contexts.py | <details><summary>Contexts</summary><img src="static/docs/validators/bag-contexts-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/bag-urls-plinter.png"></details> | <mark>PASS</mark> |
| ***checkout*** |
| models.py   | <details><summary>Models</summary><img src="static/docs/validators/checkout-models-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/checkout-views-plinter.png"></details> | <mark>PASS</mark> |
| forms.py    | <details><summary>Forms</summary><img src="static/docs/validators/checkout-forms-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/checkout-urls-plinter.png"></details> | <mark>PASS</mark> |
| admin.py    | <details><summary>Admin</summary><img src="static/docs/validators/checkout-admin-plinter.png"></details> | <mark>PASS</mark> |
| signals.py  | <details><summary>Signals</summary><img src="static/docs/validators/checkout-signals-plinter.png"></details> | <mark>PASS</mark> |
| webhooks.py  | <details><summary>Webhook</summary><img src="static/docs/validators/checkout-webhook-plinter.png"></details> | <mark>PASS</mark> |
| webhook_handlers.py | <details><summary>Webhook Handler</summary><img src="static/docs/validators/checkout-webhookhandler-plinter.png"></details> | <mark>PASS</mark> |
| ***contact*** |
| models.py   | <details><summary>Models</summary><img src="static/docs/validators/contact-models-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/contact-views-plinter.png"></details> | <mark>PASS</mark> |
| forms.py    | <details><summary>Forms</summary><img src="static/docs/validators/contact-forms-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/contact-urls-plinter.png"></details> | <mark>PASS</mark> |
| tests.py    | <details><summary>Tests</summary><img src="static/docs/validators/contact-tests-plinter.png"></details> | <mark>PASS</mark> |
| apps.py     | <details><summary>Apps</summary><img src="static/docs/validators/contact-apps-plinter.png"></details> | <mark>PASS</mark> |
| ***gemstones*** |
| models.py   | <details><summary>Models</summary><img src="static/docs/validators/gemstones-models-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/gemstones-views-plinter.png"></details> | <mark>PASS</mark> |
| forms.py    | <details><summary>Forms</summary><img src="static/docs/validators/gemstones-forms-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/gemstones-urls-plinter.png"></details> | <mark>PASS</mark> |
| admin.py    | <details><summary>Admin</summary><img src="static/docs/validators/gemstones-admin-plinter.png"></details> | <mark>PASS</mark> |
| widgets.py  | <details><summary>Widgets</summary><img src="static/docs/validators/gemstones-widgets-plinter.png"></details> | <mark>PASS</mark> |
| apps.py     | <details><summary>Apps</summary><img src="static/docs/validators/gemstones-apps-plinter.png"></details> | <mark>PASS</mark> |
| ***profiles*** |
| models.py   | <details><summary>Models</summary><img src="static/docs/validators/profiles-models-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/profiles-views-plinter.png"></details> | <mark>PASS</mark> |
| forms.py    | <details><summary>Forms</summary><img src="static/docs/validators/profiles-forms-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/project-urls-plinter.png"></details> | <mark>PASS</mark> |
| apps.py     | <details><summary>Apps</summary><img src="static/docs/validators/profiles-apps-plinter.png"></details> | <mark>PASS</mark> |
| ***reviews*** |
| models.py   | <details><summary>Models</summary><img src="static/docs/validators/reviews-models-plinter.png"></details> | <mark>PASS</mark> |
| views.py    | <details><summary>Views</summary><img src="static/docs/validators/reviews-views-plinter.png"></details> | <mark>PASS</mark> |
| forms.py    | <details><summary>Forms</summary><img src="static/docs/validators/reviews-forms-plinter.png"></details> | <mark>PASS</mark> |
| urls.py     | <details><summary>Urls</summary><img src="static/docs/validators/reviews-urls-plinter.png"></details> | <mark>PASS</mark> |
| admin.py    | <details><summary>Admin</summary><img src="static/docs/validators/reviews-admin-plinter.png"></details> | <mark>PASS</mark> |
| apps.py     | <details><summary>Apps</summary><img src="static/docs/validators/reviews-apps-plinter.png"></details> | <mark>PASS</mark> |
| tests.py    | <details><summary>Tests</summary><img src="static/docs/validators/reviews-tests-plinter.png"></details> | <mark>PASS</mark> |
|  |  |  |

## **Automated Testing**

Some automated testing was done alongside manual and results can be found below:

* Home app<br>
    ![home app](static/docs/tests/home-tests.png)
* Contact app<br>
    ![contact app](static/docs/tests/contact-tests.png)
* Reviews app<br>
    ![reviews app](static/docs/tests/reviews-tests.png)

## **Browser Testing**

The website was tested on Google Chrome, Firefox and Microsoft Edge browsers.

## **Device Testing**

The website was tested on various devices using Chrome DevTools and real-life device, such as iPhone 12, Samsung Galaxy S23, Lenovo X1 Carbon laptop and iPad Air.

## **Lighthouse**

# **Desktop**

| Home Desktop | <details><summary>Home Desktop</summary><img src="static/docs/lighthouse/home-lhouse-desktop.png"></details> |
| About Desktop | <details><summary>About Desktop</summary><img src="static/docs/lighthouse/about-lhouse-desktop.png"></details> |
| All Gemstones Desktop | <details><summary>All Gemstones Desktop</summary><img src="static/docs/lighthouse/gemstones-lhouse-desktop.png"></details> |
| Gemstone Detail Desktop | <details><summary>Gemstone Detail Desktop</summary><img src="static/docs/lighthouse/gemstone-detail-lhouse-desktop.png"></details> |
| Reviews Desktop | <details><summary>Reviews Desktop</summary><img src="static/docs/lighthouse/reviews-lhouse-desktop.png"></details> |
| Contact Desktop | <details><summary>Contact Desktop</summary><img src="static/docs/lighthouse/home-lhouse-desktop.png"></details> |
| Profile Desktop | <details><summary>Profile Desktop</summary><img src="static/docs/lighthouse/profile-lhouse-desktop.png"></details> |
| FAQ Desktop | <details><summary>FAQ Desktop</summary><img src="static/docs/lighthouse/faq-lhouse-desktop.png"></details> |
| Privacy Policy Desktop | <details><summary>Privacy Policy Desktop</summary><img src="static/docs/lighthouse/policy-lhouse-desktop.png"></details> |

# **Mobile**

| Home Mobile | <details><summary>Home Mobile</summary><img src="static/docs/lighthouse/home-lhouse-mobile.png"></details> |
| About Mobile | <details><summary>About Mobile</summary><img src="static/docs/lighthouse/about-lhouse-mobile.png"></details> |
| All Gemstones Mobile | <details><summary>All Gemstones Mobile</summary><img src="static/docs/lighthouse/gemstones-lhouse-mobile.png"></details> |
| Gemstone Detail Mobile | <details><summary>Gemstone Detail Mobile</summary><img src="static/docs/lighthouse/gemstone-detail-lhouse-mobile.png"></details> |
| Reviews Mobile | <details><summary>Reviews Mobile</summary><img src="static/docs/lighthouse/reviews-lhouse-mobile.png"></details> |
| Contact Mobile | <details><summary>Contact Mobile</summary><img src="static/docs/lighthouse/home-lhouse-mobile.png"></details> |
| Profile Mobile | <details><summary>Profile Mobile</summary><img src="static/docs/lighthouse/profile-lhouse-mobile.png"></details> |
| FAQ Mobile | <details><summary>FAQ Mobile</summary><img src="static/docs/lighthouse/faq-lhouse-mobile.png"></details> |
| Privacy Policy Mobile | <details><summary>Privacy Policy Mobile</summary><img src="static/docs/lighthouse/policy-lhouse-mobile.png"></details> |

## **Manual Testing**

### **Navigation**

| Element                | Action      | Expected Result                                         | Pass/Fail         |
| ---------------------- | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                   | Click       | Redirect to Home page                                   | <mark>PASS</mark> |
| Home Link              | Click       | Redirect to Home page                                   | <mark>PASS</mark> |
| Register Link          | Click       | Redirect to sign up page                                | <mark>PASS</mark> |
| Log in Link            | Click       | Redirect to sign in page                                | <mark>PASS</mark> |
| Log out Link           | Click       | Redirect to log out page                                | <mark>PASS</mark> |
| Chocolate Menu         | Click       | Render a dropdown menu of all links                     | <mark>PASS</mark> |
| Footer Socials         | Click       | Redirect in a new tab to all respective media platforms | <mark>PASS</mark> |
| Footer Privacy Policy Link | Click   | Redirect to Priavcy Policy page                         | <mark>PASS</mark> |
| Footer FAQ Link        | Click       | Redirect to FAQ page                                    | <mark>PASS</mark> |
| Register Link          | Display     | Render for non authenticated users                      | <mark>PASS</mark> |
| Log in Link            | Display     | Render for non authenticated users                      | <mark>PASS</mark> |
| Log out Link           | Display     | Render only if user is authenticated                    | <mark>PASS</mark> |

### Home Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Shop Now button    | Click       | Redirect to All Gesmtones page           | <mark>PASS</mark> |
| Subscribe button   | Click       | Submit request for newsletter subscription | <mark>PASS</mark> |
| Subscribe form     | Enter email | Sign up for newsletter                   | <mark>PASS</mark> |

### All Gemstones Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Category Badges    | Click       | Sorts through categories leaving selected one | <mark>PASS</mark> |
| Pagination         | Click       | Redirects to the appropriate page        | <mark>PASS</mark> |
| Sorting            | Click       | Sorting method returns the correct results when element selected | <mark>PASS</mark> |
| Gemstones Home Link | Click      | Redirects back All Gemstones page        | <mark>PASS</mark> |
| Scroll to Top button | Click        | Scrolls page to top | <mark>PASS</mark> |

### Gemstone's Detail Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Add to Bag button  | Click       | Gemstone added to shopping bag           | <mark>PASS</mark> |
| Keep Shopping button | Click     | Redirects back All Gemstones page         | <mark>PASS</mark> |
| Wishlist heart icon | Click      | User logged in: Adds gemstone to user's wishlist | <mark>PASS</mark> |
| Wishlist heart icon | Click      | User not logged in: Redirect to login page | <mark>PASS</mark> |

### Reviews Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Review Form | Click        | Takes in neccessary review info and submits    | <mark>PASS</mark> |
| Submit button | Click       | Submit review form            | <mark>PASS</mark> |
| Delete review Link | Click        | If user logged in as admin, deletes review | <mark>PASS</mark> |
| Pagination         | Click       | Redirects to the appropriate page        | <mark>PASS</mark> |
| Scroll to Top button | Click        | Scrolls page to top | <mark>PASS</mark> |

### Contact Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Contact Form | Click        | Sends requested contact message to Bling It    | <mark>PASS</mark> |
| Contact Form | Click        | Once submitted, sends confirmation email to user | <mark>PASS</mark> |
| Submit button | Click       | Submit contact form            | <mark>PASS</mark> |

### FAQ Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Collapsable question header | Click        | Toggles open/ close answers for each question | <mark>PASS</mark> |

### Privacy Policy Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Scroll to Top button | Click        | Scrolls page to top | <mark>PASS</mark> |

### Sign Up Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Form(Valid)   | Submit         | Redirects to Verify Your E-mail Address page | <mark>PASS</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>PASS</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>PASS</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>PASS</mark> |
| Login Link    | Click          | Redirect to Login Page                      | <mark>PASS</mark> |
| Sign up button | Hover/Focus   | Darken Background                           | <mark>PASS</mark> |
| Sign up button | Click         | Submits the form                            | <mark>PASS</mark> |
| Login Link    | Hover/Focus    | Darken Text                                 | <mark>PASS</mark> |

### Login Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Form(Valid)   | Submit         | Redirected to Home page                     | <mark>PASS</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>PASS</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>PASS</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>PASS</mark> |
| Register Link | Click          | Redirect to Sign Up Page                    | <mark>PASS</mark> |
| Register Link | Hover/Focus    | Darkens Text                                | <mark>PASS</mark> |
| Log in button | Hover/Focus    | Darkens Background                          | <mark>PASS</mark> |
| Log in button | Click          | Submits the form                            | <mark>PASS</mark> |

### Log Out Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Logout Button | Click          | User session is Logged out                     | <mark>PASS</mark> |
| Logout Button | Click          | Redirected to Home page                        | <mark>PASS</mark> |
| Logout Button | Hover/Focus    | Darkens Background                             | <mark>PASS</mark> |

### Shopping Bag Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Secure Checkout button | Click | Brings to CHeckout page                        | <mark>PASS</mark> |
| Keep Shopping button | Click   | Redirects back All Gemstones page              | <mark>PASS</mark> |
| Remove Link | Click            | Removes gemstone from shoppping bag            | <mark>PASS</mark> |

### Checkout Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Checkout Form | Fill out the form and click Complete Order button | Securely comppletes Order using Stripe | <mark>PASS</mark> |
| Adjust Bag button | Click          | Redirected to Home page                        | <mark>PASS</mark> |
| Adjust Bag button | Hover/Focus  | Lightens Background                       | <mark>PASS</mark> |
| Complete Order button | Hover/Focus    | Darkens Background                              | <mark>PASS</mark> |
| Complete Order button | Click    | Securely completes order and brings to success page | <mark>PASS</mark> |

### Profile Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Delivery Info Form | Change details | Details updated | <mark>PASS</mark> |
| Orders Tab | Hover | Opens wishlist | <mark>PASS</mark> |
| Delivery Info Tab | Hover | Opens wishlist | <mark>PASS</mark> |
| Wishlist Tab | Hover | Opens wishlist | <mark>PASS</mark> |
| Remove Link | Click | Removes gemstone from shoppping bag and redirects to gemstone detail page | <mark>PASS</mark> |

### Add Gemstone Page for Admin

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Add Gemstone Form | Fill in form, add image and click on Add Product button | Adds new gemstone to shop with image | <mark>PASS</mark> |
| Add Gemstone Form | Fill in form, don't image and click on Add Product button | Adds new gemstone to shop with image placeholder | <mark>PASS</mark> |
| Cancel button | Click | Cancels gemstone addition | <mark>PASS</mark> |
| Add Gemstone button | Click | Submits add gemstone form | <mark>PASS</mark> |
| Select Image button | Click | Opens window to choose image | <mark>PASS</mark> |

### Edit Gemstone Page for Admin

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Edit Gemstone Form | Fill in form, change details and click on Edit Product button | Edits gemstone | <mark>PASS</mark> |
| Cancel button | Click | Cancels gemstone addition | <mark>PASS</mark> |
| Edit Gemstone button | Click | Submits edit gemstone form | <mark>PASS</mark> |

## **Responsiveness**

Responsiveness was achieved using Bootstrap and custom CSS and tested with Chrome DevTools making sure all pages adjust to screens starting from 320px wide.

## **Bugs & Fixes**

| Bug                                          | Cause                        | Solution                                                                              |
| -------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------- |
| <details><summary>Non Nullable Field</summary><img src="static/bugs/non_nullable_field.png"></details>| Forgot to add default value to new field when modifying Gemstone model | Adding <code>default=''</code> to clarity field fixed the issue |
| <details><summary>Transparent Toast</summary><img src="static/bugs/transparent-toast.png"></details>| No background color set | Added bg-white class |
| <details><summary>Footer Not Fixed</summary><img src="static/bugs/footer-not-fixed.png"></details>| 'fixed-bottom' class | Added 'sticky-bottom' class to footer and moved it outside wrapper |
| No error message displayed when user tries to add the same gemstone to shoppping bag | No message added to 'add_to_bag' view | Adjusting view with <code>messages.error(request, 'This gemstone is already in your shopping bag.')</code> |
| <details><summary>Decimal error</summary><img src="static/bugs/decimal-error.png"></details>| Model OrderLineItem field <code>lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)</code> max digits were set as 6, causing error as gemstone price was 20000.00 | Increasing max digits to 10 resolved the issue |
| <details><summary>Subscribtion Error</summary><img src="static/bugs/subscribtion-error.png"></details>| Email verification for subscribtion letters | Newer version of Django installed and runtime.txt added to root |
| <details><summary>Test Error</summary><img src="static/bugs/test-error.png"></details>| Still connected to postgres | Commented out postgres in settings to use sqlite |
| <details><summary>Order not going through</summary><img src="static/bugs/test-error.png"></details>| Incorrect url in checkout | Removed 'checkout' from url <code>path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),</code> |
| <details><summary>Order not going through</summary><img src="static/bugs/webhook-fail.png"></details>| Typo in webhooks.py | Replaced failed with succeeded 'checkout' from url <code>'payment_intent.succeeded': (
            handler.handle_payment_intent_succeeded
        ),</code> |

[Back to Readme](README.md)