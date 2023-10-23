jour = 23
heure = 14
minute = 30
minute_du_jour = jour * 24 * 60
minute_de_l_heure = heure * 60
total_minute = minute_du_jour + minute_de_l_heure + minute
print(f"Nombre de minutes écoulées depuis le début du mois : {total_minute} minutes")