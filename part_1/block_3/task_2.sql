BEGIN;
INSERT INTO Custumers (id, firstName, middleName, lastName, Phone)
    VALUES (4, 'Timur', 'Alexsandrovich', 'Sirotin', 79998207171);

SAVEPOINT after_insert;

UPDATE Custumers
    SET lastName = 'Sirotin'
    WHERE id = 4;

ROLLBACK after_insert;
COMMIT;

