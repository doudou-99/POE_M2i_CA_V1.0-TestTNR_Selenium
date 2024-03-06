# POE_M2i_CA_V1.0-TestTNR_Selenium
## Installation du projet en local
1. Faire un git clone du projet
2. Ouvrir le dossier du projet avec Visual Studio Code
3. Saisir dans le terminal dans Visual Studio Code:
    *   python -m venv venv
    *   pip install -r requirements.txt
    *   Pour activer l'environnement virtuel de Python saisir également dans le terminal: .\venv\Scripts\Activate.ps1

## Exécution des tests du projet
Cliquer sur le bouton à forme de flèche dans Visual Studio Code pour exécuter les tests, mais pour que l'exécution fonctionne, il faut se trouver sur le fichier du test.
une autre manière d'exécuter les tests est de saisir dans le terminal du projet par exemple sur Visual Studio Code la commande:
*   python -m unittest -v test_authentification test_creation_contrat_credit_auto