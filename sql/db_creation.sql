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
    calificacion SMALLINT,
    is_popular SMALLINT
);

CREATE TABLE userSeries(
    id_userSeries SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_serie SMALLINT NOT NULL,
    id_usuario SMALLINT NOT NULL,
    imagen VARCHAR(1000),
    UNIQUE KEY (id_serie,id_usuario)
);

CREATE TABLE watchingSeries(
    id_watchingSerie SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_serie VARCHAR(50),
    temporada SMALLINT,
    capitulo SMALLINT,
    imagen VARCHAR(1000),
    id_usuario SMALLINT NOT NULL,
    id_serie SMALLINT NOT NULL,
    UNIQUE KEY (id_serie,id_usuario)
)