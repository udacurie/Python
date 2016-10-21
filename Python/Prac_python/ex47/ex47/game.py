
class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {} #not [] as written in lpthw as it's a dict not a list
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		return self.paths.update(paths)