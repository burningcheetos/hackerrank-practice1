

import sys



def stair_Case(num):

    MAX = num
    decr_counter = num
    line = []

    # init
    for i in range(num):
        line.append(" ")

    line[MAX-1] = str(num)

    # calc & print
    while decr_counter != 0:

        print "".join(line)
        decr_counter = decr_counter - 1
        line[decr_counter-1] = str(num)



if __name__ == "__main__":

    is_num = False
    while not is_num:

        _num = raw_input("Enter a num: ")

        try:
            print int(_num)
            is_num = True

        except ValueError:
            print "Not an number"

    stair_Case(int(_num))