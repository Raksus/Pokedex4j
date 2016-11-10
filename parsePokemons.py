import csv
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "1598753"))
session = driver.session()

with open('pokemon.csv', newline='') as csvfile:
	poke_reader = csv.reader(csvfile, delimiter=',')
	for row in poke_reader:
		if row[7] == "1":
			session = driver.session()
			print("pokemon_id: " + row[0])
			session.run("CREATE (p_%s:Pokemon {id:%s, name:'%s', height:%s, weight:%s, base_experience:%s})" % (row[0], row[0], row[1], row[3], row[4], row[5]))
			session.close()
