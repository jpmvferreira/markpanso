#! /usr/bin/env python3


# imports
from tabulate import tabulate
import unicodedata
import argparse
import yaml
import os


# main
def main():
    # argparse
    parser = argparse.ArgumentParser(description=" A Python script to turn a Espanso package written in the YAML format into a Markdown styled table.")
    parser.add_argument("file")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()

    # get file location
    if args.file[0] == "/":
        file_name = args.file
    else:
        cwd = os.getcwd()
        file_name = cwd + "/" + args.file

    # open file and get data
    with open(file_name, "r") as file:
        list = yaml.full_load(file)
        size = len(list["matches"])
        table = []

        for i in range(0, size):
            trigger = repr(list["matches"][i]["trigger"])[1:-1]
            replace = repr(list["matches"][i]["replace"])[1:-1]

            # check if character is combining character
            # try/except required because unicodedata.category returns exception if argument is str
            try:
                if unicodedata.category(replace) in ["Mc", "Me", "Mn"]:
                    replace = "x" + replace
            except:
                pass

            table.append([trigger, replace])

    # check if output file was specified
    if args.output:
        # get file location
        if args.output[0] == "/":
            output_name = args.output
        else:
            cwd = os.getcwd()
            output_name = cwd + "/" + args.output

        # write all lines to file
        with open(output_name, "w") as file:
            file.writelines(tabulate(table, headers=["Trigger", "Replace"], tablefmt="github"))

    # else print markdown formatted table to STDOUT
    else:
        print(tabulate(table, headers=["Trigger", "Replace"], tablefmt="github"))

    return 0


# run if called
if __name__ == "__main__":
    main()
