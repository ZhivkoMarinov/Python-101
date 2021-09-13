import re


class TemplateEngine:
    def __init__(self, template):
        self.template = template

    def exceptions(self, template_data, user_input):

        if len(template_data.keys()) != len(user_input.keys()):
            return TypeError(f'{len(template_data.keys())} arguments required, {len(user_input.keys())} found ')

        if template_data.keys() != user_input.keys():
            return TypeError(f'Wrong variable name')

        return None

    def render(self, **context):
        vars_and_indexes = {}
        vars_iter = re.finditer('{{\\s*\\w*\\s*}}', self.template)
        result = self.template

        for var in vars_iter:
            vars_and_indexes[var.group()[2:-2].strip()] = var.span()

        exception = self.exceptions(vars_and_indexes, context)

        if exception is not None:
            raise exception

        for key, span_value in vars_and_indexes.items():
            start = span_value[0]
            end = span_value[1]
            string_to_change = self.template[start:end]
            result = result.replace(string_to_change, context[key])

        return result

    def extract_variables(self):
        uniques = []
        variables = self.template.replace(' ', '')
        # variables = re.findall(r"{{\\s*\\w*\\s*}}", variables)
        variables = re.findall(r"\{{(.*?)\}}", variables)

        for var in variables:
            if var not in uniques:
                uniques.append(var)

        return uniques


a = """
Hello {{ first_name }} {{ last_name }},

I hope this email finds you well. {{ first_name }}

We are currently running a promotion for {{ product }}

You can get your discount {{here}} {{here}}
"""
template1 = 'Hello there, {{y}}'
engine = TemplateEngine(a)
# rendered = engine.render(last_name='Ivanov', first_name='Ivan', product='iPhone', here='http://dksalkdsal.com')
rendered = engine.render(last_name='marinov', first_name='zhivko', here='dhjashdjsa.com', product='iPhone')
# rendered = engine.render(y='zhivko')

# print(rendered)
# print(engine.extract_variables())

# x = re.finditer('{{\s*\\w*\s*}}', a)
# for var in x:
#     print(var.span())

