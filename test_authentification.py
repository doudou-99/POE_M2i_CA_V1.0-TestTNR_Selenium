import unittest
from selenium import webdriver

import Pages.authentpage as auth


usergcd= "gcd"
passwordgcd="acial!gcd2018"
useracd= "acd"
passwordacd="acial!acd2018"
userlcd= "lcd"
passwordlcd="acial!acd2018"
userrcd= "rcd"
passwordrcd="acial!rcd2018"
 

class TestAuthentification(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://credit-auto.qsiconseil.ma")
        self.driver.maximize_window()

    def test_authent_avec_compte_gestionnaire(self):
        page = auth.AuthentPage(self.driver)
        page.connexion(usergcd, passwordgcd)
        self.assertTrue(page.verify_presence_titre_page_accueil())
        page.deconnexion()
        self.assertTrue(page.verify_presence_bouton_Acces_Credit())

    def test_authent_avec_compte_admin(self):
        page = auth.AuthentPage(self.driver)
        page.connexion(useracd, passwordacd)
        self.assertTrue(page.verify_presence_titre_page_accueil())
        page.deconnexion()
        self.assertTrue(page.verify_presence_bouton_Acces_Credit())

    def test_authent_avec_compte_responsable(self):
        page = auth.AuthentPage(self.driver)
        page.connexion(userrcd, passwordrcd)
        self.assertTrue(page.verify_presence_titre_page_accueil())
        page.deconnexion()
        self.assertTrue(page.verify_presence_bouton_Acces_Credit())

    def test_authent_avec_compte_loueur(self):
        page = auth.AuthentPage(self.driver)
        page.connexion(userlcd, passwordlcd)
        self.assertTrue(page.verify_presence_titre_page_accueil())
        page.deconnexion()
        self.assertTrue(page.verify_presence_bouton_Acces_Credit())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        


