import ast


class FunctionFormatChecker:
    name = 'func_arg_checker'
    version = '1.2.9'

    def __init__(self, tree, filename, lines):
        self.tree = tree
        self.filename = filename
        self.lines = lines

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):

                dec_start_line = node.lineno
                dec_end_line_indx = self.find_func_declaration_end(node)
                func_def_line = self.lines[node.lineno - 1]
                def_start_index = func_def_line.index('def')

                if len(node.args.args) < 2:
                    print('len(node.args.args) < 1:')
                    result = self.check_format_one_or_none(
                        end_line=dec_end_line_indx,
                        start_line=dec_start_line)
                    if result is not None:
                        yield result['line'], result['position'], result['message'], type(self)
                else:
                    result = self.check_func_format(
                        node=node,
                        end_line=dec_end_line_indx,
                        lines=self.lines,
                        def_start_index=def_start_index)
                    if result is not None:
                        yield result['line'], result['position'], result['message'], type(self)


    def check_func_format(self, node, end_line, lines, def_start_index: int):

        for arg in node.args.args:
            arg_line = lines[arg.lineno - 1].strip()
            print(f"Argument {arg.arg} line: {arg_line}")

        # Ensure the closing parenthesis aligns with the 'd' in 'def'
        result = self.is_closing_parenthesis_aligned(
                def_start_indx=def_start_index,
                end_line_indx=end_line, lines=lines)
        if result is not None:
            return result


        result = self.check_args_alignment(node, def_start_index)
        if result is not None:
            return result
        return None

    # Checks if the function parenthesis and/or arguments are correctly aligned
    # in the case where a function has one or no arguments.
    def check_format_one_or_none(self, start_line, end_line):

        if end_line == start_line:
            return None
        else:
            return {
                'line': start_line,
                'position': 0,
                'message': "FFC001 Function with one or no arguments should have the "
                           "closing parenthesis on the same line"
            }

    # Ensures that function arguments are correctly aligned
    def check_args_alignment(self, node, def_start_index: int):
        exp_index = def_start_index + 8

        for i, arg in enumerate(node.args.args):
            arg_position = arg.col_offset
            if ((i > 0 and arg.lineno == node.args.args[i - 1].lineno)
                    or (arg_position != exp_index)):
                return {
                    'line': arg.lineno,
                    'position': arg_position,
                    'message': f"FFC001 Argument {arg.arg} is not properly aligned or on "
                               f"the same line as previous argument"
                }
        return None

    def is_closing_parenthesis_aligned(self, end_line_indx, def_start_indx, lines):

        closing_line = lines[end_line_indx - 1]
        stripped_closing_line = closing_line.strip()
        closing_parenthesis_index = closing_line.index(')')

        if not stripped_closing_line.startswith(')'):
            return {
                'line': end_line_indx,
                'position': closing_parenthesis_index,
                'message': 'FFC001 Closing parenthesis does not aligned correctly'
            }

        # Ensure the closing parenthesis aligns with the 'def' keyword

        if closing_parenthesis_index != def_start_indx:
            return {
                'line': end_line_indx,
                'position': closing_parenthesis_index,
                'message': f"FFC001 Closing parenthesis is at index {closing_parenthesis_index}, "
                           f"expected {def_start_indx}"
            }
        return None

    def find_func_declaration_end(self, node):
        function_start_line = node.lineno
        function_dec_end_line = function_start_line

        for i in range(function_start_line, node.body[0].lineno):
            function_dec_end_line = i
        return function_dec_end_line


def run_checks(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)
        lines = file.readlines()
    checker = FunctionFormatChecker(tree, filename, lines)
    return list(checker.run())
