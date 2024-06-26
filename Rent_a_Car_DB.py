import sqlite3 as my_baza
test = my_baza.connect('car_rent.sql')

with test:
    cur = test.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 
    Custumers(
        id SERIAL PRIMARY KEY,
        firstName TEXT NOT NULL,
        middlename TEXT,
        lastName TEXT NOT NULL,
        Phone VARCHAR(11) NOT NULL UNIQUE)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS
        Autos(
        id SERIAL PRIMARY KEY,
        brand TEXT NOT NULL,
        rental_price FLOAT,
         type_rental TEXT NOT NULL)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS 
        Issued_cars(
        id SERIAL PRIMARY KEY,
        custumer_id INT,
        autos_id INT,
        itogovaya_stoimost FLOAT,
        created_date Date,

        FOREIGN KEY (custumer_id) REFERENCES Custumers(id)
        FOREIGN KEY (autos_id) REFERENCES Autos(id))""")
    test.commit()