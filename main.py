# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def swap_two_elements():
    # Use a breakpoint in the code line below to debug your script.
    input = [12, 35, 9, 56, 24]
    temp = input[0]
    input[0] = input[-1]
    input[-1] = temp
    print(input)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    swap_two_elements()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
