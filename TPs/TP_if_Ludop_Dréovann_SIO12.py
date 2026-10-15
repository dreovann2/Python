#Exercice 1 Code PIN

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

#Exercice 7 Année bissextile

#Ce programme demande a l'utilisateur de mettre une année puis dit si c'est bissextile ou non
Annee=int(input("Saisir l'année :"))
if Annee%4 == 0 and Annee%100 !=0:
    print("L'année est Bissextile")
else:
    print("L'année est non Bissextile")

#Exercice 8 Société de transport
#Ce programme demande l'age de l'utilisateur pour après appliqué une reduction ou non en fonction de sont age 

Age=int(input("Saisir votre Age:"))
Prix=int(10)
if Age<5:
    total = 0
elif Age<16:
    total = Prix*0.5
elif Age<21:
    total = Prix*0.6
elif Age<51:
    total = Prix
else:
    total = Prix*0.9
    
print("votre prix est de:",total,"€")

#Exercice 9 Voyage scolaire
#le programme ne marche pas 
nbr_eleve=int(input("Nombre d’élèves :"))
duree_du_voyage=int(input("Durée du voyage en jours :"))
eleves=float(117.50)
#Partie Transport
if nbr_eleve>=25:
    transport=eleves-10
elif nbr_eleve<20:
    hébergement=transport+0.20
elif nbr_eleve>=20:
    hébergement=transport-0.20
else:
    print("Le prix du voyage revient à",hébergement,"euros à par élève.")
