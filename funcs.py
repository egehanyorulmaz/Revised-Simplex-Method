import numpy as np


def optimality_check(array_):
    """
    Deltas are checked, if all are nonnegative, then the basis solution is optimal.
    """
    if min(array_)>0:
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
    if np.min(rhs) == 0: #discards 0/number results
        leaving_idx = np.argmin(rhs)
        rhs = np.delete(rhs, leaving_idx)
        entering_vector = np.delete(entering_vector, leaving_idx)
        basis_vector = np.delete(basis_vector, leaving_idx)

    if np.min(entering_vector)==0: #discards number/0 results
        leaving_idx = np.argmin(entering_vector)
        rhs.pop(leaving_idx)
        entering_vector.pop(leaving_idx)
        basis_vector.pop(leaving_idx)
    return np.argmin(rhs/entering_vector), basis_vector[np.argmin(rhs/entering_vector)]


if __name__ == "__main__":
    t = find_nonbasis_vector([3,4,5], 6)
    print(t)


