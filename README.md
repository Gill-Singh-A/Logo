# Logo
A Program made in Python that generates a Circular logo based on the given inputs

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* pygame
* math
* time
* random
* optparse
* datetime
* colorama
<!-- -->
Install the dependencies:
```bash
pip install -r requirements.txt
```

## Input
It takes in 5 command line arguments:
* '-r', "--resolution" : Side of the Sqaure (in pixels, Default=800)
* '-c', "--circles" : Number of Circles to Draw
* '-a', "--angle" : Angle of Sector (in degrees)
* '-d', "--delay" : Delay between drawing 2 consecutive Lines
* '-s', "--save" : Name of the File in which the Image has to be stored (Default=current date and time)
* '-C', "--draw-circles" : Draw Circles (True/False, Default=True)
* '-R', "--random" : Draw an object with a probability (Between [0, 1])

## Output
It will display the Image in a new Window and will write the Image File depending upon the argument provided.