import twisted


# SSL can use the same code as TCP







from twisted.internet.protocol import Protocol

# this protocol will write back whatever is written to it
# it does not respond to all events
class Echo(Protocol):
	def dataRecieved(self, data):
		self.transport.write(data)




