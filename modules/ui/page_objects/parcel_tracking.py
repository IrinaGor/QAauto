from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ParselTracking(BasePage):
    URL = 'https://tracking.novaposhta.ua/#/uk'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(ParselTracking.URL)

    def try_track(self, invois_number):
        #Знаходимо поле, в яке будемо вводити неправильний номер накладної
        invois_number_elem = self.driver.find_element(By.ID, "en")

        #Вводимо неправильний номер накладної
        invois_number_elem.send_keys(invois_number)

        #Знаходимо кнопку Пошук
        btn_elem = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")

        #Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def try_error_message(self): 
        # Очікуємо на виникнення повідомлення про помилку
        error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "np-number-input-desktop-message-error-message")))

        # Отримуємо текст повідомлення про помилку
        error_text = error_message.text

        # Перевіряємо, чи отримано очікуване повідомлення про некоректний ввід даних
       # assert "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609" in error_text
        return error_text