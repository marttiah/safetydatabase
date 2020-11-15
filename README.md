# safetydatabase
Drug safety database

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
