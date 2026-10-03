#!/usr/bin/env python3
# Created By: Sam V
# Date: Sep 29th , 2026
# this program demonstrates the scope of variables in Python
# and how they can be accessed and modified within different functions
# global variable

variable_X = 25


def local_variable():
    # Demonstrates local scope (shadowing the global variable_X)
    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print(
        "Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".format(
            variable_X, variable_Y, variable_Z
        )
    )


def global_variable():
    # Demonstrates modifying the global variable_X
    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print(
        "Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".format(
            variable_X, variable_Y, variable_Z
        )
    )


def main():
    # Main function to control execution flow
    print("Starting global variable_X value: {0}\n".format(variable_X))

    print("--- Calling local_variable() ---")
    local_variable()
    print("Value of global variable_X after local call: {0}\n".format(variable_X))

    print("--- Calling global_variable() ---")
    global_variable()
    print("Value of global variable_X after global call: {0}".format(variable_X))


if __name__ == "__main__":
    main()
