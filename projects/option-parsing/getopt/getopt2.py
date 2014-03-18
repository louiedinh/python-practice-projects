"""
Specification

Given a list of user-specified options and arguments, argv[1:], return the options pased on the command line.
Examples:
    options = -a, -b, -c, -v, -o <output filename>

    args = -a -b -c --> (('-a', ''), ('-b', ''), ('-c', ''))
    args = -abc --> (('-a', ''), ('-b', ''), ('-c', ''))
    args = -abc -o moo --> (('-a', ''), ('-b', ''), ('-c', ''), (-o, 'moo'))
    args = -abc -omoo --> (('-a', ''), ('-b', ''), ('-c', ''), (-o, 'moo'))
    args = -abcomoo --> (('-a', ''), ('-b', ''), ('-c', ''), (-o, 'moo'))
    args = -abomooc --> (('-a', ''), ('-b', ''), (-o, 'mooc'))
    args = -abomooc fudge --> (('-a', ''), ('-b', ''), (-o, 'mooc')) + ['fudge']
"""

class NoSuchOptionError(Exception):
    pass

def getopt(args, shortopts, longopts=[]):
    """
    Given a string of arguments, return the options specified by shortopts and longopts
    """
    opts = []
    while args and args[0].startswith("-"):
        if args[0].startswith("--"):
            opts, args = do_long_option(optstring=args[0][2:], opts=opts, args=args[1:], longopts=longopts)
        elif args[0].startswith("-"):
            opts, args = do_short_option(optstring=args[0][1:], opts=opts, args=args[1:], shortopts=shortopts)

    return opts, args

def do_long_option(optstring, opts, args, longopts):
    try:
        idx = optstring.index('=')
    except:
        optarg = None
    else:
        optstring, optarg = optstring[:idx], optstring[idx+1:]

    option, has_arg = long_opt_has_arg(optstring, longopts)
    if has_arg:
        if optarg is None:
            if not args:
                raise ValueError("No argument for long option %s"%option)
            optarg, args= args[0], args[1:]
        else:
            # Already have argument from optstring
            pass

    opts.append(('--' + option, optarg or ''))
    return opts, args

def long_opt_has_arg(opt, longopts):
    if opt in longopts:
        return opt, False
    elif opt + '=' in longopts:
        return opt, True

    possibilities = [option for option in longopts if option.startswith(opt)]
    if len(possibilities) > 1:
        raise NoSuchOptionError("Non-unique options %s matched long option %s"%(possibilities, opt))
    assert len(possibilities) == 1
    option = possibilities[0]
    if option.endswith("="):
        return option[:-1], True
    else:
        return option, False

def do_short_option(optstring, opts, args, shortopts):
    """
        For every letter in the opstring
        If letter is an option w/o args. Parse it and keep going.
        If letter is an option w/ arg. Parse it, take the rest as argument.
        If letter is an option w/ arg but optstring is now empty -> Take next in args as argument
    """
    while optstring:
        opt, optstring = optstring[0], optstring[1:]
        print "optstring: %s"%optstring
        optarg = ''
        if short_opt_has_arg(opt, shortopts):
            if optstring:
                optarg, optstring= optstring, ''
            else: # Not optstring so look at args
                if args:
                    optarg, args = args[0], args[1:]
                else:
                    raise ValueError("No argument found for option %s"%opt)
        opts.append(('-' + opt, optarg))

    return opts, args

def short_opt_has_arg(opt, shortopts):
    try:
        idx = shortopts.index(opt)
    except ValueError:
        raise NoSuchOptionError("No option %s found in short options"%opt)
    else:
        return shortopts.startswith(":", idx+1)

def test(shortopts, args, options, positionals, longopts=[]):
    """
    Try running getopt with shortopts and args.
    Expect options and positionals
    """
    print "Trying to get opt with:\nshorts: %s\nlongs: %s"%(shortopts, longopts)
    print "Args: %s"%args
    opts, pos = getopt(args=args, shortopts=shortopts, longopts=longopts)

    print "Options returned: %s"%opts
    print "Options match?",
    print opts == options
    assert opts == options

    print "Positionals Returned: %s"%pos
    print "Positionals match?",
    print pos == positionals
    assert pos == positionals

if __name__ == "__main__":

    # Test 1 
    print "\nTest 1...\n"
    shortopts = 'abco:'
    args = ['-abc']
    options =  [('-a', ''), ('-b', ''), ('-c', '')]
    positionals = [] 
    test(shortopts=shortopts, args=args, options=options, positionals=positionals)

    # Test 2
    print "\nTest 2...\n"
    shortopts = 'abco:'
    args = ['-a', '-b', '-c', '-o', 'moo']
    options =  [('-a', ''), ('-b', ''), ('-c', ''), ('-o', 'moo')]
    positionals = []
    test(shortopts=shortopts, args=args, options=options, positionals=positionals)

    # Test 3
    print "\nTest 3...\n"
    shortopts = 'abco:'
    args = ['-a', '-b', '-c', '-omoo']
    options =  [('-a', ''), ('-b', ''), ('-c', ''), ('-o', 'moo')]
    positionals = []
    test(shortopts=shortopts, args=args, options=options, positionals=positionals)

    # Test 4
    print "\nTest 4...\n"
    shortopts = 'abco:'
    args = ['-abomooc']
    options =  [('-a', ''), ('-b', ''), ('-o', 'mooc')]
    positionals = []
    test(shortopts=shortopts, args=args, options=options, positionals=positionals)

    # Test 5
    print "\nTest 5...\n"
    shortopts = 'abco:'
    args = ['-a', '-bomooc', 'fudge']
    options =  [('-a', ''), ('-b', ''), ('-o', 'mooc')]
    positionals = ['fudge']
    test(shortopts=shortopts, args=args, options=options, positionals=positionals)

    # Test 6
    print "\nTest 6...\n"
    shortopts = 'abco:'
    args = ['-a', '-d']
    options =  []
    positionals = []
    try:
        test(shortopts=shortopts, args=args, options=options, positionals=positionals)
    except NoSuchOptionError:
        print "Test 6 correctly raised error"

    # Test 7
    print "\nTest 7...\n"
    shortopts = 'abco:'
    longopts = ['verbose']
    args = ['-a', '--verbose']
    options =  [('-a',''), ('--verbose','')]
    positionals = []
    test(shortopts=shortopts, args=args, options=options, positionals=positionals, longopts=longopts)

    # Test 8
    print "\nTest 8...\n"
    shortopts = 'abco:'
    longopts = ['verbose']
    args = ['-a', '--verbose', 'hey', 'hi']
    parsed_options =  [('-a',''), ('--verbose','')]
    positionals = ['hey', 'hi']
    test(shortopts=shortopts, args=args, options=parsed_options, positionals=positionals, longopts=longopts)

    # Test 9
    print "\nTest 9...\n"
    shortopts = 'abco:'
    longopts = ['verbose']
    args = ['-a', '--ver', 'hey', 'hi']
    parsed_options =  [('-a',''), ('--verbose','')]
    positionals = ['hey', 'hi']
    test(shortopts=shortopts, args=args, options=parsed_options, positionals=positionals, longopts=longopts)

    # Test 10
    print "\nTest 10...\n"
    shortopts = 'abco:'
    longopts = ['verbose', 'version=']
    args = ['-a', '--verb','--vers=10', 'hey', 'hi']
    parsed_options =  [('-a',''), ('--verbose',''), ('--version', '10')]
    positionals = ['hey', 'hi']
    test(shortopts=shortopts, args=args, options=parsed_options, positionals=positionals, longopts=longopts)
