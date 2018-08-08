import numpy as np



def battle(board, attacks):
    outcome={'sunk':0,'damaged':0,'intact':0}
    # 从题示坐标到NumPy Array的坐标变换
    attacks_arr = np.array(attacks) - 1
    board_arr = np.array(board)
    board_arr = board_arr.T[:,::-1]
    board_lst=[]
    count=[]
    flag=[]
    print(board)
    # >>>> keep calm and show me the code <<<<
    for i in board_arr:
        if i!='0':
            if i not in board_lst:
                board_lst.append(i)
                print(1)
                count[i]=1
                print(outcome['intact'])
                outcome['intact']+=1
                print(2)
            else:
                count[i]+=1
    print(outcome['intact'])
    for i in range(0,len(attacks)):
        print(attacks[i])
        attack_x=4-attackes[i][0]
        attack_y=attackes[i][1]
        i=board[attack_x][attack_y]
        if i!=0:
            count[i]-=1
            if flag[i]==0:#之前未受到攻击
                outcome['damaged']+=1
                outcome['intact']-=1
                flag[i]=1
            if count[i]==0:#全船沉没
                outcome['sunk']+=1
                




    # >>>> keep calm and show me the code <<<<



    #答案
    import numpy as np

def battle(board, attacks):

    attacks_arr = np.array(attacks) - 1
    board_arr = np.array(board)
    board_arr = board_arr.T[:,::-1]


    def ship_counts(board_arr):

        board_lst = list(board_arr.reshape(board_arr.shape[0] * board_arr.shape[1]))
        ships = {i:board_lst.count(i) for i in board_lst}
        del ships[0]

        return ships

    ships = ship_counts(board_arr)

    board_tf = board_arr > 0

    for i in zip(attacks_arr[:,0], attacks_arr[:,1]):#zip打包成元组，此array表示方法什么意思？
        if board_tf[i] == True:
            board_tf[i] = False

    board_atk = board_arr * board_tf
    ships_atk = ship_counts(board_atk)


    def ship_stats(ships, ships_atk):

        sunk = 0
        damaged = 0
        intact = 0
        # points = 0

        for i in ships:
            if i not in ships_atk:
                sunk += 1

            elif ships_atk[i] < ships[i]:
                damaged += 1

            elif ships_atk[i] == ships[i]:
                intact += 1

        return {'sunk': sunk, 'damaged':damaged, 'intact':intact}


    return ship_stats(ships, ships_atk)