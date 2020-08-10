import random
import psycopg2


monday_colors = [
    "GREEN",
    "YELLOW",
    "GREEN",
    "BROWN",
    "BLUE",
    "PINK",
    "BLUE",
    "YELLOW",
    "ORANGE",
    "CREAM",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
    "GREEN",
]
tuesday_colors = [
    "ARSH",
    "BROWN",
    "GREEN",
    "BROWN",
    "BLUE",
    "BLUE",
    "BLEW",
    "PINK",
    "PINK",
    "ORANGE",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
]
wednesday_colors = [
    "GREEN",
    "YELLOW",
    "GREEN",
    "BROWN",
    "BLUE",
    "PINK",
    "RED",
    "YELLOW",
    "ORANGE",
    "RED",
    "ORANGE",
    "RED",
    "BLUE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "WHITE",
    "WHITE",
]
thursday_colors = [
    "BLUE",
    "BLUE",
    "GREEN",
    "WHITE",
    "BLUE",
    "BROWN",
    "PINK",
    "YELLOW",
    "ORANGE",
    "CREAM",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
    "GREEN",
]
friday_colors = [
    "GREEN",
    "WHITE",
    "GREEN",
    "BROWN",
    "BLUE",
    "BLUE",
    "BLACK",
    "WHITE",
    "ORANGE",
    "RED",
    "RED",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
    "WHITE",
]

total_color = (
    monday_colors + tuesday_colors + wednesday_colors + thursday_colors + friday_colors
)


def get_color_and_frequency(colors):
    color_dic = {}
    for color in colors:
        color_dic[color] = colors.count(color)
    return color_dic


def get_most_frequent_color(colors):
    counter = 0
    first_color = colors[0]
    for color in colors:
        curr_frequency = colors.count(color)
        if curr_frequency > counter:
            counter = curr_frequency
            first_color = color
    return first_color


print(get_color_and_frequency(total_color))


# 1. Which color of shirt is the mean color?

frequent_color_monday = get_most_frequent_color(monday_colors)
frequent_color_tuesday = get_most_frequent_color(tuesday_colors)
frequent_color_wednesday = get_most_frequent_color(wednesday_colors)
frequent_color_thursday = get_most_frequent_color(thursday_colors)
frequent_color_friday = get_most_frequent_color(friday_colors)

print(
    frequent_color_monday,
    frequent_color_tuesday,
    frequent_color_wednesday,
    frequent_color_thursday,
    frequent_color_friday,
)

# Since the most frequent color worn in each day of the week is BLUE thus:

print(f"The mean of the of the shirt color is Blue")


# 2. Which color is mostly worn throughout the week?

frequent_color = get_most_frequent_color(total_color)

print(f'The most color worn throughout the the week is "{frequent_color}" ')

# 3. Which color is the median?

median = total_color[44]
print(f"The median color is {median}")

connection = psycopg2.connect(
    host="localhost", database="testload", user="haki", password=None,
)
connection.autocommit = True

# 5. BONUS if a colour is chosen at random, what is the probability that the color is red?

red_color_count = total_color.count("RED")

probability_of_red = red_color_count / len(total_color)

print(round(probability_of_red, 2))


# 7. BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.


def search(myList, number):
    def search_recursive(lst, num):
        if lst[0] == num:
            return 0
        return 1 + search_recursive(lst[1:], num)

    try:
        return search_recursive(myList, number)
    except IndexError:
        return -1


print(search([1, 2, 3, 4, 5], 6))
print(search([1, 2, 3, 4, 5], 3))

# 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

digit_options = [0, 1]
result = []
for i in range(4):
    digit = str(random.choice(digit_options))
    result.append(digit)
result = "".join(result)
result_in_base_10 = int(result, 2)
print(result)
print(result_in_base_10)

# 9. Write a program to sum the first 50 fibonacci sequence.

fib = [0, 1]
for x in range(48):
    fib_seq = fib[-1] + fib[-2]
    fib.append(fib_seq)
print(len(fib))
print(fib)
print(sum(fib))


# 6.  Save the colours and their frequencies in postgresql database

connection = psycopg2.connect(
    host="localhost", database="colors", user="ademola", password=None,
)
connection.autocommit = True


def create_staging_table(cursor) -> None:
    cursor.execute(
        """
        DROP TABLE IF EXISTS color_frequency;
        CREATE TABLE staging_beers (
            id                  INTEGER,
            color               TEXT,
            frequency            INTEGER,
        );
    """
    )
