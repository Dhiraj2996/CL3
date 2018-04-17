import json


def is_attacked(board,r,c):
	for i in range(r):
		if board[i][c]==1:
			return True
	i=r-1
	j=c-1
	while ((i>=0) and (j>=0)):
		if board[i][j]==1:
			return True
		i-=1
		j-=1
	i=r-1
	j=c+1
	while ((i>=0) and (j<=7)):
		if board[i][j]==1:
			return True
		i-=1
		j+=1
	return False


def solve(board,r):
	i=0
	while i < 8:
		if(not is_attacked(board,r,i)):
			board[r][i]=1
			if(r==7):
				return True
			else:
				if(solve(board,r+1)):
					return True
				else:
					board[r][i]=0
		i+=1
	if(i==8):
		return False
		

def printboard(board):
	for i in range(8):
		for j in range(8):
			if(board[i][j]==0):
				print ". ",
			else:
				print str(board[i][j])+" ",
		print ""
	print ""


BOARD_SIZE=8
board=[[0 for x in range(8)]for x in range(8)]

if __name__=='__main__':
	data=[]
	with open("index.json") as f:
		data=json.load(f)

	print data["start"]

	if (data["start"] < 0 or data["start"] > 7):
		print "Invalid Configuration!"
		exit()
	
	board[0][data["start"]]=1
	
	if(solve(board,1)):
		print "Queens Problem Solved"
		print "Board Configuration::"
		printboard(board)
	else:
		print "Queens Problem not Solved"
