from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Customers, Autos, IssuedCars, engine

Session = sessionmaker(bind=engine)

session = Session()

#Добавление записей в базу данных

# new_customers = Customers(first_name='Artem',
#                           middle_name='Aleksandovich',
#                           last_name='Sirotin',
#                           phone='79998207171')
#
# new_customers_2 = Customers(first_name='Alex', middle_name='Aleksandovich',
#                             last_name='Batashev', phone=79998207272)
#
# new_customers_3 = Customers(first_name='Oleg', middle_name='Olegovich',
#                             last_name='Olegov', phone=79998207475)

# session.add(new_customers)
# session.add_all([new_customers_2, new_customers_3])


# new_autos = Autos(brand='AUDI Q5',
#                   rental_price='7000',
#                   type_rental='one day')


# new_autos_2 = Autos(brand='AUDI Q5',
#                     rental_price='9000',
#                     type_rental='one day')


# new_autos_3 = Autos(brand='AUDI Q5',
#                     rental_price='9000',
#                     type_rental='one day')

# new_autos_4 = Autos(brand='Mazda 6',
#                     rental_price='8000',
#                     type_rental='one day')

# new_autos_5 = Autos(brand='Mazda 6',
#                     rental_price='8000',
#                     type_rental='one day')

# new_autos_6 = Autos(brand='Mazda 6',
#                     rental_price='8000',
#                     type_rental='one day')

# new_autos_7 = Autos(brand='Mazda 6',
#                     rental_price='6000',
#                     type_rental='one day')

# session.add_all([new_autos, new_autos_2, new_autos_3, new_autos_4, new_autos_5,
#                  new_autos_6, new_autos_7])

new_IssuedCars = IssuedCars(customer_id=1,
                            autos_id=1,
                            total_price='7000')

new_IssuedCars2 = IssuedCars(customer_id=2,
                             autos_id=2,
                             total_price='9000')

new_IssuedCars3 = IssuedCars(customer_id=3,
                             autos_id=3,
                             total_price='8000')

new_IssuedCars4 = IssuedCars(customer_id=4,
                             autos_id=4,
                             total_price='6000')

session.add(new_IssuedCars)
session.add_all([new_IssuedCars2, new_IssuedCars3, new_IssuedCars4])

#Обновление записей

# customers = session.query(Customers).get(1)

# customers.first_name = 'Timur'


# autos = session.query(Autos).update({Autos.rental_price: Autos.rental_price + '4000'})


# autos = session.query(Autos).filter(Autos.brand == 'Mazda 6').update({Autos.brand: 'BMW X5'})

#Grouping

#Находит уникальные значения в столбцах

# autos = session.query(Autos.brand).group_by(Autos.brand).all()

# print(autos)

#Находит уникальные значения в столбцах и показывает их количество(Для этого нужно импортировать метод func)

# autos = session.query(Autos.brand, func.count(Autos.id)).group_by(Autos.brand).all()

# print(autos)

#Удаление записи

#Удаляем все записи начинающиеся на А

# autos = session.query(Autos).filter(Autos.brand.like('A%')).delete()

# autos = session.query(Autos).filter(Autos.brand == 'BMW X5', Autos.rental_price == '6000').delete()

#JOIN CROSS - в alchemy нет.

# result = session.query(Customers.first_name, Autos.brand).all()

# print(result)

#Объединение по количеству id

# result = session.query(Customers.first_name, Autos.brand).join(Autos, Customers.id == Autos.id).all()

# print(result)

session.commit()
