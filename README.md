# **Bling It**

## **Overview**

Bling It is a fictional user-friendly gemstone shop, designed and developed using Django, Python, HTML, CSS and Javascript, born from my personal love for diamonds and rubies.<br>
It offers a chance to explore a curated collection of exquisite gemstones and discover diamonds, rubies, sapphires, emeralds, and more, meticulously categorized for easy browsing. Each gemstone page has an image, detailed specifications and pricing, as well as option to add gemstone to wishlist. Search can be customized by type, cut, color, and clarity to find the perfect piece. Added is a secure checkout process to ensure a safe and smooth transaction. 
<img scr><br>

Deployed project can be found here: [Bling It](https://bling-it-242ac659e1b6.herokuapp.com/)

## **Table of Contents**
* [**Overview**](#overview)
* [**User experience**](#user-experience-ux)
    + [**Strategy plane**](#strategy-plane)
        - [**Site goals**](#site-goals)
        - [**Opportunities**](#opportunities)
    + [**Scope plane**](#scope-plane)
    + [**Structure plane**](#structure-plane)
        - [**Developer Tasks & User Stories**](#developer-tasks--user-stories)
    + [**Skeleton plane**](#skeleton-plane)
        - [**Wireframes**](#wireframes)
            - [**Desktop wireframes**](#desktop-wireframes)
            - [**Mobile wireframes**](#mobile-wireframes)
        - [**Database schema**](#database-schema)
        - [**Stock keeping units**](#stock-keeping-units)
    + [**Surface plane**](#surface-plane)
        - [**Color Scheme**](#color-scheme)
        - [**Background pattern**](#background-pattern)
        - [**Typography**](#typography)
* [**Agile Development**](#agile-development)
* [**Business Model, SEO & Marketing**](#business-model-seo--marketing)
    - [**Business Model**](#business-model)
    - [**SEO**](#seo)
    - [**Marketing**](#marketing)
* [**Features & Future Development**](#features--future-development)
    - [**Features**](#features)
    - [**Future Development**](#future-development)
* [**Technologies used**](#technologies-used)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Acknowledgement & Credits**](#acknowledgement--credits)
* [**Media**](#media)
    - [**Images**](#images)

# **User experience (UX)**

During the planning phase I revisited UX videos provided on the course and used 5 planes to create my design. Due to type of e-commerce app I was planning and natural gemstones always being exclusive items with no two being the same, there won't be an option to increment amount of gemstones in a bag and I decided not to have reviews and ratings for individual gemstones bought as they would be automatically removed from shop after being sold, but instead give user an option to leave a review/ rating for Bling It as a business and their experience as customer, allowing to mention gemstones purchased if wished. As gemstones can be very expensive, not disclosing what each user has bought specifically ensures for additional safety.

## **Strategy plane**

### **Site goals**

Site goal is to give any gem lover/ collector a chance to jump into extraordinary journey of purchasing gemstones from comfort of their own home.

* Offer a fully responsive user-friendly site to browse through.
* Implement fully functional features.
* Aim to curate a diverse and exceptional collection of gemstones.
* Provide detailed information about each gemstone.
* Create a user-friendly interface with intuitive navigation and robust search capabilities.
* Create a responsive design for seamless browsing across devices.
* Implement a secure checkout process.
* Implement a wishlist feature.
* Offer ability to leave a review and read other user reviews.
* Implement SEO best practices to improve visibility in search engines and leverage digital marketing strategies.

### **Opportunities**

Opportunity | Importance | Viability/Feasibility
---|---|---
Newsletter list | 3 | 5
User register/login | 5 | 5
User profile | 5 | 5
User reviews | 3 | 4
User messages for actions taken | 5 | 5
Full CRUD funcionality for user | 5 | 5
Full CRUD funcionality for admin | 5 | 5
Admin login | 5 | 5
Product filters/searching | 5 | 5
Password recovery | 5 | 5
Order confirmation on site | 5 | 5
Order confirmation by email | 5 | 5
Option to safely pay for order with Stripe | 5 | 5
Delivery information | 4 | 4
Order history in profile | 3 | 3
Special offers | 5 | 5
About page | 5 | 5
Contact form | 5 | 5
Social media links | 3 | 5
Wishlist | 3 | 3
SEO implementation | 5 | 5
Privacy Policy | 3 | 3
FAQ | 2 | 2
Gemstone blog | 1 | 1
---|---|---
Total |100|105

## **Scope plane**

Due to a incredible amount of new knowledge and deadline for this project as for anything in life and to avoid scope creep, I used MoSCoW method to keep project on track and concentrate on delivering fully functional site. Unfortunately, since beginning of the project I knew I won't have time to implement everything I would like so decided to leave some features for future development. During development some features might be added/ discarded and some design changes are possible.

* Must Have:
    + Admin login
    + User register
    + User login/logout
    + Purchase total
    + Product list
    + Individual product page
    + Order confirmation
    + Personal and payment information safety
    + Payment information
    + View items in bag
    + Add a product
    + Edit/update a product
    + Delete a product
    + Contact details

* Should Have:
    + Personalized profile
    + Adjust bag items
    + Specials
    + Sorting list
    + Product search
    + Search results
    + Order confirmation by email
    + Contact form
    + Privacy Policy

* Could Have:
    + Sorting multiples
    + Gemstone type
    + Wishlist
    + Rating
    + Leave a review
    + Edit/update review
    + Delete a review
    + Email confirmation after registration
    + Password recovery
    + Subscription
    + FAQ

* Won't Have:
    + Bling It blog

## **Structure plane**

### **Developer Tasks & User Stories**

|   EPIC                    |ID|    Task        |
|:--------------------------|--|:---------------|
|PLANNING                   |  ||
|                           |  | As a developer I can create a flowchart so that I can clearly see the logic of the site|
|                           |  | As a developer I can create ERD so that I can clearly see my project's schema|
|                           |  | As a developer I can create wireframes so that I can clearly see the planned site layout|
|                           |  | As a developer I can choose color palette and style of the site so that I can have a clear vision of end result|
|                           |  | As a developer I can choose fonts so that I can create a sophisticated site|
|SET UP & DEPLOYMENT        |  ||
|                           |  | As a developer, I can create a new Github repository to store my project files online|
|                           |  | As a developer, I can create a new workspace on Gitpod, install Django and postgress database|
|                           |  | As a developer, I can create a Heroku app and deploy project early to confirm funcionality|
|                           |  ||

<br>

|   EPIC                    |ID|    User Story  |
|:--------------------------|--|:---------------|
|VIEWING AND NAVIGATING     |  ||
|                           |  | As a user I can view a list of products so that I can select some to purchase if I like|
|                           |  | As a user I can individual product detail page so that I can identify price, description, product rating, product image and available size/ weight|
|                           |  | As a user I can quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase|
|                           |  | As a user I can add items I like to my wishlist so that I can find them easily if I decide to purchase later|
|                           |  | As a user I can easily view the total of my purchase at any time so that I can avoid spending too much|
|REGISTRATION & USER ACCOUNTS  |  ||
|                           |  | As a user I can register on site so that I can save my personal information and wishlist|
|                           |  | As a user I can login/ logout so that I can access my personal account information|
|                           |  | As a user I can easily recover my password in case I forget it so that I can recover access to my account|
|                           |  | As a user I can have a personalized user profile so that I can view my personal order history and order confirmation, and save my payment information|
|                           |  | As a user I can receive an email confirmation after registration so that I can verify that my account registration has been successful|
|ADMIN & STORE MANAGEMENT   |  ||
|                           |  | As an admin I can easily login so that I can update site when needed|
|                           |  | As an admin I can add a product so that I can add new items to store|
|                           |  | As an admin I can edit/ update a product so that I can change product prices, descriptions, images and other product criteria|
|                           |  | As an admin I can delete a product so that I can remove items that are no longer for sale|
|SORTING & SEARCHING        |  ||
|                           |  | As a user I can search for a product by name or a description so that I can find a specific product I'd like to purchase|
|                           |  | As a user I can easily see what I've searched for and the number of results so that I can quickly see whether the product I want is available and decide if I want to purchase it|
|                           |  | As a user I can sort the list of available products so that I can easily identify the best priced products|
|                           |  | As a user I can sort multiple gemstones simultaneously so that I can search through several gemstones I like at the same time to choose the best option|
|PURCHASING & CHECKOUT      |  ||
|                           |  | As a user I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive|
|                           |  | As a user I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout|
|                           |  | As a user I can easily enter my payment information so that I can check out quickly and with no hassle|
|                           |  | As a user I can feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase|
|                           |  | As a user I can view an order confirmation after checkout so that I can verify that I haven't made any mistakes|
|                           |  | As a user I can receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records|
|REVIEWS & RATINGS                   |  ||
|                           |  | As a user I can leave a rating for the site so that I can let others know of my experience with shop|
|                           |  | As a user I can leave a review so that I can contribute to the community and help others to make informed decisions|
|                           |  | As a user I can edit/ update my review so that I can update and refine my contributions, ensuring accuracy and relevance|
|                           |  | As a user I can delete my review so that I can have control over the content associated with myself|
|CONTACT                    |  ||
|                           |  | As a user I can easily locate contact details so that I can contact shop if I need|
|                           |  | As a user I can contact someone at Bling It so that I can receive any additional information needed|
|                           |  | As a user I can subscribe to newsletters so that I can receive the latest news, special offers and sales notifications|
|FAQ & PRIVACY POLICY       |  ||
|                           |  | As an admin I can create/edit a list of FAQ so that I can offer users instant answers to their questions|
|                           |  | As a user I can read through FAQ so that I can find answers to my questions without contacting shop|
|                           |  | As a user I can read Privacy Policy so that I can see how my personal information, data will be used and what rights I have|

## **Skeleton plane**

### **Wireframes**

Wireframes for both desktop and mobile were created with [Balsamiq](https://balsamiq.com/) and can be seen below:

#### **Desktop wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/Home_desktop.png"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/About_desktop.png"></details>

<details><summary>All Gemstones Page</summary><img src="static/docs/wireframes/All_Gemstones_desktop.png"></details>

<details><summary>Gemstone Page</summary><img src="static/docs/wireframes/Gem_Page_desktop.png"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/Contact_Us_desktop.png"></details>

<details><summary>Contact Confirmation Page</summary><img src="static/docs/wireframes/Thank_You_Page_desktop.png"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Logout Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Register Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>FAQ Page</summary><img src="static/docs/wireframes/FAQ_desktop.png"></details>

<details><summary>Privacy Policy Page</summary><img src="static/docs/wireframes/Privacy_Policy_desktop.png"></details>

<details><summary>Wishlist</summary><img src="static/docs/wireframes/"></details>

#### **Mobile wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/Home_mobile.png"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/About_mobile.png"></details>

<details><summary>All Gemstones Page</summary><img src="static/docs/wireframes/All_Gemstones_mobile.png"></details>

<details><summary>Gemstone Page</summary><img src="static/docs/wireframes/Gem_Page_mobile.png"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/Contact_Us_mobile.png"></details>

<details><summary>Contact Confirmation Page</summary><img src="static/docs/wireframes/Thank_You_Page_mobile.png"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Logout Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>Register Page</summary><img src="static/docs/wireframes/"></details>

<details><summary>FAQ Page</summary><img src="static/docs/wireframes/FAQ_mobile.png"></details>

<details><summary>Privacy Policy Page</summary><img src="static/docs/wireframes/Privacy_Policy_mobile.png"></details>

<details><summary>Wishlist</summary><img src="static/docs/wireframes/"></details>

### **Database schema**

I created database schema to design the structure and organization of a database to efficiently store, manage, and retrieve data. This was crucial part when creating models and try and escape unneccesary migration complications.

![Database schema](static/docs/database.png)

### **Stock keeping units**

As I didn't use dataset but entered all gemstones manually through admin panel, I created a system to generate SKU numbers consistently as to resemble real-life scenario. In table bellow I've enter one gemstone as example of system I followed. This specific gemstone belongs to category 'Diamonds', originated in South Africa, is 3 carats in weight, flawless in clarity and as I entered it as second item, stock ID is 0002. Altogether it creates SKU - DSA3FL0002. I did some research before and know there are SKU generators but decided to go ahead with my own as to better memorize how SKU is created.

| Category | Origin | Carats | Clarity | Stock ID | SKU number |
| -------- | ------ | ------ | ------- | -------- | ---------- |
| Diamonds | SA | 3 | FL | 0002 | DSA3FL0002 |

## **Surface plane**

### **Color Scheme**

For this project I chose 3 colors - White `#ffffff`, Goldenrod `#daa520` and Midnight Blue `#020c1b`. This color palette combines the purity of white with the warmth of goldenrod and the depth of midnight blue, creating a harmonious balance of sophistication and elegance. The colors work together to highlight the beauty of gemstones and create a luxurious, visually engaging and immersive experience for users.
* `#ffffff` - White represents purity and elegance. It serves as a clean and neutral backdrop, allowing other design elements to stand out vividly.<br>
* `#daa520` - Goldenrod is a warm and luxurious yellow-gold color, reminiscent of precious metals and sun-kissed hues. It adds a touch of sophistication and vibrancy.<br>
* `#020c1b` - Midnight Blue is a deep, rich shade of blue that conveys mystery, elegance, and depth. It provides a striking contrast and a sense of tranquility.<br>

![Color palette](static/docs/color/color_palette.png)

### **Background pattern**

To add more depth and interest to design but not make it overwhelming for user to look at, I created a pattern for background using two of my colors - Midnight Blue `#020c1b` and Goldenrod `#daa520`.<br>
Midnight Blue is a deep, dark shade of blue resembling the color of a moonlit night sky. It conveys a sense of mystery, depth, and tranquility, providing a striking contrast to lighter elements. As a background color it serves as a sophisticated backdrop that enhances the visual appeal of gemstones, allowing them to stand out vividly while creating a calming and immersive browsing experience.<br>
Goldenrod is a warm and rich yellow-gold color reminiscent of the golden hue of ripe wheat fields or autumn leaves. It exudes a sense of warmth, vibrancy, and luxury, making it an excellent choice for adding a touch of elegance to project. As part of background it creates a welcoming and inviting atmosphere, evoking feelings of opulence and sophistication that complement the beauty of gemstones.<br>
Combining the warm, luxurious tones of Goldenrod with the deep, serene tones of Midnight Blue, creates a visually captivating and harmonious color palette for Bling It gemstone app. This color scheme can effectively highlight the beauty and elegance of gemstone offerings while providing a pleasing backdrop for typography and design elements.

![Pattern](static/docs/color/bg-pattern.png)

### **Typography**

In planning the visual identity of my website, I meticulously selected two Google fonts, Parisienne and Cormorant Garamond.<br>
Parisienne is an elegant and flowing script font that evokes a sense of romance and sophistication. With its graceful strokes and whimsical charm, Parisienne adds a touch of luxury to brand. This font is perfect for headings, logos, and special accents, enhancing the overall visual appeal of Bling It app.<br>
Cormorant Garamond is a classic serif font known for its timeless elegance and readability. Inspired by the traditional Garamond typefaces, Cormorant Garamond features delicate serifs and balanced proportions, making it ideal for body text and longer passages. This font exudes refinement and professionalism, enhancing the overall readability and aesthetic of Bling It gemstone app.<br>
Combining Parisienne for decorative elements and headings with Cormorant Garamond for body text and details, creates a harmonious typography scheme that reflects the sophistication and style associated with gemstones. These fonts enhance the overall visual identity of my project, making it both inviting and professional.<br>

![Parisienne](static/docs/parisienne_font.png)

![Cormorant Garamond](static/docs/cormorant_garamond_font.png)

# **Agile Development**

I have included details of agile development in a separate file [AGILE.md](AGILE.md).

# **Business Model, SEO & Marketing**

## **Business Model**

Bling It operates as a B2C (Business-to-Consumer) ecommerce model, an online retail platform for individual clients specializing in high-quality gemstones. Business model revolves around offering a curated selection of exquisite, ethically-sourced gemstones, including rubies, sapphires, emeralds, and diamonds, catering to a discerning clientele seeking luxury, elegance and uniqueness. By maintaining direct relationships with reputable gemstone suppliers and artisans, shop ensures the authenticity and superior quality of the gemstones offered.<br>
The target audience include affluent individuals, collectors, and connoisseurs of gemstones, typically aged 30 and above, who seek unique and timeless pieces to complement their personal style and celebrate special occasions. We also target professional women and men who appreciate the elegance and craftsmanship of bespoke jewelry, as well as young couples looking for exquisite engagement ring and wedding band gemstones. Additionally, Bling It appeals to gift-givers who desire to present their loved ones with meaningful and luxurious gifts. Audience is geographically diverse, with a strong presence in major metropolitan areas and an appreciation for online shopping convenience and high quality service.

## **SEO**

SEO, or Search Engine Optimization, is the process of improving your website to increase its visibility when people search for products or services related to your business on search engines like Google. The better visibility your pages have in search results, the more likely you are to attract attention and draw prospective and existing customers to your business. All search in Google was done in incognito window.
For keyword research purposes I used [Keyword Surfer](https://surferseo.com/keyword-surfer-extension/) Chrome extension and checked search results directly in Google Tools. I have included a brain dump using keywords and Google to return a list of long and short-tail keywords. All screenshots can be found in [SEO](static/docs/seo) folder. Below I have added tables created so search results are better visible:

<details><summary>Search results</summary><img src="static/docs/seo/search-table.png"></details>
<details><summary>Search results</summary><img src="static/docs/seo/search-table2.png"></details>

After concluding my research I added descriptive meta tags to the project.

## **Marketing**

For marketing purposes I created custom newsletter and included it on Home page of the project. A newsletter can significantly benefit an e-commerce store by keeping customers engaged and informed about new products, promotions, and exclusive offers. It serves as a direct line of communication, fostering customer loyalty and driving repeat business. By sharing valuable content and personalized recommendations, newsletters enhance the shopping experience and keep your brand top-of-mind. Additionally, they provide insights into customer preferences and behaviors, helping to refine marketing strategies and improve overall customer satisfaction.

# **Features & Future Development**

## **Features**

* Logo created using [Vecteezy](https://www.vecteezy.com/) - original image by joko sutrisno, available at this [link](https://www.vecteezy.com/vector-art/6552384-diamond-abstract-logo)

* Favicon created using [Favicon Generator](https://www.favicongenerator.com/)

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

* [Hero Patterns](https://heropatterns.com/) used to create background pattern
* [Google Fonts](https://fonts.google.com/) used to find and implement fonts
* [Font Awesome](https://fontawesome.com/) used for icons
* Walkthrough Boutique Ado from Code Institute course used to set up my project, styled and adjusted to suit my own project.
* Choccolate menu taken from [Codepen](https://codepen.io/Kechicheb/pen/WNyZqYJ)
* Animation for loader taken from [CSS-tricks](https://css-tricks.com/making-css-animations-feel-natural/)
* Hover tabs for profile page taken from [W3schools](https://www.w3schools.com/howto/howto_js_hover_tabs.asp)
* Privacy Policy generated with [Privacy Policy Generator](https://www.privacypolicygenerator.info/)
* [Keyword Surfer](https://surferseo.com/keyword-surfer-extension/) used for some Google searches
* Search result table generated with [Table Generator](https://www.table-generator.de/)<hr>

* The biggest thank you as always to my family during this busy time of juggling the biggest project so far, hackathon and life in general.
* Thank you as well to my mentor [David Bowers](https://github.com/dnlbowers) who supported me from the very beginning always giving the best advice and ideas for solutions and more importantly never losing hope in me, even when I did.
* And thank you to [Kim](https://github.com/kimatron) for continuous support during late and long nights and in general for convincing me to take on this course.
* And last but not least, thank you to Code Institute for organising hackathons. They have been a tremendous learning opportunity and therefore a great help during my project struggles.

# **Media**

## **Images**
* [Vecteezy](https://www.vecteezy.com/) - image by joko sutrisno, available at this [link](https://www.vecteezy.com/vector-art/6552384-diamond-abstract-logo)