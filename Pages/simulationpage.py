import Pages.base_page as b
import Resources.locators as loc
from selenium import webdriver
from selenium.webdriver.support.select import Select

class SimulationPage(b.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def saisir_info_credit(self, montant_achat, montant_credit, duree, categorie):
        self.click_element(*loc.PageCASimulationLocators.link_Credit)
        self.click_element(*loc.PageCASimulationLocators.link_Creer_contrat_credit)
        assert self.verify_element_text(*loc.PageCASimulationLocators.titre_Page_Creation_Contrat, "Création d'un contrat de crédit")
        assert self.verify_element_text(*loc.PageCASimulationLocators.titre_Formulaire_Simulation, "Simulation d'un crédit")
        self.set_text_element(*loc.PageCASimulationLocators.input_Montant_achat, "20000")
        self.set_text_element(*loc.PageCASimulationLocators.input_Montant_credit, "18000")
        self.set_text_element(*loc.PageCASimulationLocators.input_Duree, "24")
        Select(self.get_element(*loc.PageCASimulationLocators.select_Categorie)).select_by_value("B")
        
    def verifier_champ_montant_achat_entre(self, valeurinf, valeursup):
        val = int(self.get_text_element(*loc.PageCASimulationLocators.input_Montant_achat))
        return val > valeurinf and val < valeursup
    
    def verifier_champ_montant_credit_entre(self, valeurinf, valeursup):
        val = int(self.get_text_element(*loc.PageCASimulationLocators.input_Montant_credit))
        return val > valeurinf and val < valeursup
    
    def verifier_champ_duree_entre(self, valeurinf, valeursup):
        val = int(self.get_text_element(*loc.PageCASimulationLocators.input_Duree))
        return val > valeurinf and val < valeursup

    def cliquer_bouton_Calcul(self):
        self.click_element(*loc.PageCASimulationLocators.btn_Calculer_credit)


