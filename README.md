# The Poster Shop e-commerce store

Welcome to the Shop Store, a Django-based e-commerce website specialized in selling vintage and retro posters online. With an extensive collection of nostalgic artworks, our platform aims to bring the charm of the past to your modern living space. 

![Screenshot of how the app looks on different screen sizes](docs/images/responsive-screens.jpg)

The live version of this app is located [here](https://poster-shop-4968517d882f.herokuapp.com). 

## Table Of Contents:
1. [Design](#design)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Database Diagram](#database-diagram)
    * [Features](#features)
    * [Future Features](#future-features)
    * [Technologies Used](#technologies-used)
    * [Testing](#testing)
    * [Deployment](#deployment)



# User Stories

User stories are a great way to define the functionality and features of a ecommerce site from the perspective of the end users. Here are some user stories for the e-commerce site Poster Shop:

## Site User


- As a site user, I would like to view a list of available posters so that I can select one or more to purchase.

- As a site user, I would like to click on an individual poster so that I can see its image in full, title, price, category, year, description, and artist. 

- As a site user, I would like to search for a poster using different search criterea such as title or artist name as well as other parametrs so that I can easily find the poster I want to purchase.

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

Wireframes provide a visual representation of the site's layout and structure, making it easier to conceptualize and understand the overall design and functionality. 

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


## Features


Vintage & Retro Collection: Browse through a curated selection of vintage and retro posters from various eras.
User Authentication: Register an account or log in securely to manage your orders and preferences.
Shopping Cart: Add posters to your cart for easy checkout.
Secure Checkout: Process payments securely using integrated payment gateways.
Order Management: View and manage your orders through the user dashboard.
Admin Panel: Admins can manage products, orders, and users through an intuitive admin interface.
Search & Filter: Easily find posters by searching or filtering based on categories, eras, artists, and more.
Responsive Design: Enjoy a seamless browsing experience across devices with our responsive design.

- Site Navagation 
  - The site havigation is added in the header of the site and consists of three sections - the main menu bar centered horizontally, the members area, and search bar. The search field is placed in the center of page just above the main menu bar. The members area is placed in the top right corner of the page for optimizing visibility, accessibility, and user experience, contributing to a smoother and more intuitive browsing experience for users.

  - The site logo was placed on the top left side of the navigation bar which optimizes brand recognition, navigation flow, consistency, and space efficiency, contributing to a positive user experience and reinforcing the website's identity. The Logo image is linked to the home page, clicking on it will bring the user back to the home page from any other page.

  - The site basket is located in the top right corner of the navigation bar. Placing the site basket in the top right corner of the navigation bar maximizes visibility, accessibility, and usability, while also maintaining consistency with established navigation patterns and user expectations.

  - When viewed on smaller screens, the navigation bar transforms into a compact hamburger menu, represented by a simple icon consisting of three horizontal lines. Clicking on this icon reveals a dropdown menu with all navigation options, providing users with a streamlined and mobile-friendly navigation experience.

  - On smaller screens the search is collapced into a search icon clicking on which reveals full search bar in the dropdown.

  - Links in the navigation menu have visual cues, with the hover over color change. On About us and Contact pages different color or the menue item indicates current page location.

 - Navigation links include filtering by different parametres such as By Price, By Category, and All Posters. 

   ![Main site navigation bar](docs/images/navigation-bar.png)




- Home page

   - The Home page is the main entry page to the site. It intuitively shows the site visiton what the site is about via the page background and the jumbotron containing very short intro and the click to action button.  
