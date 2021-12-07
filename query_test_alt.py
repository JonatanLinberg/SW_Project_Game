from SPARQLWrapper import SPARQLWrapper, JSON

queries = ["""
SELECT DISTINCT ?n ?b ?d ?blat ?blong WHERE {
?p a dbo:Person.
?p foaf:name ?n.
?p dbo:birthYear ?b.
?p dbo:deathYear ?d.
?p dbo:birthPlace ?c.
?c geo:lat ?blat.
?c geo:long ?blong.
} LIMIT 10
""",
"""
SELECT DISTINCT ?Concept WHERE {[] a ?Concept. } LIMIT 10
"""]

endpts = ['https://dbpedia.org/sparql', 'https://query.wikidata.org/sparql']

res = []

for i in range(len(queries)):
	conn = SPARQLWrapper(endpts[i])
	conn.setQuery(queries[i])
	conn.setReturnFormat(JSON)
	try:
		res.append(conn.query().convert())
	except Exception as e: 
		print(e)


for r in res[0]['results']['bindings']:
	print("%s, born %s, died %s\t\t%f:%f" % (r['n']['value'], r['b']['value'], r['d']['value'], float(r['blong']['value']), float(r['blat']['value'])))

for r in res:
	print("#######################################\n\n#######################################")
	print(r)