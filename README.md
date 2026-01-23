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
- 23/12/2025 -> Re: Fwd: Fw: Count
    ```
    Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

    For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

    "fw:"
    "fwd:"
    "re:"
    Return the total number of occurrences of these markers.
    ```
- 24/12/2025 -> Markdown Image Parser
    ```
    Given a string of an image in Markdown, return the equivalent HTML string.

    A Markdown image has the following format: "![alt text](image_url)". Where:

    alt text is the description of the image (the alt attribute value).
    image_url is the source URL of the image (the src attribute value).
    Return a string of the HTML img tag with the src set to the image URL and the alt set to the alt text.

    For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';

    Make sure the tag, order of attributes, spacing, and quote usage is the same as above.
    Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.
    ```
- 26/12/25 -> Sum Of Divisors
    ```
    Given a positive integer, return the sum of all its divisors.

    A divisor is any integer that divides the number evenly (the remainder is 0).
    Only count each divisor once.
    For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.

    ```
- 27/12/2025 -> Rock,Paper and Scissors
    ```
    Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

    The input strings will always be "Rock", "Paper", or "Scissors".
    "Rock" beats "Scissors".
    "Paper" beats "Rock".
    "Scissors" beats "Paper".
    Return:

    "Player 1 wins" if Player 1 wins.
    "Player 2 wins" if Player 2 wins.
    "Tie" if both players choose the same option.

    ```
- 28/12/2025 -> Screaming_Snake_Case
    ```
    Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

    The given variable names will be written in one of the following formats:

    camelCase
    PascalCase
    snake_case
    kebab-case
    In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

    To convert to SCREAMING_SNAKE_CASE:

    Make all letters uppercase
    Separate words with an underscore (_)
    ```
- 29/12/2025 -> Takeoff Fuel
    ```
    Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

    1 gallon equals 3.78541 liters.
    If the airplane already has enough fuel, return 0.
    You can only add whole gallons.
    Do not include decimals in the return number.

    ```
- 21/01/2026 -> Markdown Inline Code Parser
    ```
    Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

    Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

    Return the given string with all code blocks converted to HTML code tags.

    For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

    Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
    ```
    
- 22/01/2026 -> Class Average
    ```
    Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:

    Average Score	Letter Grade
    97-100	"A+"
    93-96	"A"
    90-92	"A−"
    87-89	"B+"
    83-86	"B"
    80-82	"B-"
    77-79	"C+"
    73–76	"C"
    70-72	"C-"
    67-69	"D+"
    63-66	"D"
    60–62	"D-"
    below 60	"F"

    Calculate the average by adding all scores in the array and dividing by the total number of scores.
    ```