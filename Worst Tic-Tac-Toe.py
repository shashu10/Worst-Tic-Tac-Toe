# User is X. Computer is O. Create a new instance and call start()
class TicTacToe:

	# Setup the maze and welcome the user
	def __init__(self, size = 3):
		self.SIZE = size
		self.maze = [[" " for i in range(size)] for i in range(size)]
		
		self.printMaze([[1,4,7],[2,5,8],[3,6,9]])
		print "Type your move with numbers as shown in the grid"

		self.run(size)

	def printMaze(self, maze = None):
		if not maze:
			maze = self.maze
		for i in range(self.SIZE):
			row = []
			for j in range(self.SIZE):
				row = row + [str(maze[j][i])]
			print '|'.join(row)

	def userDidWin(self, player):
		return self.isStraightWin(player, horizontal = False) or self.isStraightWin(player, horizontal = True) or self.isDiagonalWin(player, opposite = False) or self.isDiagonalWin(player, opposite = True)

	def isStraightWin(self, player, horizontal):
		for j in range(self.SIZE):
			count = 0
			for i in range(self.SIZE):
				currentValue = self.maze[j][i] if horizontal else self.maze[i][j]
				if currentValue == player:
					count += 1
			if count == self.SIZE:
				return True
		return False

	# TODO opposite diag
	def isDiagonalWin(self, player, opposite, count = 0):
		primaryAxis = range(self.SIZE - 1, -1, -1) if opposite else range(self.SIZE)
		for i, j in zip(primaryAxis, range(self.SIZE)):
			if self.maze[i][j] == player:
				count += 1
		return count == self.SIZE

	def cannotMakeMove(self, l):
		l = l - 1
		return self.maze[l % self.SIZE][l / self.SIZE] != " "

	def setValueAtLocation(self, l, v):
		l = l - 1
		self.maze[l % self.SIZE][l / self.SIZE] = v

	def isLastMove(self, maze):
		count = 0
		for i in range(self.SIZE):	
			for j in range(self.SIZE):
				if maze[i][j] == " ":
					count += 1
		return count == 0

	def makeCounterMove(self, maze):
		for i in range(self.SIZE):
			for j in range(self.SIZE):
				if maze[i][j] != " ":
					continue
				maze[i][j] = "O"
				didPlay = True
				if self.userDidWin("O"):
					possibleMove = (i, j)
					didPlay = False
					maze[i][j] = " "
				else:
					return
		if not didPlay:
			if possibleMove:
				maze[possibleMove[0]][possibleMove[1]] = "O"

	def run(self, size = 3):

		# Continuously ask for input until user cancels
		while True:
			print "Enter a number:"

			# Validate Move
			try:
				move = int(raw_input())
			except Exception, e:
				print "Didn't understand that. Type 0 to cancel or type a number from 1 - 9"
				continue
			if move == 0:
				break
			if move > (self.SIZE * self.SIZE) or move < 1:
				print "Type a number from 1 - 9"
				continue
			if self.cannotMakeMove(move):
				print "You cannot move there"
				continue

			# User's Move
			self.setValueAtLocation(move, "X")
			if self.userDidWin("X"):
				self.printMaze()
				print "I lost :("
				break
			
			# Computer's Move
			self.makeCounterMove(self.maze)
			if self.userDidWin("O"):
				self.printMaze()
				print "Haha you suck!"
				break

			self.printMaze()

			if self.isLastMove(self.maze):
				print "Draw :("

		print "Thanks for playing"

# Initializes and runs the default tic tac toe game
ttc = TicTacToe()

