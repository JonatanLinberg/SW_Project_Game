class Point():
	def __init__(self, lon, lat):
		self.long = lon
		self.lat = lat

	def __str__(self):
		return "%s\u00b0N %s\u00b0E." % (self.long, self.lat)

class Person():
	def __init__(self, name, byear, dyear, img_url, blong, blat):
		self.name = name
		self.byear = int(byear)
		self.dyear = int(dyear)
		self.img_url = img_url
		self.bcoord = Point(float(blong), float(blat))

	def __str__(self):
		return "%s %d-%d" % (self.name, self.byear, self.dyear)

def _get_example():
	return Person("Jonatan Linberg", "1998", "2098", "https://scontent-arn2-1.xx.fbcdn.net/v/t1.18169-9/12274332_929685350448462_8506403662972366596_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=Wg30YHeUNhgAX-_IQIo&_nc_ht=scontent-arn2-1.xx&oh=c4bb686eebdcc020999953c8ebc22c6d&oe=61D25DD5", "13.533334", "59.383335")

if (__name__ == "__main__"):
	p = _get_example()
	print("%s was born %s at %s" % (p.name, p.byear, p.bcoord))