import time

temp_arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
compare_arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
x, y, x1, Y1 = 0, 0, 0, 0

def input_Q(input_mat, output_mat):
    print("Enter the start then End at same location matrix")
    for i in range(3):
        for j in range(3):
            print("position", i, j)
            input_mat[i][j] = int(input())
            output_mat[i][j] = int(input())

def find(input_mat, output_mat):
    global x, y, x1, Y1
    for i in range(3):
        for j in range(3):
            if input_mat[i][j] == 0:
                x, y = i, j
            if output_mat[i][j] == 0:
                x1, Y1 = i, j

def ouput_Q(mat):
    print()
    for row in mat:
        print(" ".join(map(str, row)))
    print()

def compare(in_mat, ot_mat):
    count = 0
    for i in range(3):
        for j in range(3):
            if in_mat[i][j] != ot_mat[i][j]:
                count += 1
    return count

def h_value(in_x, in_y, in_mat, ot_mat):
    arr1, arr2, arr3, arr4 = [], [], [], []
    h_value_arr = [0, 0, 0, 0]

    if in_mat[in_x-1][in_y] != 0:
        arr1 = [row[:] for row in in_mat]
        arr1[in_x-1][in_y], arr1[in_x][in_y] = arr1[in_x][in_y], arr1[in_x-1][in_y]
        h_value_arr[0] = compare(arr1, ot_mat)
        ouput_Q(arr1)
    else:
        h_value_arr[0] = 999

    if in_mat[in_x][in_y-1] != 0:
        arr2 = [row[:] for row in in_mat]
        arr2[in_x][in_y-1], arr2[in_x][in_y] = arr2[in_x][in_y], arr2[in_x][in_y-1]
        h_value_arr[1] = compare(arr2, ot_mat)
        ouput_Q(arr2)
    else:
        h_value_arr[1] = 999

    if in_mat[in_x+1][in_y] != 0:
        arr3 = [row[:] for row in in_mat]
        arr3[in_x+1][in_y], arr3[in_x][in_y] = arr3[in_x][in_y], arr3[in_x+1][in_y]
        h_value_arr[2] = compare(arr3, ot_mat)
        ouput_Q(arr3)
    else:
        h_value_arr[2] = 999

    if in_mat[in_x][in_y+1] != 0:
        arr4 = [row[:] for row in in_mat]
        arr4[in_x][in_y+1], arr4[in_x][in_y] = arr4[in_x][in_y], arr4[in_x][in_y+1]
        h_value_arr[3] = compare(arr4, ot_mat)
        ouput_Q(arr4)
    else:
        h_value_arr[3] = 999

    k = h_value_arr.index(min(h_value_arr))
    global temp_arr
    temp_arr = [row[:] for row in [arr1, arr2, arr3, arr4][k] if row]
    return min(h_value_arr)

def astar(g, h, f, in_mat, ot_mat, x_in, y_in):
    if h > 0:
        g += 1
        h = h_value(x, y, in_mat, ot_mat)
        f = g + h
        find(temp_arr, ot_mat)
        compare_arr[x][y] = 1
        time.sleep(2)
        print("---------------------")
        print("\nselected!!!\n")
        ouput_Q(compare_arr)
        print("heuristic value :", h)
        print("G value:", g, "\nF value:", f)
        print("---------------------")
        time.sleep(3)
        x_in, y_in = x, y
        astar(g, h, f, temp_arr, ot_mat, x_in, y_in)

def main():
    input_mat = [[0 for _ in range(3)] for _ in range(3)]
    output_mat = [[0 for _ in range(3)] for _ in range(3)]

    input_Q(input_mat, output_mat)

    global temp_arr
    find(input_mat, output_mat)
    compare_arr[x][y] = 1
    h = compare(input_mat, output_mat)
    print("---------------------")
    print("\nselected!!!\n")
    ouput_Q(compare_arr)
    print("heuristic value :", h)
    print("G value:", 0, "\nF value:", 0)
    print("---------------------")

    astar(0, h, 0, input_mat, output_mat, x, y)

if __name__ == "__main__":
    main()
