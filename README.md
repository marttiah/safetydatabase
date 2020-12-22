# safetydatabase
Drug safety database
https://safetydatabase.herokuapp.com/

22-Dec-2020:

Updates: 
- Bootstrap added 
- Minor changes to the content of the website (text, links)
- Testing with 'admin' and 'user' roles done 
    - Still needs updating 
- Peer review read
    - Suggestions to to-do
- CSRF tested, not working, removed
    - Still needs to be added 

To-do: 
- Password requirements 
- Add session and session checking 
- CSRF
- ADR information page formatting 
- ?Admin and User roles? - not absolutely necessary 

22-Nov-2020:

- error message fixed when username is taken
- the username was removed from the message because the tuple only contains password and user id
- linelisting in the information page working now


18-Nov-2020:

I fixed the issue with opening the app locally and in Heroku. The main reason was missing "import routes" in the app.py. 

Some other issues in the code was debugged. Now the system is working as it should except for ADR linelisting not working at /information.html

Bugs:
- error message not working correctly when username is taken 
- after login, the username is displaying the ID of the user, not the username

15-Nov-2020: 

I changed the app structure according to the example in the course material. The main change was to split the app.py to smaller apps with the aim to have the registration working. 

The first deployment to Heroku worked otherwise fine, but it was missing the possibility to add new users - and thus it was not possible to login to the app. 

After splitting the main app, the locally ran 'flask run' stopped working and so did the updated deployed version in Heroku. 

Troubleshooting:
- The issue is "GET / HTTP/1.1" 404" so the index page is not found (neither is anything else.)
- git remote -v not showing origin
- git push heroku master not working - deployment had to be done through Heroku's website
- DATABASE_URL for Heroku - Where is this set in order to keep it secret but make it possible to connect to the database? (now in .env)

This is a project for creating a simple but functional database for adverse events. Safety database is used for collecting, storing and sharing adverse event information. 

The functionalities of the safety database include: 
- An SQL database for storing the information with the following tables: 
    - users
    - adverseevents
    - companies
    - products 
    - countries 
- User rights: user and admin
- Possibility to submit a new adverse event (maybe E2B R3)
    - List of products (registered medical products)
    - List of companies (marketing authorization holders)
    - List of adverse events (MedDRA code)
    - List of countries, country codes and languages
- Notification to admins
- Searching for statistics related to the adverse events 

Planned structure of the form:
Login
username 
Password
Company
User access
user
Products of their company
Admin
Everything
Companies
ID
Company name
Products
list of APIs 
Countries
List of European countries
Form
Date (Time stamp)
Country
Product
Adverse event 
Reporter 
Patient 

Planned report options for the information page: 
Information 
Choose report 
Admin has access to everything 
User has access to their company’s data
Line listing of all reports 
Graph - Reported cases by country
Graph - Reported cases by date

Planned schema of the database: 
CREATE TABLE adrs (id SERIAL PRIMARY KEY, dayzero TIMESTAMP, aedescription TEXT, reporter TEXT, patient TEXT);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, company TEXT);
CREATE TABLE countries (country TEXT);
CREATE TABLE companies (id SERIAL PRIMARY KEY, name TEXT UNIQUE, product TEXT);
