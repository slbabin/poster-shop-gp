# The Poster Shop e-commerce store

Welcome to the Shop Store, a Django-based e-commerce website specialized in selling vintage and retro posters online. With an extensive collection of nostalgic artworks, our platform aims to bring the charm of the past to your modern living space. 

![Screenshot of how the app looks on different screen sizes](docs/images/responsive-screens.jpg)

The live version of this app is located [here](https://poster-shop-4968517d882f.herokuapp.com). 

## Table Of Contents:

* [User Stories](#user-stories)
    * [Site User](#site-user)
    * [Site Admin](#site-admin)
* [Wireframes](#wireframes)
* [Features](#features)
* [Future Features](#future-features)
* [Database Diagram](#database-diagram)
* [Agile Methodology](#agile-methodology)
* [Bussniess model & Marketing](#business-model-marketing)
    * [Business Model](#business-model)
    * [Marketing Strategy](#marketing-strategy)
* [Robots](#robots)
* [Sitemap](#sitemap)
* [Testing](#testing)
* [Deployment](#deployment)
    * [ElephantSQL Database](#elephantSQL-database)
    * [Amazon AWS](#amazon-AWS)
    * [S3 Bucket](#S3-bucket)
    * [AM](#AWS)
    * [Final AWS Setup](#final-awsssetup)
    * [Heroku Deployment](#heroku-deploymentp)
* [Technologies Used](#technologies-used)
* [Credits](#credits)

<br />

# User Stories

User stories are a great way to define the functionality and features of a ecommerce site from the perspective of the end users. Here are some user stories for the e-commerce site Poster Shop:

## Site User

- As a site user, I would like to view a list of available posters so that I can select one or more to purchase.

- As a site user, I would like to click on an individual poster so that I can see its image in full, title, price, category, year, description, and artist. 

- As a site user, I would like to search for a poster using different search criteria such as title or artist name as well as other parameters so that I can easily find the poster I want to purchase.

- As a site user I would like to sort posters by price, name, and category so that I can easily find the poster that I like or need.

- As a site user I would like to add, view, update and delete poster in the shopping basket so that I can review or manage my shopping basket before proceeding to checkout.

- As a site user I would like to view the total amount of posters in my shopping basket so that I can know how many posters were added in the basket at all times.

- As a site user I would like to provide the necessary billing and delivery information so that I can purchase poster and view an order confirmation after checkout to verify all the information from my purchase is accurate.

- As a site user I would like to receive an email confirmation after the purchase so that I can keep records of my transactions.

- As a site user, I have the ability to create an account, so I can log in and log out using personalized credentials. Additionally, I can request assistance in recovering my password if I happen to forget it.

- As a site user I would like to create/manage my personal profile on the site so that I can view/update my profile, view my order history and save my billing information.

- As a site user I would like to contact the site admin in case I need have any queries.

- As a site user I would like to subscribe to the site newsletters so that I can receive news, special offers and general information related to the store.

- As a site user I would like to see information about shipping and returns in addition to general site information such as about us, terms of use, privacy policy by navigating to corresponding pages.

## Site Admin

- As a site admin, I should be able to add, view, update and delete posters so that I can manage posters on the site.

- As a site admin, I should be able to view who signed up for the site newsletters.



# Wireframes 

Wireframes provide a visual representation of the site's layout and structure, making it easier to conceptualize and understand the overall design and functionality. Wireframe mockups were created using MockFlow - online wireframing and product design tool. 

<details>
    <summary>Start Page</summary>  

![Wireframe of home page](docs/images/index-page-wireframes.png)
</details>
  
<details>
    <summary>Posters List Page</summary>  
    
![Wireframe of recipe page](docs/images/posters-page-wireframes.png)  
</details>  

<details>
    <summary>Poster Detail Page</summary>  
    
![Wireframe of recipe details page](docs/images/details-page-wireframes.png)  
</details>  

<details>
    <summary>Checkout Page</summary>  
    
![Wireframe of recipe details page](docs/images/checkout-page-wireframes.png)  
</details> 
  
<details>
    <summary>Shopping Bag Page</summary>  
    
![Wireframe of Add recipe page](docs/images/bag-page-wireframes.png)  
</details>

<details>
    <summary>About Us Page</summary>  
    
![Wireframe of Add recipe page](docs/images/about-page-wireframe.png)  
</details>

<details>
    <summary>Sign Up Page</summary>  
    
![Wireframe of Add recipe page](docs/images/signup-wireframes.png)  
</details>

<details>
    <summary>Sign In Page</summary>  
    
![Wireframe of Add recipe page](docs/images/siging-wireframes.png)  
</details>

<details>
    <summary>Newsletter Signup Page</summary>  
    
![Wireframe of Add recipe page](docs/images/siging-wireframes.png)  
</details>


# Features


- Site Navigation  
  - The site havigation is added in the header of the site and consists of three sections - the main menu bar centered horizontally, the members area, and search bar. The search field is placed in the center of page just above the main menu bar. The member area is placed in the top right corner of the page for optimizing visibility, accessibility, and user experience, contributing to a smoother and more intuitive browsing experience for users.

  - The site logo was placed on the top left side of the navigation bar which optimizes brand recognition, navigation flow, consistency, and space efficiency, contributing to a positive user experience and reinforcing the website's identity. The Logo image is linked to the home page, clicking on it will bring the user back to the home page from any other page.

  - The site basket is located in the top right corner of the navigation bar. Placing the site basket in the top right corner of the navigation bar maximizes visibility, accessibility, and usability, while also maintaining consistency with established navigation patterns and user expectations.

  - When viewed on smaller screens, the navigation bar transforms into a compact hamburger menu, represented by a simple icon consisting of three horizontal lines. Clicking on this icon reveals a dropdown menu with all navigation options, providing users with a streamlined and mobile-friendly navigation experience.

  - On smaller screens the search is collapsed into a search icon clicking on which reveals full search bar in the dropdown.

  - Links in the navigation menu have visual cues, with the hover over color change. On About us and Contact pages different color or the menu item indicates current page location.

 - Navigation links include filtering by different parameters  such as By Price, By Category, and All Posters. 

   ![Main site navigation bar](docs/images/navigation-bar.png)


- Home Page

   - The Home page is the main entry page to the site. It intuitively shows the site visitor what the site is about via the page background and the jumbotron containing short intro text and the click to action button.  

    ![Site's home page screenshot](docs/images/index-page.png)

- Posters Page

   - This page displays a list of all posters. The user can use filters and search queries to filter the list to their desired result.
        - Poster Cards - The poster cards display the posters listed on the site. The information shown on each card is the poster's image, title, price, category, and artist.
        - Responsive behavior - Poster cards will display different amount of columns depending on the viewed screen size. 
        - Sort By Selector - This selector allows the user to order the products displayed by title, price and category in both ascending and descending orders.
        - Products Home Link - There is a link to bring the user back to the 'Products Home', this will display all products rather than filtering by category or search queries.
        - Search Results/Product Counter - Right next to the link to the 'Products Home' is a counter that tells the user how many products are displayed on the page. If the user has entered a search query, the counter will advise how many products were found for that specific search query.
        - Update/Delete Links - These links are located below a poster card and appear only to the authorized user. They allow to manage posters from the front end of the site instead of logging into the admin dashboard. Clicking on the Delete button triggers the alert message asking for confirmation of the delete action. 
   
 ![Site's home page screenshot](docs/images/posters-page.png)

- Posters Detail Page

   - The poster detail page will render the information for the chosen product and allow the user to select a size and add the item to the shopping bag:

        - Poster Details - This is a dynamic page that will display the selected poster's image, title, price, category, description and artist.
        - Size Selector - The size selector can be used to select the specific size the user wants to purchase.
        - Add to Bag Button - Below the size selector there is the Add to Bag button which allows the user to add the desired product and size to their shopping basket for purchasing.       
        - Keep Shopping Button - After the user added the desired poster to the shopping basket, they have the option to continue shopping by clicking on the Keep shopping button which is located next to the Add to bag button. 
        - Update/Delete Links - The poster detail page also provided the ability to manage posters from the front end to the authorized user.

        ![Site's home page screenshot](docs/images/poster-detail-page.png)


- Shopping Bag Page

   - This page allows the user to view, edit and delete items in their shopping bag before proceeding to the checkout screen.

       - Poster Information - This feature displays the information of each poster added to the shopping bag. This includes the poster image, title, price, size, quantity. On the page, separate entries are displayed for each size of an individual poster, indicating the quantity available for each size variant of the item.
       - Update/Remove Buttons - These features allow the user to update the quantity of posters in their shopping bag, or remove it entirely. 
       - Updated Total, Shipping and Grand Total - The total cost of the shopping bag updates each time an item is added, updated or removed from the shopping bag. If the user spends more than €50.00 on items, they qualify for free shipping. Otherwise, shipping is calculated to be 10% of the user's total cost, which is then added to create the grand total.

       ![Site's home page screenshot](docs/images/shopping-bag.png)

- Checkout Page

   - The checkout page is where the user will input their delivery and payment details in order to complete the purchase.

        - Shipping Info Form - This feature allows the user to enter the shipping details they wish their items to be delivered to. These details are then displayed on the confirmation screen.
        - Order Summary - This feature allows the user to take one more look at the items in their shopping bag and the total cost before paying and submitting their order.
        - Stripe Payment Feature - This feature allows the user to securely submit their payment information to the Stripe payment system, securing the placement of their order.
        - Save delivery information - This checkbox on a checkout form is used to offer users the option to save their shipping information for future purchases or account management.
        - Loading spinner - Upon clicking "Complete Order," a friendly loading spinner will appear, signaling that the payment is undergoing processing by the backend code and the Stripe API.

      ![Site's home page screenshot](docs/images/checkout-page.png)


- Order Confirmation

    - This page shows the order details of the purchase that was just carried out.
        - Order summary - The order summary page provides a comprehensive overview of the customer's purchase. A unique order number is also provided.
        - Return To Store Button - This button brings the user back to the store where they can continue to browse posters on offer.
        
     ![Site's home page screenshot](docs/images/order-confirmation.png) 

- Profile Page 

    - The profile page shows the user their saved profile and delivery information and their order history.
        - User's Profile Heading - The heading of the profile page updates to the user's chosen username.
        - Order History Log - This feature is a list of past orders placed while logged in. There are links on each order which allows the user to go to the order history page to get a detailed view of the order placed.


    ![Site's home page screenshot](docs/images/profile-page.png)

- Poster Management Page 

    - This page allows the authenticated users with superuser privileges to manage posters from the front end of the store without login into the Django admin page. 

        - Add Poster Form - The Add poster form allows the authenticated user a new poster to the store stock.
        - Edit Poster Form - The Edit poster form allows authenticated user to editor currently listed on the store posters. To access the edit form, the user needs to click on the Edit link under the poster card. 

    ![Site's home page screenshot](docs/images/poster-management-page.png)


- Delete Poster

    - The delete poster option allows authenticated users with superuser privileges to delete an existing poster from the store. Clicking on the Delete button triggers the alert message asking to confirm the deletion. 
    
    ![Site's home page screenshot](docs/images/delete-confirmation.png)


- Form errors

   - Every form on the site displays a warning message on the incorrect input. Displaying errors on a form is essential for providing feedback to users when they input incorrect or incomplete information. 

   ![Site's home page screenshot](docs/images/form-errors.png)


- Contact us

    - The contact us page allows the user should they have any question, concern or suggestion, to contact the site's admin.

    ![Site's home page screenshot](docs/images/contact-form.png)

- Newsletter

    - The newsletter page allows the user to subscribe to the site's newsletter. Newsletters allow websites to stay connected with their audience by providing regular updates, announcements, and curated content. This engagement helps maintain interest in the site and encourages visitors to return.

    ![Site's home page screenshot](docs/images/newsletter-form.png) 


- Messages

    - Toast messages - Toast messages, also known as toast notifications, are small, transient messages that appear temporarily on a website or application to provide users with important feedback, updates, or alerts. 
    
    - Every time a user completes an action on the site such as register, login, logout, add, update, or delete a poster and other actions a relevant message will be displayed at the top of the screen to inform the user about the action being completed successfully.    

    ![Site's home page screenshot](docs/images/404-error.png)


- Back to Top Button
    
    - Adding a "back to top" button on a website enhances user experience by providing a convenient way for users to quickly navigate to the top of the page, improving accessibility, mobile usability, time efficiency, and overall navigation convenience.   

    ![Site's home page screenshot](docs/images/back-to-top-button.png)


- Footer
    
    - Each page of the site features a consistent responsive footer design. 

    - Footer was split into three columns. Including navigational links in the footer with three columns enhances website usability by organizing content effectively, providing users with easy access to important pages, improving navigation efficiency, and optimizing space utilization, thereby enhancing overall user experience.

    - Links to social media such as Facebook, Instagram, and GitHub profile.

    - The footer contains the Subscribe to Newsletters button, clicking on which opens a dedicated page with the subscribe form.

    ![Site's home page screenshot](docs/images/footer.png) 
 

# Database Diagram
    
- Database diagram for this project was created using online tool [https://dbdiagram.io](https://dbdiagram.io). A diagram provides a clear visual representation of the database structure, including tables, fields, and relationships between different models. 

    ![Site's home page screenshot](docs/images/diagram.png)


# Agile Methodology
    
    - Github Projects was used to keep track of the User Stories and progress of the project. 
    - The link to the project is located [here](https://github.com/users/slbabin/projects/6/views/1). 


# Business model & Marketing

### Business Model:

The business model for the Poster Shop website follow an e-commerce model, focusing on curating and selling a wide variety of vintage and retro posters to customers worldwide. Here's a breakdown of the key components: 
  - **Product Curation:** Curate a diverse collection of vintage and retro posters spanning various themes such as movie posters, travel posters, art deco, music, and more. Ensure high-quality images and accurate descriptions for each poster.

  - **Inventory Management:** Maintain an organized inventory system to track available posters, manage stock levels, and update listings promptly. Regularly source new posters to keep the collection fresh and appealing to customers.

  - **E-commerce Platform:** Set up a user-friendly e-commerce website where customers can easily browse, search, and purchase posters. Implement secure payment gateways to facilitate smooth transactions.

  - **Shipping and Fulfillment:** Partner with reliable shipping carriers to offer worldwide shipping options. Implement efficient fulfillment processes to ensure orders are processed promptly and posters are securely packaged for delivery.

  - **Customer Service:** Provide excellent customer service by promptly addressing inquiries, resolving issues, and ensuring customer satisfaction. Implement a returns and refunds policy to offer peace of mind to customers.


### Marketing Strategy:

To effectively market the online vintage and retro poster website and attract customers, the following marketing strategy incorporating channels have been adopted:

- **Search Engine Optimization (SEO):** Optimized the website for relevant keywords related to vintage and retro posters to improve visibility in search engine results pages (SERPs).

- **Email Marketing:** Created a newsletters subscribe form in order to build email list of customers and prospects and send out regular newsletters featuring new arrivals, special promotions, and exclusive discounts. Can personalize email content to cater to the interests of different segments of subscribers.

- **Social Media Marketing:** Utilized popular social media platforms such as Facebook to showcase posters, engage with followers, and run targeted advertising campaigns to reach potential customers. 

    ![Site's home page screenshot](docs/images/Facebook-business-page.png) 

The following marketing strategies can be implemented in the future incorporating various online and offline channels:

- **Content Marketing:** Create engaging blog posts, articles, and guides related to vintage posters, retro aesthetics, poster collecting tips, etc., to attract and engage the target audience. Share this content on social media and other platforms to drive traffic to the website.

- **Social Media Marketing:** Utilize other popular social media platforms such as Instagram, Facebook, Pinterest, and Twitter to showcase posters, engage with followers, and run targeted advertising campaigns to reach potential customers.

- **Influencer Partnerships:** Collaborate with influencers, bloggers, and content creators in the vintage, retro, and interior design niches to showcase posters, gain exposure to their audiences, and drive traffic to the website.

- **Affiliate Marketing:** Set up an affiliate program where bloggers, influencers, and other partners can earn commissions for referring customers to the website. Provide them with marketing materials and tracking tools to facilitate promotion and tracking of referrals.


By implementing a robust business model and executing a comprehensive marketing strategy, the online vintage and retro poster website can effectively attract customers, drive sales, and establish itself as a premier destination for vintage poster enthusiasts.

# Robots
The robots.txt file was included at the root-level. Including a robots.txt file in a Django project is a good practice to control web crawlers' access to certain parts of your website. The robots.txt file serves as a directive for search engine crawlers and other automated bots, indicating which pages or sections of your site should not be crawled or indexed.
    ![Site's home page screenshot](docs/images/robots-txt.png) 

# Sitemap

For this project the sitemap.xml file was generated using the online sitemap generator tool [XML Sitemaps Generator](https://www.xml-sitemaps.com/). Creating a sitemap.xml file for this project facilitates efficient search engine indexing, prioritizes and signals update frequency of URLs, improves crawl efficiency, expedites new content discovery, and aids in error identification for enhanced website visibility and search engine optimization.

# Testing

For detailed information on testing procedures, please refer to the [TESTING.md](TESTING.md) file located in the project's root directory.
This file provides comprehensive guidance on running tests, understanding test coverage, and ensuring the robustness of the Django project.

# Deployment

The live project was deployed on Heroku. Heroku is a cloud platform as a service (PaaS) that enables developers to build, deploy, manage, and scale web applications without having to worry about infrastructure management. The following steps were taken prior deploying to Heroku. 

### ElephantSQL Database

The [ElephantSQL](https://www.elephantsql.com) PostgreSQL database was used for this project. The following steps were taken in order to create a database.

  - Sign-up with your GitHub account on the ElephantSQL site.
  - Click Create New Instance to start a new database.
  - Provide a name for the database.
  - Select the Tiny Turtle (Free) plan.
  - Select the Region and Data Center closest .
  - Once created, click on the new database name, where you can get the database URL and Password.

### Amazon AWS

Due to the fact that Heroku doesn't allow persist media and static files, I used  Amazon Web Services (AWS) to store media and static files online.

After an AWS account is created, make sure you logged to the AWS Management Console page.

#### S3 Bucket
S3 bucket is a scalable storage service provided by AWS that allows users to store and retrieve data and objects, such as files and images, over the internet. 

  - Search for S3.

  - Create a new bucket.

  - Uncheck Block all public access, and acknowledge that the bucket will be public.

  - From Object Ownership, make sure to have ACLs enabled, and Bucket owner preferred selected.

  - From the Properties tab, turn on static website hosting, and type index.html and error.html in their respective fields, then click Save.

  - From the Permissions tab, add the following CORS configuration:
```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
```


 - Copy the ARN string.
 - From the Bucket Policy, select the Policy Generator link and generate a Bucket Policy.
 - Copy the entire Policy, and paste it into the Bucket Policy Editor.
 - Click Save.
 - From the Access Control List (ACL) section, click "Edit" and enable List for Everyone (public access).

#### IAM

On the AWS Services Menu, search for and open IAM (Identity and Access Management).

 - From User Groups, click Create New Group.
 - From User Groups, select your newly created group, and go to the Permissions tab.
 - Open the Add Permissions dropdown, and click Attach Policies.
 - Select the policy, then click Add Permissions at the bottom when finished.
 - From the JSON tab, select the Import Managed Policy link
 - From User Groups, click your on your newly created group.
 - Click Attach Policy.
 - Search for the policy and select it, then Attach Policy.
 - From User Groups, click Add User.
 - Select the group to add a new user.
 - Click Create User once done.
 - You should see a button to Download .csv file. This contains Access key ID and Secret access key, so it should be stored safely on a computer.

#### Final AWS Setup

- Back within S3, create a new folder called: media.
- Select project images to prepare them for being uploaded into the new folder.
- Under Manage Public Permissions, select Grant public read access to this object.
- Click Upload.

## Heroku Deployment

 - Navigate to the top-right corner of your Heroku Dashboard, click on the "New" button, and then choose "Create new app" from the dropdown menu.
- Ensure that your app name is distinct, opt for a region nearest to your location (either EU or USA), and then proceed by selecting "Create App."
- From the new app Settings, click Reveal Config Vars, and set your environment variables.

Heroku needs two additional files in order to deploy properly.

 - requirements.txt
 - Procfile

 - In the project's settings file in ALLOWED_HOSTS you need to add Heroku app URL.

 For Heroku deployment, you need to connect your own GitHub repository to the newly created app:
 - Click on the Deploy tab.
 - Choose GitHub and connect with your GitHub account.
 - Search for your project repository and connect to it. 
 - Project can be deployed manually by selecting the branch and clicking Deploy Branch.
 - Alternatively, automatic deployment can be enabled.


# Technologies used for this project

[Django](https://en.wikipedia.org/wiki/Django_web_framework) - Django is a high-level Python web framework primarily used for building this ecommerce application. It provides a robust set of tools, libraries, and patterns that facilitate rapid development, scalability, and maintainability of a web application.

[Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_front-end_framework) -  It provides a collection of pre-designed HTML, CSS, and JavaScript components and utilities that helped streamline the development process.

[GitPod](https://gitpod.io/) - Used for writing code, committing, and then pushing to GitHub.

[GitHub](https://github.com/) - Used to store the project after pushing.

[Heroku](https://heroku.com/) - Used to deploy the project online. 

[AWS](https://aws.amazon.com/) - Used to store MEDIA and STATIC files for deployed site.

[ElephantSQL](https://www.elephantsql.com) - Used as a cloud PostgreSQL database service provider. 

[https://dbdiagram.io](https://dbdiagram.io) - Was used to create a database diagram for this project.

[www.mockflow.com](www.mockflow.com) - Used to create site pages wireframes.

[Font Awesome](https://fontawesome.com/) - Used Font Awesome icons for various purposes, such as buttons and decorative elements, providing a consistent and visually appealing user experience.

[XML Sitemaps Generator](https://www.xml-sitemaps.com/) - Used to create a sitemap.xml file for this project. 

# Credits

### Code

- The code in this project incorporates elements from Code Institute tutorials on the "Boutique Ado" project, which have been tailored to fit the project's unique needs, along with custom-written code and models developed by me.

### Content

 - Content for the site was take from the following sites:
    
    - [https://mymodernmet.com](https://mymodernmet.com/download-free-posters-belle-epoque-art/)
    - [https://www.vintagemovieposters.co.uk](https://www.vintagemovieposters.co.uk)

### Media

 - Poster images were take from the following sites:

    - [https://www.internationalposter.com](https://www.internationalposter.com)
    - [https://mymodernmet.com](https://mymodernmet.com/download-free-posters-belle-epoque-art/)
    - [https://www.vintagemovieposters.co.uk](https://www.vintagemovieposters.co.uk)
