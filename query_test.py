from stardog import Connection as SDConn

query = """select distinct ?n ?b ?d ?lat ?long where {
?p a dbo:Person.
?p foaf:name ?n.
?p dbo:birthYear ?b.
?p dbo:deathYear ?d.
?p dbo:birthPlace ?c.
?c geo:lat ?lat.
?c geo:long ?long.
}"""

with SDConn('sparql', endpoint='https://dbpedia.org/') as conn:
	res = conn.select(query)

for r in res['results']['bindings']:
	print("%s, born %s, died %s\t\t%f:%f" % (r['n']['value'], r['b']['value'], r['d']['value'], float(r['long']['value']), float(r['lat']['value'])))
