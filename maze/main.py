maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

start = 1, 1
end = 5, 19


def make_maze(maze: list):
    v_maze = []
    x = len(maze)
    y = len(maze[0])
    print(x, y)

    for x_i in range(x):

        v_maze.append([0])
        for y_i in range(y):
            v_maze[-1].append(0)

    return v_maze


v_maze = make_maze(maze)
v_maze[start[0]][start[1]] = 1



def make_step(step: int, v_maze: list, maze: list):
    for x in range(len(v_maze)):
        for y in range(len(v_maze[0])):
            if v_maze[x][y] == step:
                if x > 0 and maze[x - 1][y] == 0 and v_maze[x - 1][y] == 0:
                    v_maze[x - 1][y] = step + 1
                if y > 0 and maze[x][y - 1] == 0 and v_maze[x][y - 1] == 0:
                    v_maze[x][y - 1] = step + 1
                if x < len(maze) - 1 and maze[x + 1][y] == 0 and v_maze[x + 1][y] == 0:
                    v_maze[x + 1][y] = step + 1
                if y < len(maze[0]) - 1 and maze[x][y + 1] == 0 and v_maze[x][y + 1] == 0:
                    v_maze[x][y + 1] = step + 1

# make_step(1, v_maze, maze)
# make_step(2, v_maze, maze)
# make_step(3, v_maze, maze)
# make_step(4, v_maze, maze)
# make_step(5, v_maze, maze)
# make_step(6, v_maze, maze)
# make_step(7, v_maze, maze)
# make_step(8, v_maze, maze)
# make_step(9, v_maze, maze)
# make_step(10, v_maze, maze)
# print(v_maze)

k = 0
while v_maze[end[0]][end[1]] == 0:
    k += 1
    print("K", k)
    make_step(k,v_maze,maze)

print(v_maze)

i, j = end
k = v_maze[i][j]
the_path = [(i,j)]
while k > 1:
  if i > 0 and v_maze[i - 1][j] == k-1:
    i, j = i-1, j
    the_path.append((i, j))
    k-=1
  elif j > 0 and v_maze[i][j - 1] == k-1:
    i, j = i, j-1
    the_path.append((i, j))
    k-=1
  elif i < len(v_maze) - 1 and v_maze[i + 1][j] == k-1:
    i, j = i+1, j
    the_path.append((i, j))
    k-=1
  elif j < len(v_maze[i]) - 1 and v_maze[i][j + 1] == k-1:
    i, j = i, j+1
    the_path.append((i, j))
    k -= 1

print("PATH", the_path)