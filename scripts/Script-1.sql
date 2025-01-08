CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT
);

CREATE TABLE consultas (
    id_consulta SERIAL PRIMARY KEY,
    resultados INT not null,
    fecha_consulta DATE NOT NULL
);

CREATE TABLE historicos_productos (
    id_historico SERIAL PRIMARY KEY,
    id_producto INT NOT NULL,
    id_consulta INT NOT NULL,
    CONSTRAINT fk_producto FOREIGN KEY (id_producto) REFERENCES productos (id_producto) ON DELETE CASCADE,
    CONSTRAINT fk_consulta FOREIGN KEY (id_consulta) REFERENCES consultas (id_consulta) ON DELETE CASCADE
);

INSERT INTO productos (nombre, descripcion) 
VALUES ('Producto A', 'Descripción del Producto A');

INSERT INTO consultas (fecha_consulta) 
VALUES ( '2025-01-05');

INSERT INTO historicos_productos (id_producto, id_consulta) 
VALUES (1, 1),(10,1),(11,1);

select count(*) from productos where nombre = 'Camiseta de manga corta de compresión UA Iso-Chill para hombre' 

select * from historicos_productos hp 
join consultas c on hp.id_consulta = c.id_consulta 
join productos p on hp.id_producto = p.id_producto 
-- where hp.descuento > 35 and c.fecha_consulta = '2025-01-07'
where p.nombre = 'Playera sin mangas HeatGear® Armour para hombre'
order by hp.precio_descuento asc
