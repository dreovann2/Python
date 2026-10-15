#Exercice 1 Code PIN
"""
#Ce script permet de demander un code PIN pour donner "l'accès au télephone" de Marc
mots_de_passe=int(4567)
mots= (int (input("Entrée le mots de passe:")))
if mots == mots_de_passe:
    print("code correct")

else:
    print("code incorrect")

#Exercice 2 Signe d'un nombre

#Ce code demande un nombre entier puis dit si c'est positif, nul ou negatif
a=int(input("Saisir un nombre entier :"))
if a>0:
    print("positif")
elif a==0:
    print("nul")
else:
    print("negatif")

#Exercice 3 Parité

#Ce programe demande un nopbre entier et dit si c'est pair ou impair
nombre=int(input("Saisir un nombre :"))
paire_ou_impair=(nombre % 2)    #ça calcule le reste du nombre pour voir sir c'est impair ou pair 
if paire_ou_impair == 0:
    print(nombre, "est Pair")
else:
    print(nombre, "est impair")

#Exercice 4 Age 

#Ce programe demande l'age de l'utilisateur et dit si c'est un enfant un ados ou un adulte 
Age=int(input("Saisir votre age :"))
if Age>=18: 
    print("A",Age,"ans, vous êtes un adulte.")
elif Age>=12:
    print("A",Age,"ans, vous êtes un adolescent.")
else:
    print("A",Age,"ans, vous êtes un enfant.")

#Exercice 4 Perte ou profit

#Ce code demande le prix de fabrication puis le prix de vente pour faire un calcule et dire si c'est du profit ou non
Prix_de_fabrication=float(input("Prix de fabrication :"))
Prix_de_vente=float(input("Prix de vente :"))
Profit=(Prix_de_vente - Prix_de_fabrication) 
if Profit>0:
    print("Profit")
elif Profit==0:
    print("Nul")
else:
    print("Negatif")

#Exercice 5 Maximum

#Ce programe demande a utilisateur de saisir 3 nombre et le code dira quel nombre est le plus grand 
A=float(input("Saisir le premier nombre :"))
B=float(input("Saisir le deuxieme nombre :"))
C=float(input("Saisir le troisieme nombre :"))
if A>B and A>C: #Si A est plus grand que les 2 autres nombre alors c'est lui le max pareil pour les autres 
    print("Le maximum est le premier nombre",A)
elif B>A and B>C:
     print("Le maximume est le deuxième nombre",B)
else:
        print("Lemaximum est le troisième nombre",C)

#Exercice 6 Triangle rectangle

#Ce programe prend les coté d'un triangle (du plus petit au plus grand) pour après les mettre au carré puis lancer le calcule pour voir si le plus grand coté au carré fesait la même taille que les deux autres coté au carrés
BC=float(input("Saisir le coté qui n'est pas le plus grand:")) 
AC=float(input("Saisir le deuxième coté qui n'est pas le plus grand:"))
AB=float(input("Saisir le coté le plus grand:"))
BC2= float(BC ** 2) #J'ai mis tous les coté au carré pour les calculer après
AC2= float(AC ** 2)
AB2= float(AB ** 2)
if AB2==BC2+AC2: #je vérifie si le coté le plus grand est égale au deux coté les plus petit pour savoir si c'est un triangle rectangle
    print ("Le triangle est rectangle")
else :
    print ("Le triangle est non rectangle")

#################################
### Exercice 7 Année bissextile
################################

#Ce programme demande a l'utilisateur de mettre une année puis dit si c'est bissextile ou non
Annee=int(input("Saisir l'année :"))
if Annee%4 == 0 and Annee%100 !=0:
    print("L'année est Bissextile")
else:
    print("L'année est non Bissextile")
"""
"""
#########################################
###Exercice 8 Société de transport
#########################################
#Ce programme demande l'age de l'utilisateur pour après appliqué une reduction ou non en fonction de sont age 

# Saisie des variables.
price = int(10)
age = int(input("Le prix de base, est de " +  str(price) + "€. Veuillez saisir votre age pour une reduction de prix : "))

# Définition du taux de reduction.
if age < 5:
    rate = 0
elif age < 16:
    rate = 50
elif age < 21:
    rate = 60
elif age < 51:
    rate = 100
else:
    rate = 90

# Définition du prix final.
total = price * (rate / 100)

# Affichage du résultat.
print('Votre réduction :', str(rate), "%")
print("Votre prix final est de :", total , "€.")
"""
"""
#Exercice 9 Voyage scolaire
#le programme ne marche pas 
nbr_eleve=int(input("Nombre d’élèves :"))
duree_du_voyage=int(input("Durée du voyage en jours :"))
nourriture=float(nbr_eleve*3.50)
voyage=int(110)
if nbr_eleve <= 25:
    if nbr_eleve<20:
        coût_du_voyage=float(nourriture*duree_du_voyage+(nbr_eleve*voyage)+(duree_du_voyage*4.20))
        print("Le prix du voyage revient à",coût_du_voyage,"euros à par élève.")
    else:
        coût_du_voyage=float(nourriture*duree_du_voyage+(nbr_eleve*voyage)+(duree_du_voyage*3.80))
        print("Le prix du voyage revient à",coût_du_voyage,"euros à par élève.")
elif nbr_eleve <=35:
    voyage-10
    coût_du_voyage=float(nourriture*duree_du_voyage+(nbr_eleve*voyage)+(duree_du_voyage*3.80))
    print("Le prix du voyage revient à",coût_du_voyage,"euros à par élève.")
else:
    voyage-10
    coût_du_voyage=float(nourriture*duree_du_voyage+(nbr_eleve*voyage)+(duree_du_voyage*4.00))
    print("Le prix du voyage revient à",coût_du_voyage,"euros à par élève.")
##################################
###Vinci location 
type_de_véhicule=input("Type du véhicule :")
type_de_carburant=input("Type du Carburant :")
Durée_du_voyage=input("Durrer du voyage :")
Distance_en_km=input("Distance en km :")
Offre_commerciale=input("Offre commerciale :")
#type du véhicule 
voiture=["Citadine","Berline","Sportive"]
if type_de_véhicule == voiture:
#Carburant
Carburant=["Essence","Diesel"]

#Durée de location en jour

#Distance en km

#offre commerciale

#Total
"""
######################################
###Voyage
########################################
"""
#Variable fixe"

nbr_days=int(input("please set who nbr days of the vacation : "))
nbr_students=int(input("please set who students in the vacation : "))
price_f= 3.50

#Calcule Transport

if nbr_students > 25:
    price_t = 100
else:
    price_t = 110

#Calcule Hebergement 

if nbr_students < 20:
    price_h = 4.20
elif nbr_students < 35:
    price_h = 3.80
else:
    price_h = 4.00

#Total du prix 

total= price_t + (price_f * nbr_days) + (price_h * nbr_days)
print("The price of the vacation is" ,total, "euros for one student")
"""
###################################################################
###Vinci Location
####################################################################

#Variable
vehicule=(input("Type du vehicule : "))
carburant=(input("Carburant : "))
jours=int(input("Durée de location en jour : "))
distance=int(input("Distance en km : "))
offre=bool(input("Offre commerciale : "))

#type de véhicule
if vehicule == "Citadine":
    location= 80 * jours
elif vehicule == "Berline":
    location= 100 * jours
elif vehicule == "Sportive":
    location= 130 * jours
else:
    print("Erreur les véhicule disponible sont Citadine,Berline,Sportive")

#Carburant
if carburant == "Essence":
    consomation = 1.93 * distance
elif carburant == "Diesel":
    consomation = 1.89 * distance
else:
    print("Erreur les carburant sont Essence,Diesel")

#Total
total = location + consomation

#Offre
if offre:
    total= 30+total*0.90

print("Le prix de la location est de" ,total, "euros.")
########################################################################
###
########################################################################
#15,50×10 et 10,50×10 