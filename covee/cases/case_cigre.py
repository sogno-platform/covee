"""Power flow data for CIGRE MV European Network test case.
"""

from numpy import array

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

    baseKV = 20;
    
    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
		[1,  3,	0.160,	0.080,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [2,  1,	0.040,	0.020,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[3,  1,	0.2764,	0.008,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[4,  1,	0.4316,	0.013,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[5,  1,	0.7275,	0.022,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[6,  1,	0.5481,	0.016,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[7,  1,	0.040,	0.020,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[8,  1,	0.5868,	0.018,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[9,  1,	0.020,	0.010,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[10, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[11, 1,	0.0329,	0.010,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
        [1, 0,	0,	200, -200,  1,	1,	1,  200, -200,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		[3, 0.20,	0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [4, 0.20,	0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		[5, 0.30,	0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		[6, 0.30,	0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [7, 1.600,	0,	200, -200,	 1,	 1,	 1,	 0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
		[8, 0.30,   0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [9, 0.20,   0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [10, 0.150, 0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [11, 0.10,  0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ])


    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
		[1, 	 2,	0.0035,	        0.0050,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[2,	     3,	0.0035,	        0.0050,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[3,	     4,	7.51E-004,	    0.0012,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[4,	     5,	7.51E-004,	    0.0012,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[5,	     6,	0.0019,	        0.0027,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[3,	     8,	0.0016,	        0.0023,	    	0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[8,	     7,	0.0021,     	0.0030,     	0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[8,	     9, 3.75E-004,	    5.36E-004,      0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[9,	    10, 0.0010,	        0.0014,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[10, 	11,	3.75E-004,	    5.36E-004,      0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360]
    ])

    ##-----  OPF Data  -----##
    ## generator cost data
    # 1 startup shutdown n x1 y1 ... xn yn
    # 2 startup shutdown n c(n-1) ... c0
    ppc["gencost"] = array([
        [2, 0, 0, 3, 0.0430293, 20, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0],
        [2, 0, 0, 3, 0.01,      40, 0]
    ])

    return ppc