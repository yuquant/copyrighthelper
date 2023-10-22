import unittest


class TestCopyrightHelper(unittest.TestCase):
    def test_from_dir(self):
        dir_path = './files'
        doc_path = './files/code.docx'
        from copyright_helper import CopyrightHelper
        helper = CopyrightHelper.from_dir(dir_path)
        code = helper.get_removed_code()
        helper.write_to_docx(code, doc_path)


class TestFunctions(unittest.TestCase):
    def test_write_cleaned_code_to_doc(self):
        file = './files/text2vec-master.zip'
        doc_path = './files/code.docx'
        from copyright_helper import write_cleaned_code_to_doc
        write_cleaned_code_to_doc(file, doc_path)


if __name__ == '__main__':
    unittest.main()
