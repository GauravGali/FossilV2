# processing fsl data
from fsl_sub_processes import fsl_print_stmt , fsl_printas_stmt , fsl_decl_stmt


def processor(tokenized_file_data , line , plain_data_in_line = None):
    in_line_kwrds = tokenized_file_data[line]['keywords'] # [line][attribute]
    in_line_datps = tokenized_file_data[line]['datatypes']
    in_line_litrls = tokenized_file_data[line]['literals']
    in_line_idntfrs = tokenized_file_data[line]['identifiers']
    in_line_pnctrs = tokenized_file_data[line]['punctuators']
    in_line_oprtrs = tokenized_file_data[line]['operators']

    result = None # incase line can't be processed

    if in_line_kwrds[0] == 'print': # checking and executing for print statement
        result = fsl_print_stmt(in_line_litrls , in_line_kwrds , in_line_idntfrs , line)

    elif in_line_kwrds[0] == 'printas': # checking for executing for printas statement
        result = fsl_printas_stmt(plain_data_in_line)

    elif in_line_kwrds[0] == 'decl':
        fsl_decl_stmt(in_line_datps , in_line_idntfrs , in_line_litrls , line) # storing variable values in cache

    elif in_line_kwrds[0] == 'end' :
        result = 'Terminate'
        
    else:
        pass

    return result