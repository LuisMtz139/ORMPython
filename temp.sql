-- Crear la base de datos "primer" si no existe
CREATE DATABASE IF NOT EXISTS primer;

-- Usar la base de datos "primer"
USE primer;

-- Crear la tabla "usuarios" con los atributos especificados
CREATE TABLE IF NOT EXISTS people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    password VARCHAR(255) NOT NULL
);


select * from people;

-- Insertar datos en la tabla "usuarios"
INSERT INTO people (full_name, phone, password) VALUES
('Juan Perez', '1234567890', 'contraseña1'),
('María García', '9876543210', 'contraseña2'),
('Pedro Ramirez', '5555555555', 'contraseña3'),
('Luisa Martínez', '7777777777', 'contraseña4'),
('Carlos Sánchez', '9999999999', 'contraseña5'),
('Ana Rodríguez', '1111111111', 'contraseña6'),
('Miguel López', '3333333333', 'contraseña7'),
('Sofía Hernández', '6666666666', 'contraseña8'),
('Alejandro González', '4444444444', 'contraseña9'),
('Laura Diaz', '2222222222', 'contraseña10');
