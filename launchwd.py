#!python3
"""Import packages"""
import sys
import subprocess

try:
    # Run the batch file to set up redirection
    # ON PC
    subprocess.run(['C:\\Users\\enado\\blrobot26\\redir.bat'], check=False)
    # ON LAPTOP
    #subprocess.run(['C:\\Users\\enado\\Proyectos\\Python33\\blrobot26\\redir.bat'], check=False)
    #subprocess.run(['C:\\Users\\enado\\blrobot25\\redir.bat'], check=False) #or your own path
    print("Launching robot...")
    import precomputewd
    import fetchwd
    import seasonbuilderwd
    import computelocal
    import computevisitor #NEW
    import computetotall #NEW
    import computetotalv #NEW
    import injectsqlwd
    #import injectsqllocal
    #import injectsqlvisitor

except IndexError:
    print("Error. La jornada no ha finalizado. Matchday not finished.", sys.exc_info()[0])

except OSError as err:
    print("OS error: {0}".format(err))

except ValueError:
    print("Could not convert data to an integer.", sys.exc_info()[0])

except KeyError:
    print("Error. No pasó la clave de un club. ¿Se jugó ya la jornada completa?", sys.exc_info()[0])

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
