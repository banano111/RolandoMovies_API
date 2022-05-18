CREATE DATABASE testRolandoM;

USE testRolandoM;

CREATE TABLE users (
    id SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(30),
    password VARBINARY(256)
);