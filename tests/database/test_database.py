import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] =='Ukraine'



@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1
    # Check structure os data
    assert orders [0][0] == 1
    assert orders [0][1] == 'Sergii'
    assert orders [0][2] == 'Product 1'
    assert orders [0][3] == 'Description'


@pytest.mark.database
def test_insert_incorrect_data_type():
    db = Database()
    result = db.insert_incorrect_data_type(100, "Product 100", "Description", {'key': 'value'})
    assert result  # Перевірка, що функція повертає помилку
    if result is None:
        print("Вставка даних пройшла успішно.")
    else:
        print("Помилка при вставці даних:", result)

    
@pytest.mark.database
def test_insert_integer():
    db = Database()
    result = db.insert_incorrect_data_type(100, "Product 100", "Description", 10)
    assert result is None
    if result is None:
        print("Числовий тип даних")
    else:
        print("Помилка при вставці даних:", result)

@pytest.mark.database
def test_insert_string():
    db = Database()
    result = db.insert_incorrect_data_type(101, "Product 101", "Description", "string data")
    assert result 
    if result is None:
        print("Строковий тип даних")
    else:
        print("Помилка при вставці даних:", result)

@pytest.mark.database
def test_insert_dict():
    db = Database()
    result = db.insert_incorrect_data_type(102, "Product 102", "Description", {'key': 'value'})
    assert result  # Перевірка, що функція повертає помилку
    if result is None:
        print("Тип даних: словник")
    else:
        print("Помилка при вставці даних:", result)


@pytest.mark.database
def test_insert_float():
    db = Database()
    result = db.insert_incorrect_data_type(103, "Product 103", "Description", 3.14)
    assert result is None
    if result is None:
        print("Тип даних: float")
    else:
        print("Помилка при вставці даних:", result)

