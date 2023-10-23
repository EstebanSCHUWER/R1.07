jour = int(input("Jour : "))
heure = int(input("Heure : "))
minute = int(input("Minute : "))
minute_du_jour = jour * 24 * 60
minute_de_l_heure = heure * 60
total_minute = minute_du_jour + minute_de_l_heure + minute
print(f"Nombre de minutes écoulées depuis le début du mois : {total_minute} minutes")