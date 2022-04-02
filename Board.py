#CPSC231 LEC 01
#Hasan Nassar
#TUT T04/ Shauvik Shadman
#30099862
#Constants for piece types

EMPTY = 0
X = 1
O = 2
class Board:
    board = None
    # Constructor of the class

    # Parameters:
    # rows: The amount of rows in the tictactoe game (default =  3)
    # cols: The amount of columns in the tictactoe game (default = 3)

    # Returns: Nothing

    def __init__(self, rows = 3, cols = 3):
        self.board = []      
        self.nrows = rows    
        self.ncols = cols

         # Got help from the slides
         # Make a 2D list
        for i in range(rows):      
            self.board.append([])
            for p in range(cols):
                self.board[i].append(EMPTY) 
                
    # Gives the number of rows

    # Returns: (len(self.board)) --> Gives the amount of rows in the tictactoe game

    def rows(self):
        return len(self.board)

    # Gives the number of columns

    # Returns: (len(self.board[0])) --> Gives the amount of columns in the tictactoe game

    def cols(self):
        return len(self.board[0])

    # Will determine if the specified area in the row and column is Empty (equal to 0)

    #Parameters:
    # rows: Looking inside a specific row in the tictactoe game
    # cols: Looking inside a specific column in the tictactoe game

    #Returns: 1) True only if the area in the specified row and column are empty
    #         2) False only if the area in the specified row and column are not empty

    def canPlay(self, rows, cols):

        #Checks to see if the row and column is empty (equal to 0)
        if self.board[rows][cols] == EMPTY:  
            return True
        else:
            return False

    # Will play the piece in the specified area given by the row and column

    #Parameters:
    # rows: Go to the specified row given
    # cols: Go to the specified column given
    # piece: Will play your chosen piece in the given row and column

    # Returns: Nothing

    def play(self, rows, cols, piece):

        # Play the piece in the specified row and column
        self.board[rows][cols] = piece 

    # Will determine if the board is filled and has no winner (becomes a draw)

    # Returns: 1) False only when the function detects there is still an empty space in the tictactoe game
    #          2) True only when the function detects there are no more empty spaces in the tictactoe game

    def full(self):

        #Access every row and column
        for r in range(self.rows()):     
            for c in range(self.cols()):    
                if self.board[r][c] == EMPTY:    
                    return False
        return True

    # Determines if the user or AI has won in any given row

    # Parameters:
    # rows: A number for a specific row inside the tictactoe game
    # piece: The piece that the user is using (X or O)

    # Returns: 1) True only if it detects a row with three of the same pieces next to eachother
    #          2) False only if it does not detect a row with three of the same pieces next to eachother
    
    def winInRow(self, rows, piece):
        
        # Access each row inside of the board
        row_win = self.board[rows] 
        for i in range(len(row_win) - 2): 
            if row_win[i] == piece: 
                if row_win[i+1] == piece:   
                    if row_win[i+2] == piece:   
                        return True
        return False
                
    # Determines if the user or the AI wins a column

    # Parameters:
    # cols: A number for a specific column inside the tictactoe game
    # piece: The piece that the user is using (X or O)

    # Returns: 1) True only if the function has detected three of the same pieces next to eachother in the same specified column
    #          2) False only if the function does not detect three of the same pieces next to eachother in the same specified column

    def winInCol(self, cols, piece):

        # Got help from Shauvik for this function
        # Create a list in order to get the columns in the same list
        col_win = [] 
        for i in range(len(self.board)): 
            col_win.append(self.board[i][cols])

        # Create the step to win in a column
        for i in range(len(col_win)-2): 
            if col_win[i] == piece: 
                if col_win[i+1] == piece:    
                    if col_win[i+2] == piece:   
                        return True
        return False
    
    # Determines if the user or AI wins in a diagonal line

    # Parameters:
    # piece: The piece that the user is using (X or O)

    # Returns: 1) True only if the function has detected three of the same pieces next to eachother in a diagonal line
    #          2) False only if the function has not detected three of the same pieces next to eachother in a diagonal line

    def winInDiag(self, piece):

        # Got help from Shauvik for this function
        # First diagonal situation
        for i in range(len(self.board) - 2): 
            for j in range(len(self.board[0]) - 2):
                if self.board[i][j] == piece: 
                    if self.board[i+1][j+1] == piece: 
                        if self.board[i+2][j+2] == piece:  
                            return True

        # Second diagonal situation
        for i in range(len(self.board) - 2):
            for j in range(2 , len(self.board[0])): 
                if self.board[i][j] == piece:
                    if self.board[i+1][j-1] == piece:
                        if self.board[i+2][j-2] == piece: 
                            return True
        return False
                
    # Determines if the user of the AI has won the game

    # Parameters:
    # piece: The piece the user chose (X or O)

    # Returns: 1) True only if the user or AI has won in a row, column, or in a diagonal line
    #          2) False only if the user or AI has not won in any way
    
    def won(self, piece):

        # Win in a row
        for i in range(len(self.board)):
            if self.winInRow(i, piece): 
                return True

        # Win in a column
        for j in range (len(self.board[0])): 
            if self.winInCol(j, piece): 
                return True

        # Win in a diagonal line
        if self.winInDiag(piece): 
            return True
        return False
            

    # Gives a hint to the player

    # Parameters:
    # piece: The piece the user chose (X or O)

    # Returns: 1) i(row), j(column) only when the user or AI will win at that specific location
    #          2) -1, -1 only if the user or AI will not win at that location
    def hint(self, piece):
        for i in range(len(self.board)): 
            for j in range(len(self.board[0])): 
                if self.board[i][j] == EMPTY: 
                    self.play(i, j, piece) 
                    if self.won(piece):
                        self.board[i][j] = EMPTY 
                        return i, j
                    else:
                        self.board[i][j] = EMPTY
        return -1, -1
    
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False

