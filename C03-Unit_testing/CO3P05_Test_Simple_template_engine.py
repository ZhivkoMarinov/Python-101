import unittest
from C03P05_Simple_template_engine import TemplateEngine


class TestTemplateEngine(unittest.TestCase):

    def test_render_for_exceptions(self):
        with self.subTest('If args < template vars'):
            template = 'Hello, {{ first_name }} {{ last_name }}'
            engine = TemplateEngine(template)
            with self.assertRaises(TypeError):
                engine.render(first_name='Ivan')

        with self.subTest('If args > template vars'):
            template = 'Hello, {{ first_name }} {{ last_name }}'
            engine = TemplateEngine(template)
            with self.assertRaises(TypeError):
                engine.render(first_name='Ivan', last_name='Ivanov', product='Phone')

        with self.subTest('If args names != var names'):
            template = 'Hello, {{ first_name }} {{ last_name }}'
            engine = TemplateEngine(template)
            with self.assertRaises(TypeError):
                engine.render(first_name='Ivan', lastname='Ivanov')

    def test_render_correct_functionality(self):

        with self.subTest('If args = template vars, count = 1'):
            template = 'Hello, {{ first_name }}.'
            engine = TemplateEngine(template)
            expected = 'Hello, Ivan.'
            self.assertEqual(engine.render(first_name='Ivan'), expected)

        with self.subTest('If args = template vars, count = many'):
            template = 'Hello, {{ first_name }} {{ last_name }}, did you receive your {{ product }} ?'
            engine = TemplateEngine(template)
            expected = 'Hello, Ivan Ivanov, did you receive your Phone ?'
            self.assertEqual(engine.render(first_name='Ivan',
                                           last_name='Ivanov',
                                           product='Phone'
                                           ), expected)

        with self.subTest('random whitespaces in template var'):
            templates = ['Hello, {{first_name    }} {{     last_name  }}',
                         'Hello, {{first_name}} {{last_name}}',
                         'Hello, {{    first_name}} {{  last_name  }}',
                         'Hello, {{ first_name}} {{     last_name}}',
                         'Hello, {{ first_name }} {{ last_name }}']
            for template in templates:
                engine = TemplateEngine(template)
                expected = 'Hello, Ivan Ivanov'
                self.assertEqual(engine.render(first_name='Ivan', last_name='Ivanov'), expected)

        with self.subTest('Template var used many times'):
            template = '{{ first_name }} {{ last_name }}, {{ product }} {{ last_name }} {{ first_name }} {{ product }}'
            engine = TemplateEngine(template)
            expected = 'Ivan Ivanov, Phone Ivanov Ivan Phone'
            self.assertEqual(engine.render(first_name='Ivan', last_name='Ivanov', product='Phone'), expected)

        with self.subTest('Multiline template'):
            template = """
            Hello {{first_name     }} {{ last_name }},

            I hope this email finds you well.

            We are currently running a promotion for {{   product}}.

            You can get your discount {{here}}, thank you mr. {{ last_name }}
            """
            engine = TemplateEngine(template)
            expected = """
            Hello Ivan Ivanov,

            I hope this email finds you well.

            We are currently running a promotion for Phone.

            You can get your discount www.djksaj.com, thank you mr. Ivanov
            """
            self.assertEqual(engine.render(last_name='Ivanov',
                                           first_name='Ivan',
                                           here='www.djksaj.com',
                                           product='Phone',
                                           ), expected)

        with self.subTest('single { or }'):
            template = 'Hello, { first_name }} {{ last_name }'
            engine = TemplateEngine(template)
            with self.assertRaises(TypeError):
                engine.render(first_name='Ivan', last_name='Ivanov')
            self.assertEqual(engine.render(), 'Hello, { first_name }} {{ last_name }')

    def test_extract_variables(self):

        with self.subTest('test one var'):
            template = 'Hello, {{ first_name }}'
            engine = TemplateEngine(template)
            self.assertEqual(engine.extract_variables(), ['first_name'])

        with self.subTest('test many var'):
            template = 'Hello, {{ first_name }} {{ last_name }} {{ email }} {{ tel }}'
            engine = TemplateEngine(template)
            self.assertEqual(engine.extract_variables(), ['first_name', 'last_name', 'email', 'tel'])

        with self.subTest('test with random whitespaces'):
            template = 'Hello, {{first_name}} {{      last_name}} {{email          }} {{     tel     }}'
            engine = TemplateEngine(template)
            self.assertEqual(engine.extract_variables(), ['first_name', 'last_name', 'email', 'tel'])

        with self.subTest('test repetitive vars with random spaces'):
            template = '{{first_name}} {{ first_name  }}{{tel}} {{   last_name}} {{email    }} {{   tel   }}'
            engine = TemplateEngine(template)
            self.assertEqual(engine.extract_variables(), ['first_name', 'tel', 'last_name', 'email'])

        with self.subTest('single { or }'):
            template = 'Hello, { first_name }} {{ last_name } { product }'
            engine = TemplateEngine(template)
            self.assertEqual(engine.extract_variables(), [])

        with self.subTest('test multiline template'):
            template = """
                        Hello {{first_name     }} {{ last_name }},

                        I hope this email finds you well.

                        We are currently running a promotion for {{   product}}.

                        You can get your discount {{here}}, thank you mr. {{ last_name }}
                        """
            engine = TemplateEngine(template)
            self.assertEqual(engine.extract_variables(), ['first_name', 'last_name', 'product', 'here'])


if __name__ == '__main__':
    unittest.main()
