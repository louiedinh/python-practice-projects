import options_parser

def test(shortopts, args, options, positionals, longopts=[]):
    """
    Try running parse_options with shortopts and args.
    Expect options and positionals
    """
    print("Trying to get opt with:\nshorts: %s\nlongs: %s" % (shortopts, longopts))
    print("Args: %s" % args)
    opts, pos = options_parser.parse_options(args=args, shortopts=shortopts, longopts=longopts)

    print("Options returned: %s"%opts)
    print("Options match? ", end="")
    print(opts == options)
    assert opts == options

    print("Positionals Returned: %s" % pos)
    print("Positionals match? ", end="")
    print(pos == positionals)
    assert pos == positionals

# Test 1 
print("\nTest 1...\n")
shortopts = 'abco:'
args = ['-abc']
options =  [('-a', ''), ('-b', ''), ('-c', '')]
positionals = [] 
test(shortopts=shortopts, args=args, options=options, positionals=positionals)

# Test 2
print("\nTest 2...\n")
shortopts = 'abco:'
args = ['-a', '-b', '-c', '-o', 'moo']
options =  [('-a', ''), ('-b', ''), ('-c', ''), ('-o', 'moo')]
positionals = []
test(shortopts=shortopts, args=args, options=options, positionals=positionals)

# Test 3
print("\nTest 3...\n")
shortopts = 'abco:'
args = ['-a', '-b', '-c', '-omoo']
options =  [('-a', ''), ('-b', ''), ('-c', ''), ('-o', 'moo')]
positionals = []
test(shortopts=shortopts, args=args, options=options, positionals=positionals)

# Test 4
print("\nTest 4...\n")
shortopts = 'abco:'
args = ['-abomooc']
options =  [('-a', ''), ('-b', ''), ('-o', 'mooc')]
positionals = []
test(shortopts=shortopts, args=args, options=options, positionals=positionals)

# Test 5
print("\nTest 5...\n")
shortopts = 'abco:'
args = ['-a', '-bomooc', 'fudge']
options =  [('-a', ''), ('-b', ''), ('-o', 'mooc')]
positionals = ['fudge']
test(shortopts=shortopts, args=args, options=options, positionals=positionals)

# Test 6
print("\nTest 6...\n")
shortopts = 'abco:'
args = ['-a', '-d']
options =  []
positionals = []
try:
    test(shortopts=shortopts, args=args, options=options, positionals=positionals)
except options_parser.NoSuchOptionError:
    print("Test 6 correctly raised error")

# Test 7
print("\nTest 7...\n")
shortopts = 'abco:'
longopts = ['verbose']
args = ['-a', '--verbose']
options =  [('-a',''), ('--verbose','')]
positionals = []
test(shortopts=shortopts, args=args, options=options, positionals=positionals, longopts=longopts)

# Test 8
print("\nTest 8...\n")
shortopts = 'abco:'
longopts = ['verbose']
args = ['-a', '--verbose', 'hey', 'hi']
parsed_options =  [('-a',''), ('--verbose','')]
positionals = ['hey', 'hi']
test(shortopts=shortopts, args=args, options=parsed_options, positionals=positionals, longopts=longopts)

# Test 9
print("\nTest 9...\n")
shortopts = 'abco:'
longopts = ['verbose']
args = ['-a', '--ver', 'hey', 'hi']
parsed_options =  [('-a',''), ('--verbose','')]
positionals = ['hey', 'hi']
test(shortopts=shortopts, args=args, options=parsed_options, positionals=positionals, longopts=longopts)

# Test 10
print("\nTest 10...\n")
shortopts = 'abco:'
longopts = ['verbose', 'version=']
args = ['-a', '--verb','--vers=10', 'hey', 'hi']
parsed_options =  [('-a',''), ('--verbose',''), ('--version', '10')]
positionals = ['hey', 'hi']
test(shortopts=shortopts, args=args, options=parsed_options, positionals=positionals, longopts=longopts)




