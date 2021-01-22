import numpy as np
from funcs import *

"""
GUI'de objective function kısmına yazılan
objective : max or min
objective_string = 3*x1+4*x2+10*x3

variable_list = [x1, x2, x3, x4]

constraints: tek bir box içerisinde
x1 +3*x2 <=10
x2 +x3 <= 15
x1 +x2 <= 11
x1>=0
x2>=0
x3>=0
"""

    #text processing (constraint_matrix (number_of_constraint, number_of_variables)
    #objective function control ( min -> max ) [1, 2, 3] -> *-1 -> [-1, -2, -3]
    #constraint control ( >= -> <=) for all constraints > *-1 > updated_constraint_matrix
    #rhs of constraints will be controlled. (must be bi >= 0) -> if violated *-1
    #slack variable adding -> constraint matrix, objective_constraint_vector will be updated.
    # all_constraint_coef_matrix -> objective coefficient will be included. videonun 10. dakikasındaki olay
        #elimizde 3 tane matrix var. coefficient_matrix, variable_vector, objective_coef_vector

    #iteration 0:


constmatrix =np.array(
[[1, -1, -2, 0, 0, 0],
 [0, 1, 1, 1, 0, 0],
 [0, 1, 2, 0, 1, 0],
 [0, 3, 1, 0, 0 ,1]])



var_vector = np.array(['z', 'x1', 'x2', 'x3', 'x4', 'x5'])
rhs = np.array([0, 3, 5, 6])
slack_vars_positions = [3,4,5]


#initialization
number_of_const = constmatrix.shape[0]
number_of_vars = constmatrix.shape[1]
basis_var_vector = [0] + slack_vars_positions #[0,3,4,5]
nonbasis_var_vector = find_nonbasis_vector(basis_var_vector, number_of_vars)

basis_matrix = constmatrix[:, basis_var_vector]
basis_matrix_b = np.insert(basis_matrix, number_of_const, rhs, axis=1)
additional_table = constmatrix[:, nonbasis_var_vector]

optimality_condition=False
iteration_number = 0
while True:
    print(f"Iteration {iteration_number}:")
    delta_vector = np.dot(basis_matrix[0, :], additional_table)
    optimality_condition = optimality_check(delta_vector)

    if optimality_condition:
        print("Optimal solution is found")
        break
    entering_basis_idx, entering_basis = find_entering_vector(delta_vector, nonbasis_var_vector)
    print(f"\tVariable {entering_basis} enters the basis")

    entering_vector = additional_table[:,entering_basis_idx]
    leaving_basis_idx, leaving_basis = find_leaving_vector(rhs, entering_vector, basis_var_vector)
    print(f"\tVariable {leaving_basis} leaves the basis")

    #update basis, non-basis vectors

    basis_var_vector[basis_var_vector.index(leaving_basis)] = entering_basis
    nonbasis_var_vector[nonbasis_var_vector.index(entering_basis)] = leaving_basis

    intermediate_coef_matrix = basis_matrix_b

    print('a')



    #entering vector


basis_vector = [0, 3,4,5] #variable position index
nonbasis_vector = [1,2]


