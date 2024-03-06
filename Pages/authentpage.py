
import Pages.base_page as b
import Resources.locators as loc
import time

class AuthentPage(b.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def connexion(self, username, password):
        self.click_element(*loc.PageCAAuthentLocators.btn_Acces_Credit)
        self.verify_element_text(*loc.PageCAAuthentLocators.info_Connectez_vous, "Connectez-vous")
        self.set_text_element(*loc.PageCAAuthentLocators.input_username,username)
        self.set_text_element(*loc.PageCAAuthentLocators.input_password, password)
        self.click_element(*loc.PageCAAuthentLocators.btn_Connecter)
        
    
    def deconnexion(self):
        self.wait_element_visible(loc.PageCAAuthentLocators.link_Deconnexion).click()
        time.sleep(5)
        

    def verify_presence_titre_page_accueil(self):
        return self.verify_element_text(*loc.PageCAAuthentLocators.titre_Page_Accueil, "Bienvenue sur l'application Crédit Auto")
    
    def verify_presence_bouton_Acces_Credit(self):
        return self.verify_element_present(*loc.PageCAAuthentLocators.btn_Acces_Credit)






