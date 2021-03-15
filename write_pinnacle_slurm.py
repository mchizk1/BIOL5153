#! /usr/bin/env python3

# This script generates a .slurm file for the AHPCC Pinnacle cluster

# These variable are inputs for the job
name = 'tmchizk_$JOBID'
queue = 'comp06'
prefix = name
nodes = 1
processors = 1
wall = 1
modules = ''

# Scheduling the job and setting options  
print('#SBATCH -J', name)
print('#SBATCH --partition', queue)
print('#SBATCH -oe', prefix) 
print('#SBATCH --nodes=' + str(nodes))
print('#SBATCH --cpus-per-task=' + str(processors))
print('#SBATCH --ntasks-per-node=32')
print('#SBATCH --time='+ str(wall) +':00:00')
print()
 
# load required modules
print('module load',modules)
print()
 
# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')
print()

# Job commands go here


