import allure
from playwright.sync_api import Page, expect
from page_objects.auth_form import AuthForm
from utils.dot_dict import load_file_data
from utils.fake_generator import RandomUser
from  config import USER_LOGIN, USER_PASS

USERS = load_file_data('users.json')

@allure.feature("Авторизація")
@allure.story("Тестування сторінки входу в систему")
@allure.severity(allure.severity_level.CRITICAL)
class Test:

    @allure.title("Позитивний сценарій — успішна авторизація з коректними даними")
    @allure.description(
        "Перевіряє, що користувач із валідними даними успішно входить у систему та бачить панель Dashboard.")
    def test_login_form_positive(self, page: Page):
        auth_form = AuthForm(page)

        with allure.step("Відкриваємо сторінку авторизації"):
            auth_form.goto()

        with allure.step("Вводимо правильний логін і пароль"):
            auth_form.fill_sing_in_form(USER_LOGIN, USER_PASS)

        with allure.step("Перевіряємо, що відображається панель керування (Dashboard)"):
            expect(page.locator('//div[@title="Dashboard"]')).to_be_visible(timeout=10000)

        with allure.step("Зберігаємо скріншот успішного входу"):
            screenshot_path = "allure-results/login_positive.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Скріншот успішного входу",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("Негативний сценарій — помилка при авторизації з некоректними даними")
    @allure.description(
        "Перевіряє, що при введенні неправильного логіна або пароля з’являється повідомлення про помилку.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_form_negative(self, page: Page):
        user = RandomUser()
        auth_form = AuthForm(page)

        with allure.step("Відкриваємо сторінку авторизації"):
            auth_form.goto()

        with allure.step(f"Вводимо невірні дані: {user.username} / {user.password}"):
            auth_form.fill_sing_in_form(user.username, user.password)

        with allure.step("Перевіряємо, що з’являється повідомлення про помилку"):
            expect(auth_form.error_alert).to_have_text("Неправильне ім'я користувача або пароль")

        with allure.step("Зберігаємо скріншот помилки"):
            screenshot_path = "allure-results/login_negative.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Скріншот помилки авторизації",
                attachment_type=allure.attachment_type.PNG
            )
