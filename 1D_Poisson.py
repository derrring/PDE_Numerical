#For P,T matrix, we could use sparse matrix in scipy
import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

def solver_FE_1D_Poisson():
    # basis_type_trial == 101 :1D linear
    (P,T) = generate_PbTb()
    if basis_type_trial == 101:
        Pb = []
        Tb = []
    elif basis_type_trial == 102:

    boundarynodes = generate_boundarynodes()

    A = assemble_matrix_1D()

    b = assemble_vector_1D()

    (A,b) = treat_Dirichlet_boundary()

    solution = A/b

    error = compute_max_FE_nodes()
    pass

def generate_PbTb():
    pass


def assemble_matrix_1D():
    A = sp.sparse.

    for n in range(num_elements):
        for aplha in range(num_local_basis_func_trial):
            for beta in range(num_local_basis_func_test):

                int_value = Gauss_quadrature_1D_trial_test
                T(i,j) += int_value
    pass
