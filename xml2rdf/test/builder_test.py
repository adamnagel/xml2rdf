import unittest
from xml2rdf.builder import Builder
from os.path import dirname, realpath, join


class BuilderTestCase(unittest.TestCase):
    THIS_DIR = dirname(realpath(__file__))

    def test_ttl(self):
        path_test = join(self.THIS_DIR, 'test_one.xml')
        b = Builder()
        b.parse(path_test)
        g = b.g

        print(g.all_nodes())


if __name__ == "__main__":
    unittest.main()
