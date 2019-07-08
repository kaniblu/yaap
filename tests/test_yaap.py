from yaap import *


def test_yaap():
    parser = Yaap()
    parser.add(Int("foo", min_bound=0, required=True))
    parser.add(FloatList("bar", min_bound=2.0))
    parser.add(StrList("foobar",
                       choices=frozenset(["white", "black", "blue"])))
    parser.add(Bool("foobarbar"))
    parser.add(Bool("foobarbarbar", invert=True))
    parser.add(Bool("fofofofo"))
    parser.add(Path("testpath", must_exist=True, required=True))
    parser.add(Path("testdir", must_exist=True, is_dir=True))
    args = parser.parse("@load tests/test.json".split())
    print(args)
    parser.validate(args)


def test_yaap2():
    parser = Yaap()
    parser.add(Int(
        "int", shortcut="i", min_bound=0, required=True
    ))
    parser.add(IntList(
        "int-list"
    ))
    parser.add(Float(
        "float", min_bound=-2.0, required=True
    ))
    parser.add(FloatList(
        "float-list", min_bound=2.0, multiples=5.0
    ))
    parser.add(Path(
        "path", must_exist=True, required=True
    ))
    parser.add(Path(
        "dir", must_exist=True, is_dir=True
    ))
    parser.add(Str(
        "str", regex=r"[a-c][0-9]"
    ))
    parser.add(StrList(
        "str-list", min_length=3
    ))
    parser.add(Bool(
        "bool", help="this is a bool"
    ))

    args = parser.parse(
        "--int 3 --int-list 2 3 --float 3.0 --float-list 5 10 "
        "--path tests/test.json --dir tests --str b5 "
        "--str-list abc defg --bool".split()
    )
    print(args)
    parser.validate(args)
