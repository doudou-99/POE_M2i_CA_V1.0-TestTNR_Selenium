import unittest
from selenium import webdriver
import Pages.authentpage as auth
import Pages.simulationpage as simu
import Pages.echeancierpage as echeancier
import Pages.rechercheclientpage as recherche
import Pages.resumepage as resume
 

usergcd= "gcd"
passwordgcd="acial!gcd2018"
montant_achat=20000
montant_credit=18000
valeurMinAchat=6250
valeurMaxAchat=50000
valeurMinCredit=5000
valeurMaxCredit=40000
valeurMinDuree=12
valeurMaxDuree=48
duree=24
categorie="B"
prenom="Jonathan"
nom="MULLER"

class TestCreationContratCreditAuto(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://credit-auto.qsiconseil.ma")
        self.driver.maximize_window()

    def test_mettre_en_place_contrat_credit(self):
        authpage = auth.AuthentPage(self.driver)
        simupage = simu.SimulationPage(self.driver)
        authpage.connexion("gcd","acial!gcd2018")
        simupage.saisir_info_credit(montant_achat, montant_credit, duree, categorie)
        self.assertTrue(simupage.verifier_champ_montant_achat_entre(valeurMinAchat, valeurMaxAchat))
        self.assertTrue(simupage.verifier_champ_montant_credit_entre(valeurMinCredit, valeurMaxCredit))
        self.assertTrue(simupage.verifier_champ_duree_entre(valeurMinDuree, valeurMaxDuree))
        simupage.cliquer_bouton_Calcul()
        echepage = echeancier.EcheancierPage(self.driver)
        echepage.tester_echeancier()
        rechpage= recherche.RechercheClientPage(self.driver)
        rechpage.tester_recherche_client(prenom,nom)
        rechpage.tester_validation_client(prenom,nom)
        respage = resume.ResumePage(self.driver)
        respage.tester_impression_contrat()
        respage.tester_enregistrement_contrat()
        authpage.deconnexion()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()