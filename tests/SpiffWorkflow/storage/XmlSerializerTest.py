import sys, unittest, re, os
dirname = os.path.dirname(__file__)
data_dir = os.path.join(dirname, '..', 'data')
sys.path.insert(0, os.path.join(dirname, '..', '..', '..', 'src'))

from SpiffWorkflow.storage import XmlSerializer
from xml.parsers.expat import ExpatError
from SerializerTest import SerializerTest

class XmlSerializerTest(SerializerTest):
    CORRELATE = XmlSerializer

    def setUp(self):
        self.serializer = XmlSerializer()

    def get_state(self):
        xml_file  = os.path.join(data_dir, 'spiff', 'workflow1.xml')
        xml       = open(xml_file).read()
        path_file = os.path.splitext(xml_file)[0] + '.path'
        path      = open(path_file).read()
        return xml, path

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(XmlSerializerTest)
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())