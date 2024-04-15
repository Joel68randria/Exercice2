from itertools import product

def enter_logical_function():
    function = input("Entrez la fonction logique (utilisez 'AND', 'OR', 'NOT', 'XOR', etc.): ")
    return function

def build_karnaugh_table(variables):
    table = {}
    for assignment in product([0, 1], repeat=len(variables)):
        assignment_str = ''.join(map(str, assignment))
        table[assignment_str] = int(input(f"Entrez la valeur de la fonction pour l'assignation {assignment}: "))
    return table

def identify_adjacent_groups(table):
    groups = []
    all_assignments = list(table.keys())  
    for assignment, value in table.items():
        if value == 1:
            adjacent_group = [assignment]
            for neighbor_assignment in get_neighbors(assignment, all_assignments):
                if table[neighbor_assignment] == 1:
                    adjacent_group.append(neighbor_assignment)
            if len(adjacent_group) > 1:
                groups.append(adjacent_group)
    return groups

def get_neighbors(assignment, all_assignments):
    neighbors = []
    assignment = list(assignment)
    for i in range(len(assignment)):
        flipped_assignment = list(assignment)
        flipped_assignment[i] = str(int(not int(flipped_assignment[i])))
        flipped_assignment_str = ''.join(flipped_assignment)
        if flipped_assignment_str in all_assignments:
            neighbors.append(flipped_assignment_str)
    return neighbors

def simplify_groups(groups):
    simplified_groups = []
    for group in groups:
        simplified_group = simplify_group(group)
        simplified_groups.append(simplified_group)
    return simplified_groups

def simplify_group(group):
    simplified_group = []
    for term in group:
        simplified_term = []
        for i in range(len(term)):
            if term[i] == '0':
                simplified_term.append(f"A{i+1}'")
            elif term[i] == '1':
                simplified_term.append(f"A{i+1}")
        simplified_group.append(''.join(simplified_term))
    return "+".join(simplified_group)

def rebuild_simplified_function(groups):
    simplified_function = ""
    for group in groups:
        simplified_function += "(" + "+".join(group) + ")"
    return simplified_function

def display_simplified_function(simplified_function):
    print("La fonction simplifiée est:", simplified_function)

def main():
    logical_function = enter_logical_function()
    variables = ['A', 'B', 'C']  
    karnaugh_table = build_karnaugh_table(variables)
    groups = identify_adjacent_groups(karnaugh_table)
    simplified_groups = simplify_groups(groups)
    simplified_function = rebuild_simplified_function(simplified_groups)
    display_simplified_function(simplified_function)

if __name__ == "__main__":
    main()
