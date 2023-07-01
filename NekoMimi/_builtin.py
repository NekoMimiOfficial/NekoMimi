"""
builtin tools only used internally by NekoMimi
"""

def parser(argv: list[str]):

    cmd_list = {}
    for key in range(0, (len(argv) - 1)):
        val = argv[key]
        if val.startswith("--nm_"):
            head = val.split("--nm_", 1)[1]
            head = head.split("=", 1)[0]
            body = val.split("=", 1)[1]

            cmd_list[head] = body

    return cmd_list
