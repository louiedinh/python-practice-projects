Title: Getopt - A Case Study in Reading Source 
Date: 2014-07-19
Category: Blog
Tags: practice, reading, command-line-parser
Slug: getopt-case-study
Author: Louie Dinh
Summary: An Example of Reading Source Code

To get better at reading source code, you just have to do it more often.

Here is an example annotation that I did while reading the source
for getopt, a deprecated Python Standard Library module. Despite
the simplicity, I picked up a few golden stylistic tips and abstraction
techniques that I still use in my programming today.

All of my annotations start with ##. The original author's comments
is written with #.

    """Parser for command line options.

    This module helps scripts to parse the command line arguments in
    sys.argv.  It supports the same conventions as the Unix getopt()
    function (including the special meanings of arguments of the form `-'
    and `--').  Long options similar to those supported by GNU software
    may be used as well via an optional third argument.  This module
    provides two functions and an exception:

    getopt() -- Parse command line options
    gnu_getopt() -- Like getopt(), but allow option and non-option arguments
    to be intermixed.
    GetoptError -- exception (class) raised with 'opt' attribute, which is the
    option involved with the exception.
    """

    # Long option support added by Lars Wirzenius <liw@iki.fi>.
    #
    # Gerrit Holl <gerrit@nl.linux.org> moved the string-based exceptions
    # to class-based exceptions.
    #
    # Peter Åstrand <astrand@lysator.liu.se> added gnu_getopt().
    #
    # TODO for gnu_getopt():
    #
    # - GNU getopt_long_only mechanism
    # - allow the caller to specify ordering
    # - RETURN_IN_ORDER option
    # - GNU extension with '-' as first character of option string
    # - optional arguments, specified by double colons
    # - a option string with a W followed by semicolon should
    #   treat "-W foo" as "--foo"

    __all__ = ["GetoptError","error","getopt","gnu_getopt"]

    import os

    class GetoptError(Exception):
        opt = ''
        msg = ''
        def __init__(self, msg, opt=''):
            self.msg = msg
            self.opt = opt
            Exception.__init__(self, msg, opt)

        def __str__(self):
            return self.msg

    error = GetoptError # backward compatibility

    def getopt(args, shortopts, longopts = []):
        """getopt(args, options[, long_options]) -> opts, args

        Parses command line options and parameter list.  args is the
        argument list to be parsed, without the leading reference to the
        running program.  Typically, this means "sys.argv[1:]".  shortopts
        is the string of option letters that the script wants to
        recognize, with options that require an argument followed by a
        colon (i.e., the same format that Unix getopt() uses).  If
        specified, longopts is a list of strings with the names of the
        long options which should be supported.  The leading '--'
        characters should not be included in the option name.  Options
        which require an argument should be followed by an equal sign
        ('=').

        The return value consists of two elements: the first is a list of
        (option, value) pairs; the second is the list of program arguments
        left after the option list was stripped (this is a trailing slice
        of the first argument).  Each option-and-value pair returned has
        the option as its first element, prefixed with a hyphen (e.g.,
        '-x'), and the option argument as its second element, or an empty
        string if the option has no argument.  The options occur in the
        list in the same order in which they were found, thus allowing
        multiple occurrences.  Long and short options may be mixed.

        """

        ## opts holds all options parsed so far
        ## args holds all unparsed data

        opts = []
        if type(longopts) == type(""):
            longopts = [longopts]
        else:
            longopts = list(longopts)
        while args and args[0].startswith('-') and args[0] != '-':

        ## We are in something like:
        ## -a -b x -c --ef - <positional> <positional>
        ## This loop instantly stops at the - or any none 
        ## flagged (starts with a -) argument.
        ## Loop Invariant: All options seen have been 
        ## successfully parsed and stored in opts.
        ## Exit Condition: Either no arguments left (arg is empty) 
        ## or next argument to be 
        ## parsed is either a positional, '-', or '--' argument 
        ## Main steps: Consume one optional parameter

            if args[0] == '--':

        ## Stop at '--' but DON'T include it in the returned arguments
        ## i.e '-a -b -- c d' returns options=(a,b) and args=(c,d) 
        ## if it was '-a -b - c d' you would get options=(a,b) args=(-, c, d)

            args = args[1:]
                break
            if args[0].startswith('--'):

        ## handle '--long_option' case
        ## Strip off the '--' from the argument before passing it to do_longs

                opts, args = do_longs(opts, args[0][2:], longopts, args[1:])
            else:

        ## Handle '-o' case
        ## Pass in opts so far, first optional arg w/o the leading '-',
        ##  handled shortopts, all other args

                opts, args = do_shorts(opts, args[0][1:], shortopts, args[1:])

        return opts, args

    def do_longs(opts, opt, longopts, args):
        try:

        ## If = is in the argument, this opt should take an argument

            i = opt.index('=')
        except ValueError:

        ## None = means no argument

            optarg = None
        else:

        ## Split the argument into parts. opt is stuff before the '=' and 
        ## optarg is stuff after the =.
        ## E.g opt="outfile=result.txt" --> opt = "outfile" optarg = "result.txt"

            opt, optarg = opt[:i], opt[i+1:]

        # Check that this specific opt should take an argument
        has_arg, opt = long_has_args(opt, longopts)
        if has_arg:
            if optarg is None:
                if not args:

        ## No more arguments after this long option.
        ##  We didn't get the argument we expected

                    raise GetoptError('option --%s requires argument' % opt, opt)

        ## If there is an argument, put it in optarg and move arg forward

                optarg, args = args[0], args[1:]
        elif optarg:

        ## Got argument when we didn't expect one

            raise GetoptError('option --%s must not have an argument' % opt, opt)

        ## Append in optarg with appropriate argument

        opts.append(('--' + opt, optarg or ''))
        return opts, args

    # Return:
    #   has_arg?
    #   full option name
    def long_has_args(opt, longopts):

        ## Returns has_arg (True | False)
        ## Returns the full option name given a shorter prefix

        possibilities = [o for o in longopts if o.startswith(opt)]
        if not possibilities:
            raise GetoptError('option --%s not recognized' % opt, opt)
        # Is there an exact match?
        if opt in possibilities:
            return False, opt
        elif opt + '=' in possibilities:
            return True, opt
        # No exact match, so better be unique.
        if len(possibilities) > 1:
            # XXX since possibilities contains all valid continuations, might be
            # nice to work them into the error msg
            raise GetoptError('option --%s not a unique prefix' % opt, opt)

        ## Assert is clearly not necessary because we checked 
        ## possibilities == 0 and possibilities > 1
        ## Serves as a clever comment

        assert len(possibilities) == 1
        unique_match = possibilities[0]
        has_arg = unique_match.endswith('=')
        if has_arg:
            unique_match = unique_match[:-1]
        return has_arg, unique_match

    def do_shorts(opts, optstring, shortopts, args):

        ## optstring is a short argument or a list of short arguments like
        ##  -abcd with the '-' prefix removed
        ## Process the whole piece

        while optstring != '':

            ## Remove the first letter from the optstring

            opt, optstring = optstring[0], optstring[1:]

        ## Check if opt is even an argument

            if short_has_arg(opt, shortopts):

        ## If the optstring is followed by an argument

                if optstring == '':

        ## We are parsing a flag with an argument
        ## This is the case where there is a space between the flag 
        ## and the argument - like -o out.txt

                    if not args:
                        raise GetoptError('option -%s requires argument' % opt,
                                          opt)

        ## Grab the subsequent argument right after this flag to be the arg to the flag

                    optstring, args = args[0], args[1:]

        ## If there is stuff after the flag, all of it is the argument

                optarg, optstring = optstring, ''
            else:

            ## If the opstring is standalone i.e 'v' from '-v'

                optarg = ''
            opts.append(('-' + opt, optarg))
        return opts, args

    def short_has_arg(opt, shortopts):
        """
        ## Check that opt exists and requires an arg
        """
        for i in range(len(shortopts)):
            if opt == shortopts[i] != ':':
                return shortopts.startswith(':', i+1)
        raise GetoptError('option -%s not recognized' % opt, opt)

    if __name__ == '__main__':
        import sys
        print getopt(sys.argv[1:], "a:b", ["alpha=", "beta"])
