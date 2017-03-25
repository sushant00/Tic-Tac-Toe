# Tic-Tac-Toe Bot

from random import choice

mark=["X","O","X"]

def playermark():
	"""Takes the input for players letter and return a tuple of player and computer's letter """

	mark=""
	while (mark!="X" and mark!="O"):
		print("Please choose among 'X' or 'O':")
		mark=input().upper()
	if mark=='X':
		return ("X","O")
	else:	
		return ("O","X")





def firstturn():
	"""Decide the first turn based on user input y/n """

	letter=""
	while (letter!="Y" and letter!="N"):
		print("Do you want to go first ? :(Y/n)")
		letter=input().upper() 
	if letter=='Y':
		return "you"
	else:	
		return "com"

def won(board,mark):
	"""based on the board and the mark of player, check if player won and return True/False resp."""
	wincase=[[9,5,1],[7,5,3],[9,6,3],[8,5,2],[7,4,1],[1,2,3],[4,5,6],[7,8,9]]
	for i in wincase:
		sum=0
		for k in i:
			if board[k]==mark:
				sum+=1
		if sum==3:
			return True
	return False


def again():
	"""return True/False based on user's need to play or not"""
	letter=""
	while (letter!="Y" and letter!="N"):
		print("Do you want to Play Again ? :(Y/n)")
		letter=input().upper() 
	if letter=='Y':
		return True
	else:	
		return False


def moveit(board,mark,move):
	board[move]=mark


def checkspace(board,move):
	return board[move]==" "



def youmove(board):
	move=0
	while (move not in range(1,10)) or not (checkspace(board,move)):
		print("Take your move : integer 1 to 9")
		move=int(input())
	return move


def selectmove(board,mlist):
	trys=[]
	for i in mlist:
		if checkspace(board,i):
			trys.append(i)
	if len(trys)>0:
		return choice(trys)
	else:
		return None


def commove(board,commark):
	playermark=mark[mark.index(commark)+1]
	for i in range(1,10):
		checkboard=list(board)
		if checkspace(checkboard,i):
			moveit(checkboard,commark,i)
			if won(checkboard,commark):
				return i

	for i in range(1,10):
		checkboard=list(board)
		if checkspace(checkboard,i):
			moveit(checkboard,playermark,i)
			if won(checkboard,playermark):
				return i
	if checkspace(board, 5):
		return 5
	if (board[1]==mark[mark.index(commark)+1] and board[5]==commark and board[9]==mark[mark.index(commark)+1]) or (board[1]==mark[mark.index(commark)+1] and board[5]==commark and board[9]==mark[mark.index(commark)+1]):
		return selectmove(board, [2, 4, 6, 8])
	move = selectmove(board, [1, 3, 7, 9])
	if move != None:
		return move
	return selectmove(board, [2, 4, 6, 8])


def boardfull(board):
	for i in range(1,10):
		if checkspace(board,i):
			return False
	return True


def showboard(board):
	"""Draw the board with current positions, takes a list of 10 strings(marks) """	
	print()
	print()
	print('                           |       |')
	print('                       ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3])
	print('                           |       |')
	print('                    -----------------------')
	print('                           |       |')
	print('                       ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6])
	print('                           |       |')
	print('                    -----------------------')
	print('                           |       |')
	print('                       ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9])
	print('                           |       |')
	print()
	print()


if __name__=='__main__':
	print("Let's play Tic-Tac-Toe!!! (indexes for marking are similar to your dialpad (1-9))")
	tplayermark,commark=playermark()
	while True:
		board=[" "]*10
		turn=firstturn()
		print(turn+" will go first:")
		play=True
		while play:
			if turn=="you":
				showboard(board)
				move=youmove(board)
				moveit(board,tplayermark,move)
				if won(board,tplayermark):
					showboard(board)
					print("Yaeeehhh! you won")
					play=False
				else:
					if boardfull(board):
						showboard(board)
						print("It's a tie")
						break
					else:
						turn="com"
			else:
				move=commove(board,commark)
				moveit(board,commark,move)
				if won(board,commark):
					showboard(board)
					print("hola!!! com wins")
					play=False
				else:
					if boardfull(board):
						showboard(board)
						print("It's a tie")
						break
					else:
						turn="you"
		if not(again()) :
			break
			



	
