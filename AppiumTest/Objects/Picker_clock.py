from Objects.BaseObject import BaseObjectClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ClockClass(BaseObjectClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_alarm(self, hour, minutes):
        self.get_add_button().click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'com.google.android.deskclock:id/material_clock_face')))
            self.set_an_alarm(hour, minutes)
        except:
            self.select_type_clock()
            self.set_an_alarm(hour, minutes)

    def set_an_alarm(self, hour, minutes):
        self.get_hour_button(hour).click()
        self.get_minutes_button(minutes).click()
        self.get_OK_button().click()

    def get_hour_button(self, hour):
        hour = hour + " o'clock"
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@content-desc="{hour}"]')))

    def get_minutes_button(self, minutes):
        minutes = minutes + ' minutes'
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@content-desc="{minutes}"]')))


