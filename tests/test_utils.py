import unittest


class TestFunctions(unittest.TestCase):
    def test_remove_annotations__python(self):
        from copyright_helper.utils import remove_annotations
        with open('./files/python_code.txt', 'r') as f:
            code = f.read()
        out = remove_annotations(code)
        self.assertNotIn('"""', out)
        print(out)

    def test_remove_annotations__html(self):
        from copyright_helper.utils import remove_annotations
        with open('./files/html_code.txt', 'r') as f:
            code = f.read()
        out = remove_annotations(code)
        self.assertNotIn('//', out)
        print(out)


if __name__ == '__main__':
    unittest.main()
