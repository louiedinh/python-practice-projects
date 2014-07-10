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

def parse_options(args, shortopts, longopts=[]):
    opts = []
    # While args exists and the first arg starts with a -
    while args and args[0].startswith('-'):
        if args[0].startswith('--'):
            opts, args = do_long_opt(longopts, args[0][2:], opts, args[1:])
        else:
            opts, args = do_short_opt(shortopts, args[0][1:], opts, args[1:])

    return opts, args

def do_long_opt(longopts, optstring, opts, args):
    """
    longopts:
        List of accepted long options
    optstring:
        The string to parse without --
    opts:
        List of opts parsed so far
    args:
        List of args left to parse
    """
    try:
        idx = optstring.index('=')
    except ValueError:
        optarg = None
    else:
        optstring, optarg = optstring[:idx], optstring[idx+1:]
        
    ## Optstring contains the option part of the string, optarg holds the arg part of the string if any

    has_arg, long_option = long_option_has_arg(optstring, longopts)

    ## long_option is the real option name, has_arg determines if argument is needed

    if has_arg:
        if optarg is None:
            if not args:
                raise NoSuchOptionError("%s expected argument but not found"%long_option)
            optarg, args = args[0], args[1:]
    elif optarg:
        raise NoSuchOptionError("Given argument to %s where none expected"%long_option)

    ## optarg is correctly populated, long_option is corrected populated

    opts.append(('--' + long_option, optarg or ''))
    return opts, args

def long_option_has_arg(option, longopts):
    possibilities = [x for x in longopts if x.startswith(option)]

    if not possibilities:
        raise NoSuchOptionError("Cannot find option matching %s"%option)

    # Exact match
    if option in possibilities:
        return False, option
    elif option + '=' in possibilities:
        return True, option
    # No exact match - better be unique
    if len(possibilities) > 1:
        raise NoSuchOptionError("Non-unique prefix %s"%option)
    assert len(possibilities) == 1
    long_option = possibilities[0]

    has_arg = long_option.endswith('=')
    if has_arg:
        long_option = long_option[:-1]
    return has_arg, long_option

def do_short_opt(shortopts, optstring, opts, args):
    """
    shortopts: 
        options accepted
    optstring: 
        First opt string to parse without - prefix
    opts: 
        List of opts parsed so far
    args: 
        List of args left, not including optstring
    """
    while optstring:
        flag, optstring = optstring[0], optstring[1:]
        optarg = ''
        if short_option_has_arguments(flag, shortopts):
            if not optstring:
                assert args != ''
                optstring, args = args[0], args[1:]
            optarg, optstring = optstring, ''
        opts.append(('-' + flag, optarg))

    return opts, args

def short_option_has_arguments(flag, shortopts):
    """
    Check to see if this argument has args
    """
    idx = shortopts.find(flag)
    if idx == -1:
        raise NoSuchOptionError()
    else:
        return shortopts.startswith(':', idx+1)
