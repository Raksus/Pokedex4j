import csv

def searchPokemonById(id):
	with open('pokemon_forms.csv', newline='') as csvforms:
		forms_reader = csv.reader(csvforms, delimiter=',')
		for row in forms_reader:
			if row[3] == id:
				return row[0]




with open('pokemon_forms_stats.csv', newline='') as csvfile:
	stat_reader = csv.reader(csvfile, delimiter=',')
	rows = []
	for row in stat_reader:
		#print(row)
		pokemon_real_id = searchPokemonById(row[0])
		#print(pokemon_real_id)
		row.append(pokemon_real_id)
		#print(row)
		rows.append(row)
	for row in rows:
		print(row)