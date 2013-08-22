Title: Command Line Parser
Date: 2013-08-19
Category: Pages
Tags: command-line-parser
Slug: command-line-parser
Author: Louie Dinh
Summary: Problem definition for a command line parser.

Motivation
==========

Mastery of the command line is prerequisite to effective computer use. Unix allows you to pipe data between
small programs that do one job well. However, almost all command line applications need a little direction
to be of use. Each program can be thought of as a mini-language that allows you to transform text data
in various ways.

If you've written any command line application at all, you've probably used a library like argparse to
read in arguments to your program. Let's explore how command line parsers work and try to write one ourselves.

Problem Statement
=================

A command line parser takes a string and interprets it as a series of arguments and options. An argument is
the input to the program. For example, the sort command takes in as an argument the name of a file and 
outputs the lines in sorted alphabetical order. Here example_file is the argument

    $ cat example_file
    one
    two
    three
    $ sort example_file
    one
    three
    two

In addition, the sort command takes a number options also known as flags that modify the operation
of the program. For example, if I ran the sort command with the -r flag, the sort ordering is reversed.
Options have two forms, long and short. Short forms are a single letter, like -r. The long forms
are indicated by a double dash and then the full word, like --reversed.

    $ sort -r example_file
    two
    three
    one

Options can take in arguments too. This is specified in the short form by immediately following
the short form flag with the value (space optional). The long form is specified by a double dash
followed by an equal sign.

    $ sort -o out_file example_file            # Writes the line sorted contents to out_file
    $ sort -oout_file example_file             # Same as above
    $ sort --output=out_file example_file      # Same as above

Allow the user to specify a set of positional and optional parameters. The user should be
able to indicate whether the optional parameter takes an argument or not. Then given a string,
return the positional parameters, optional parameters and their values if any.
