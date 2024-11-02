CREATE DATABASE libreria;

USE libreria;

CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    fecha_publicacion DATE,
    genero VARCHAR(50)
);

CREATE TABLE venta (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    fecha_venta DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE detalle_venta (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_venta INT,
    id_libro INT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
);

-- Inserciones de ventas
INSERT INTO venta (id_usuario, total) VALUES (1, 27.50); -- Total: 12.50 + 15.00
INSERT INTO detalle_venta (id_venta, id_libro, cantidad, precio_unitario) VALUES 
(LAST_INSERT_ID(), 1, 1, 12.50),  -- El Principito
(LAST_INSERT_ID(), 2, 1, 15.00);  -- Cien años de soledad

INSERT INTO venta (id_usuario, total) VALUES (2, 11.99); -- Total: 11.99
INSERT INTO detalle_venta (id_venta, id_libro, cantidad, precio_unitario) VALUES 
(LAST_INSERT_ID(), 3, 1, 11.99);  -- Veinte mil leguas de viaje submarino

INSERT INTO venta (id_usuario, total) VALUES (3, 27.50); -- Total: 15.00 + 12.50
INSERT INTO detalle_venta (id_venta, id_libro, cantidad, precio_unitario) 
VALUES (LAST_INSERT_ID(), 2, 1, 15.00),  -- Cien años de soledad
(LAST_INSERT_ID(), 1, 1, 12.50);  -- El Principito

SHOW plugins