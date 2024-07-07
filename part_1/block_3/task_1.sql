SELECT *
FROM Custumers
CROSS JOIN Autos;

SELECT *
FROM Custumers
JOIN Autos ON Custumers.Id = Autos.Id;


CREATE UNIQUE INDEX Autos_id_index ON Autos (id);
CREATE INDEX Issued_cars_id_index ON Issued_cars (id)
WHERE id > 3;

DROP INDEX Autos_id_index;
DROP INDEX Issued_cars_id_index;