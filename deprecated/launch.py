#!python3
import sys
import subprocess

try:
	subprocess.run(['C:\\Users\\enado\\Proyectos\\Python33\\blrobot22\\redir.bat']) #or your own path
	print("Launching robot...")
	import precompute
	import fetch
	import seasonbuilder
	import computelocal
	import computevisitor #NEW
	import computetotall #NEW
	import computetotalv #NEW
	import injectsql
	#import injectsqllocal
	#import injectsqlvisitor



except IndexError:
	print("Error. La jornada no ha finalizado. Matchday not finished.", sys.exc_info()[0])

except OSError as err:
    print("OS error: {0}".format(err))

except ValueError:
    print("Could not convert data to an integer.", sys.exc_info()[0])

except KeyError:
	print(f"Error. No pasó la clave de un club. ¿Se jugó ya la jornada completa?", sys.exc_info()[0])
    
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise