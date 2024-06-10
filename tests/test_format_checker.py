import ast
import pytest
from checkers.func_checker.func_arg_checker import FunctionFormatChecker


def run_checker(code):
    tree = ast.parse(code)
    lines = code.splitlines()
    checker = FunctionFormatChecker(tree, "test_file.py", lines)
    return list(checker.run())


def test_properly_formatted_no_args():
    code = '''
def properly_formatted_no_args():
    pass
'''
    errors = run_checker(code)
    assert errors == []


def test_properly_formatted_function():
    code = '''
class Test:
    def properly_formatted_function(
            self,
            token: str,
            uuid4: str = None,
            phone: str = None,
            email: str = None
    ):
        pass
'''
    errors = run_checker(code)
    assert errors == []


def test_improperly_formatted_function():
    code = '''
def improperly_formatted_function_with_args(self, sdk_partner_token: str, user_uuid4: str = None, phone: str = None, email: str = None):
    pass
'''
    errors = run_checker(code)
    assert len(errors) == 1
    assert errors[0][2] == "FFC001 Closing parenthesis does not aligned correctly"


def test_properly_formatted_one_argument():
    code = '''
def properly_formatted_one_argument(self):
    pass
'''
    errors = run_checker(code)
    assert errors == []


def test_properly_formatted_function_2():
    code = '''
class Test:
    def properly_formatted_function_with_args(
            self,
            some_arg: str,
            other: str
    ):
        self.properly_formatted_function(token='t', uuid4='uuid', phone='79', email='email')
        pass
'''
    errors = run_checker(code)
    assert errors == []


def test_properly_formatted_nested():
    code = '''
class Test:
    class SomeClass:
        def properly_formatted_nested(
                self,
                i: int,
                test: str,
                sdk_partner_token: str,
                some_data: int,
                something: bool
        ):
            pass
'''
    errors = run_checker(code)
    assert errors == []


def test_improperly_formatted_one_argument():
    code = '''
def improperly_formatted_one_argument(
        self
):
    pass
'''
    errors = run_checker(code)
    assert len(errors) == 1
    assert errors[0][2] == ("FFC001 Function with one or no arguments should "
                            "have the closing parenthesis on the same line")


def test_closing_parenthesis_not_aligned():
    code = '''
def improperly_formatted_closing_parenthesis(
        self,
        sdk_partner_token: str
        ):
    pass
'''
    errors = run_checker(code)
    assert len(errors) == 1
    assert errors[0][2] == "FFC001 Closing parenthesis is at index 8, expected 0"
