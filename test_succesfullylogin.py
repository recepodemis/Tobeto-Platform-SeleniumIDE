# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSuccesfullylogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_succesfullylogin(self):
    self.driver.get("https://tobeto.com/")
    self.driver.set_window_size(1680, 953)
    self.driver.find_element(By.LINK_TEXT, "Giriş Yap").click()
    element = self.driver.find_element(By.LINK_TEXT, "Giriş Yap")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "email").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "email")))
    self.driver.find_element(By.NAME, "email").send_keys("r********@gmail.com")
    self.driver.find_element(By.NAME, "password").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
    self.driver.find_element(By.NAME, "password").send_keys("*************")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn:nth-child(3)")))
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "lessons-tab")))
    self.driver.find_element(By.ID, "lessons-tab").click()
    element = self.driver.find_element(By.ID, "lessons-tab")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".showMoreBtn:nth-child(2)")))
    self.driver.find_element(By.CSS_SELECTOR, ".showMoreBtn:nth-child(2)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.close()
  
