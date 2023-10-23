Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nom = 'SCHUWER'
>>> prénom = 'Esteban'
>>> math = 13.5
>>> anglais = 11.2
>>> info = 12.7
>>> promotion = 2023
>>> moy = (math + anglais + info) /3
>>> type(nom)
<class 'str'>
>>> type(prénom)
<class 'str'>
>>> type(math)
<class 'float'>
>>> type(anglais)
<class 'float'>
>>> type(info)
<class 'float'>
>>> type(promotion)
<class 'int'>
>>> type(moy)
<class 'float'>
>>> moy
12.466666666666667
>>> print = f"L'étudiant {nom_etudiant} de la promotion {promotion} a une moyenne de {moyenne:.1f}"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print = f"L'étudiant {nom_etudiant} de la promotion {promotion} a une moyenne de {moyenne:.1f}"
NameError: name 'nom_etudiant' is not defined
>>> print = f"L'étudiant {nom , prénom} de la promotion {promotion} a une moyenne de {moyenne:.1f}"
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print = f"L'étudiant {nom , prénom} de la promotion {promotion} a une moyenne de {moyenne:.1f}"
NameError: name 'moyenne' is not defined
>>> 
>>> print(f"L'étudiant {nom , prénom} de la promotion {promotion} a une moyenne de {moyenne:.1f}")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(f"L'étudiant {nom , prénom} de la promotion {promotion} a une moyenne de {moyenne:.1f}")
NameError: name 'moyenne' is not defined
>>> print(f"L'étudiant {nom , prénom} de la promotion {promotion} a une moyenne de {moy:.1f}")
L'étudiant ('SCHUWER', 'Esteban') de la promotion 2023 a une moyenne de 12.5
>>> # Déclaration des variables
... jour = 15  # Exemple : jour du mois
... heure = 10  # Exemple : heure de la journée (entre 0 et 23)
... minute = 30  # Exemple : minute de l'heure (entre 0 et 59)
... 
... # Calcul du nombre de minutes écoulées depuis le début du mois
... minutes_du_jour = jour * 24 * 60  # Nombre de minutes dans un jour
... minutes_de_l_heure = heure * 60  # Nombre de minutes dans une heure
... total_minutes = minutes_du_jour + minutes_de_l_heure + minute
... 
... # Affichage du résultat
... print(f"Nombre de minutes écoulées depuis le début du mois : {total_minutes} minutes")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> jour = 15
>>> jour = 23
>>> heure = 14
>>> minute = 30
