from selenium.webdriver.common.by import By

class PageCAAuthentLocators():
    btn_Acces_Credit= (By.XPATH, "//a[@id='lnkAccesCreditAuto']")
    btn_Connecter=(By.XPATH, "//button[@type='submit']")
    info_Connectez_vous=(By.XPATH,"//body[@id='page-top']/div[2]/div/div/form/fieldset/legend")
    titre_Page_Accueil = (By.XPATH, "//body[@id='page-top']/div/h4")
    input_username = (By.XPATH,"//input[@id='username']")
    input_password = (By.XPATH, "//input[@id='password']")
    link_Deconnexion = (By.XPATH, "//a[@id='lnkDeconnexion']")

class PageCAEcheancierLocators():
    btn_Echeancier= (By.XPATH, "//div[@id='ech']")
    Tableau_echeances= (By.XPATH, "//div[@id='echeance']")
    btn_Creer_contrat= (By.XPATH, "(//a[@id='lnkCreerContrat'])[2]")

class PageCASimulationLocators():
    link_Credit= (By.XPATH, "//a[@id='lnkCredit']")
    link_Creer_contrat_credit= (By.XPATH, "//a[@id='lnkCreerContrat']")
    titre_Page_Creation_Contrat= (By.XPATH, "//body[@id='page-top']/div/h3")
    titre_Formulaire_Simulation= (By.XPATH, "//div[@id='contract']/form/fieldset/legend")
    input_Montant_achat= (By.XPATH, "//input[@id='form_simulation_montantAchat']")
    input_Montant_credit= (By.XPATH, "//input[@id='form_simulation_montantCredit']")
    input_Duree= (By.XPATH, "//input[@id='form_simulation_duree']")
    select_Categorie= (By.XPATH, "//select[@id='form_simulation_categorie']")
    btn_Calculer_credit= (By.XPATH, "//button[@id='calcul']")
    legend_Nouveau_Contrat= (By.XPATH,"//div[@id='contract']/form/fieldset/legend")

class PageCARechercheClientLocators():
    legend_Recherche=(By.XPATH, "//div[@id='contract']/fieldset/legend")
    input_Prenom_Client=(By.XPATH, "//input[@id='firstname']")
    input_Nom_Client= (By.XPATH, "//input[@id='name']")
    btn_Recherche= (By.XPATH, "//input[@id='btnRechercher']")
    table_Clients= (By.XPATH, "//table[@id='clients']")
    btn_Valider= (By.XPATH, "//button[@id='submit']")

class PageCAResumeContratLocators():
    btn_Imprimer= (By.XPATH, "//button[@id='print']")
    btn_Enregistrer= (By.XPATH, "//button[@id='register']")
    verif_creation_contrat= (By.XPATH, "//body[@id='page-top']/div[2]/div")
    titre_recap_contrat= (By.XPATH, "//legend")
