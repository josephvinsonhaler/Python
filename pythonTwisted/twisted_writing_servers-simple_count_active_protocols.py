import twisted

# the connectionMade event is usually where setip of the connection object happens, as well
# 	as  any initial greetings (as in the QOTD protocol above, which is actually based on RFC865)
# the connectionLost event is where tearing down of any connection-specific object is done

from twisted.internet.protocol import Protocol

class Echo(Protocol):

	def __init__(self, factory):
		self.factory = factory

	def connectionMade(self):
		self.factory.numProtocols = self.factory.numProtocols + 1
		self.transport.write(
			'Welcome! There are currently %d open connections. \n' % 
			(self.factoy.numProtocols,))

	def connectionLost(self, reason):
		self.factory.numProtocols = self.factory.numProtocols - 1

	def dataReceived(self, data):
		self.transport.write(data)
