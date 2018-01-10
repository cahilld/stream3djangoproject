Stream 3 Django project<br/>

Issues outstanding:<br/>
1   In mobile mode page heading on index page being hidden with collapsed menu (design)
2   Payment success page (UX)

Purpose:<br/>
This is a lightweight app that allows users to login and configure their own workflow similar to a KanBan board with a focus on doing one task at a time until it is fully completed.<br/>

Needs it fulfils:<br/>
Put an end to multitasking, by using a lightweight easy to configure workflow app.<br/>

Functionality:<br/>
Login create items/tasks for projects, and organise by priority to show what needs to be done next.<br/>
A shopping cart will be used for a donation page for the public to use in non commercial environments.<br/>
Permission for commercial use of the app is to be decided.<br/>

User Interface (UI):<br/>
Register, Log In, Log Out, Create Item in an easy manner with no clutter to not waste time.<br/>
Mobile first approach, with ability to display more on larger screens.<br/>

User Experience (UX):<br/>
Each user will have the functionality brought by the implementation of the Dragula library to allow users to drag a new item/task into their WIP bin.<br/>
Minimal style design that is easy to read.<br/>

Technologies used:<br/>
Django, Bootstrap, Pencil, Dragula JS, Stripe, HTML5, CSS3, Python3, SQL Database

Deployment method:<br/>
Heroku<br/>

Testing:<br/>
Register, Log In, Log Out, Create To Do Items, Donate, Add donations to cart, Checkout with Stripe, Verify payment received in Stripe.

Accreditation:<br/>
Dragula<br/>
https://bevacqua.github.io/dragula/
<br/>
  
A lot of customisation was done to the files, but the core drag and drop functionality was used to style the front end and contribute to UX and UI.<br/>

Mockup file:<br/>
stream3mockup.png
<br/>
  
List of Django reusable app components:<br/>
* Accounts    Authentication mechanism for users to register, login, logout, and view profile.
* To Do Item  App functionality for task management, specific to the logged in user.
* Donations   Products page, where different types of donations are the products.
* Cart        Shopping cart functionality, ability to adjust quantities before committing to the checkout payment.
* Checkout    Pay for cart using Stripe to fulfil e-commerse payments.

Requirements for project:<br/>
* Multiple app Django apps for each separate reusable component
* Authentication mechanism - register, login, log out, and reset password.
* E-commerce functionality - Stripe and/or Paypal
* Validaton form allowing users to edit models
* Project needs to connect to a SQL database
* Responsive UI - Bootstrap & media queries
* Great User Experiemce UX
* Javascript Logic for enhanced frontend UX
* Backend Python/Django Packages - EG Disquis, Django Rest Framework - using the best tool for the task
* Text Exensively - Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests. 
* README.md - What the project does, Need that it fulfils, Functionality of the project, Technologies used, Deployment method, Testing and Accreditation, What was kept and How it was changed.

