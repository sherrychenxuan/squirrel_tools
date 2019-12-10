from gurobipy import *

try:

    # Create a new model
    m = Model("example4")

    # Create variables
    x11 = m.addVar(vtype=GRB.CONTINUOUS, name="x11", lb=0)
    x12 = m.addVar(vtype=GRB.CONTINUOUS, name="x12", lb=0)
    x13 = m.addVar(vtype=GRB.CONTINUOUS, name="x13", lb=0)
    x21 = m.addVar(vtype=GRB.CONTINUOUS, name="x21", lb=0)
    x22 = m.addVar(vtype=GRB.CONTINUOUS, name="x22", lb=0)
    x23 = m.addVar(vtype=GRB.CONTINUOUS, name="x23", lb=0)

    # Integrate new variables
    m.update()

    # Set objective
    m.setObjective(10*x11 + 12*x12 + 14*x13 + 11*x21 + 12*x22 + 13*x23, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(x11 + x12 + x13 <= 100, "c0")
    m.addConstr(x21 + x22 + x23 <= 200, "c1")
    m.addConstr(x11 + x21 >= 50, "c2")
    m.addConstr(x12 + x22 >= 100, "c3")
    m.addConstr(x13 + x23 >= 150, "c4")

    # Optimize (model is updated when we optimize)
    m.optimize()

    #print model status (2 is optimal)
    #https://www.gurobi.com/documentation/6.5/refman/optimization_status_codes.html
    print 'Model status:', m.status

    #print decision variables
    for v in m.getVars():
        print v.varName, v.x

    #print objective function value
    print 'Obj:', m.objVal

except GurobiError:
    print 'Error reported'
