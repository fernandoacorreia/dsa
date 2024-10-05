# solve_maze returns a list of positions (tuples of row and column) that must be visited
# to find the exit of the maze (indicated by X) from the start (indicated by S at position 0,0).
def solve_maze(m):
    # Validate maze.
    num_rows = len(m)
    if num_rows < 1:
        raise ValueError("The maze must have at least one row.")
    num_cols = len(m[0])
    if num_cols < 1:
        raise ValueError("The maze must have at least one column.")
    if m[0][0] != 'S':
        raise ValueError("Position 0,0 must be S.")

    current_row = 0
    current_col = 0

    def find_exit(r, c, visited):
        # If outside the maze, return None, indicating no valid solution left.
        if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
            return None

        # If the current position is a wall (0), return None indicating an invalid move.
        if m[r][c] == '0':
            return None

        # If the position had already been visited, return None, indicating that it is an invalid move.
        if (r, c) in visited:
            return None

        # If the current position is the end of the maze, return its tuple.
        if m[r][c] == 'X':
            visited.append((r, c))
            return visited

        # Add the current position to the list of visited positions.
        visited.append((r, c))
        original_length = len(visited)  # Keep track of how many steps were taken.

        # Try down.
        path = find_exit(r + 1, c, visited)
        if path != None:
            return path
        del visited[original_length:]  # Discard any changes introduced by the previous attempt.

        # Try up.
        path = find_exit(r - 1, c, visited)
        if path != None:
            return path
        del visited[original_length:]  # Discard any changes introduced by the previous attempt.

        # Try left.
        path = find_exit(r, c - 1, visited)
        if path != None:
            return path
        del visited[original_length:]  # Discard any changes introduced by the previous attempt.

        # Try right.
        path = find_exit(r, c + 1, visited)
        if path != None:
            return path
        del visited[original_length:]  # Discard any changes introduced by the previous attempt.

        return None  # There is no solution from this position.

    return find_exit(current_row, current_col, [])
