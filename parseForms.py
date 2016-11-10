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
			print("form_id: " + row[0])
			session.run("CREATE (f_%s:Form {id:%s, name:'%s', form:'%s'})" % (row[0], row[0], name, row[2]))
			session.close()
		elif row[7] == "1":
			session = driver.session()
			print("mega_id: " + row[0])
			session.run("CREATE (m_%s:Mega {id:%s, name:'%s'})" % (row[0], row[0], name))
			session.close()
		else:
			session = driver.session()
			print("primal_id: " + row[0])
			session.run("CREATE (r_%s:Primal {id:%s, name:'%s'})" % (row[0], row[0], name))
			session.close()