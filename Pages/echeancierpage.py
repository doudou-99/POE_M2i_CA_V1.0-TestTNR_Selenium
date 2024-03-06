import Pages.base_page as b
import Resources.locators as loc
from selenium import webdriver

class EcheancierPage(b.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tester_echeancier(self):
        assert self.verify_element_text(*loc.PageCASimulationLocators.legend_Nouveau_Contrat, "Nouveau contrat")
        self.click_element(*loc.PageCAEcheancierLocators.btn_Echeancier)
        assert self.verify_element_present(*loc.PageCAEcheancierLocators.Tableau_echeances)
        self.click_element(*loc.PageCAEcheancierLocators.btn_Creer_contrat)

    