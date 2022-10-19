# subprocesses in fsl
from fsl_mry_ptrs import fsl_memry_store , fsl_get_memry_from_store
from fsl_errors_sts import error_at_line
from start_end_processes import end_processes

def concat_with_space(lis): # joins literals previously seperated by lexer
    word = ''
    for i in lis:
        word += i
        word += ' '

    return word

def fsl_print_stmt(in_line_litrl , in_line_kwrd , in_line_idfrs , line):
    try: # fsl print statement
        if len(in_line_kwrd) == 1:
            return concat_with_space(in_line_litrl)
        elif in_line_kwrd[1] == 'var':
            if in_line_idfrs[0] == '!': # checking for all variabes request
                all_memory = fsl_get_memry_from_store(in_line_idfrs[0])
                return all_memory
            else: # returning requested values
                memory_stored = fsl_get_memry_from_store(in_line_idfrs[0])
                return memory_stored
    except:
        error_at_line(line + 1) # error message
        end_processes()

def fsl_printas_stmt(in_line_data):
    line = in_line_data[0].split() # seperating each word in line
    line_litrl = line[1:len(line)+1] # obtaining the literal
    return concat_with_space(line_litrl) # converting from list to string

def fsl_decl_stmt(in_line_datatype , in_line_identifier , in_line_literal , line): # fsl decl statement
    literal = concat_with_space(in_line_literal) # concatinating different multiple literals

    try:
        if in_line_datatype != []: # checking if datatype is defines
    
            if in_line_datatype[0] == 'int': # checking for int datatype
                fsl_memry_store(in_line_identifier[0] , int(float(literal)))
            elif in_line_datatype[0] == 'flt': # checking for float datatype
                fsl_memry_store(in_line_identifier[0] , float(literal))
            elif in_line_datatype[0] == 'str': # checking for string datatype
                fsl_memry_store(in_line_identifier[0] , str(literal))
            else:
                pass
        else: # if data type is not mentioned then default str will be taken
            fsl_memry_store(in_line_identifier[0] , str(literal)) # by default datatype is string

    except:
        error_at_line(line + 1)
        end_processes()

    return