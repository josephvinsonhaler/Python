import twisted

from tiwsted.internet.protocol import Protocol



# this protocol responds to the initial connection with a well known qoute
# then it terminates the connecton
class QOTD(Protocol):

	def connectionMade(self):
		self.transport.write("An apple a day keeps the doctor away\r\n")
		self.transport.loseConnection()
