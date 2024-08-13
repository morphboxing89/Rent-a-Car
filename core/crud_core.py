import sqlalchemy as crud_core
import datetime

engine = crud_core.create_engine('sqlite:///database.db')
meta = crud_core.MetaData()

Customers = crud_core.Table(
    'customers',
    meta,
    crud_core.Column('id', crud_core.Integer, primary_key=True),
    crud_core.Column('first_name', crud_core.Text, nullable=False),
    crud_core.Column('middle_name', crud_core.Text),
    crud_core.Column('last_name', crud_core.Text, nullable=False),
    crud_core.Column('phone', crud_core.String(11), nullable=False)
)
Autos = crud_core.Table(
    'autos',
    meta,
    crud_core.Column('id', crud_core.Integer, primary_key=True),
    crud_core.Column('brand', crud_core.Text, nullable=False),
    crud_core.Column('rental_price', crud_core.Text, nullable=False),
    crud_core.Column('type_rental', crud_core.String(20), nullable=False)
)
IssuedCars = crud_core.Table(
    'Issued_cars',
    meta,
    crud_core.Column('id', crud_core.Integer, primary_key=True),
    crud_core.Column('customer_id', crud_core.ForeignKey("customers.id")),
    crud_core.Column('autos_id', crud_core.ForeignKey("autos.id")),
    crud_core.Column('total_price', crud_core.Float),
    crud_core.Column('created_date', crud_core.String, default=datetime.datetime.now())
)


meta.drop_all(engine)
meta.create_all(engine)

# ==============================Заполнение================================
with engine.connect() as conn:
    input_1 = crud_core.insert(Customers).values(first_name='Artem',
                                                 middle_name='Aleksandovich',
                                                 last_name='Sirotin', phone='79998207171')
    input_2 = crud_core.insert(Customers).values(first_name='Alex', middle_name='Aleksandovich', last_name='Batashev',
                                                 phone='79998207272')
    input_3 = crud_core.insert(Customers).values(first_name='Oleg', middle_name='Olegovich', last_name='Olegov',
                                                 phone='79998207475')
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)

    # select_test = crud_core.select(Customers)
    # print(conn.execute(select_test).all())
    conn.commit()


with engine.connect() as conn:
    input_1 = crud_core.insert(Autos).values(brand='Audi Q5', rental_price='7000', type_rental='one day')
    input_2 = crud_core.insert(Autos).values(brand='Audi Q5', rental_price='9000', type_rental='one day')
    input_3 = crud_core.insert(Autos).values(brand='Audi Q5', rental_price='9000', type_rental='one day')
    input_4 = crud_core.insert(Autos).values(brand='Mazda 6', rental_price='8000', type_rental='one day')
    input_5 = crud_core.insert(Autos).values(brand='Mazda 6', rental_price='8000', type_rental='one day')
    input_6 = crud_core.insert(Autos).values(brand='Mazda 6', rental_price='6000', type_rental='one day')
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)
    conn.execute(input_4)
    conn.execute(input_5)
    conn.execute(input_6)

    # select_test = crud_core.select(Autos)
    # print(conn.execute(select_test).all())
    conn.commit()


with engine.connect() as conn:
    input_1 = crud_core.insert(IssuedCars).values(
                                        customer_id=1,
                                        autos_id=1,
                                        total_price=7000)
    input_2 = crud_core.insert(IssuedCars).values(
                                        customer_id=2,
                                        autos_id=2,
                                        total_price=9000)
    input_3 = crud_core.insert(IssuedCars).values(
                                        customer_id=3,
                                        autos_id=3,
                                        total_price=8000)
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)
    conn.commit()


# ----------------------------------Изменения и выборки-----------------------------------
with engine.connect() as conn:

    # -
    update_1 = crud_core.update(Customers).where(Customers.c.id == 1).values(first_name='Timur')

    select_test1 = crud_core.select(Customers)
    print(conn.execute(select_test1).all())

    # update_2 = crud_core.update(Autos).where(Autos.c.rental_price).values(rental_price=12000)
    #
    # select_test1 = crud_core.select(Autos)
    # print(conn.execute(select_test1).all())

    # update_3 = crud_core.update(Autos).where(Autos.c.brand == 'Mazda 6').values(brand='BMW X5')

    # select_test1 = crud_core.select(Autos)
    # print(conn.execute(select_test1).all())

    # # # +
    # delete_1 = crud_core.delete(Autos).where(Autos.c.brand == 'Audi Q5')
    # conn.execute(delete_1)

    # select_test2 = crud_core.select(Autos)
    # print(conn.execute(select_test2).all())

    # # -
    # delete_2 = crud_core.delete(Autos).where(Autos.c.brand == 'Audi Q5', Autos.c.rental_price == 7000)
    # conn.execute(delete_2)

    # select_test3 = crud_core.select(Autos)
    # print(conn.execute(select_test3).all())

    conn.commit()
    