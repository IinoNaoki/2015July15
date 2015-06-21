'''
Created on 22 Apr, 2015

@author: yzhang28
'''

import pickle
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import FuncFormatter
from matplotlib.transforms import Bbox
import sys
from matplotlib.lines import fillStyles
from matplotlib.markers import MarkerStyle
from matplotlib.backends.backend_pdf import PdfPages

import sys
sys.path.append("..")

TEST_SET = pickle.load(open("../rawresults/ESize/TEST_SET","r"))
x_axis = pickle.load(open("../rawresults/ESize/TEST_RANGE","r"))
# TEST_SET = ['MDP', 'CAS', 'GREEDY', 'RANDOM', 'THRESHOLDRANDOM']

exp_v, steady_v, steady_chg_r, steady_snd_r = [],[],[],[]
steady_estate = []
for j,t in enumerate(TEST_SET): 
    exp_v.append(pickle.load(open("../rawresults/ESize/exp_value_lis_"+'_'+t,"r")))
    steady_v.append(pickle.load(open("../rawresults/ESize/steady_value_lis"+'_'+t,"r")))
    steady_chg_r.append(pickle.load(open("../rawresults/ESize/steady_chg_rate_lis_"+'_'+t,"r")))
    steady_snd_r.append(pickle.load(open("../rawresults/ESize/steady_snd_rate_lis_"+'_'+t,"r")))
    steady_estate.append(pickle.load(open("../rawresults/ESize/steady_estate_lis_"+'_'+t,"r")))

plt.figure(figsize=(4.5,5.0))
grid(True, which="both")
plot(x_axis,exp_v[0],color='red',markerfacecolor='none', markeredgecolor='red', marker='o',markersize=8,label='MDP')
plot(x_axis,exp_v[1],color='green',markerfacecolor='none', markeredgecolor='green', marker='^',markersize=8,label='CAT')
plot(x_axis,exp_v[2],color='blue',markerfacecolor='none', markeredgecolor='blue', marker='s',markersize=8,label='GRD')
plot(x_axis,exp_v[3],color='black',markerfacecolor='none', markeredgecolor='black', marker='x',markersize=8,label='RND', linestyle='')
plot(x_axis,exp_v[4],color='magenta',markerfacecolor='none', markeredgecolor='magenta', marker='d',markersize=8,label='THR', linestyle='')
xlabel('Maximum energy capacity $E$',fontsize=14)
ylabel('Expected utility',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best', ncol=1,fancybox=True,shadow=True)
ylim([-3,26])
# legend(loc='best',fancybox=True)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
pp = PdfPages('ESize_figure1.pdf')
plt.savefig(pp, format='pdf')
pp.close()


plt.figure(figsize=(4.5,5.0))
grid(True, which="both")
plot(x_axis,steady_chg_r[0],color='red',markerfacecolor='none', markeredgecolor='red', marker='o',markersize=8,label='MDP (Charge)',linestyle='--')
plot(x_axis,steady_chg_r[1],color='green',markerfacecolor='none', markeredgecolor='green', marker='^',markersize=8,label='CAT (Charge)',linestyle='--')
plot(x_axis,steady_chg_r[2],color='blue',markerfacecolor='none', markeredgecolor='blue', marker='s',markersize=8,label='GRD (Charge)',linestyle='--')
# plot(x_axis,steady_chg_r[3],color='black',markerfacecolor='none', markeredgecolor='black', marker='x',markersize=8,label='RND', linestyle='')
# plot(x_axis,steady_chg_r[4],color='magenta',markerfacecolor='none', markeredgecolor='magenta', marker='d',markersize=8,label='THR', linestyle='')

plot(x_axis,steady_snd_r[0],color='red',markerfacecolor='none', markeredgecolor='red', marker='o',markersize=8,label='MDP (Transfer)')
plot(x_axis,steady_snd_r[1],color='green',markerfacecolor='none', markeredgecolor='green', marker='^',markersize=8,label='CAT (Transfer)')
plot(x_axis,steady_snd_r[2],color='blue',markerfacecolor='none', markeredgecolor='blue', marker='s',markersize=8,label='GRD (Transfer)')
plot(x_axis,steady_snd_r[3],color='black',markerfacecolor='none', markeredgecolor='black', marker='x',markersize=8,label='RND (Transfer)', linestyle='')
plot(x_axis,steady_snd_r[4],color='magenta',markerfacecolor='none', markeredgecolor='magenta', marker='d',markersize=8,label='THR (Transfer)', linestyle='')

xlabel('Maximum energy capacity $E$',fontsize=14)
ylabel('Charging/Sending rate',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc=(0.15,0.4), ncol=2,fancybox=True,shadow=True,fontsize=10)
ylim([0.05,0.43])
# legend(loc='best',fancybox=True)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
pp = PdfPages('ESize_figure3.pdf')
plt.savefig(pp, format='pdf')
pp.close()

plt.figure(figsize=(4.5,5.0))
grid(True, which="both")
plot(x_axis,steady_estate[0],color='red',markerfacecolor='none', markeredgecolor='red', marker='o',markersize=8,label='MDP')
plot(x_axis,steady_estate[1],color='green',markerfacecolor='none', markeredgecolor='green', marker='^',markersize=8,label='CAT')
plot(x_axis,steady_estate[2],color='blue',markerfacecolor='none', markeredgecolor='blue', marker='s',markersize=8,label='GRD')
plot(x_axis,steady_estate[3],color='black',markerfacecolor='none', markeredgecolor='black', marker='x',markersize=8,label='RND', linestyle='')
plot(x_axis,steady_estate[4],color='magenta',markerfacecolor='none', markeredgecolor='magenta', marker='d',markersize=8,label='THR', linestyle='')
xlabel('Maximum energy capacity $E$',fontsize=14)
ylabel('Average energy level',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best', ncol=1,fancybox=True,shadow=True)
ylim([0.0,4.4])
# legend(loc='best',fancybox=True)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
pp = PdfPages('ESize_figure4.pdf')
plt.savefig(pp, format='pdf')
pp.close()
