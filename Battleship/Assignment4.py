import sys


txt1_=open(sys.argv[1],"r",encoding="utf-8")
txt1_=txt1_.readlines()
txt1_in = open(sys.argv[3], "r")
txt1_in = txt1_in.readlines()
txt2_=open(sys.argv[2],"r")
txt2_= txt2_.readlines()
txt2_in = open(sys.argv[4], "r")
txt2_in = txt2_in.readlines()
w_txt= open("Battleship.out", "w")


column = [" ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
round = 1
row_labels = [str(i + 1) for i in range(10)]
print("Battle of Ships Game")
w_txt.write("Battle of Ships Game\n\n")

def grid_creator(name):
    name = []
    name.append(column)
    for i in range(10):
        name.append([row_labels[i], *("-"*10)])
    return name


pool_1hidden = grid_creator("pool_1")
pool_2hidden = grid_creator("pool_2")
grid1 = grid_creator("1")
grid2 = grid_creator("2") 
a = grid_creator("3")

alp=" ABCDEFGHIJ"
def place_let(txt,para):
    for i  in range(10):
        
        differ = 0
        idx = 1
        
        for a in txt[i]:
            if a != ";":
                if a=="\n":
                    pass
                else:  
                    para[i+1][idx - differ]=a
                    differ +=1
                    idx+=1
            else:
                idx +=1
    return        
place_let(txt1_,pool_1hidden)
place_let(txt2_,pool_2hidden)

def print_grids(grid1,grid2):

    print("Player1’s Hidden Board\t\t Player2’s Hidden Board")
    w_txt.write("Player1’s Hidden Board\t Player2’s Hidden Board\n")
    for i in range(11):
        print(" ".join(grid1[i]), end="\t\t ")
        print(" ".join(grid2[i]))
        w_txt.write(" ".join(grid1[i]))
        w_txt.write("\t\t")
        w_txt.write(" ".join(grid2[i]))
        w_txt.write("\n")
    print("")
    w_txt.write("\n")


def play(ftxt_in, grid2, stxt_in, grid1):
    round = 0
    while True:
        if round % 2 == 0:
            player = "Player 1"
            txt_in = ftxt_in[0].split(";")
            del txt_in[-1]
            grid = grid2

        else:
            player = "Player 2"
            txt_in = stxt_in[0].split(";")
            del txt_in[-1]
            grid = grid1
        
        if round%2 == 0 :
            
            shot = txt_in[round //2]
            idx = shot.index(",")
            row = int(shot[:idx]) 
            col = alp.index(shot[idx+1])
      
            if pool_2hidden[row][col] != "-":
                grid2[row][col] = grid2[row][col].replace("-","X")
            else:
                grid2[row][col] = grid2[row][col].replace("-","O")
        else:
            
            shot = txt_in[round//2 +1]
            idx = shot.index(",")
            row = int(shot[:idx]) 
            col = alp.index(shot[idx+1])
            
            if pool_1hidden[row][col] != "-":
                grid1[row][col] = grid1[row][col].replace("-","X")
            else:
                grid1[row][col] = grid1[row][col].replace("-","O")
        print(f"{player}'s move:\n")
        w_txt.write(f"{player}'s move:\n\n")   
        print("Round:", round // 2 +1 ,"\t\tGrid Size: 10x10\n")
        w_txt.write("Round:")
        w_txt.write(str(round // 2 +1))
        w_txt.write("\t\tGrid Size: 10x10\n\n")
        print_grids(grid1,grid2)
        y = 0
        for i in grid1:
            y += i.count("X")

        x = 0
        for i in grid1:
            x += i.count("X")

        # Check if the game is over (i.e., all ships have been sunk)
        if y == 27:
            print("Game over! Player 1 wins!")
            w_txt.write("Game over! Player 1 wins!")
            break
        elif x== 27:
            print("Game over! Player 2 wins!")
            break
        
        round += 1
play(txt1_in,grid2,txt2_in,grid1)
print_grids(grid1,grid2)
print(place_let(txt1_,a))