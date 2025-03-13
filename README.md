# Calc_Demo_Pair-Programming

## Description  
This is a command-line math quiz application that generates 10 randomized arithmetic problems per round. Built with Python for simplicity and efficiency.

## Key Features  
- **Dynamic Question Generation**:  
  - Combines 3-5 random numbers (0-100) with mixed operations (`+`, `-`, `*`, `/`).
  - Automatic regeneration of invalid expressions (e.g., division by zero).  
- **Flexible Input Handling**:  
  - Accepts floating-point answers with ±0.1 tolerance.  
  - Empty inputs allowed (counted as incorrect).  
- **Performance Analytics**:  
  - Total completion time.  
  - Score (correct answers/10).  
  - Detailed review of mistakes.  
- **Repeatable Sessions**: Continue indefinitely or exit after any round.

### How to use:
Generates a valid expression using Channel_Operation_Gen().
Enter numerical answers or press ENTER to skip (marked wrong).

Compares user input against eval()-computed result with tolerance.

Tracks errors and compiles post-quiz statistics via Statistics().

See time elapsed, score, and incorrect answers with solution.

Press any key to retry or q to exit.


### Functions: 
- Number_Generator(): Returns a random integer (0-100).
- Operation_Generator(): Randomly picks +, -, *, or /.
- Channel_Operation_Gen(): Builds multi-operation expressions (e.g., 5 + 3 * 2).
- start(): Manages quiz flow, timing, and user input.
- Menu(): It print the message to ask to the user if retry the quizzes or stop.
- Statistics(): Show the statistics.
