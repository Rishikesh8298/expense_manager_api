# expense_manager_api

* Description:
  The Expense Manager API facilitates efficient tracking of personal finances. Users can securely authenticate, submit,
  retrieve, and manage expenses, specifying details such as amount, category, and description. The API supports dynamic
  category management and generates insightful reports. With robust user authentication, this RESTful API ensures data
  privacy and integrity.


* Project Setup
  Step 1: Prequisites python 3.9.0 or greater version is available. AND postman for api testing.
  Step 2: pip install -r requirement.txt
  Step 3: python manage.py makemigrations
  Step 4: python manage.py migrate
  Step 5: python manage.py runserver

* Documentations (swagger)
  api-doc/

* Permissions
  BasicAuthentication.

* Authentication
  TokenBasedAuthentication

* Endpoints
  ● POST /accounts/register/ for creating users and sample data:
  {
  "username": "test",
  "email": "test@example.com",
  "password": "test1@123"
  "re_password": "test1@123"
  }
  ● POST /accounts/login/ for login users and sample data:
  {
  "username": "test",
  "password": "test1@123"
  }
  ● POST /api/expenses/: Create a new expense.
  ● GET /api//expenses/: List all expenses.
  ● GET /api//expenses/{pk}/: Retrieve a specific expense's detail.
  ● PUT /api//expenses/{pk}/: Update particular expense's detail.
  ● DELETE /api//expenses/{pk}/: Delete an expense.
  ● GET /api/category/: Category information
  ● POST /accounts/logout/ for logout.
 
