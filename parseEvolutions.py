import csv
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "1598753"))
session = driver.session()

with open('pokemon_evolution.csv', newline='') as csvfile:
	csvfile.readline()
	poke_reader = csv.reader(csvfile, delimiter=',')
	for row in poke_reader:
		if row[2] == "1":
			session = driver.session()
			relation = "EVOLUTION {{trigger: '{trigger}' ,lvl: {nivel} {gender} {location} {item} {time_of_day} {move_id} {move_type} {relative_physical_stats} {party_type_id} {rain} {upside_down} }}"
			gender = ",gender: %s" % row[5] if row[5] != "" else ""
			location = ",location: %s" % row[6] if row[6] != "" else ""
			item = ",item: %s" % row[7] if row[7] != "" else ""
			time_of_day = ",time_of_day: '%s'" % row[8] if row[8] != "" else ""
			move_id = ",move_id: %s" % row[9] if row[9] != "" else ""
			move_type = ",move_type: %s" % row[10] if row[10] != "" else ""
			relative_physical_stats = ",relative_physical_stats: %s" % row[14] if row[14] != "" else ""
			party_type_id = ",party_type_id: %s" % row[16] if row[16] != "" else ""
			rain = ",rain: %s" % row[18] if row[18] != "0" else ""
			upside_down = ",upside_down: %s" % row[19] if row[19] != "0" else ""
			relation = relation.format(trigger="nivel", nivel=row[4], gender=gender, location=location, item=item, time_of_day=time_of_day, move_id=move_id, move_type=move_type, relative_physical_stats=relative_physical_stats, party_type_id=party_type_id, rain=rain, upside_down=upside_down)
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:%s]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], relation, row[1]))
			session.close()
		elif row[2] == "2":
			session = driver.session()
			relation = "EVOLUTION {{trigger: '{trigger}' {item} {con_pokemon}}}"
			con_pokemon = ",con_pokemon: %s" % row[17] if row[17] != "" else ""
			item = ",item: %s" % row[7] if row[7] != "" else ""
			relation = relation.format(trigger="intercambio", item=item, con_pokemon=con_pokemon)
			print(relation)
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:%s]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], relation, row[1]))
			session.close()
		elif row[2] == "3":
			session = driver.session()
			print("relacion_evolucion: " + row[0])
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:EVOLUTION {trigger: '%s', obj_id: %s}]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], "objeto", row[3], row[1]))
			session.close()
		elif row[2] == "4":
			session = driver.session()
			print("relacion_evolucion: " + row[0])
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:EVOLUTION {trigger: '%s'}]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], "hueco_en_el_equipo", row[1]))
			session.close()
		elif row[2] == "5": # Felicidad
			session = driver.session()
			relation = "EVOLUTION {{trigger: '{trigger}' {time_of_day} {happiness} }}"
			happiness = ",happiness: %s" % row[11] if row[11] != "" else ""
			time_of_day = ",time_of_day: '%s'" % row[8] if row[8] != "" else ""
			relation = relation.format(trigger="afecto", happiness=happiness, time_of_day=time_of_day)
			print(relation)
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:%s]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], relation, row[1]))
			session.close()
		elif row[2] == "6": # Belleza
			session = driver.session()
			relation = "EVOLUTION {{trigger: '{trigger}' {beauty} }}"
			beauty = ",beauty: %s" % row[12] if row[12] != "" else ""
			relation = relation.format(trigger="belleza", beauty=beauty)
			print(relation)
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:%s]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], relation, row[1]))
			session.close()
		elif row[2] == "7": # Afecto
			session = driver.session()
			relation = "EVOLUTION {{trigger: '{trigger}' {move_type} {affection} }}"
			move_type = ",move_type: %s" % row[10] if row[10] != "" else ""
			affection = ",affection: %s" % row[13] if row[13] != "" else ""
			relation = relation.format(trigger="afecto", move_type=move_type, affection=affection)
			print(relation)
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:%s]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], relation, row[1]))
		elif row[2] == "8": # 1 lvl
			session = driver.session()
			relation = "EVOLUTION {{trigger: '{trigger}' {item} {time_of_day} {move_id} {party_poke_id} {location}}}"
			item = ",item: %s" % row[7] if row[7] != "" else ""
			time_of_day = ",time_of_day: '%s'" % row[8] if row[8] != "" else ""
			move_id = ",move_id: %s" % row[9] if row[9] != "" else ""
			party_poke_id = ",party_poke_id: %s" % row[15] if row[15] != "" else ""
			location = ",location: %s" % row[6] if row[6] != "" else ""
			relation = relation.format(trigger="lvling", item=item, time_of_day=time_of_day, move_id=move_id, party_poke_id=party_poke_id, location=location)
			print(relation)
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (p_%s:Pokemon {id: %s})
				CREATE UNIQUE (p_%s)-[:%s]->(p_%s)
				""" % (row[0], row[0], row[1], row[1], row[0], relation, row[1]))