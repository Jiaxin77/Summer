import numpy as np

def valid_battleship(board):

    board_arr = np.array(board)

    if board_arr.sum() != 20:  #4+3+3+2+2+2+1+1+1+1
        return False

    board_arr = np.pad(board_arr, 1, 'constant') #填补一个数组


    filter_battleship = np.pad([[1], #布局
                            [1], 
                            [1], 
                            [1]], 1, 'constant', constant_values=-1)

    filter_cruiser = np.pad([[1], 
                         [1], 
                         [1]], 1, 'constant', constant_values=-1)

    filter_destroyer = np.pad([[1], 
                           [1]], 1, 'constant', constant_values=-1)

    filter_submarine = np.pad([[1]], 1, 'constant', constant_values=-1)


    def convolution(image, kernel, flag):

        count = 0

        image_height = image.shape[0]
        image_width = image.shape[1]

        kernel_height = kernel.shape[0]
        kernel_width = kernel.shape[1]


        for i in range(image_height - kernel_height):
            for j in range(image_width - kernel_width):

                receptive_field = board_arr[i:i + kernel_height, 
                                            j:j + kernel_width]

                if (receptive_field * kernel).sum() == flag:
                    count += 1

                    #print(receptive_field)
                    #print((receptive_field * kernel).sum())

        return count


    def search_ship():    

        ship_counts = {4:0,
                       3:0,
                       2:0,
                       1:0}

        filters = [filter_battleship, filter_battleship.T,
                   filter_cruiser, filter_cruiser.T,
                   filter_destroyer, filter_destroyer.T,
                   filter_submarine]

        ship_sizes = [4,4,3,3,2,2,1]


        for i,j in zip(filters, ship_sizes):

            ship_counts[j] += convolution(board_arr, i, j)

        return ship_counts

    return search_ship() == {1: 4, 2: 3, 3: 2, 4: 1}