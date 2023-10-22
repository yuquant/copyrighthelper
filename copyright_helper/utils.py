import re
import os
# import gzip
import tarfile
import zipfile
# import rarfile
# import time
def remove_annotations(code: str,
                       symbols=[
                           ("#", "\n"),
                           ("<!--", "-->"),
                           ("//", "\n"),
                           ('"""', '"""'),
                           ("'''", "'''"),
                           ("/\*", "\*/")
                       ]
                       ) -> str:
    """

    :param code:
    :param symbols:
    :return:
    """
    for s in symbols:
        pattern = '{}.*?{}'.format(s[0], s[1])
        p = re.compile(pattern, re.DOTALL | re.MULTILINE)  # option needed
        code = re.sub(p, "\n", code)

    # remove all \n
    p = re.compile(r'\n\s{1,}\n', re.DOTALL | re.MULTILINE)
    code = re.sub(p, "\n", code)

    p = re.compile(r'\n{2,}', re.DOTALL | re.MULTILINE)
    code = re.sub(p, "\n", code)

    code = code.strip('\n')
    return code


class Extractor:
    def __init__(self, zipped_file: str):
        self._zipped_file = zipped_file

    def extract_to(self, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        if self._zipped_file.endswith('.txt'):
            os.link(self._zipped_file, os.path.join(output_dir, 'tmp.txt'))
        elif self._zipped_file.endswith('.zip'):
            self._unzip(self._zipped_file, output_dir)
        elif self._zipped_file.endswith('.tar'):
            self._untar(self._zipped_file, output_dir)
        else:
            raise ValueError('Unsupported format:{}'.format(self._zipped_file))

    @staticmethod
    def _untar(filename, output_dir):
        tar = tarfile.open(filename)
        names = tar.getnames()
        for name in names:
            tar.extract(name, output_dir)
        tar.close()

    @staticmethod
    def _unzip(filename, output_dir):
        zip_file = zipfile.ZipFile(filename)
        for names in zip_file.namelist():
            zip_file.extract(names, output_dir)
        zip_file.close()