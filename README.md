# E-Commerce
<p>DealBazar is an e-commerce platform offers a comprehensive suite of features catering to both users and administrators. Users can seamlessly register, log in, and log out, facilitating a streamlined shopping experience where they can browse, purchase products, and utilize additional functionalities such as order tracking and cart management. Meanwhile, for the platform owner, an array of robust tools is available, enabling the tracking of total expenses, profit margins, and inventory management.

Furthermore, the administrative control extends to the workforce, where the owner can precisely define permissions for each team member. Workers are granted specific privileges, focusing on essential tasks such as product creation, updates, deletions, and inventory monitoring. This meticulous control ensures an efficient and secure operation, aligning with the strategic decisions and preferences of the administrator.</p>

**➤ FEATURES :**
<p>1.The application ensures a secure and dependable user experience through robust user registration and login functionalities. In the event of a forgotten password, a user-friendly "Forget Password" feature is available. This feature initiates a secure email link, allowing users to effortlessly create a new password and regain access to their accounts. Additionally, for added convenience, the application offers a "Reset Password" feature, empowering users to proactively change their passwords when needed, further enhancing the overall security and control over their account credentials.</p>
<p>2. ⁠The product catalog enables the user to browse through the products and get an overview of the product that creates a rich and engaging experience for the user.</p>
<p>3. Upon selecting a product within the catalog, users will be presented with concise yet comprehensive details about the item. The dedicated product details page not only offers a closer look at the features and specifications but also provides convenient options for seamless interaction. Users can effortlessly add the product to their cart for future consideration or proceed to make a direct purchase, streamlining the shopping experience with efficiency and ease.</p>
<p>4. ⁠The Add to Cart feature equips the user a seamless and wholesome shopping experience to add the desired items in the cart and buy at once.</p>
<p>5. ⁠This application is also integrated with RazorPay to provide the users a smooth and hassle-free payment experience during transactions while placing an order.</p>
<p>6. ⁠The application incorporates an intuitive admin panel, providing administrators with comprehensive control and functionality. Within this panel, administrators can seamlessly add new products, efficiently manage and confirm orders post-payment verification, and curate the workforce by adding staff profiles. The admin has the flexibility to assign specific permissions to each staff member according to individual roles and responsibilities, thereby ensuring a tailored and efficient management system aligned with the administrator's preferences.</p>
<p>7. Upon the user's placement of an order, an efficient order management system is activated, allowing the administrator or authorized personnel to meticulously review and accept the order. The dynamic order status feature empowers the admin or authorized workers to seamlessly update the status in accordance with the order's progression. Furthermore, for enhanced customer transparency and service, the system supports integration with leading courier services through APIs, facilitating real-time order tracking capabilities from acceptance to final delivery. This sophisticated approach ensures a seamless and accountable order fulfillment process, enhancing both customer satisfaction and operational efficiency.</p>


**➤ TECH USED :**
<p>HTML, CSS, BOOTSTRAP, JAVASCRIPT, JQUERY, AJAX, DJANGO, PYTHON, MARIADB, HEIDISQL, RAZORPAY API.</p>

**➤ To run this Ecom website in your local computer follow the steps below and run the commands :**

1. Clone this git repo->

   ```git
   git clone https://github.com/NirbanPal/E-Commerce.git
   ```
2. Go to the directory->

   ```git
   cd E-Commerce
   ```
   
3. Put your django secret key in the settings.py SECRET_KEY section.

4. After creating an account in Razorpay. Generate a razorpay key and secretid(Here we are using the razorpay api for tesing purpose. You also can use paid api). Use that key and secret id in the settings.py and checkout.html(under templete folder) file as mentiond. Go through the documentation of razor pay for better understanding.     
   
5. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
6. To activate your virtual environment(windows)->

   ```python
   <your_virtual_environment_name>\Scripts\activate
   ```
   
