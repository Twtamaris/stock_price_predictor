def is_valid(state):
    farmer, goat, wolf, cabbage = state

    if (goat == wolf and farmer != goat) or (goat == cabbage and farmer != goat):
        return False
    return True



def tree(start_state):


    second_height, count, index1 = nodes_at_height(start_state, 0)
    third_height, count, index2 = nodes_at_height(second_height, count)
    fourth_height, count, index3 = nodes_at_height(third_height, count)
    fifth_height, count, index4 = nodes_at_height(fourth_height, count)
    sixth_tree_structure, count, index5 = nodes_at_height(fifth_height, count)
    seventh_tree_structure, count, index6 = nodes_at_height(sixth_tree_structure, count)
    eighth_tree_structure, count, index7 = nodes_at_height(seventh_tree_structure, count)
    # total_tree = second_height+third_height+fourth_height+fifth_height+sixth_tree_structure+seventh_tree_structure+eighth_tree_structure
    total_tree = [[start_state],second_height, third_height, fourth_height, fifth_height, sixth_tree_structure, seventh_tree_structure, eighth_tree_structure]
    index = [[0],index1, index2, index3, index4, index5, index6, index7]
    
    return total_tree, index



def nodes_at_height(previous_height_nodes, count):
    if isinstance(previous_height_nodes, tuple):
        previous_height_nodes = [previous_height_nodes]
    index = []
    west_east = count % 2
    next_height_nodes = []
    for h,i in enumerate(previous_height_nodes):
        new_objects = list(i)

        for j,k in enumerate(new_objects):
            if j == 0:
                index.append(h)
                new_objects[j] = abs(west_east - 1)
                next_height_nodes.append(tuple(new_objects))

            elif new_objects[j] == abs(west_east):
                index.append(h)
                new_objects[j] = abs(west_east - 1)
                next_height_nodes.append(tuple(new_objects))
                new_objects[j] = abs(west_east)
    count += 1
    # print("index", index)
    return next_height_nodes, count, index

def dfs(total_tree, visited, index):
    stack = [(0, 0)]
    steps = []
    while stack:
        height, index_value = stack.pop()
        node = total_tree[height][index_value]
        if node not in visited and is_valid(node):
            print("Step:", node)
            steps.append(node)
            visited.add(node)

            if height + 1 < len(total_tree):
                for i, child_node in enumerate(total_tree[height + 1]):
                    if index[height + 1][i] == index_value:  
                        stack.append((height + 1, i))
    return steps





def main():
    start_state = (0,0,0,0)
    visited = set()
    tree_structure = []
    total_tree, index = tree(start_state)
    steps = dfs(total_tree, visited, index)
    # print(steps)


main()
