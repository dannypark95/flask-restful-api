board = []

# create the board
for i in range(8):
  row = []
  for j in range(8):
    if (i + j) % 2 == 0:
      row.append("W")
    else:
      row.append("B")
  board.append(row)

# print the board
for row in board:
  print(row)

# main game loop
while True:
  # player 1's turn
  print("Player 1's turn")
  x1, y1 = input("Enter the x and y coordinates of the piece you want to move, separated by a comma: ").split(",")
  x1, y1 = int(x1), int(y1)
  x2, y2 = input("Enter the x and y coordinates of where you want to move the piece, separated by a comma: ").split(",")
  x2, y2 = int(x2), int(y2)

  # check if the move is valid
  if board[x1][y1] == "W" and x2 == x1 + 1 and y2 == y1 + 1:
    board[x1][y1] = "B"
    board[x2][y2] = "W"
  else:
    print("Invalid move")
    continue

  # check if player 1 has won
  if y2 == 7:
    print("Player 1 wins!")
    break

  # player 2's turn
  print("Player 2's turn")
  x1, y1 = input("Enter the x and y coordinates of the piece you want to move, separated by a comma: ").split(",")
  x1, y1 = int(x1), int(y1)
  x2, y2 = input("Enter the x and y coordinates of where you want to move the piece, separated by a comma: ").split(",")
  x2, y2 = int(x2), int(y2)

  # check if the move is valid
  if board[x1][y1] == "B" and x2 == x1 - 1 and y2 == y1 + 1:
    board[x1][y1] = "W"
    board[x2][y2] = "B"
  else:
    print("Invalid move")
    continue

  # check if player 2 has won
  if y2 == 7:
    print("Player 2 wins!")
    break

  # print the board
  for row in board:
    print(row)