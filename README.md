<div align='center'>

# Uniform Cost Search Seating Algorithm

<p>
  <a href="https://linkedin.com/in/pierreccesario">
    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555">
  </a>
  
  <a href="https://github.com/PScoriae/UCS-Seating-Algorithm/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-WTFPL-brightgreen?style=for-the-badge">
  </a>
</p>

</div>

# About

A Python3 CLI implementation of the Uniform Cost Search (UCS) algorithm.

The objective of this modified UCS is to find solutions to the table seating problem to position participants in the most optimal arrangement in a round table with the highest overall comfortability score. Comfortability score is determined by the affinity of people seated beside each other.

For a more detailed writeup and explanation of how this algorithm works, please read the included [report](https://github.com/PScoriae/UCS-Seating-Algorithm/blob/main/report.pdf).

# Prerequisites

You'll need to install **Python3** on your system to run this program. Consult the [official website](https://www.python.org/downloads/) for installation instructions.

# Installation

Simply `git clone` this repository,

    git clone https://github.com/PScoriae/MastermindPy

or copy the code in [`main.py`](https://github.com/PScoriae/MastermindPy/blob/master/main.py) into a `.py` file onto your system.

There are no dependencies to install since the program only makes use of the standard library.

# Running the Program

First, open a terminal in the project's root directory. Then, `cd` into the `src` folder like so:

    cd src

Finally, run the following command:

    python3 main.py

# Program Flow

1. Program starts.

2. At the prompt, enter the number of people you would like to seat or arrange.

3. The program will then create a **one way comfort value** matrix by assigning a randomised integer to each person where 5 is the most comfortable and -5 is the least comfortable.

4. Then, another matrix is made using the original one way comfort value matrix to determine the **two way comfort value matrix**.

5. Finally, the optimal solution(s) will be displayed:
   - Optimal solution(s) and their overall comfort values
   - The UCS' time taken in milliseconds rounded to 5 decimal places
   - The number of steps taken to reach the solution(s).
