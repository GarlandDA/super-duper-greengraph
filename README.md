Howdy!
======
The package you have downloaded can be used to generate a graph of the proportion of green pixels in a series of satellite images between two locations. 

To pip install, use the following line in an appropriate command prompt/ bash shell/ terminal:
pip install git+https://github.com/GarlandDA/super-duper-greengraph

The user need only input three arguments (*) from a command line to use greengraph:
- begin: name of place, e.g. 'New York' or 'Nicosia' (the user needs to include '' for places specified by more than one word)
- end: name of place, e.g. 'Boston' or 'Limassol'
- steps: number of equally spaced points between the endpoints (begin, end) specified, e.g. 30
- out: name of file graph should be saved as, e.g. graph.png

The command needed is:
greengraph --begin * --end * --steps * --out *