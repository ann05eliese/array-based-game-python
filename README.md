# Tic-Tac-Toe

## Features
* **Dynamic 2D Array Rendering:** Translates a matrix containing structural board dividers (`|`) and underscores (`_`) serving as placeholders, into a clean game board that prints to the terminal.
* **Layered Input Validation:** Implements three strict validation layers (`validate1`, `validate2`, `validate3`) to parse inputs, catch non-numeric strings, bound entries to valid $1-3$ ranges, and prevent game overwrites.
* **Comprehensive Intersection Tracking:** Evaluates the matrix (the gameboard), after each turn to automatically identify horizontal, vertical, and diagonal win patterns, as well as any ties that may also occur.
* **Continuous Play Loop:** allows players to instantly clear tracking variables(restart the checking process), re-initialize the matrix (clear the gameboard), and start a new game without restarting the script.

---

## Functional Layout
The program logic employs functions that are strictly separated from eachother to make things more organized, easy to manipulate, and productive. Multiple functions were created to ensure state management(the values of the game variables, aka the empty spot values), rule validation (which players win or tie), and input processing (checking for things like user typos or mistakes the game cannot process).

* **Game Loop (`play`):** Controls the overall lifecycle of the gametime, handling resetting states and verifying play-again triggers.
* **Input Analysis & Transformation (`update_board`):** Manages player turns (odd vs. even turn alterations) and converts raw user strings into spatial array coordinates ($row, col$).
* **The Validation Process:**
  * `validate3`: Checks for string-to-integer safety using `.isdigit()`.
  * `validate1`: Restricts entries to acceptable 1–3 Cartesian dimensions.
  * `validate2`: Evaluates the target coordinate state to verify if a tile is already occupied.
* **Win/Tie Mechanics (`check_for_win` & `check_tie`):** Performs linear scans through rows, columns, and diagonal vectors (`[0][1]`, `[1][3]`, `[2][5]`) to locate three-in-a-row matches.
