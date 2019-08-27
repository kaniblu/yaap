from yaap import *


def create_parser():
    parser = Yaap()
    parser.add_int("int", min_bound=0, required=True)
    parser.add_int("int-list", is_list=True)
    parser.add_flt("float")
    parser.add_flt("float-list", is_list=True)
    parser.add_flt("float-list-default", is_list=True, default=(1.3, 3.4))
    parser.add_str("str")
    parser.add_str("str-list", is_list=True)
    parser.add_bol("bool-true")
    parser.add_bol("bool-false")
    parser.add_pth("path", must_exist=True)
    parser.add_pth("dir", must_exist=True, is_dir=True)
    return parser


def test_yaap():
    parser = create_parser()
    args = parser.parse("@load tests/test.json".split())
    parser.validate(args)
    print(args)


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


def main():
    test_yaap()


if __name__ == "__main__":
    main()
