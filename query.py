from SPARQLWrapper import SPARQLWrapper, JSON
from random import randrange
import person

def make_wd_query(URIs):
	query = "SELECT ?uri ?img WHERE { \n"
	for URI in URIs[:-1]:
		query += "{ <%s> wdt:P18 ?img.\nBIND(<%s> AS ?uri) } UNION\n" % (URI, URI)
	query += "{ <%s> wdt:P18 ?img.\nBIND(<%s> AS ?uri) } }" % (URIs[-1], URIs[-1])
	return query

def query(endpoint, query, timeout=0):
	conn = SPARQLWrapper(endpoint)
	conn.setQuery(query)
	if (timeout != 0):
		conn.setTimeout(timeout)
	conn.setReturnFormat(JSON)
	return conn.query().convert()

def find_images_for(persons):
	e = 'https://query.wikidata.org/sparql'
	results = query(e, make_wd_query([p.wd_uri for p in persons]))
	for res in results['results']['bindings']:
		for i in range(len(persons)):
			if (persons[i].wd_uri == res['uri']['value']):
				persons[i].setImage(res['img']['value'])
	return persons


def get_dbpedia_persons(n=40):
	o = randrange(9000)

	q = """
	SELECT DISTINCT ?wd ?n ?b ?d WHERE {
	?p a dbo:Person.
	?p owl:sameAs ?wd.
	?p foaf:name ?n.
	?p dbo:birthYear ?b.
	?p dbo:deathYear ?d.
	FILTER (?b < "2000-01-01"^^xsd:date)
	FILTER (?p != dbr:Al-Damiri)
	FILTER regex(?wd, "wikidata")
	} ORDER BY RAND() OFFSET %d LIMIT %d
	""" % (o, n)

	e = 'https://dbpedia.org/sparql'

	result = query(e, q)
	return [person.Person(r['n']['value'], r['b']['value'], r['d']['value'], wd_uri=r['wd']['value']) for r in result['results']['bindings']]


if (__name__ == "__main__"):
	print("Querying 5 people from DBPedia...")
	persons = get_dbpedia_persons(n=5)
	for p in persons:
		print(p)
	print("Looking for their photos...")
	for p in find_images_for(persons):
		print(p.image)
	