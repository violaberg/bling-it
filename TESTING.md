# **TESTING**

## **Table of Contents**
* [**User Story Testing**]()
* [**Code Validation**]()
    + [**HTML**]()
    + [**CSS**]()
    + [**JavaScript**]()
    + [**Python**]()
* [**Browser Testing**]()
* [**Device Testing**]()
* [**Lighthouse**]()
* [**Manual Testing**]()
    + [**Navigation**]()
    + [**Home Page**]()
    + [**About Page**]()
    + [**Gallery**]()
    + [**Book a Tour**]()
    + [**Contact Us Page**]()
    + [**Sign Up Page**]()
    + [**Login Page**]()
    + [**Logout Page**]()
* [**Responsiveness**]()
* [**Bugs & Fixes**]()

## **User Story Testing**

|   USER STORY                                     |   TEST                |   RESULT      |
|--------------------------------------------------|-----------------------|---------------|
| As a user, I want to navigate through site easily|                       | <mark></mark> |

## **Code Validation**

### **HTML**

All HTML pages were validated using [W3C HTML Validator](https://validator.w3.org/).

|   PAGE                                     |  VALIDATOR SCREENSHOT                                     |   RESULT    |
|--------------------------------------------|-----------------------------------------------------------|-------------|
| Home Page                                  |<details><summary>Home Page</summary><img src=""></details>| <mark></mark> |
| About Page                                 |<details><summary>About Page</summary><img src=""></details>| <mark></mark> |
| Gallery Page                               |<details><summary>Gallery</summary><img src=""></details>| <mark></mark> |
| Book a Tour                                |<details><summary>Book a Tour</summary><img src=""></details>| <mark></mark> |
| Contact Page                               |<details><summary>Contact Page</summary><img src=""></details>| <mark></mark> |
| Sign up Page                               |<details><summary>Sign up Page</summary><img src=""></details>| <mark></mark> |
| Login Page                                 |<details><summary>Login Page</summary><img src=""></details>| <mark></mark> |
| Logout Page                                |<details><summary>Logout Page</summary><img src=""></details>| <mark></mark> |

### **CSS**

### **JavaScript**

### **Python**

| FILE    | VALIDATOR SCREENSHOT                                                                                                    | RESULT            |
| -------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Models   | <details><summary>Models</summary><img src=""></details>     | <mark></mark> |
| Views    | <details><summary>Views</summary><img src=""></details>       | <mark></mark> |
| Forms    | <details><summary>Forms</summary><img src=""></details>       | <mark></mark> |
| Urls     | <details><summary>Urls</summary><img src=""></details>      | <mark></mark> |
| Admin    | <details><summary>Admin</summary><img src=""></details>       | <mark></mark> |
| Settings | <details><summary>Settings</summary><img src=""></details> | <mark></mark> |

## **Browser Testing**

The website was tested on Google Chrome, Firefox and Microsoft Edge browsers.

## **Device Testing**

The website was tested on various devices using Chrome DevTools and real-life device, such as iPhone 12, Samsung Galaxy S23, Lenovo X1 Carbon laptop and iPad Air.

## **Lighthouse**

| Page            | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                                                                  |
| --------------- | --------- | ----------- | ------------ | - | --------------------------------------------------------------------------------------------------------------------------- |
| ***Desktop***     |             |               |                |     |
| Home            |           |            |             |  | <details><summary>Home</summary><img src=""></details> |
|                 |             |               |                |     |

<br>

| Page            | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                                                                  |
| --------------- | --------- | ----------- | ------------ | - | --------------------------------------------------------------------------------------------------------------------------- |
| ***Mobile***     |             |               |                |     |
| Home            |           |            |             |  | <details><summary>Home</summary><img src=""></details> |
|                 |             |               |                |     |

## **Manual Testing**

### **Navigation**

| Element                | Action      | Expected Result                                         | Pass/Fail         |
| ---------------------- | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                   | Click       | Redirect to Home page                                   | <mark></mark> |
| Home Link              | Click       | Redirect to Home page                                   |  |
| Register Link          | Click       | Redirect to sign up page                                |  |
| Log in Link            | Click       | Redirect to sign in page                                |  |
| Log out Link           | Click       | Redirect to log out page                                |  |
| Hamburger Menu         | Click       | Render a dropdown menu of all links                     |  |
| Footer Socials         | Click       | Redirect in a new tab to all respective media platforms |  |
| Footer Email           | Click       | Open up an email provider with developer email attached |  |
| Register Link          | Display     | Render for non authenticated users                      |  |
| Log in Link            | Display     | Render for non authenticated users                      |  |
| Log out Link           | Display     | Render only if user is authenticated                    |  |

### Home Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### About Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### Contact Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### Delete Confirmation Modal

| Element               | Action      | Expected Result                       | Pass/Fail         |
| --------------------- | ----------- | ------------------------------------- | ----------------- |
| Close Button          | Click       | Modal and opacic background disappear | <mark></mark> |
| Confirm Delete Button | Click       | Context item is delete from database  |  |
| Close Button          | Hover/Focus | Darken Background                     |  |
| Confirm Delete Button | Hover/Focus | Darken Background                     |  |

### Sign Up Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark></mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     |  |
| Form(Valid)   | Submit         | Sign up in Notification received            |  |
| Form(Invalid) | Submit         | Error Context rendered to UI                |  |
| Form(Invalid) | Submit         | Error Notification received                 |  |
| Login Link    | Click          | Redirect to Login Page                      |  |
| Form Button   | Hover/Focus    | Darken Background                           |  |
| Login Link    | Hover/Focus    | Darken Text                                 |  |

### Login Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark></mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     |  |
| Form(Valid)   | Submit         | Sign up in Notification received            |  |
| Form(Invalid) | Submit         | Error Context rendered to UI                |  |
| Form(Invalid) | Submit         | Error Notification received                 |  |
| Register Link | Click          | Redirect to Sign Up Page                    |  |
| Form Button   | Hover/Focus    | Darken Background                           |  |
| Register Link | Hover/Focus    | Darken Text                                 |  |

### Log Out Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Page          | Authentication | Un-authenticated users redirected to Home page | <mark></mark> |
| Logout Button | Click          | User session is Logged out                     |  |
| Logout Button | Click          | Redirected to Home page                        |  |
| Form Button   | Hover/Focus    | Darken Background                              |  |

## **Responsiveness**

Responsiveness was achieved using Bootstrap and custom CSS and tested with Chrome DevTools making sure all pages adjust to screens starting from 280px wide.

## **Bugs & Fixes**

| Bug                                          | Cause                        | Solution                                                                              |
| -------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------- |

[Back to Readme](README.md)