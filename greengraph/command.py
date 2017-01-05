from matplotlib import pyplot as plt
from argparse import ArgumentParser
from .graph import Greengraph

def process():
    parser = ArgumentParser(description = "Generate  a graph of the proportion of green pixels in a series of satellite images between two points")
    parser.add_argument('--begin')
    parser.add_argument('--end')
    parser.add_argument('--steps')
    parser.add_argument('--out')

    arguments = parser.parse_args()    

    mygraph=Greengraph(arguments.begin, arguments.end)
    data = mygraph.green_between(arguments.steps)
    
    fig = plt.plot(data)
    fig = plt.savefig(arguments.out)
    
if __name__ =="__main__":
    process()