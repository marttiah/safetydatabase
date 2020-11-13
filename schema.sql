CREATE TABLE adrs (id SERIAL PRIMARY KEY, TIMESTAMP, aedescription TEXT, reporter TEXT, patient TEXT);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, company);
CREATE TABLE countries (country TEXT);
CREATE TABLE companies (id SERIAL PRIMARY KEY, name TEXT UNIQUE, product TEXT);