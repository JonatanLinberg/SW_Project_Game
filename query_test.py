from stardog import Connection as SDConn

query = """select distinct ?n ?b ?d ?blat ?blong where {
?p a dbo:Person.
?p foaf:name ?n.
?p dbo:birthYear ?b.
?p dbo:deathYear ?d.
?p dbo:birthPlace ?c.
?c geo:lat ?blat.
?c geo:long ?blong.
}"""

q2 = """
SELECT DISTINCT ?Concept WHERE {[] a ?Concept. } LIMIT 10
"""

with SDConn('sparql', endpoint='https://dbpedia.org/') as conn:
	res = conn.select(query)

with SDConn('sparql', endpoint='https://query.wikidata.org/') as conn:
	res2 = conn.select(q2)

print(res2)
quit()

for r in res['results']['bindings']:
	print("%s, born %s, died %s\t\t%f:%f" % (r['n']['value'], r['b']['value'], r['d']['value'], float(r['blong']['value']), float(r['blat']['value'])))
