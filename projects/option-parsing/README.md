Running Tests
-------------
python3 tests.py

Using Options Parser
--------------------
Here is a small example, with plenty of comments

    from options_parser import parse_options

    # These are the short options we accept
    options =  [('-a', ''), ('-b', ''), ('-c', ''), ('-o', 'moo')]
    # These are the long options we accept
    longopts = ['verbose']

    # Passed in arguments, this would normally be sys.argv[1:]
    args = ['-a', '-o', 'moo', '--verbose', 'hi']
    # Do the parsing
    opts, pos = parse_options(args=args, shortopts=shortopts, longopts=longopts)

    # opts is  [('-a', ''), ('-o', 'moo'), ('--verbose', '')]
    # pos is  now ['hi']
