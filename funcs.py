import numpy as np


def process_const(str_, const_names):
    coefficient_lst = np.zeros(len(const_names))
    lhs = str_.split(' <= ')[0]
    lhs_lst = lhs.split(' ')

    for el in lhs_lst:
        if "*" in el:
            var_name = el[el.find('*')+1:]
            var_idx = const_names.index(var_name)
            coefficient_lst[var_idx] = int(el[:el.find('*')])
    return coefficient_lst

if __name__ == "__main__":
    a = "1*a +3*b -1*c <= 10"
    print(process_const(a, ['a', 'b', 'c']))

