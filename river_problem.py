def is_valid(state):
    farmer, goat, wolf, cabbage = state

    if (goat == wolf and farmer != goat) and (goat == cabbage and farmer != goat):
        return False
    return True



def tree(start_state, visited, tree_structure):
    

    second_height, count = nodes_at_height((0,0,0,0), 0)
    
    third_height, count = nodes_at_height(second_height, count)
    fourth_height, count = nodes_at_height(third_height, count)
    fifth_height, count = nodes_at_height(fourth_height, count)
    sixth_tree_structure, count = nodes_at_height(fifth_height, count)
    seventh_tree_structure, count = nodes_at_height(sixth_tree_structure, count)
    eighth_tree_structure, count = nodes_at_height(seventh_tree_structure, count)

    print(len(second_height))
    print(len(third_height))
    print(len(fourth_height))
    print(len(fifth_height))
    print(len(sixth_tree_structure))
    print(len(seventh_tree_structure))
    print(len(eighth_tree_structure))


    



def nodes_at_height(previous_height_nodes, count):
    print(count)
    print("*************************************")
    if isinstance(previous_height_nodes, tuple):
        previous_height_nodes = [previous_height_nodes]

    west_east = count % 2
    next_height_nodes = []
    for i in previous_height_nodes:
        new_objects = list(i)
        print('i', i)
        for j,k in enumerate(new_objects):
            if j == 0:
                new_objects[j] = abs(west_east - 1)
                next_height_nodes.append(tuple(new_objects))
                print("object", new_objects)

            elif new_objects[j] == abs(west_east):
                new_objects[j] = abs(west_east - 1)
                next_height_nodes.append(tuple(new_objects))
                print("object", new_objects)
                new_objects[j] = abs(west_east)
    count += 1
    return next_height_nodes, count

    

# def dfs(tree_structure, visited):
                        
# def dfs(tree_structure, visited):



def main():
    start_state = (0,0,0,0)
    visited = set()
    tree_structure = []
    new_tree = tree(start_state,visited, tree_structure )
    # dfs(tree_structure, visited)
    print(tree_structure)

main()
