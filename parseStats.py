import csv
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "1598753"))
session = driver.session()

def crawlStats(id):
	stats = {}
	ev = []
	with open('pokemon_stats.csv', newline='') as csvfile:
		stat_reader = csv.reader(csvfile, delimiter=',')
		for row in stat_reader:
			if row[0] == id:
				stats[row[1]] = int(row[2])
				if row[3] != "0":
					ev += [{"stat": int(row[1]), "effort": int(row[3])}]
	return stats, ev

session = driver.session()
session.run("CREATE (s_1:Stat {id_stat: 1, name: 'hp'})")
session.run("CREATE (s_2:Stat {id_stat: 2, name: 'ataque'})")
session.run("CREATE (s_3:Stat {id_stat: 3, name: 'defensa'})")
session.run("CREATE (s_4:Stat {id_stat: 4, name: 'at_especial'})")
session.run("CREATE (s_5:Stat {id_stat: 5, name: 'def_especial'})")
session.run("CREATE (s_6:Stat {id_stat: 6, name: 'velocidad'})")
session.close()

with open('pokemon_stats.csv', newline='') as csvfile:
		stat_reader = csv.reader(csvfile, delimiter=',')
		for row in stat_reader:
			if row[0] == id:
				session = driver.session()
				session.run("""
					MERGE (p_%s {id: %s})
					MERGE (s_%s:Stat {id_stat: %s})
					CREATE UNIQUE (p_%s)-[:PRIMAL]->(r_%s)
				""" % (row[10], row[10], row[0], row[0], row[10], row[0]))
				if row[3] != "0":
					ev += [{"stat": int(row[1]), "effort": int(row[3])}]
				session.close()
	return stats, ev