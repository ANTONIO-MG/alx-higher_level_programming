#!/usr/bin/python3
"""
Square is a grnadchill class that inherits from rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
	"""
	class with attributes of a squere, they inherits all it's properties from rectangle
	and has one combined size 
	"""

	def __init__(self, size, x=0, y=0, id=None):
		"""
		the initialization of teh sqare class, is initialized by the super class with
		the size attributes as the width and the height and also the X, Y and the id attributes 
		"""
	   	super().__init__(size, size, x, y, id)

	def __str__(self):
		"""
		the string representation of the square class
		"""
		return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x, self.y, self.width)

	@property
	def size(self):
		"""
		returns the size of the square
		"""
		return self.width

	@size.setter
	def size(self, value):
		"""
		sets the value of the size private attribute
		"""
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		"""
		updates the values of the attributes 
		"""
		argc = len(args)
		kwargc = len(kwargs)
		modif_attrs = ['id', 'size', 'x', 'y']

		if argc > 4:
			argc = 4

		if argc > 0:
			for i in range(argc):
				setattr(self, modif_attrs[i], args[i])
		elif kwargc > 0:
			for k, v in kwargs.items():
				if k in modif_attrs:
					setattr(self, k, v)

		def to_dictionary(self):
			"""
			takes the attribvutes and converst them into dictionaries
			"""
			return {
				'id': self.id,
				'size': self.size,
				'x': self.x,
				'y': self.y
				}

