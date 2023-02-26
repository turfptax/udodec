# udodec
udodec is a MicroPython module that controls an NeoPixel LED Dodecahedron using 'Right, Left, and Back' commands. Its focus is to be a recursive way to program animations on a dodecahedron that is a Non-Eulerian path object.

## Usage
To use udodec, you first need to import the module in your MicroPython project:

```python
import udodec
```

Then, you can control the dodecahedron by appending commands to the pixel list. Each command is a list with the following parameters:

- edge: the edge of the dodecahedron where the pixel should be placed (an integer between 0 and 29).
- pixel_location: the location of the pixel on the edge (a float between 0 and 1).
- length: the length of the animation in seconds.
- speed: the speed of the animation (a float between 0 and 1).
- pattern: the pattern of the animation (a string).
- adjustment: the adjustment of the animation (an integer).
- ttl: the time-to-live of the animation in seconds (an integer).

Here's an example of how to add a command to the pixel list:

```python
import udodec
# To run the animations, you can use a for loop to iterate over the pixel list:
udodec.pixel.append([0, 0.5, 1, 1, "fade", 0, 10])

udodec.pixel.append()
for i in range(100):
    udodec.move()
```
# License
udodec is released under the MIT License. See LICENSE for more information.

# Contributing
Contributions to udodec are welcome! Please see CONTRIBUTING.md for more information.

# Acknowledgments
udodec was inspired by the Dodecahedron from harifun on youtube.
