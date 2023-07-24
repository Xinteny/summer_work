import os
import sys
import runpy

# cd to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

args = 'python test.py args1 args2'

args = args.split()

if args[0] == 'python': 
    args.pop(0)

if args[0] == '-m':
    args.pop(0)
    fun = runpy.run_module
else:
    fun = runpy.run_path
sys.argv.extend(args[1:])
fun(args[0], run_name='__main__')