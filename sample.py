import blueqat.wq as wq


a = wq.Opt()
a.dwavetoken = "your token here"
a.qubo = [[0,0,0,0,-4],[0,2,0,0,-4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,4]]
a.dw()
