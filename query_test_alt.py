from SPARQLWrapper import SPARQLWrapper, JSON


def make_query(name):
	return """SELECT ?img WHERE {
	?person wdt:P31 wd:Q5;
			wdt:P18 ?img.
	SERVICE wikibase:label {
    	bd:serviceParam wikibase:language "en" .
   	}
   	} LIMIT 1
   	"""



q = """
SELECT DISTINCT ?n ?b ?d ?blat ?blong WHERE {
?p a dbo:Person.
?p foaf:name ?n.
?p dbo:birthYear ?b.
?p dbo:deathYear ?d.
?p dbo:birthPlace ?c.
?c geo:lat ?blat.
?c geo:long ?blong.
FILTER (?b < "2000-01-01"^^xsd:date)
} GROUP BY ?p LIMIT 20
"""

e = ['https://dbpedia.org/sparql', 'https://query.wikidata.org/sparql']

conn = SPARQLWrapper(e[0])
conn.setQuery(q)
conn.setReturnFormat(JSON)
try:
	res = (conn.query().convert())
except Exception as err: 
	print(err)

print(len(res['results']['bindings']))

for r in res['results']['bindings']:
	print("%s, born %s, died %s\t\t%f:%f" % (r['n']['value'], r['b']['value'], r['d']['value'], float(r['blong']['value']), float(r['blat']['value'])))

	conn = SPARQLWrapper(e[1])
	conn.setQuery(make_query(r['n']['value']))
	conn.setReturnFormat(JSON)
	try:
		res = (conn.query().convert())
	except Exception as err: 
		print(err)

	print(res['results']['bindings'][0]['img']['value'])