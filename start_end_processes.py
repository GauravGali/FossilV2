# runs while starting or ending a process
import pickle

def start_processes():
    with open('fsl_caches/memory_caches/fsl_memry_caches.bin' , 'wb') as fh: # creates empty {} for temp variables to get stored
        pickle.dump({} , fh)

def end_processes():
    with open('fsl_caches/memory_caches/fsl_memry_caches.bin' , 'wb') as fh: # erases cache file for fresh setup for rerun
        pass
    quit()