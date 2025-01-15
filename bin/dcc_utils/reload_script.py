import sys
dir = 'H:/git-dev/pylab/bin/qt'
if dir not in sys.path:
    sys.path.append(dir)
try:
    reload(makeCube)
except:
    import makeCube
makeCube.main()
