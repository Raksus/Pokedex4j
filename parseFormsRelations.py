import csv
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "1598753"))
session = driver.session()

with open('pokemon_forms.csv', newline='') as csvfile:
	csvfile.readline()
	poke_reader = csv.reader(csvfile, delimiter=',')
	for row in poke_reader:
		name = row[1].split("-")[0]
		if row[7] == "0":
			session = driver.session()
			print("relacion_forma: " + row[0])
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (f_%s:Form {id: %s})
				CREATE UNIQUE (p_%s)-[:FORMA]->(f_%s)
				""" % (row[10], row[10], row[0], row[0], row[10], row[0]))
			session.close()
		elif row[7] == "1":
			session = driver.session()
			print("relacion_mega: " + row[0])
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (m_%s:Mega {id: %s})
				CREATE UNIQUE (p_%s)-[:MEGA]->(m_%s)
				""" % (row[10], row[10], row[0], row[0], row[10], row[0]))
			session.close()
		else:
			session = driver.session()
			print("relacion_primal: " + row[0])
			session.run("""
				MERGE (p_%s:Pokemon {id: %s})
				MERGE (r_%s:Primal {id: %s})
				CREATE UNIQUE (p_%s)-[:PRIMAL]->(r_%s)
				""" % (row[10], row[10], row[0], row[0], row[10], row[0]))
			session.close()