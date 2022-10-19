#status of errors

def fsl_errors_tmplt(status , reason , buffer = None): # Errors Template
    print('Status : ' , status)
    print('Reason : ' , reason)
    if buffer != None:
        print('Buffer : ' , buffer )

def success(): # Success Message
    fsl_errors_tmplt('Processed Succesfully' , 'No Errors')

def file_not_fsl(): # File Not Found 
    fsl_errors_tmplt('Prossesor Terminated' , 'File not Fossil')


def line_not_worthy(lines): # Non Worthy Lines
    if len(lines) == 1:
        fsl_errors_tmplt('Processed Succesfully' , 'No Errors' , f'Line {lines} not worthy !')
    else:
        fsl_errors_tmplt('Processed Succesfully' , 'No Errors' , f'Lines {lines} not worthy !')        


def error_at_line(line): # Data Types Missing
    print()
    fsl_errors_tmplt('Processed Unsuccesfully' , f'Error at line {line}')
