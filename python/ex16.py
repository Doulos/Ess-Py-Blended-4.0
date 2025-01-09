import argparse


def print_file(fname, uppercase=False, capitalize=False):
    print(30 * "-")
    print(f"processing: {fname}")
    print(30 * "-")
    try:
        with open(fname) as f:
            for line in f:
                if uppercase:
                    print(line.upper(), end="")
                elif capitalize:
                    print(line.capitalize(), end="")
                else:
                    print(line, end="")
    except Exception:
        print(f"Could not process file")
    print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="exercise 16- Practicing Argparse", epilog="Ciao :)"
    )
    parser.add_argument("filename", nargs="+", help="one or more filename")
    parser.add_argument(
        "-u",
        "--upper",
        dest="uppercase",
        action="store_true",
        help="convert content in UPPERCASE",
    )
    parser.add_argument(
        "-c",
        "--capitalize",
        dest="capitalize",
        action="store_true",
        help="Capitalize each line",
    )

    args = parser.parse_args()

    for fname in args.filename:
        print_file(fname, args.uppercase, args.capitalize)
