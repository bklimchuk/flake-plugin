import ast


class BracesChecker:
    name = 'braces_checker'
    version = '1.1.8'

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                print(f"Checking function: {node.name}")
                if len(node.args.args) > 1:
                    if not self.is_properly_formatted(node):
                        yield (node.lineno, 0, "FFC001 Function arguments are not properly formatted", type(self))

    def is_properly_formatted(self, node):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            func_def_line = lines[node.lineno - 1]
            last_arg_line_num = node.args.args[-1].end_lineno  # Line number of the last argument
            closing_parenthesis_line = lines[last_arg_line_num]  # Line immediately after the last argument
        except Exception as e:
            print(f"Error reading lines: {e}")
            return False

        print(f"Function definition line: {func_def_line.strip()}")
        for arg in node.args.args:
            arg_line = lines[arg.lineno - 1].strip()
            print(f"Argument {arg.arg} line: {arg_line}")

        print(f"Closing parenthesis line: {closing_parenthesis_line.strip()}")

        # Ensure the closing parenthesis aligns with the 'd' in 'def'
        if not self.is_closing_parenthesis_aligned(func_def_line, closing_parenthesis_line):
            print("Closing parenthesis is not aligned")
            return False

        # Ensure all arguments start on a new line after the function definition
        for i, arg in enumerate(node.args.args):
            if i > 0 and arg.lineno == node.args.args[i - 1].lineno:
                print(f"Argument {arg.arg} is on the same line as the previous argument")
                return False

        return True

    def is_closing_parenthesis_aligned(self, func_def_line, closing_parenthesis_line):
        # Find the starting index of the 'def' keyword
        def_start_index = func_def_line.index('def')

        # Expected index for the closing parenthesis
        expected_index = def_start_index

        # Check if the closing line contains the closing parenthesis
        stripped_closing_line = closing_parenthesis_line.strip()

        if not stripped_closing_line.startswith(')'):
            print(f"Closing line does not start with ')': {stripped_closing_line}")
            return False

        # Ensure the closing parenthesis aligns with the 'def' keyword
        closing_parenthesis_index = closing_parenthesis_line.index(')')
        if closing_parenthesis_index != expected_index:
            print(f"Closing parenthesis is at index {closing_parenthesis_index}, expected {expected_index}")
            return False

        return True


def run_checks(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)
    checker = BracesChecker(tree, filename)
    return list(checker.run())