import numpy as np


def optimality_check(array_):
    """
    Deltas are checked, if all are nonnegative, then the basis solution is optimal.
    """
    if min(array_)>=0:
        return True
    else:
        return False


def find_nonbasis_vector(basis_vector, number_of_vars):
    """
    Just for initialization process, returns non-basis vector.
    :param basis_vector:
    :param number_of_vars:
    :return:
    """
    return [x for x in range(number_of_vars) if x not in basis_vector]


def find_entering_vector(delta_vector, nonbasis_vector):
    return np.argmin(delta_vector), nonbasis_vector[np.argmin(delta_vector)]


def find_leaving_vector(rhs, entering_vector, basis_vector):
    """
    Performs minimum-ratio test to find leaving variable from basis_vector.
    Not considers results with 0, and infinite value
    """
    basis_vector = np.array(basis_vector)
    minimum_idx = 0
    min_value = 500
    for idx in range(len(entering_vector)):
        if rhs[idx] == 0:
            pass
        elif entering_vector[idx]==0:
            pass
        else:
            new_value = rhs[idx]/entering_vector[idx]
            if new_value<=min_value:
                min_value = new_value
                minimum_idx = idx
    return minimum_idx

def update_matrix(matrix, vector_ele, idx):
    """
    matrix
    """
    total_operation = matrix.shape[0]

    matrix[idx, :] = matrix[idx, :]/vector_ele[idx]
    for i in range(total_operation):
        if i == idx:
            pass
        else:
            matrix[i] = matrix[i]-1*vector_ele[i]*matrix[idx]
    new_col_for_additionaltable = np.zeros(len(vector_ele))
    new_col_for_additionaltable[idx] = 1
    return matrix, new_col_for_additionaltable





if __name__ == "__main__":
    t = find_nonbasis_vector([3,4,5], 6)
    print(t)


