class CommandParser:
    def __init__(self, file_system):
        self.commands = {}

    def parse_and_execute(self, command_line):
        if not command_line:
            return
        parts = []
        current = []
        in_quotes = False
        quote_char = None
        
        for char in command_line:
            if char in ['"', "'"]:
                if not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char:
                    in_quotes = False
                    quote_char = None
                else:
                    current.append(char)
            elif char == ' ' and not in_quotes:
                if current:
                    parts.append(''.join(current))
                    current = []
            else:
                current.append(char)
                
        if current:
            parts.append(''.join(current))
        if not parts:
            return

        command_name = parts[0]
        args = parts[1:]

        if command_name in self.commands:
            try:
                return self.commands[command_name].execute(args)
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print(f"Command not found: {command_name}")