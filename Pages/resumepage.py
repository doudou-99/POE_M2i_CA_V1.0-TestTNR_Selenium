import Pages.base_page as b
import Resources.locators as loc
from selenium import webdriver
import time

class ResumePage(b.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tester_impression_contrat(self):
        assert self.verify_element_text(*loc.PageCAResumeContratLocators.titre_recap_contrat,"Contrat de crédit")
        self.click_element(*loc.PageCAResumeContratLocators.btn_Imprimer)

    def tester_enregistrement_contrat(self):
        time.sleep(5)
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)
        time.sleep(5)
        self.click_element(*loc.PageCAResumeContratLocators.btn_Enregistrer)
        assert self.verify_element_present(*loc.PageCAResumeContratLocators.verif_creation_contrat)
        time.sleep(5)
