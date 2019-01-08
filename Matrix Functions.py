def get_coordinates(n_points, matrix_size):

    # Get valid user input, store as a list of coordinates for the coord_list.
    coord_list = []
    coord_count = 0
    while len(coord_list) <= n_points:
        coord = input("Enter coordinates of point {}: ".format(coord_count + 1)).split(",")

        # Check input, convert to integers.
        try:
            # Check each entry has a row and column coordinate
            if len(coord) != 2:
                raise ValueError
            # Convert each coordinate to an integer.
            for char_idx in range(len(coord)):
                coord[char_idx] = int(coord[char_idx])
                if coord[char_idx] >= matrix_size:
                    raise ValueError
        except ValueError:
            print("Those are not valid coordinates. Re-enter coordinates of point {}: ".format(coord_count + 1))
            continue

        # Input is valid, so record coordinates, increment counter to get next coordinates.
        coord_list.append(coord)
        coord_count += 1

    # All coordinates have been inputted.
    return coord_list


def coordinates_to_matrix(coord_list, matrix_size):
    """
    Represent list of coordinates in a list of lists to represent a matrix.
    :param coord_list: list of coordinates. Each coordinate is a list, with the row and column values at indexes 0 and 1
    respectively. If there are three values exactly, the third value is taken to be value at the coordinates. Otherwise,
    the value is recorded as a '1'.
    :param matrix_size: number of rows desired in the output matrix.
    :return: A square matrix of size matrix_size, with the coordinates given in coord_list.
    """

    if len(coord_list) == 3:
        entry_value = lambda index: coord_list[index[2]]
    else:
        entry_value = lambda index: 1

    # Initialise matrix with zeros.
    matrix = []
    row_list = [0]*matrix_size
    for row in range(matrix_size):
        matrix.append(row_list[:])

    # Fill with points in coord_list.
    for coord in coord_list:
        matrix[coord[0]][coord[1]] = entry_value(coord)


def print_matrix(matrix):
    print()
    for row in matrix:
        row_string = ""
        for entry in row:
            entry = str(entry)
            row_string += entry + " "
        print(row_string)


def transposeTable(table):
    """
    Find the transpose of a table - A table containing the same values as the original, but with the row and column
    indexes for each element switched
    :param table: A table, represented as a list of lists.
    :return: The transpose of 'table', represented as a list of lists.
    """
    transpose = []

    tableSize = len(table)
    for col in range(tableSize):

        # Construct list of column elements in 'table'.
        columnList = []

        # Get item at specific column index from each row
        for row in range(tableSize):
            columnList.append(table[row][col])

        # Append column from original table as a row of the transpose.
        transpose.append(columnList)
    return transpose