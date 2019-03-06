#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adam.gutonski
#
# Created:     04/03/2019
# Copyright:   (c) adam.gutonski 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, time, sys, arcpy, traceback, time
from datetime import datetime


def trace_error(pyscript):

    tb = sys.exc_info()[2]  #----> grab the traceback object, tuple of type which is a type of the exception being handled (class object)
                 #----> value is the exception paramter to raise, 3rd is tracback object which encapsulates teh call stack at the point where the exception occured

    tbinfo = traceback.format_tb(tb)[0] #----> format the traceback object to a list of strings, we get the trackback object as last of 3 item tuple
                                        #----> returned by sys.exc_info()...traceback.format_tb returns a list of pre_processed stack trace entries extracted from traceback object
                                        #----> We grab the first stack trace [0] index

    line = tbinfo.split(", ")[1]    #----> tbinfo will have a 4 tuple (filename, line num, func name, text) for the stack, so we
                                    #----> split along commas and grab the second tuple item [1] which is the line occurance of the error

    synerror = traceback.format_exc().splitlines(0)[-1] #----> format_exc() prints the exception information and trace entries from the traceback
                                                        #----> split lines splits by the \n character, the last line in the list now is the error report with associated error type
    arcerror = ''
    for i in range(len(traceback.format_exc().splitlines(0))):
        arcerror += '\n' + traceback.format_exc().splitlines(0)[-i]
        #arcerror += '\n' + traceback.format_exc().splitlines(0)[-3]
        #arcerror += '\n' + traceback.format_exc().splitlines(0)[-4]

    currentPath = os.path.split(sys.argv[0])[0]+"\ErrorLogs"

    currentFile = os.path.split(sys.argv[0])[1]
    filename = sys.path[0] + os.sep + pyscript

    return line, filename, synerror, arcerror

def error_report(pyscript, start_time):
    end = datetime.now() - start_time

    line, filename, synerror, arcerror = trace_error(pyscript)

    user = os.environ.get('USERNAME')

    report_path = os.path.split(sys.argv[0])[0] + os.sep + 'Error_Reporting'
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    arcpy.AddError('\nError at line ' + line + ' filename: ' + filename + '\n')
    log = open(report_path + os.sep + pyscript + '_reporting.txt', 'a')
    log.writelines('\n' + '*' * 50)
    log.writelines('\n' + 'User ' + user + ' experienced error at ' + line + ' in file ' + filename)
    log.writelines('\nTime: ' + time.asctime())
    log.writelines('\nPyError: ' + synerror)
    log.writelines('\nArcError: ' + arcerror)
    log.writelines('\nScript runtime: %s' % end)
    log.writelines('\n' + '*' * 50)

def report_good_run(pyscript, start_time):
    end = datetime.now() - start_time
    user = os.environ.get('USERNAME')
    report_path = os.path.split(sys.argv[0])[0] + os.sep + 'Error_Reporting'
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    log = open(report_path + os.sep + pyscript + '_reporting.txt', 'a')
    log.writelines('\n' + '*' * 50)
    log.writelines('\n' + user + " has succesfully run " + pyscript + ' at ' + time.asctime())
    log.writelines('\nScript runtime: %s' % end)
    log.writelines('\n' + '*' * 50)