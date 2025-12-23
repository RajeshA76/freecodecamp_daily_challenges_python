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
- 15/12/2025 -> Speed Check
    ```
    Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

    1 mile equals 1.60934 kilometers.
    If you are travelling less than or equal to the speed limit, return "Not Speeding".
    If you are travelling 5 KPH or less over the speed limit, return "Warning".
    If you are travelling more than 5 KPH over the speed limit, return "Ticket".
    ```
- 16/12/2025 -> Consonant Count
    ```
    Given a string and a target number, determine whether the string contains exactly the target number of consonants.

    Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
    Ignore digits, punctuation, spaces, and other non-letter characters when counting.

    ```
- 17/12/2025 -> Markdown Blockquote Parser
    ```
    Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

    A blockquote in Markdown is any line that:

    Starts with zero or more spaces
    Followed by a greater-than sign (>)
    Then, one or more spaces
    And finally, the blockquote text.
    Return the blockquote text surrounded by opening and closing HTML blockquote tags.

    For example, given "> This is a quote", return <blockquote>This is a quote</blockquote>.

    Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
    ```
- 18/12/2025 -> Checkboard
    ```
    Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

    The characters should alternate like a checkerboard.
    The top-left cell must always be "X".
    For example, given [3, 3], return:

    [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
    ]
    ```
- 19/12/2025 -> Pairwise
    ```
    Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

    For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

    2 and 8 (2 + 8 = 10), whose indices are 0 and 4
    4 and 6 (4 + 6 = 10), whose indices are 2 and 3
    Add all the indices together to get a return value of 9.
    ```
- 20/12/2025 -> Purge Most Recent
    ```
    Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

    If multiple values are tied for most frequent, remove all of them.
    Do not change any of the other elements or their order.
    ```
- 21/12/2025 Daylight Hours
    ```
    December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

    Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

    Latitude	Daylight Hours
    -90	24
    -75	23
    -60	21
    -45	15
    -30	13
    -15	12
    0	12
    15	11
    30	10
    45	9
    60	6
    75	2
    90	0
    If the given latitude does not exactly match a table entry, use the value of the closest latitude.
    ```
- 22/12/2025 -> Traveling Shopper
    ```
    Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

    The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
    Each array item you want to purchase will be in the same format.
    Use the following exchange rates to convert values:

    Currency	1 Unit Equals
    USD	1.00 USD
    EUR	1.10 USD
    GBP	1.25 USD
    JPY	0.0070 USD
    CAD	0.75 USD
    
    If you can afford all the items in the list, return "Buy them all!".
    Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.
    ```