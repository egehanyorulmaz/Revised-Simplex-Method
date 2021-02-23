import json as js

# text processing (constraint_matrix (number_of_constraint, number_of_variables)
# objective function control ( min -> max ) [1, 2, 3] -> *-1 -> [-1, -2, -3]
# constraint control ( >= -> <=) for all constraints > *-1 > updated_constraint_matrix
# rhs of constraints will be controlled. (must be bi >= 0) -> if violated *-1
# slack variable adding -> constraint matrix, objective_constraint_vector will be updated.
# all_constraint_coef_matrix -> objective coefficient will be included. videonun 10. dakikasındaki olay
# elimizde 3 tane matrix var. coefficient_matrix, variable_vector, objective_coef_vector

def obj_func_control (dict):

    if dict["objective"] == "min":

        dict["objective_equation"]["values"] = [-1*a for a in dict["objective_equation"]["values"]]

        dict["objective"] = "max"

    return dict

def const_control(dict):

    newdict = dict

    for constraint in newdict["constraints"]:

        path = newdict["constraints"][constraint]

        if path["notation"][0].find(">=") != -1:

            path["values"] = [-1*a for a in path["values"]]
            path["notation"] = "<="

    print(newdict)

if __name__ == '__main__':
    json = open("Extraction.json")

    data = js.load(json)

    const_control(data)
