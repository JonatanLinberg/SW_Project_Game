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

with SDConn('sparql', endpoint='https://dbpedia.org/') as conn:
	res = conn.select(query)

for r in res['results']['bindings']:
	print("%s, born %s, died %s\t\t%f:%f" % (r['n']['value'], r['b']['value'], r['d']['value'], float(r['blong']['value']), float(r['blat']['value'])))
