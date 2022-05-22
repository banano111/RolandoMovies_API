CREATE DATABASE testRolandoM;

USE testRolandoM;

CREATE TABLE users (
    id SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(30),
    password VARBINARY(256)
);

CREATE TABLE series (
    id_serie SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_serie VARCHAR(40),
    genero VARCHAR(20),
    descripcion VARCHAR(500),
    imagen VARCHAR(1000),
    calificacion SMALLINT
);