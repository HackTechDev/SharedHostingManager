#!/usr/bin/python3
# -*-coding:Utf-8 -*-

import sys
sys.path.append('./packages')
import Password

nbrAccounts = 0
while nbrAccounts <= 0 :
    nbrAccounts = input("Combien de comptes souhaitez-vous ajouter (> à 0) ? ")
    nbrAccounts = int(nbrAccounts)

# On lance la création des comptes

# Generate an encoded password
newPassword = Password.Password()
password = newPassword.generateRandomPassword(6)
encodedPassword = newPassword.generateEncodedPassword(password)

# On lance la création de la BDD

# On lance la création du virtualhost

# On envoi les informations des comptes par email
