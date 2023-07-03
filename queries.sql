-- SQL-команды для создания таблиц
CREATE TABLE employer
(
	id_employer int PRIMARY KEY,
	company_name varchar(100) NOT NULL
);

CREATE TABLE vacancy
(
	id_vacancy int PRIMARY KEY,
	id_employer int REFERENCES employer(id_employer),
	vacancy_name varchar(255) NOT NULL,
	salary_from int,
	salary_to int,
	url varchar(50) NOT NULL,
	requirements text NOT NULL
);

