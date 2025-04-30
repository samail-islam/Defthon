import commands
COMMAND_MAP = {
    'ls': commands.cmd_ls,
    'cd': commands.cmd_cd,
    'pwd': commands.cmd_pwd,
    'mkdir': commands.cmd_mkdir,
    'touch': commands.cmd_touch,
    'rm': commands.cmd_rm,
    'rename': commands.cmd_rename,
    'edit': commands.cmd_edit,
    'runpy': commands.cmd_runpy,
    'pipinstall': commands.cmd_pipinstall,
    'clear': commands.cmd_clear,
    'date': commands.cmd_date,
    'echo': commands.cmd_echo,
    'help': commands.cmd_help,
    'exit': commands.cmd_exit,
}

def parse_command(command_line):
    tokens = command_line.strip().split()
    if not tokens:
        return
    cmd, args = tokens[0], tokens[1:]
    handler = COMMAND_MAP.get(cmd)
    if handler:
        handler(args)
    else:
        print(f"Unknown command: {cmd}")

def main():
    while True:
        try:
            user_input = input("pyos> ")
            parse_command(user_input)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
