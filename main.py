import numpy as np
import funcs

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

def extract_problem(str_):
    constraint_bool= False
    for line in str_.split("\n"):
        if line == "s.t":
            constraint_bool = True

        if constraint_bool==False:
            #now we are in objective function declaration
            pass
            objective = line.split(" ")[0]
            if objective=="max":
                pass
            else:
                #multiply objective function coefficients by -1
                pass
        else:
            pass


example1 = """1*x1 +3*x2 <=10
1*x2 +1*x3 <= 15
1*x1 +1*x2 <= 11"""

example1_vars = ['x1', 'x2', 'x3']

number_of_const = len(example1.split('\n'))
number_of_vars = len(example1_vars)

coefficient_matrix = np.array(np.zeros(shape=(number_of_const, number_of_vars)))
idx = 0
for line in example1.split('\n'):
    coefficient_matrix[idx]=funcs.process_const(line, example1_vars)
    idx += 1












