import Pages.base_page as b
import Resources.locators as loc
from selenium import webdriver
import time
class RechercheClientPage(b.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tester_recherche_client(self, prenom_client, nom_client):
        assert self.verify_element_text(*loc.PageCARechercheClientLocators.legend_Recherche,"Rechercher un client")
        self.set_text_element(*loc.PageCARechercheClientLocators.input_Prenom_Client, prenom_client)        
        self.set_text_element(*loc.PageCARechercheClientLocators.input_Nom_Client, nom_client)
        prenom = self.get_text_element(*loc.PageCARechercheClientLocators.input_Prenom_Client)
        nom = self.get_text_element(*loc.PageCARechercheClientLocators.input_Nom_Client)
        self.click_element(*loc.PageCARechercheClientLocators.btn_Recherche)

    def tester_validation_client(self, prenom, nom):
        assert self.verify_element_present(*loc.PageCARechercheClientLocators.table_Clients)
        self.driver.execute_script("document.querySelector('#customControlValidation1').click()")
        time.sleep(5)
        assert self.verify_element_text(*loc.PageCARechercheClientLocators.table_Clients, prenom)
        assert self.verify_element_text(*loc.PageCARechercheClientLocators.table_Clients, nom)
        self.click_element(*loc.PageCARechercheClientLocators.btn_Valider)
        time.sleep(5)