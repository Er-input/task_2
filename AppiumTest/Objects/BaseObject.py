from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseObjectClass():

    def __init__(self, driver):
        self.driver = driver

    def open_app(self):
        self.driver.activate_app("com.google.android.deskclock")

    def get_add_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.google.android.deskclock:id/fab')))

    def get_OK_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.google.android.deskclock:id/material_timepicker_ok_button')))

    def select_type_clock(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.google.android.deskclock:id/material_timepicker_mode_button'))).click()

    def delete_alarm(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '(//android.widget.ImageButton[@content-desc="Expand alarm"])[1]'))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'com.google.android.deskclock:id/delete'))).click()

