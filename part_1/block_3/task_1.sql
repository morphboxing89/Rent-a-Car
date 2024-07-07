SELECT *
FROM Custumers
CROSS JOIN Autos;

SELECT *
FROM Custumers
JOIN Autos ON Custumers.Id = Autos.Id;


CREATE INDEX Custumers_id_index ON Custumers (id);

CREATE INDEX Issued_cars_id_index ON Issued_cars (id)
WHERE id > 2;

DROP INDEX Custumers_id_index;
DROP INDEX Issued_cars_id_index;
