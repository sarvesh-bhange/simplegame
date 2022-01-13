class hitbox(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width

	def get_rect(self):
		return (self.x,self.y,self.width,self.height)

	def update(self,x,y,width,height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width