INSERT INTO Custumers (id, firstName, middleName, lastName, Phone)
    VALUES(6621, 'Artem', 'Alexsandrovich', 'Sirotin', 79998207171),
          (6622, 'Oleg', 'Olegovich', 'Olegov', 79998207474),
          (7354, 'Alex', 'Alexsandrovich', 'Batashev', 79998207272);

INSERT INTO Autos (id, brand, rental_price, type_rental)
    VALUES(3368, 'Audi Q5', 7000, 'one day'),
           (3343, 'Audi Q5', 9000, 'one day'),
           (4875, 'Mazda 6', 8000, 'one day'), 
           (4874, 'Mazda 6', 6000, 'one day'); 

INSERT INTO Issued_cars (id, custumer_id, autos_id, total_price)
    VALUES(1, 6621, 3368, 7000),
          (2, 6622, 3343, 9000),
          (3, 6622, 4875, 8000),
          (4, 7354, 4874, 6000);    

UPDATE Custumers
    SET firstname='Timur'
    WHERE id = 6621;

DELETE
    FROM Autos
    WHERE brand = 'Audi Q5'; 

