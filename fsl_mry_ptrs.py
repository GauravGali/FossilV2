# storing variable values
import pickle

def fsl_memry_store(memory_pointer , store_value):
    
    memory = {} # temperory storage to manuplate and dump later

    with open('fsl_caches/memory_caches/fsl_memry_caches.bin' , 'rb') as fh: # getting previosly stores values and saving it in memory <dict>
        memory = pickle.load(fh)

    memory[memory_pointer] = store_value # storing / updating requested variable data

    with open('fsl_caches/memory_caches/fsl_memry_caches.bin' , 'wb') as fh: # saving the updated memory to the file
        pickle.dump(memory , fh)

def fsl_get_memry_from_store(memory_pointer):
    store_value = None

    with open('fsl_caches/memory_caches/fsl_memry_caches.bin' , 'rb') as fh: # getting previosly stores values and saving it in memory <dict>
        if memory_pointer == '!': # checking to print all variable values
            data = pickle.load(fh) # all data
            if data != {}: # returning all values if not empty
                store_value = data
        else:
            store_value = pickle.load(fh)[memory_pointer] # returning requested values

    return store_value