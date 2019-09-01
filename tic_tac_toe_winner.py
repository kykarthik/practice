
class Tic(object):
	game = [[11, 12, 13],
			[14, 15, 16],
			[17, 18, 19]]
	matrix_len = len(game[0])
	diagonal = 0

	def __init__(self):
		self.stop = False

	def winner_check(self):
		for i in range(self.matrix_len):
			count = 0
			for j in range(self.matrix_len):
				if j+1 == self.matrix_len:
					break
				elif self.game[i][j] == self.game[i][j+1]:
					count = count + 1
					if count == self.matrix_len - 1:
						print("player %d wins from row %d " %(self.game[i][j], i+1))
						self.stop = True
						break
				else:
					pass

		for i in range(self.matrix_len):
			count = 0
			for j in range(self.matrix_len):
				if j+1 == self.matrix_len:
					break
				elif self.game[j][i] == self.game[j+1][i]:
					count = count + 1
					if count == self.matrix_len - 1:
						print("player %d wins from column %d " %(self.game[j][i] , i+1))
						self.stop = True
						break
				else:
					pass

		for i in range(self.matrix_len):
			if i+1 == self.matrix_len:
				break
			elif self.game[i][i] == self.game[i+1][i+1]:
				self.diagonal = self.diagonal + 1
				if self.diagonal == self.matrix_len:
					print("Player %d wins from right diagonal " %self.game[i][i])
					self.stop = True
					break
		for i in range(self.matrix_len):
			if i+1 == self.matrix_len:
				break
			elif self.game[i][self.matrix_len-i-1] == self.game[i + 1][self.matrix_len-i-2]:
				self.diagonal = self.diagonal + 1
				if self.diagonal == self.matrix_len:
					print("Player %d wins from left diagonal " %self.game[0][self.matrix_len-1])
					self.stop = True
					break
			else:
				pass

	def start(self):
		k = 1
		while self.stop == False:
			if k == (self.matrix_len*self.matrix_len) + 1:
				print("No winner")
				quit()
			values = input("Enter the row and col value between 0 and 2 separated by a comma: ")
			row, col = values.split(',')
			row = int(row)
			col = int(col)
			if self.game[row][col] == 1 or self.game[row][col] == 2:
				print("The co-ordinates are already taken please select any other co-ordinates")
				continue
			else:
				if k % 2 != 0:
					self.game[row][col] = 1
					k = k + 1
					self.winner_check()
				else:
					self.game[row][col] = 2
					k = k + 1
					self.winner_check()

if __name__ == '__main__':
	tic = Tic()
	tic.start()

	