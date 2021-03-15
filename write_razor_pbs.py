#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster

# define some variables
name = 'tmchizk.$PBS_JOBID'
queue = 'med16core'
prefix = name
nodes = 1
processors = 1
wall = 3 # this is in hours
modules = ''

# This section prints the header/required info for the PBS script
print('#PBS -N', name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o', prefix) # set the name of the job output file
print('#PBS -l nodes=' + str(nodes) + ':ppn=' + str(processors)) # how many resources to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

# Cd into working directory
print('cd $PBS_O_WORKDIR')
print()

#load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1', modules)
print()

# commands for this job
print('# insert commands here')