class Graph:
	def __init__(self, flights):
		self.airports = []
		self.graph = {}
		for depart, destin in flights:
			self.addAirport(depart, destin)
			# self.addFlights(flight)

	def addAirport(self, depart, destin):
		if depart not in self.graph:
			self.airports.append(depart)
			self.graph[depart] = []
		if destin not in self.graph:
			self.airports.append(destin)
		self.graph[depart].append(destin)

	def printFlights(self):
		for flight in self.graph:
			print(flight, ":", self.graph[flight])
			print()
# class Airport:
# 	def __init__(self, airport):
# 		self.airport = airport


flights = [['Newark, NJ', 'Los Angeles, CA'],
			['Miami, FL', 'Los Angeles, CA'],
			['Fort Laud, FL', 'Newark, CA'],
			['New Orleans, LA', 'JFK, NY'],
			['JFK, NY', 'Dallas, TX'],
			['Minnestoa, MI', 'Newark, NJ'],
			['Houston, TX', 'Fort Laud, FL'],
			['Houston, TX', 'Miami, FL'],
			['Las Vegas, NV', 'San Fran, CA'],
			['San Fran, CA', 'Miami, FL']]

myFlights = Graph(flights)
# print(myFlights.graph)
myFlights.printFlights()

# ------------------------------------