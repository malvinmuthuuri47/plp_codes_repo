CREATE DATABASE IF NOT EXISTS week_three_plp;

USE week_three_plp;

CREATE TABLE IF NOT EXISTS students (
	name varchar(100),
	age int,
	gender varchar(10),
	UNIQUE (name, age, gender)
);

/*
INSERT INTO students (name, age, gender)
VALUES  ("John Doe", 30, "Male"),
	("Jane Doe", 31, "Female"),
	("Michael Johnson", 25, "Male");
*/

CREATE TABLE IF NOT EXISTS student (
	id int NOT NULL AUTO_INCREMENT,
	fullName varchar(100),
	age int,
	PRIMARY KEY (id)
);

/*
INSERT INTO student (fullName, age)
VALUES  ("Maxwell Trance", 30),
	("Innocent Drake", 35),
	("Michale Moore", 45);
*/

UPDATE student
SET age = 20
WHERE id = 2;
