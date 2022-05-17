CREATE DATABASE testRolandoM;

USE testRolandoM;

CREATE TABLE users (
    id SMALLINT NOT NULL PRIMARY KEY IDENTITY,
    name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(30),
    password VARBINARY
);