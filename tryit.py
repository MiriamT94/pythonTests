# This is a sample Python script.
import sys
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_nos(a):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, ')  # Press ⌘F8 to toggle the breakpoint.

    store = [1,2,3,4,5,6,7,9,9,0]
    store.append(a)
    return store
def print_nos(n):
    for i in n:
        print(i)


# Press the green button in the gutter to run the script.
def main(a):
    no= get_nos(a)
    print_nos(no)


if __name__ == '__main__':
    main(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

