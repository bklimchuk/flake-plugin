
def properly_formatted_no_args() -> str:
    print('t')
    str = ""
    str2 = ""
    pass


def properly_formatted_one_arg(t: str):
    pass


def improperly_formatted_no_args(

):
    pass

def some_function_with_a_pretty_long_declaration_name_kind_of(
        f: str,
        long_named_argument: str,
        another_argiment:str
):
    print()


class Test:
    def properly_formatted_function_with_args(
            self,
            token: str,
            uuid4: str = None,
            phone: str = None,
            email: str = None
    ):
        pass

    def improperly_arg_align(
        self,
        token: str,
        uuid4: str = None,
        phone: str = None,
        email: str = None
    ):
        pass

    def improperly_formatted_function_with_args(self, sdk_partner_token: str, user_uuid4: str = None, phone: str = None, email: str = None):
        pass

    def improperly_formatted_one_argument(
            self):
        pass

    def improperly_formatted_lines_argument(
            self, test: int,
            test2: str, i: bool
    ):
        pass

    def properly_formatted_function_2(
            self,
            some_arg: str,
            other: str
    ):
        self.properly_formatted_function(token='t', uuid4='uuid', phone='79', email='email')
        pass

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
