#a script to run several replicates of several treatments locally
#RUN SIMPLE_REPEAT.PY FROM WITHIN THE FOLDER WHERE THE DATA SHOULD GO
#EX: INSIDE OF SymbulationEmp/Data, RUN python3 ../stats_scripts/simple_repeat.py
import sys

plrs = [0.0, 0.025, 0.05, 0.075, 0.1] #prophage loss rates

import subprocess

def cmd(command):
    '''This wait causes all executions to run in sieries.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    return subprocess.Popen(command, shell=True).wait()

def silent_cmd(command):
    '''This wait causes all executions to run in sieries.                          
    For parralelization, remove .wait() and instead delay the                      
    R script calls unitl all neccesary data is created.'''
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()

start_range = 10
end_range = 21

if(len(sys.argv) > 1):
    start_range = int(sys.argv[1])
    if(len(sys.argv) > 2):
        end_range = int(sys.argv[2]) + 1
    else:
        end_range = start_range + 1

seeds = range(start_range, end_range)

print("Using seeds", start_range, "through", end_range-1)

for a in seeds:
    for b in plrs:
        command_str = './symbulation_lysis -SEED '+str(a)+' -PROPHAGE_LOSS_RATE '+str(b)+' -FILE_NAME PLR'+str(b)
        settings_filename = "Output_PLR"+str(b)+"_SEED"+str(a)+".data"
        print(command_str)
        cmd(command_str+" > "+settings_filename)
