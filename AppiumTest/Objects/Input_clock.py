from Objects.BaseObject import BaseObjectClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WriteClockClass(BaseObjectClass):

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
        self.set_value(self.get_hour_input(), hour)
        self.set_value(self.get_minutes_input(), minutes)
        self.get_OK_button().click()

    def get_hour_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')))

    def get_minutes_input(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout'))).click()
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')))
    def set_value(self, element, value):
        element.clear()
        element.send_keys(value)


