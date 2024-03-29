"""Power flow data for 10 nodes test case.
"""

from numpy import array
import numpy as np

class case_():

  def __init__(self):
    pass

  def case(self):

    ppc = {"version": '2'}

    ##-----  Power Flow Data  -----##
    ## system MVA base

    ppc["baseMVA"] = 1
    
    VMAX = 21
    VMIN = 19
    
    ppc["VMAX"] = VMAX
    ppc["VMIN"] = VMIN

    baseKV = 1
    
    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
		[1,  3,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
    [2,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[3,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[4,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[5,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[6,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
    [7,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[8,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[9,  1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
    [10, 1,	0.0,	0.0,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
        [1, 0,	0,	200, -200,   1,	 1,	 1,  200, -200,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [2, 0,	-0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		    [3, 0,	-0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		    [4, 0,	-0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [5,0,  -0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [6,0,  -0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [7, 0,	-0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		    [8, 0,	-0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		    [9, 0,	-0.0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [10,0,  -0.,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]
    ])


    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
		[1, 	   2,	0.0015,	   0.8e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[2, 	   3,	0.0017,	   1e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[3, 	   4,	0.0015,	   0.8e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[2,	     5,	0.0017,	   1e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[5,	     6,	0.0015,	   0.8e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[3,	     7,	0.0017,	   1e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[7,	     8,	0.0015,	   0.8e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[8,	     9,	0.0017,	   1e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
    [9,	     10,0.0015,	   0.8e-3,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360]
    ])

    ##-----  OPF Data  -----##
    ## generator cost data
    # 1 startup shutdown n x1 y1 ... xn yn
    # 2 startup shutdown n c(n-1) ... c0
    ppc["gencost"] = np.vstack([[2, 0, 0, 3, 0.01,      40, 0] for i in range(np.shape(ppc["gen"])[0])
    ])


    return ppc