
### Code Validation

This section displays code validations for this project. 

### HTML
For the HTML code validation it was used the [HTML W3C Validator](https://validator.w3.org) to validate HTML files.

| Page | W3C URL |  Screenshot | Notes |
| --- | --- | --- | --- |
| Index/Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2F) | ![screenshot](docs/images/index-page-html-validation.png) |   |
| Posters page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fposters%2F) | ![screenshot](docs/images/posters-page-html-validation.png) |    |
| Poster detail page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fposters%2F2%2F) | ![screenshot](docs/images/poster-detail-page-html-validation.png) |    |
| Shopping bag page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fbag%2F) | ![screenshot](docs/images/bag-page-html-validation.png) |    |
| Sign up page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](docs/images/signup-page-html-validation.png) |    |
| Login page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](docs/images/login-page-html-validation.png) |    |
| Profile page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fprofile%2FF) | ![screenshot](docs/images/profile-page-html-validation.png) |  No error or warning, just notification about trailing slash on void elements has no effect.  |
| Add poster page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fposters%2Fadd%2F) | ![screenshot](docs/images/profile-page-html-validation.png) |  No error or warning, just notification about trailing slash on void elements has no effect.  |
| Checkout page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fcheckout%2F) | ![screenshot](docs/images/checkout-page-html-validation.png) |    |
| Checkout success page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fcheckout%2Fcheckout_success) | ![screenshot](docs/images/checkout-success-page-html-validation.png) |    |
| Contact page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fcontact%2F) | ![screenshot](docs/images/contact-page-html-validation.png) |    |
| Newsletter subscribe page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fnewsletters%2F) | ![screenshot](docs/images/newsletter-page.png) |    |
| About page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fabout%2F) | ![screenshot](docs/images/about-page-html-validation.png) |    |
| Order history page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fprofile%2Forder_history%2F282FCCEC776149C5833165520A5B09E5) | ![screenshot](docs/images/order-history-page-html-validation.png |    |
| Order history page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fposter-shop-4968517d882f.herokuapp.com%2Fabout%2F) | ![screenshot](docs/images/about-page-html-validation.png) |    |



### CSS

