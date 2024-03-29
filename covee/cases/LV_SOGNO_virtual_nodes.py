"""Power flow data for LV grid in doi: 10.1109/TSG.2014.2303580.
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
    
    VMAX = 0.4*1.05
    VMIN = 0.4*0.95
    
    ppc["VMAX"] = VMAX
    ppc["VMIN"] = VMIN

    baseKV = 0.4;
    
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
		[11, 1,	0.0329,	0.010,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]   ,
		[12, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[13, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
		[14, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [15, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [16, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [17, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [18, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [19, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [20, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [21, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [22, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	,
        [23, 1,	0.4753,	0.014,	0.000,	0.000,	1,	1,	0,	baseKV,	1,	VMAX,	VMIN]	        
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
        [1, 0,	0,	200, -200,  1,	1,	1,  200, -200,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [19, 0.20, 0, 200, -200, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [20, 0.20,   0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [21, 0.150, 0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [22, 0.150, 0, 200, -200, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [23, 0.10,  0,  200, -200,   1,  1,  1,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ])


    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
		[1, 	 2,	 0.0004	,              0.003172,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[2,	     3,	 0.00108675	,          0.0004095,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[3,	     4,	 0.0004269375	,      0.000160875,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[4,	     5,  0.00087975	,          0.0003315,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[5,	     6,	 0.0009315	,          0.000351,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[3,	     7,	 0.0013584375	,      0.000511875,	    	0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[7,	     8,	 0.0000388125	,      0.000014625,     	0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[7,	     9,  0.0006856875	,      0.000258375,         0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[7,	    10,  0.00098325	,          0.0003705,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
		[7, 	11,	 0.0007115625	,      0.000268125,         0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [10,	12,  0.00098325	,          0.0003705,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [10,	13,  0.0007245	,          0.000273,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [13,	14,  0.000414	,          0.000156,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [11,	15,  0.000905625	,      0.00034125,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [15,	16,  0.000802125	,      0.00030225,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [15,	17,  0.000336375	,      0.00012675,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [17,	18,  0.0006598125	,      0.000248625,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [18,	19,  0.0005304375	,      0.000199875,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [19,	20,  0.0008150625	,      0.000307125,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [20,	21,  0.000336375	,      0.00012675,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [21,	22,  0.00025875	,          0.0000975,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360],
        [22,	23,  0.0004528125	,      0.000170625,	        0.01E-008,	            300,	300,	300,	0,	0,	1,	-360,	360]
    ])

    ##-----  OPF Data  -----##
    ## generator cost data
    # 1 startup shutdown n x1 y1 ... xn yn
    # 2 startup shutdown n c(n-1) ... c0
    ppc["gencost"] = array([
        [2, 0, 0, 3, 0.0430293, 20, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0]
    ])

    return ppc