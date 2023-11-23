import pytest
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.parcel_tracking import ParselTracking


@pytest.mark.ui 
def test_incorrect_username_page():
    #Створення об'єкту сторінки
    sign_in_page = SignInPage()

    #Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    #Виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui 
def ttest_incorrect_parcel_tracking():
    #Створення об'єкту сторінки
    parsel_tracking_page = ParselTracking()

    #Відкриваємо сторінку https://tracking.novaposhta.ua/#/uk
    parsel_tracking_page.go_to()

    #Виконуємо спробу відстежити посилку
    parsel_tracking_page.try_track("59500000031")

    # Отримуємо повідомлення про помилку
    error_message = parsel_tracking_page.try_error_message()
    
    # Очікуване повідомлення про помилку
    expected_text = "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609"

    # Перевіряємо, чи отримане повідомлення про помилку містить очікуваний текст
    assert expected_text in error_message
    
    #Закриваємо браузер
    parsel_tracking_page.close()