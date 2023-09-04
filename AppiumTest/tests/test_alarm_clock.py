from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Objects.BaseObject import BaseObjectClass
from Objects.Picker_clock import ClockClass
from Objects.Input_clock import WriteClockClass
from conftest import driver
import pytest

@pytest.mark.parametrize("hour,minutes", [("2","30")])
def test_add_clock_with_interactive_button(driver, hour, minutes):
    select_time = hour + ':' + minutes
    clock = ClockClass(driver)
    clock.open_app()
    clock.add_alarm(hour, minutes)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@content-desc="2:30 PM"]'))).text[:-3] == select_time

@pytest.mark.parametrize("hour,minutes", [("2","30")])
def test_add_clock_with_input_time(driver, hour, minutes):
    select_time = hour + ':' + minutes
    clock = WriteClockClass(driver)
    clock.open_app()
    clock.add_alarm(hour, minutes)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@content-desc="2:30 PM"]'))).text[:-3] == select_time

def test_delete_alarm(driver):
    clock = BaseObjectClass(driver)
    clock.open_app()
    clock.delete_alarm()