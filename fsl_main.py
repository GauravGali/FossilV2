#executer
from fsl_file_srcer import fsl_file_data
from fsl_lexer import tokenize , buffer_lines
from fsl_errors_sts import success , line_not_worthy
from fsl_processes import processor
from start_end_processes import start_processes , end_processes

keywords = ['print' , 'printas' , 'decl' , 'var' , 'block' , 'end' , 'get' , '!' , 'imut']
datatypes = ['int' , 'flt' , 'str' , 'null' , 'dynamic']
identifiers = []
punctuators = ['{' , '}']
operators = ['=' , '+' , '-' , '/' , 'flr' , 'rem']

#start
start_processes() # creates memory cache files for storing in session data

tokenized_fsl_file_data = tokenize(fsl_file_data() , keywords , datatypes , identifiers , punctuators , operators)

# Output
print()
for line in tokenized_fsl_file_data: # processign each line
    result = processor(tokenized_fsl_file_data , line , fsl_file_data()[line]) # getting proccesed data from proccesor
                                                        # content in the line
    if result == 'Terminate': # Terminates Processing when called
        break

    if result != None:                                  
        print(result)

#end
print()


buffered = buffer_lines(keywords) # lines which are not worthy

if buffered == []: # checking for un-worthy lines
    success()
else:
    line_not_worthy(buffered)

end_processes() # deletes all memory caches stored during session