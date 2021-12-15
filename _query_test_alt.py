from SPARQLWrapper import SPARQLWrapper, JSON
from random import randrange

def make_wd_query(URIs):
	query = "SELECT ?uri ?img WHERE { \n"
	for URI in URIs[:-1]:
		query += "{ <%s> wdt:P18 ?img.\nBIND(<%s> AS ?uri) } UNION\n" % (URI, URI)
	query += "{ <%s> wdt:P18 ?img.\nBIND(<%s> AS ?uri) } }" % (URIs[-1], URIs[-1])
	return query


offset = randrange(9000)
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
} ORDER BY RAND() OFFSET %d LIMIT 20
""" % offset

e = ['https://dbpedia.org/sparql', 'https://query.wikidata.org/sparql']

conn = SPARQLWrapper(e[0])
conn.setQuery(q)
conn.setReturnFormat(JSON)
try:
	res = (conn.query().convert())
except Exception as err: 
	print(err, err.__class__)
	quit()

print(len(res['results']['bindings']))

conn = SPARQLWrapper(e[1])
# all wd URIs: 		[r['wd']['value'] for r in res['results']['bindings']]
q = make_wd_query([r['wd']['value'] for r in res['results']['bindings']])
print(q)
conn.setQuery(q)
conn.setReturnFormat(JSON)
res2 = (conn.query().convert())

print(len(res2['results']['bindings']))

for r in res['results']['bindings']:
	print("%s, %s-%s" % (r['n']['value'], r['b']['value'], r['d']['value']))
