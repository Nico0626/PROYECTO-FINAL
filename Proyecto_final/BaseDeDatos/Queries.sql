-- Inserción de usuarios
INSERT INTO usuario (nombre, email, telefono) 
VALUES 
    ('Juan Pérez', 'juan.perez@example.com', '123456789'),
    ('Homero Simpson', 'homero.simpson@example.com', '3242556'),
    ('Maximo Cosetti', 'maximo.cosetti@example.com', '18237164');
    
-- Inserción de libros
INSERT INTO libros (titulo, autor, precio, stock, fecha_publicacion, genero) 
VALUES 
    ('El Principito', 'Antoine de Saint-Exupéry', 12.50, 10, '1943-04-06', 'Ficción'),
    ('Cien años de soledad', 'Gabriel García Márquez', 15.00, 5, '1967-05-30', 'Ficción'),
    ('Veinte mil leguas de viaje submarino', 'Jules Verne', 11.99, 7, '1870-01-01', 'Ciencia ficción');
    
SELECT usuario.id_usuario, usuario.nombre, 
       venta.id_venta, venta.fecha_venta, 
       libros.titulo, detalle_venta.cantidad, detalle_venta.precio_unitario
FROM usuario
JOIN venta ON usuario.id_usuario = venta.id_usuario
JOIN detalle_venta ON venta.id_venta = detalle_venta.id_venta
JOIN libros ON detalle_venta.id_libro = libros.id_libro
WHERE usuario.id_usuario = 1;  -- Cambia "1" por el ID del usuario que deseas consultar

SELECT venta.id_venta, venta.fecha_venta, 
       venta.total, libros.titulo, detalle_venta.cantidad
FROM venta
JOIN detalle_venta ON venta.id_venta = detalle_venta.id_venta
JOIN libros ON detalle_venta.id_libro = libros.id_libro
ORDER BY venta.fecha_venta DESC;



INSERT INTO libros (titulo, autor, precio, stock, fecha_publicacion, genero) 
VALUES ('NombreNuevoLibro', 'Autor1', 24000, 10, CURDATE(), 'Género');


UPDATE libros
SET stock = stock + 100
WHERE titulo = 'NombreNuevoLibro'; 

DELETE FROM detalle_venta
WHERE id_venta = 3; 

DELETE FROM venta
WHERE id_venta = 3;  

SELECT titulo, stock, precio, genero
FROM libros
WHERE autor = 'Jules Verne'  -- Cambia 'Nombre del Autor' por el nombre del autor que deseas consultar
AND precio < 10000;


