# Online store on Django

## Main dependencies.
- Python 3+
- Django framework
- Sqlite database
- all dependencies you can see in requirements.txt ...


## Build and launch the app
1. Clone the Project
2. Setup Environment  
`pip install pipenv`
3. Install dependencies  
`pip install -r requirements.txt`
4. Initialization database and execution migrations    
`python manage.py makemigrations`.  
`python manage.py migrate`
5. Upload data from fixtures.   
`python manage.py loaddata fixtures/database_data.json`.    
This command:  
	- import users, banners, products, baskets.
	- create superuser with name "manager" and password "manager".
	- create group "managers".
	
6. Run server  
`python manage.py runserver`


##### App is accessed on http://0.0.0.0:8000/

## Project structure

### Apps:

- `users` - app for user`s basket logic (user is default django).
- `goods` - app for brand\`s, product\`s, banner`s logic.  

### Folders:
- templates/ - for all templates
- static/media/pictures/ - for product`s images   

### Files:

- fixtures/database\_data.json - data for database
- information/user\_data.md - information about users(passwords)


## Database structure

![](information/db.jpg)

## User flow
- `/` main page contains:  
	-  products with links to products` pages.
	-  banners ( information about banner`s product with the ability to go to the product page )
	- for auth user:
		-  `logout/` link, that deauthorize user.
		-  `basket/` link to user`s basket.
	- for not auth user:
		- `login/` link to login page.

- `/basket` basket page contains:  
	- user purchase with links to products` pages.
	- quantity of purchase.
	- ability to delete purchase from basket.
	- link to main page.
	
- `/product/<product_id>` product page contains:  
	- form for buy.
	- link to main page.
	- information about product(price, title, definition, image).

- `/login` login page contains:  
	- ability to login.
	- link to `admin/login` page
	- link to `register/` page
	
- `/logout` logout page contains:  
	- link to `login/` page
	
- `/register` register page contains:  
	- ability to create account.
	- link to `alogin/` page


![](information/uflow.jpg)