7. Install dependencies(requirements.py file)->
   
   ```python
   pip install -r requirements.txt
   ```
   
8. Create a database and Configure your database here->
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE':'yourenginename',
            'NAME':'nameOfYourDB',
            'USER':'username',
            'PASSWORD':'password',
            'HOST':'localhost',
            'PORT': <portNumber>,
        }
    }
    ```

9. Migrate your database->

   ```python
   python manage.py makemigrations
   ```

   ```python
   python manage.py migrate
   ```

10. To access the admin panel you have to create an account as superuser by giving a username and password->
    
    ```python
    py manage.py createsuperuser
    ```

11. To run the application in your local machine->
   
    ```python
    python manage.py runserver
    ```
12. As an administrator, access to the admin portal can be attained by navigating to the designated URL, typically located at "http://127.0.0.1:8000/admin" Upon entering valid credentials, a secure login to the admin portal is established, affording the administrator exclusive control over product management. In instances where additional personnel operate under the administrator's purview, the admin holds the authority to designate them as staff members.
    <p>The empowerment to customize and assign permissions to each staff member aligns with the administrator's discerning requirements. This dynamic functionality enables a tailored approach, granting staff members specific privileges in product-related tasks. The ability to fine-tune and customize permissions ensures a nuanced delegation of responsibilities within the administrative ecosystem, fostering optimal efficiency and operational control.</p>

**➤ Click this for the demo of this website/project (Youtube link) : <span><a href="https://youtu.be/AgzthfV_qsI">Click Here</span>**
     
**➤ Glimpses of DesiBazar Ecom Website :**
<p>⦿ Home page for user(Not logged in)</p>
<img src="https://i.ibb.co/bgcD8mz/screencapture-127-0-0-1-8000-2023-12-14-00-10-37-1.png" alt="screencapture-127-0-0-1-8000-2023-12-14-00-10-37-1" border="0">
<p>⦿ Home page for authorized user</p>
<img src="https://i.ibb.co/kMvnf4C/screencapture-127-0-0-1-8000-2023-12-13-22-36-32.png" alt="screencapture-127-0-0-1-8000-2023-12-13-22-36-32" border="0">
<p>⦿ Product details page</p>
<img src="https://i.ibb.co/SQpN6sR/screencapture-127-0-0-1-8000-product-detail-16-2023-12-13-22-37-54.png" alt="screencapture-127-0-0-1-8000-product-detail-16-2023-12-13-22-37-54" border="0">
<img src="https://i.ibb.co/nwgp5m8/screencapture-127-0-0-1-8000-product-detail-11-2023-12-13-22-37-19.png" alt="screencapture-127-0-0-1-8000-product-detail-11-2023-12-13-22-37-19" border="0">
<p>⦿ User registration page</p>
<img src="https://i.ibb.co/k23S4rS/screencapture-127-0-0-1-8000-registration-2023-12-13-23-14-56.png" alt="screencapture-127-0-0-1-8000-registration-2023-12-13-23-14-56" border="0">
<p>⦿ User login page</p>
<img src="https://i.ibb.co/VLgtwfb/screencapture-127-0-0-1-8000-accounts-login-2023-12-13-23-14-13.png" alt="screencapture-127-0-0-1-8000-accounts-login-2023-12-13-23-14-13" border="0">
<p>⦿ Change password page</p>
<a href="https://ibb.co/100KQyX"><img src="https://i.ibb.co/nwwfmd1/screencapture-127-0-0-1-8000-passwordchange-2023-12-14-02-07-38.png" alt="screencapture-127-0-0-1-8000-passwordchange-2023-12-14-02-07-38" border="0"></a>
<p>⦿ Forgot/Reset password page</p>
<img src="https://i.ibb.co/6Xn0qqM/screencapture-127-0-0-1-8000-password-reset-2023-12-13-23-14-32.png" alt="screencapture-127-0-0-1-8000-password-reset-2023-12-13-23-14-32" border="0">
<p>⦿ Profile page</p>
<img src="https://i.ibb.co/v1t0kCR/screencapture-127-0-0-1-8000-profile-2023-12-13-23-13-34.png" alt="screencapture-127-0-0-1-8000-profile-2023-12-13-23-13-34" border="0">
<img src="https://i.ibb.co/nPt2QWZ/screencapture-127-0-0-1-8000-profile-2023-12-13-23-12-38.png" alt="screencapture-127-0-0-1-8000-profile-2023-12-13-23-12-38" border="0">
<p>⦿ Address page</p>
<img src="https://i.ibb.co/4mk0wkB/screencapture-127-0-0-1-8000-address-2023-12-13-23-13-18.png" alt="screencapture-127-0-0-1-8000-address-2023-12-13-23-13-18" border="0">
<p>⦿ Cart page</p>
<img src="https://i.ibb.co/gFdprJs/screencapture-127-0-0-1-8000-cart-2023-12-14-02-55-55.png" alt="screencapture-127-0-0-1-8000-cart-2023-12-14-02-55-55" border="0">
<p>⦿ Cart page(Empty card)</p>
<img src="https://i.ibb.co/c1HyvLg/screencapture-127-0-0-1-8000-cart-2023-12-13-23-42-32.png" alt="screencapture-127-0-0-1-8000-cart-2023-12-13-23-42-32" border="0">
<p>⦿ Checkout Page</p>
<img src="https://i.ibb.co/87QC4wh/screencapture-127-0-0-1-8000-checkout-2023-12-13-23-39-03.png" alt="screencapture-127-0-0-1-8000-checkout-2023-12-13-23-39-03" border="0">
<p>⦿ Payment Gateway Page</p>
<img src="https://i.ibb.co/SJN74yL/screencapture-127-0-0-1-8000-checkout-2023-12-14-03-13-19.png" alt="screencapture-127-0-0-1-8000-checkout-2023-12-14-03-13-19" border="0">
<p>⦿ My order page With order status</p>
<img src="https://i.ibb.co/tCDjwtm/screencapture-127-0-0-1-8000-orders-2023-12-13-23-41-55.png" alt="screencapture-127-0-0-1-8000-orders-2023-12-13-23-41-55" border="0">
<img src="https://i.ibb.co/99F6Fbh/screencapture-127-0-0-1-8000-orders-2023-12-14-03-03-14.png" alt="screencapture-127-0-0-1-8000-orders-2023-12-14-03-03-14" border="0">
<img src="https://i.ibb.co/WtnddfY/screencapture-127-0-0-1-8000-orders-2023-12-14-00-05-18.png" alt="screencapture-127-0-0-1-8000-orders-2023-12-14-00-05-18" border="0">
<img src="https://i.ibb.co/px4dvZS/screencapture-127-0-0-1-8000-orders-2023-12-14-03-03-35.png" alt="screencapture-127-0-0-1-8000-orders-2023-12-14-03-03-35" border="0">
<img src="https://i.ibb.co/jwpwDbs/screencapture-127-0-0-1-8000-orders-2023-12-14-03-02-07.png" alt="screencapture-127-0-0-1-8000-orders-2023-12-14-03-02-07" border="0">
<p>⦿ Admin Login Page</p>
<img src="https://i.ibb.co/hXtPdp5/screencapture-127-0-0-1-8000-admin-login-2023-12-14-01-45-52.png" alt="screencapture-127-0-0-1-8000-admin-login-2023-12-14-01-45-52" border="0">
<p>⦿ Glimpses of Admin Page(Have many functionality)</p>
<img src="https://i.ibb.co/Jc65dSg/screencapture-127-0-0-1-8000-admin-ecomwebapp-orderplaces-2023-12-14-01-48-09.png" alt="screencapture-127-0-0-1-8000-admin-ecomwebapp-orderplaces-2023-12-14-01-48-09" border="0">


