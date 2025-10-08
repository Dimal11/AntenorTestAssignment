from playwright.sync_api import Page
from page_objects.base_form import BaseForm

class AuthForm(BaseForm):
    def __init__(self, page: Page, url = ''):
        super().__init__(page = page, url = url)
        self.login_inpt = self.page.locator('#user')
        self.pwd_inpt = self.page.locator('#passw')
        self.lang_slct = self.page.locator('#lang')
        self.save_me_ckbx = self.page.locator('#store_cookie')
        self.submit_btn = self.page.locator('#submit')
        self.error_alert = self.page.get_by_test_id('alerts-content')

    def fill_sing_in_form(self, login, password, lang='uk'):
        self.login_inpt.fill(login)
        self.pwd_inpt.fill(password)
        self.lang_slct.select_option(value=lang)

        if self.save_me_ckbx.is_checked():
            self.save_me_ckbx.uncheck()

        self.submit_btn.click()
