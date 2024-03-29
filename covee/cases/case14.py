"""Power flow data for IEEE 14 bus test case.
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

    ppc["baseMVA"] = 100
    
    VMAX = 1.06
    VMIN = 0.96
    
    ppc["VMAX"] = VMAX
    ppc["VMIN"] = VMIN
    baseKV = 1
    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
		[1,  3,	0.160,	0.080,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[2,  1,	0.020,	0.010,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[3,  1,	0.120,	0.060,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[4,  1,	0.100,	0.050,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[5,  1,	0.040,	0.020,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[6,  1,	0.040,	0.020,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[7,  1,	0.000,	0.000,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[8,  1,	0.020,	0.010,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[9,  1,	0.020,	0.010,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[10, 1,	0.000,	0.000,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[11, 1,	0.020,	0.010,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[12, 1,	0.040,	0.020,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[13, 1,	0.040,	0.020,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	,
		[14, 1,	0.075,	0.035,	0.000,	0.000,	1,	1,	0,	4.16,	1,	VMAX,	VMIN]	
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
        [1, 0,	0,	200, -200,  1,	1,	1,  200, -200,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [2, 0,	0,	0.0,	0, 	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [3, 0,	0,	0.0,    0,	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [4, 0,  0,  0.,    0,  1,  1,  1,  0,      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [5, 0,	0,	0.0,	0, 	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [6, 0,	0,	0.0,    0,	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [7, 0,  0,  0.,    0,  1,  1,  1,  0,      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [8, 0,	0,	0.0,	0, 	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [9, 0,	0,	0.0,    0,	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [10, 0,  0,  0.,    0,  1,  1,  1,  0,      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [11, 0,  0,  0.,    0,  1,  1,  1,  0,      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [12, 0,	0,	0.0,	0, 	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [13, 0,	0,	0.0,    0,	1,	1,	1,	0,  	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
        [14, 0,  0,  0.,    0,  1,  1,  1,  0,      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],

    ])

    ## branch data
    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
		[1, 	 2,	0.0013398623,	0.0027450827,	3.02770271595392E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[2,	     3,	0.0010048967,	0.0020588120,	2.27077703696544E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[3,	     4,	0.0006699312,	0.0013725413,	1.51385135797696E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[4,	     5,	0.0010048967,	0.0020588120,	2.27077703696544E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[5,	     6,	0.0013398623,	0.0027450827,	3.02770271595392E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[6,	     7,	0.0006699312,	0.0013725413,	1.51385135797696E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[7,	     8,	0.0004187070,	0.0008578383,	9.46157098735599E-009,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[8,	     9,	0.0009211553,	0.0018872444,	2.08154561721832E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[9,	    10, 0.0009211553,	0.0018872444,	2.08154561721832E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[10,	11, 0.0011723795,	0.0024019474,	2.64923987645968E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[11, 	12,	0.0025122418,	0.0051470300,	5.67694259241360E-008,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[12, 	13,	0.0027749546,	0.0013221274,	1.83926822251266E-007,	100,	100,	100,	0,	0,	1,	-360,	360],	
		[13, 	14,	0.0019424682,	0.0009254892,	1.28748775575886E-007,	100,	100,	100,	0,	0,	1,	-360,	360]		
    ])

    ppc["gencost"] = np.vstack([[2, 0, 0, 3, 0.01,      40, 0] for i in range(np.shape(ppc["gen"])[0])
    ])

    return ppc
