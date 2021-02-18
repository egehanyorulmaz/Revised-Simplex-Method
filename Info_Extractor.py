# text processing (constraint_matrix (number_of_constraint, number_of_variables)
# objective function control ( min -> max ) [1, 2, 3] -> *-1 -> [-1, -2, -3]
# constraint control ( >= -> <=) for all constraints > *-1 > updated_constraint_matrix
# rhs of constraints will be controlled. (must be bi >= 0) -> if violated *-1
# slack variable adding -> constraint matrix, objective_constraint_vector will be updated.
# all_constraint_coef_matrix -> objective coefficient will be included. videonun 10. dakikasındaki olay
# elimizde 3 tane matrix var. coefficient_matrix, variable_vector, objective_coef_vector

import os
import numpy as np
def process_input_for_optimization():
    files = ["1.constraint_variables.txt", "2.result.txt", "3.values.txt", "4.objective_variables.txt", "5.objective_values.txt", "objective.txt"]
    for filename in files:
        if filename == "1.constraint_variables.txt":
            varlist = []
            linelist = []
            const_var = open(filename)
            num_of_slack = 0
            for line in const_var:
                line = line.strip()
                variables = line.split(" ")
                for variable in variables:
                    linelist.append(variable)
                    if variable not in varlist:
                        varlist.append(variable)
                linelist.append("|")
                num_of_slack += 1
            total_variable_num = len(varlist) + num_of_slack
            const_var.close()
            const_var = open(filename)
            countline = 0
            start = len(varlist)
            arr = np.zeros((num_of_slack, total_variable_num), int)
            for newline in const_var:
                mewline = newline.strip()
                variables = mewline.split(" ")
                for variable in variables:
                    arr[countline][int(variable[1:]) - 1] = 1
                arr[countline][start] = 1
                start += 1
                countline += 1
            const_var.close()
        elif filename == "3.values.txt":
            val_txt = open(filename)
            rowcount = 0
            for lines in val_txt:
                lines = lines.strip()
                element = lines.split(" ")
                colcount = 0
                used = []
                for value in element:
                    while arr[rowcount][colcount] != 1:
                        colcount += 1
                    if iden_list[rowcount] == "+":
                        arr[rowcount][colcount] = int(value)
                    else:
                        arr[rowcount][colcount] = -1 * int(value)
                    colcount += 1
                rowcount += 1
            val_txt.close()
        elif filename == "4.objective_variables.txt":
            objtxt = open(filename)
            for line in objtxt:
                line = line.strip()
                elements = line.split(" ")
                obj_varlist = [0] * (len(elements) + num_of_slack)
                for variable in elements:
                    obj_varlist[int(variable[1:]) - 1] = 1
            objtxt.close()
        elif filename == "5.objective_values.txt":
            objval = open(filename)
            counter = 0
            for line in objval:
                line = line.strip()
                elements = line.split(" ")
                for values in elements:
                    while obj_varlist[counter] != 1:
                        counter += 1
                    obj_varlist[counter] = int(values)
                    counter += 1
            objval.close()
        elif filename == "objective.txt":
            obj = open(filename)
            for objective in filename:
                if objective == "max":
                    for i in range(len(obj_varlist)):
                        obj_varlist[i] = -1 * obj_varlist[i]
        elif filename == "2.result.txt":
            res = open(filename)
            res_list = []
            iden_list = []
            for line in res:
                line = line.strip()
                element = line.split(" ")
                counter = 0
                for x in element:
                    if counter == 0:
                        res_list.append(x)
                    else:
                        if x != "<=":
                            iden_list.append("-")
                            res_list[counter - 1] = -1 * res_list[counter - 1]
                        else:
                            iden_list.append("+")
                    counter += 1
            res.close()

    arr = np.insert(arr, 0, obj_varlist, axis=0)
    col_vec = [0] * (num_of_slack + 1)
    col_vec[0] = 1
    arr[0] = -1* arr[0]
    arr = np.insert(arr, 0, col_vec, axis=1)

    len_varlist = len(varlist)
    for i in range(num_of_slack):
        varlist.append(f"x{i+len_varlist+1}")

    return arr, varlist, res_list, num_of_slack


if __name__ == "__main__":
    process_input_for_optimization()

