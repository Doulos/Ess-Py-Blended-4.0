# use a context manager
try:
    with open(__file__) as f:
        content = f.read()
    print(content, end="")
except FileNotFoundError:
    content = "Couldn't open the file. Use default string for content."

try:
    with open("reversed2.txt", "w") as output:
        for l in content.splitlines():
            print(l[::-1], file=output)
except Exception as e:
    """Catching Exception is the recommended way to catch all exceptions
    that signal runtime program errors.

    See: https://peps.python.org/pep-0008/#programming-recommendations
    """
    print(f"Ooops, something went wrong :( \n{e}")
