# Freecodecamp Daily Challenges in python

## Starting from 12-Decemeber-2025

- 12/12/2025 -> Inventory Update
    ```
    Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

    Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
    Update items in the inventory by adding the quantity of any matching items from the shipment.
    If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
    Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
    For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].
    ```
- 13/12/2025 -> Game of Life
    ```
    Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

    Each cell is either 1 (alive) or 0 (dead).
    A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
    Cells on the edges have fewer than eight neighbors.
    Rules for updating each cell:

    Any live cell with fewer than two live neighbors dies (underpopulation).
    Any live cell with two or three live neighbors lives on.
    Any live cell with more than three live neighbors dies (overpopulation).
    Any dead cell with exactly three live neighbors becomes alive (reproduction).
    For example, given:

    [
    [0, 1, 0],
    [0, 1, 1],
    [1, 1, 0]
    ]
    return:

    [
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
    ]
    Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.
    ```
- 14/12/2025 -> Capitalize It
    ```
    Given a string title, return a new string formatted in title case using the following rules:

        Capitalize the first letter of each word.
        Make all other letters in each word lowercase.
        Words are always separated by a single space.
    ```