'''
Created on 20 May, 2015

@author: yzhang28
'''
import pickle
from experiment import Experiment
from parameters import Parameters
import myopic
from util import Util
import numpy as np

import sys
sys.path.append("..")

##################################################################
s_nothing, s_charger, s_messenger = [0], [1,2,3,4,5,6], [7,8,9,10,11,12]

charging_price = [-0.00, -1.00, -4.0, -9.0, -16.0, -25.0]
sending_prob = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
sending_gain = 15.0

if (len(s_charger) != len(charging_price)) or (len(s_messenger)!=len(sending_prob)):
    print "Error, head of main.py"
    exit(0)

csize = len(s_nothing) + len(s_charger) + len(s_messenger)
esize = 10
qsize = 10

inj_prob, charge_prob = 0.4, 0.9

discount = 0.9
##################################################################

para = Parameters(s_nothing, s_charger, s_messenger, \
                  charging_price, sending_prob, sending_gain,\
                  csize, esize, qsize, \
                  inj_prob, charge_prob, discount)
expt = Experiment(para)
util = Util(para)

R, P, vi = expt.Build_Problem('MDP')
vi.run()
print vi.policy

util.Action_2Dlized_Result(vi,['E','Q'],"EQ")
util.Action_2Dlized_Result(vi,['C','E'],"CE")