INSERT INTO Custumers (id, firstName, middleName, lastName, Phone)
    VALUES(1, 'Artem', 'Alexsandrovich', 'Sirotin', 79998207171),
          (2, 'Oleg', 'Olegovich', 'Olegov', 79998207474),
          (3, 'Alex', 'Alexsandrovich', 'Batashev', 79998207272);

INSERT INTO Autos (id, brand, rental_price, type_rental)
    VALUES(1, 'Audi Q5', 7000, 'one day'),
           (2, 'Audi Q5', 9000, 'one day'),
           (3, 'Audi Q5', 9000, 'one day'),
           (4, 'Mazda 6', 8000, 'one day'),
           (5, 'Mazda 6', 8000, 'one day'),
           (6, 'Mazda 6', 8000, 'one day'), 
           (7, 'Mazda 6', 6000, 'one day') 

INSERT INTO Issued_cars (id, custumer_id, autos_id, total_price)
    VALUES(1, 1, 1, 7000),
          (2, 2, 2, 9000),
          (3, 4, 4, 8000),
          (4, 7, 7, 6000)  