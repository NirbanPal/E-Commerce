# E-Commerce
This is an e-commerce website where users can Register, login, logout ,buy products and there are also many features like tracking order, view carts etc. Here Owner also can keep track of total expense, profit, inventory and everything. Workers can do only create, update, delete and see the products to the inventory.

**Tech used->**
<p>HTML, CSS, BOOTSTRAP, JAVASCRIPT, JQUERY, AJAX, DJANGO, PYTHON, MYSQL, SQL, RAZORPAY API</p>

### To run this Ecom website in your local computer follow the steps below and run the commands:

1. Clone this git repo->

  ```git
  git clone https://github.com/NirbanPal/E-Commerce.git
  ```
2. Go to the directory->

   ```git
   cd E-Commerce
   ```
   
3. Put your django secret key in the settings.py SECRET_KEY section.

5. After creating an account in Razorpay. Generate a razorpay key and secretid(Here we are using the razorpay api for tesing purpose. You also can use paid api). Use that key and secret id in the settings.py and checkout.html(under templete folder) file as mentiond. Go through the documentation of razor pay for better understanding.     
   
6. Create virtual environment->
   
   ```python
   python -m venv <your_virtual_environment_name>
   ```
7. To activate your virtual environment(windows)->

   ```python
   <your_virtual_environment_name>\Scripts\activate
   ```
   
8. Install dependencies(requirements.py file)->
   
   ```python
   pip install -r requirements.txt
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

12. To run the application in your local machine->
   
   ```python
   python manage.py runserver
   ```
