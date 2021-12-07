from SPARQLWrapper import SPARQLWrapper

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

endpts = ['https://dbpedia.org/', 'https://www.wikidata.org/sparql/']

res = []

for i in range(len(queries)):
	conn = SPARQLWrapper(endpts[i])
	conn.setQuery(queries[i])
	try:
		res.append(conn.query())
	except Exception as e: 
		print(e)