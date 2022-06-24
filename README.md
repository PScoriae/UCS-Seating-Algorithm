# Modified Uniform Cost Search Algorithm
Implementation of the Uniform Cost Search (UCS) algorithm with Python to find solutions to the table seating problem to position participants in the most optimal arrangement in a round table with the highest overall comfortability score.

## Requirements
All you need to run this program for **Python3** to be installed on your computer.

To execute the program:
- Simply run the ucs.py file via a terminal/command line
- At the prompt, enter the number of people you would like to seat or arrange.
- Finally, follow the instructions given.

The program will then create a **one way comfort value** matrix by assigning a randomised integer to each person where 5 is the most comfortable and -5 is the least comfortable.

Then, another matrix is made using the original one way comfort value matrix to determine the **two way comfort value matrix**.

Finally, the optimal solution(s) will be displayed:
- Optimal solution(s) and their overall comfort values
- The UCS' time taken in milliseconds rounded to 5 decimal places
- The number of steps taken to reach the solution(s).
