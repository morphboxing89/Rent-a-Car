CREATE TABLE Сustumers --Клиенты
(
    id SERIAL PRIMARY KEY,
    firstName TEXT NOT NULL,
    middlename TEXT,
    lastName TEXT NOT NULL,
    Phone VARCHAR(11) NOT NULL UNIQUE
);


CREATE TABLE Autos --Автомобили
  (  id INT PRIMARY KEY,
    brand TEXT NOT NULL,
    rental_price FLOAT,
    type_rental TEXT NOT NULL
);


CREATE TABLE Issued_cars --Выданные автомобили
(
    id INT PRIMARY KEY,
    custumer_id INT,
    autos_id INT,
    itogovaya_stoimost FLOAT,
    created_date Date,

    FOREIGN KEY (custumer_id) REFERENCES Custumers(id),
    FOREIGN KEY (autos_id) REFERENCES Autos(id)
);