## Introduction

This package implements the following command.
    <COMMAND> --transaction-id <ID> --output <output.docx>

It takes in a transction ID from the commandline and write out the result
a docx file as specified on the commandline.

## How to run the tests

There are three test cases.

1. Check whether the API is valid
2. Check whether the transcript extraction is valid
3. Check whether the time formatting is valid.

Each test cases include from 2-3 test cases

From the top level directory, 

    python tests/test.py


## The program structure

    0. The webconfig is placed in a separate file.
    1. Process commandline parameters. Exit program on error with help
       message. On success return transaction ID and output filename.
    2. Download transcript as specified by the transaction ID. Exit program
       on error with http error message.
    3. Traverse the data and extract the list of timestamp and complete
       transcripts. The timestamp from the first word is used.
    4. Format and write out and timestamp and transcript to the specified
       output file.

## How to run the program

    1. Make sure that the API in the configuration file is set before
       running the program.