The [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate CSS files for this project.

| Page | Jigsaw URL |  Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [URL](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fposter-shop.s3.amazonaws.com%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](docs/images/base-css.png) | Six warning related to a vendor extension and same color for background and border |
| checkout.css | [URL](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fposter-shop.s3.amazonaws.com%2Fstatic%2Fcheckout%2Fcss%2Fcheckout.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](docs/images/checkout-css.png) |    |


### JavaScript

The [JShint Validator ](https://jshint.com/) was used to validate JS files for this project.

| Page | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js  | ![screenshot](docs/images/stripe_elements_js.png) | Warning about undefined Stripe variable |
| countryfield.js  | ![screenshot](docs/images/countryfield-js.png) | No issues |
| Update quantity in a bag script  | ![screenshot](docs/images/update-quantity-script.png) | No issues |
| Quantity input script  | ![screenshot](docs/images/quantity_input-script.png) | No issues |
| Add/edit poster js  | ![screenshot](docs/images/add-poster-js.png) | No issues |
| Poster sort js  | ![screenshot](docs/images/posters-sort-js.png) | No issues |


### Python

Python files were validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/).

| Page | Screenshot | Notes |
| --- | --- | --- |
| setting.py  | ![screenshot](docs/images/setting-py.png) | Were getting E501 line too long errors. I had to add # noqa where lines of code could not be broken. |
| Products admin.py  | ![screenshot](docs/images/products-admin-py.png) | All clear |
| Products forms.py  | ![screenshot](docs/images/products-form-py.png) | All clear |
| Products models.py  | ![screenshot](docs/images/products-models-py.png) | All clear |
| Products urls.py  | ![screenshot](docs/images/products-urls-py.png) | All clear |
| Products views.py  | ![screenshot](docs/images/products-views-py.png) | All clear |
| Products widgets.py  | ![screenshot](docs/images/products-widget-py.png) | All clear |

| Bag context.py  | ![screenshot](docs/images/bag-context-py.png) | All clear |
| Bag urls.py  | ![screenshot](docs/images/bag-urls-py.png) | All clear |
| Bag views.py  | ![screenshot](docs/images/docs/images/bag-views-py.png) | One line with E501 line too long |

| Checkout admin.py  | ![screenshot](docs/images/checkout-admin-py.png) | All clear |
| Checkout forms.py  | ![screenshot](docs/images/checkout-forms-py.png) | All clear |
| Checkout models.py  | ![screenshot](docs/images/checkout-models-py.png) | All clear |
| Checkout signals.py  | ![screenshot](docs/images/checkout-signals-py.png) | All clear |
| Checkout urls.py  | ![screenshot](docs/images/checkout-urls-py.png) | All clear |
| Checkout views.py  | ![screenshot](docs/images/checkout-views-py.png) | One line with E501 line too long |
| Checkout webhooks.py  | ![screenshot](docs/images/checkout-webhooks-py.png) | All clear |

| Checkout forms.py  | ![screenshot](docs/images/homeapp-forms-py.png) | All clear |
| Checkout models.py  | ![screenshot](docs/images/homeapp-models-py.png) | All clear |
| Checkout urls.py  | ![screenshot](docs/images/homeapp-urls-py.png) | All clear |
| Checkout views.py  | ![screenshot](docs/images/homeapp-views-py.png) | All clear |

| Profiles forms.py  | ![screenshot](docs/images/profile-forms-py.png) | All clear |
| Profiles models.py  | ![screenshot](docs/images/profile-models-py.png) | All clear |
| Profiles views.py  | ![screenshot](docs/images/profile-views-py.png) | All clear |


# User Story Testing

User stories were manually tested to ensure all acceptance criteria were met. 
### As a site user

| Feature               | Test Performed                                                     | Result  | Notes    |
|-----------------------|--------------------------------------------------------------------|---------|------------
| View list of all posters | Clicking on the Shop now button redirects to all posters page   | Pass    |          |
| View poster details | Clicking on an individual I can see its image in full, title, price, category, year, description, and artist.| Pass    |
| Search for poster | Entering different search criteria into the search field returns a list of posters matching search those criteria  | Pass    |        |
| Register account | Clicking on the Register link redirects to the form. After filling out the form you redirected to the confirmation page   | Pass    |
| Confirmation email | After registering for an account, you receive a confirmation email in your inbox with the verification link.   | Pass    |        |
| Login | Clicking on the login link redirects to the login form, after login you get a success notification | Pass    |
| Logout | Clicking on the logout link redirects to the logout confirmation page. After clicking on Sign out you get a success message  | Pass    |
| Recover password | Clicking on the Forgot password link redirects to the recovery form. After entering email address you get the password reset link in your inbox.  | Pass    |       
| Sort posters  | Clicking on the sorting dropdown allows to sort posters by price, name, and category.   | Pass    |   |
| Change quantity  | Clicking on the quantity button changes the amount.| Pass    |   |
| Add to bag  | Clicking on the Add to bag button adds the item to the shopping bag. | Pass    |   |
| Open checkout  | Clicking on the Go to Checkout button redirects to the checkout page. | Pass    |   |
| Update items in bag | Clicking Update button allows to change amount of purchasing items. | Pass    |   |
| Delete items in bag | Clicking Delete button allows to delete the item from the shopping bag. | Pass    |   |
| Complete checkout | Clicking on the Complete checkout button open the billing and shipping form info. | Pass    |   |
| Oder confirmation notification | After completing the form and clicking Complete order, receive an order confirmation page with the order details. | Pass    |   |
| Oder confirmation email | After successfully completed purchase, an email with order details should be send to the user. | Fail    | The email is not being sent.  |
| View saved profile info | Clicking on My Profile will open the page with user's information. | Pass    |   |
| View order history | My profile page will display all previously completed orders. | Pass    |   |
| View individual order | Clicking on the old order link will open that order details.  | Pass    |   |
| Contact form | Clicking on the Contact menu item on top or in the footer will redirect to the Contact form. | Pass    |   |
| Contact success message | Upon submitting the contact form, the success message will display.  | Pass    |   |
| Subscribe to newsletters | Clicking on the Subscribe to newsletters button in the footer redirects to the newsletters form.  | Pass    |   |
| Pages links | Clicking on the links in the site menu will open the corresponding page.  | Pass    |   |

### As a site admin

| Feature               | Test Performed                                                     | Result  | Notes    |
|-----------------------|--------------------------------------------------------------------|---------|------------
| Add new poster on the site | Clicking on the Poster Management button open a form which allows to submit a new poster without login into Django admin dashboard   | Pass    |          |
| Edit poster | Clicking on the Edit button allows to edit poster details.   | Pass    |          |
| Delete poster | Clicking on the Delete button allows to delete poster from the site.   | Pass    |       |
| Delete confirmation | Clicking on the Delete button displays the delete confirmation alert. | Pass    |          |



# Automated testing

Only a limited amount of automated tests were conducted on this application, mostly on the Homeapp app. I understand that, in a real-world scenario, an extensive set of automated tests would be required. Used Django default test framework to test views, forms, and models of the Homeapp app.

- Views.py test. Used the assertEqual() method to confirm that the HTTP response returns status code 200, and uses the assertTemplateUsed() to confirm that the correct template used.

    ![screenshot](docs/images/test-views-py.png) 

- Models.py test. Used the assertTrue() and assertEqual() method to confirm that data can be added.

    ![screenshot](docs/images/test-models-py.png) 

- Forms.py test. Used the assertFalse(), assertIn(), and assertEqual() methods to validate field data.

    ![screenshot](docs/images/test-forms-py.png) 


# Lighthouse Audit

| Page | Mobile | Desktop | Notes !
| --- | --- | --- | --- |
| Home page  | ![screenshot](docs/images/home-mobile.png) | ![screenshot](docs/images/home-desktop.png)  |     |
| Posters page  | ![screenshot](docs/images/posters-page-mobile.png) | ![screenshot](docs/images/posters-page-desktop.png)  |     |
| Details page  | ![screenshot](docs/images/details-page-mobile.png) | ![screenshot](docs/images/details-page-desktop.png)  |     |
| Bag page  | ![screenshot](docs/images/bag-page-mobile.png) | ![screenshot](docs/images/bag-page-desktop.png)  |     |
| Checkout page  | ![screenshot](docs/images/checkout-page-mobile.png) | ![screenshot](docs/images/checkout-page-desktop.png)  |     |
| Contact page  | ![screenshot](docs/images/contact-page-mobile.png) | ![screenshot](docs/images/contact-page-desktop.png)  |     |
| Newsletters page  | ![screenshot](docs/images/newsletter-page-mobile.png) | ![screenshot](docs/images/newsletter-page-desktop.png)  |     |
| About page  | ![screenshot](docs/images/about-page-mobile.png) | ![screenshot](docs/images/about-page-desktop.png)  |     |
| Shipping page  | ![screenshot](docs/images/shipping-page-mobile.png) | ![screenshot](docs/images/shipping-page-desktop.png)  |     |
| Privacy page  | ![screenshot](docs/images/privacy-page-mobile.png) | ![screenshot](docs/images/privacy-page-desktop.png)  |     |
| Login page  | ![screenshot](docs/images/login-page-mobile.png) | ![screenshot](docs/images/login-page-desktop.png)  |     |
| Register page  | ![screenshot](docs/images/register-page-mobile.png) | ![screenshot](docs/images/register-page-desktop.png)  |     |


# Stripe purchase confirmatin

- Stripe developer console payment confirmation
   ![screenshot](docs/images/stripe-payment-confirmation.png)

- Order confirmation email
   ![screenshot](docs/images/email-confirmation.png)    


# Bugs

| Bug/Issue | Solution |
| --- | --- | 
| After completing the purchase, no order confirmation email was sent to the user. | It turned out that I didn't include stripe library in the webhook_handler file and this caused error 500 in the Stripe logs. I fixed this by importing stripe in this file | 
| Stripe displayed the error: null value in column "street_address2" of relation "checkout_order" violates not-null constraint  | This field accidentally was made required, but in the form this field was not required. So if this field was left empty, it would give an error in Stripe account. Due to time constrains I left this bag unfixed. | 