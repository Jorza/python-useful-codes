def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def has_valid_diags(possible_sol):
    N = len(possible_sol)
    for i in range(N-1):
        for j in range(i+1,N):
            if j-i == abs(possible_sol[j]-possible_sol[i]):
                return False
    return True


def single_board_sols(N, number=None):
    sol_count = 0
    sol_list = []
    # Iterate through all possible permutations of the numbers 1 to N.
    # This accounts every possible way the queens can be placed in different rows and columns.
    for perm in all_perms(list(range(N))):
        # Check each permutation to check if no two queens share a diagonal.
        if has_valid_diags(perm):
            # Record valid solution.
            sol_count += 1
            sol_list.append(perm)
            if sol_count == number:
                return sol_list
    return sol_list


def print_board(sol):
    N = len(sol)
    for col_value in sol:
        print(". " * col_value + "Q " + ". " * (N - 1 - col_value))
    print()


def print_sols(sol_list):
    # Print number of sols, and solution boards.
    sol_count = len(sol_list)
    if sol_count > 0:
        print("\nThe solutions are:")
    for sol in sol_list:
        print_board(sol)
    print("There are {} solutions for this board size.".format(sol_count))


def print_sol_counts(N):

    count_list = [None]*N
    header_string = "    Board size:"
    values_string = "# of solutions:"
    # Iterate through all board sizes from 1 to N. For each, record the number of solutions.
    for board_size in range(1, N+1):
        sol_count = 0
        # Iterate through all possible permutations of the numbers 1 to N.
        # This accounts every possible way the queens can be placed in different rows and columns.
        for perm in all_perms(list(range(board_size))):
            # Check each permutation to check if no two queens share a diagonal.
            if has_valid_diags(perm):
                # Record valid solution.
                sol_count += 1
        count_list[board_size-1] = sol_count
        header_string += " | {:3d}".format(board_size)
        values_string += " | {:3d}".format(sol_count)

    # Print the number of solutions for each board size in a table.
    print()
    print(header_string)
    print(values_string)
    return count_list


# Get size of board from user.
N = int(input("How big is the board? Enter the number of rows: "))

# Below are a collection of different ways to represent the solutions to the N Queens problem;
# They include:
#       1) Printing all solutions for a given board size.
#       2) Printing only the first solution found for a given board size.
#       3) Printing the number of solutions for all board sizes from 1 up to a given size.

# print_sols(single_board_sols(N))

# print("\nThe first solution found for a board of size {} was: ".format(N))
# print_board(single_board_sols(N, 1)[0])

print_sol_counts(N)
