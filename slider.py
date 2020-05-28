import random


class Puzzle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_puzzle(self):
        puz_length = self.width * self.height
        puz_chars = ""
        # create string of numbers.  Last number should be '_'
        for i in range(puz_length):
            if (i+1) != puz_length:
                puz_chars += str(i+1) + ' '
            elif (i+1):
                puz_chars += '_'
        return puz_chars

    def set_puzzle(self, puz_chars):
        parent_array = []
        child_array = []

        # split puz chars into an array
        split_array = puz_chars.split()

        for i in split_array:\
            # all comparisons based on the index of i
            test_index = split_array.index(i) + 1
            if i != "_":
                if test_index % self.width != 0:
                    child_array.append(i)
                elif test_index % self.width == 0:
                    child_array.append(i)
                    parent_array.append(child_array)
                    child_array = []
            elif i == "_" and test_index % self.width != 0:
                child_array.append(i)
            elif i == "_" and test_index % self.width == 0:
                child_array.append(i)
                parent_array.append(child_array)
                child_array = []
        return parent_array


    def move_up(self, puz_array):
        # get index of '_'
        blank_location = self.__find_empty(puz_array, '_')

        #get location of value above blank
        val_above = [blank_location[0]-1, blank_location[1]]

        if val_above[0] < 0:
            val_above[0] = 0

        #get value above blank
        num_above = puz_array[val_above[0]][val_above[1]]

        #assign puz_array new values
        puz_array[val_above[0]][val_above[1]] = '_'
        puz_array[blank_location[0]][blank_location[1]] = num_above
        return(puz_array)

    def move_down(self, puz_array):
        # get index of '_'
        blank_location = self.__find_empty(puz_array, '_')

        #get location of value below blank
        val_below = [blank_location[0] + 1, blank_location[1]]

        if val_below[0] > (self.height - 1):
            val_below[0] = (self.height - 1)

        #get value below blank
        num_below = puz_array[val_below[0]][val_below[1]]

        #assign puz_array new values
        puz_array[val_below[0]][val_below[1]] = '_'
        puz_array[blank_location[0]][blank_location[1]] = num_below
        return(puz_array)


    def move_right(self, puz_array):
        # get index of '_'
        blank_location = self.__find_empty(puz_array, '_')

        #get location of value below blank
        val_right = [blank_location[0], blank_location[1] + 1]

        if val_right[1] > (self.width - 1):
            val_right[1] = (self.width - 1)

        #get value above blank
        num_right = puz_array[val_right[0]][val_right[1]]

        #assign puz_array new values
        puz_array[val_right[0]][val_right[1]] = '_'
        puz_array[blank_location[0]][blank_location[1]] = num_right
        return(puz_array)


    def move_left(self, puz_array):
        # get index of '_'
        blank_location = self.__find_empty(puz_array, '_')

        #get location of value below blank
        val_left = [blank_location[0], blank_location[1] - 1]

        if val_left[1] < 0:
            val_left[1] = 0

        #get value above blank
        num_left = puz_array[val_left[0]][val_left[1]]

        #assign puz_array new values
        puz_array[val_left[0]][val_left[1]] = '_'
        puz_array[blank_location[0]][blank_location[1]] = num_left
        return(puz_array)

    def solve(self):
        puz_chars = self.get_puzzle()
        puz_array = self.set_puzzle(puz_chars)
        return puz_array

    def scramble(self):
        puz_chars = self.get_puzzle()
        split_array = puz_chars.split(' ')
        random.shuffle(split_array)
        #list to sting
        list_to_str = ' '.join([str(elem) for elem in split_array])
        return(self.set_puzzle(list_to_str))


    def to_s(self, puz_array):
        index = 0
        new_row = ''
        for i in puz_array:
            puz_str_row = ' '.join(([str(elem) for elem in puz_array[index]]))
            new_row += ('{0}\n').format(puz_str_row)
            index += 1
        print(new_row)
        return new_row



    def run_puzzle(self):
        # run get puzzle to get the puzzle string
        puz_chars = self.get_puzzle()

        # run set puzzle to set the puzzle into an array
        puz_array = self.set_puzzle(puz_chars)
        print(puz_array)
        self.to_s(puz_array)

        # prompt the user to enter a command
        # u = up, d = down, l = left, r = right, s = scramble,
        # = is solve, x = quit
        input_msg = ("u = move up, d = move down, l = move left, r = move right\n"
                           "s = scramble, v = solve, and x = quit\n"
                           "please select an option: ")

        continue_game = True
        while continue_game == True:
            user_input = input(input_msg)
            if user_input == 'u':
                self.move_up(puz_array)
                self.to_s(puz_array)
            elif user_input == 'd':
                self.move_down(puz_array)
                self.to_s(puz_array)
            elif user_input == 'l':
                self.move_left(puz_array)
                self.to_s(puz_array)
            elif user_input == 'r':
                self.move_right(puz_array)
                self.to_s(puz_array)
            elif user_input == 's':
                puz_array = self.scramble()
                self.to_s(puz_array)
            elif user_input == 'v':
                puz_array = self.solve()
                self.to_s(puz_array)
            elif user_input == 'x':
                continue_game = False
            else:
                print("Please choose one of the provided options")

        print("Thank you for playing.")



    #private function that finds the location of '_'
    def __find_empty(self, puz_array, val):
        for par, chld in enumerate(puz_array):
            if val in chld:
                return (par, chld.index(val))






