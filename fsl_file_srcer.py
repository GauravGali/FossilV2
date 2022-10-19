#fsl file sourcer
from fsl_errors_sts import file_not_fsl

file = input('Fossil : ') #source of the file
if file.endswith('.fsl') == False:
    file_not_fsl()
    quit()

def fsl_file_data(): #returning the proccessed file data
    modified_to_fsl_formated_data = []
    for line in file_data:
        modified_to_fsl_formated_data.append([line])
    return modified_to_fsl_formated_data

file_data = None 
with open(file , 'r') as fh: #reading the fsl src
    file_data = fh.readlines()
    