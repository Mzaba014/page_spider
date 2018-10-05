import os
import argparse
from utilities import url_utilities as url_utils


def main(database: str, url_list_file: str):
    big_word_list = []
    print("We are gonna work with: " + database + " DB")
    print("We are gonna scan: " + url_list_file + " URL file")
    urls = url_utils.load_urls_from_file(url_list_file)
    for url in urls:
        print("reading: " + url)
        page_content = url_utils.load_page(url=url)  # Using the load_page function in url_ulitiliesi
                                                     # to open the url contents and decode using utf-8
        words = url_utils.scrape_page(page_content)  #filtering out numbers, single letter words etc
        big_word_list.extend(words) #Note: append adds an object, extend adds an iterable object i.e. list



if __name__ == "__main__":
    parser = argparse.ArgumentParser()  # Creation of parser object for CLI functionality.
    parser.add_argument("-db", "--database",
                        help="SQLite File Name")  # Adding -db option with --database argument to the parser
    parser.add_argument("-i", "--input",
                        help="File containing URLs to read")  # Adding -i option with --input (URL file)
    args = parser.parse_args()  # Does actual parsing, converts the CLI info using the above rules
    database_file = args.database  # Assigning parsed values to local vars
    input_file = args.input  # " "
    main(database=database_file, url_list_file=input_file)  # Calling main using the values parsed from the CLI

"""Essentially, the CLI script portion will parse the CLI opts/args and create the proper
vars for their manipulation, these args are then passed to the main for the actual program
function"""
