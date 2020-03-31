import main
from selenium.webdriver.support.ui import WebDriverWait
import unittest

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class stand(main.MainTest):
    
    def test_Navigate_to_any_category_and_make_sure_there_are_products(self):
        self.category = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//a[contains(@href,'/categories/5167988722368512')]"))
        print (self.category)
        self.category.click()
        try:
            assert self.category.text == 'Getränke'
        except AssertionError:
            print("Assertion failed. Actual value is %s" % self.category.text)

        self.categorywine=WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//a[contains(@href,'/categories/6226596490903552')]"))
        print(self.categorywine.text)
        self.categorywine.click()
        try:
            assert self.categorywine.text == 'Weine'
        except AssertionError:
            print("Assertion failed. Actual value is %s" % self.categorywine.text)

        self.verifyproduct=WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//a[. = 'Met,  weiß, 6 x 500ml']"))
        print(self.verifyproduct.text)

        try:
            assert self.verifyproduct.text == 'Met, weiß, 6 x 500ml'
            print("Test pass")
        except AssertionError:
            print("Assertion failed. Actual value is %s" % self.verifyproduct.text)

    def test_registration(self):
        self.registration = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//span[. = 'Registrieren']")).click()
        self.firstname = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_input_firstName_0']"))
        self.firstname.click()
        self.firstname.send_keys("Luke")
        self.lastname = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_input_lastName_1']"))
        self.lastname.click()
        self.lastname.send_keys("Skywalker")

        self.telephone = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_phone-input_phone_2']"))
        self.telephone.click()
        self.telephone.send_keys("0178654756")
        self.ort = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_input_city_3']"))
        self.ort.click()
        self.ort.send_keys("Berlin")
        self.plz = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_input_zip_4']"))
        self.plz.click()
        self.plz.send_keys("10365")

        self.strase = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_input_street_5']"))
        self.strase.click()
        self.strase.send_keys("Berlin")

        self.Geburtstag = WebDriverWait(self.driver, 20). \
            until(
            lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_datepicker-input_birthday_6']"))
        self.Geburtstag.click()
        self.Geburtstag.send_keys("04.01.1983")


        self.land = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_select-input_residenceCountryCode_7']"))
        self.land.click()
        for option in self.land.find_elements_by_tag_name('span'):
            if option.text == 'Deutschland':
                option.click()
                break

        time.sleep(10)

        self.Staatsangehörigkeit = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_select-input_nationalityCountryCode_8']"))
        self.Staatsangehörigkeit.click()
        for nationality in self.Staatsangehörigkeit.find_elements_by_tag_name('span'):
            if nationality.text == 'Albanien':
                nationality.click()
                break

        self.EMail = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_1_input_email_9']"))
        self.EMail.click()
        self.EMail.send_keys("xyz@gmail.com")

        self.Passwort = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_2_input_password_0']"))
        self.Passwort.send_keys
        self.Passwort.send_keys("Xyzef123")

        self.Passwort_wdh = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_2_input_passwordConfirm_1']"))
        self.Passwort_wdh.send_keys
        self.Passwort_wdh.send_keys("Xyzef123")

        self.Firma = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_2_input_companyName_11']"))
        self.Firma.click()
        self.Firma.send_keys("XYZ GMbH")

        time.sleep(10)
        self.Unternehmenstyp = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_2_select-input_companyType_15']"))
        self.Unternehmenstyp.click()
        for optiony in self.Unternehmenstyp.find_elements_by_tag_name('span'):
            if optiony.text == 'Gewerbliche GbR':
                optiony.click()
                break

        self.IBAN = WebDriverWait(self.driver, 20). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='formly_2_input_iban_18']"))
        self.IBAN.click()
        self.IBAN.send_keys("DE12647598756479824668")
        time.sleep(10)

        self.dataprivacy=self.dataprivacy=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[. ='Ich akzeptiere die ']"))).click()

        self.registration = WebDriverWait(self.driver, 20). \
        until(lambda driver: driver.find_element_by_xpath("//span[. = 'Registrieren']")).click()
        time.sleep(10)
if __name__ == "__main__":
    unittest.main()
