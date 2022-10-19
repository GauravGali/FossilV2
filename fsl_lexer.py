#lexer
from fsl_file_srcer import fsl_file_data


def tokenize( file_data , keywords , datatypes , identifiers , punctuators , operators): #tokenizes the entire fsl file

    tokenized_data = {} #the tokenized data

    line_count = 0 #the worthy lines count

    for line in file_data:
        in_fsl_kwrds = [] #keywords in fsl file
        in_fsl_datps = []
        in_fsl_idntfrs = [] #identifiers in fsl file
        in_fsl_pnctrs = [] #punctuators in fsl file
        in_fsl_oprtrs = [] #operators in fsl file
        in_fsl_litrls = [] #literals in fsl file

        line = line[0].split() #seperates line into tokens
        if line == []:
            continue

        for word in line: #scanning each line

            if 'var' in line: #checking for identifiers
                if line.index('var') == line.index(word)-1:
                    in_fsl_idntfrs.append(word)
            

            if word in keywords: #checking for keywords
                in_fsl_kwrds.append(word)
            elif word in identifiers: #checking for pre-defined identifiers 
                in_fsl_idntfrs.append(word)
            elif word in punctuators: #checking for punctuators
                in_fsl_pnctrs.append(word)
            elif word in operators: #checking for operators
                in_fsl_oprtrs.append(word)
            elif word in datatypes: #checking for data types
                in_fsl_datps.append(word)
            elif word in punctuators:
                in_fsl_pnctrs.append(word)
            else: #seperating literals and comments
                if word not in in_fsl_idntfrs and len(in_fsl_idntfrs) + len(in_fsl_kwrds) + len(in_fsl_oprtrs) + len(in_fsl_pnctrs) != 0: #checking if line is interpreting worthy
                    if word == '..': #checking comments
                        break
                    else:
                        in_fsl_litrls.append(word)
                    
        if len(in_fsl_idntfrs) + len(in_fsl_kwrds) + len(in_fsl_oprtrs) + len(in_fsl_pnctrs) != 0: #checking for non-worthy lines before saving tokens
            tokenized_data[line_count] = {'keywords' : in_fsl_kwrds , 'datatypes' : in_fsl_datps , 'literals' : in_fsl_litrls , 'identifiers' : in_fsl_idntfrs , 'punctuators' : in_fsl_pnctrs , 'operators' : in_fsl_oprtrs}
            line_count += 1
        
    return tokenized_data

def buffer_lines(kwrds): # checking for buffers in file
    data = fsl_file_data() # file data

    line_count = 1 # line counter for future reference

    for line in data: # iterating to check for unworthy lines
        if line != ['\n']: # to check for last line to avoid error
            kwrd = line[0].split()[0]
            
            if kwrd not in kwrds and kwrd != '..': # verifying un-worthy lines
                buffer.append(line_count)
        
        line_count += 1 # updating line count

    return buffer

buffer = [] # buffer lines not worthy
