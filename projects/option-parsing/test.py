import getopt
import sys

# set version, verbose, and output filename
# print out argv
# get options
# parse options
# print out all options recieved 

version = 1.0
verbose = False
output_filename = "default.out"

print "argv: %s"%sys.argv

opts, remainder = getopt.getopt(sys.argv[1:], 'o:vabc', ['version=', 'verbose', 'output='])

a = b = c = False

for (option, value) in opts:
    if option in ('-o', '--output'):
        output_filename = value    
    elif option in ('-v', '--verbose'):
        verbose = True
    elif option in ('--version'):
        version = value
    elif option in ('-a'):
        a = True
    elif option in ('-b'):
        b = True
    elif option in ('-c'):
        c = True

print "Options: %s, Remainder: %s"%(opts, remainder)

print
print "Version: %s"%version
print "Verbose: %s"%verbose
print "Output Filename: %s"%output_filename
print "a flag: %s"%a
print "b flag: %s"%b
print "c flag: %s"%c


