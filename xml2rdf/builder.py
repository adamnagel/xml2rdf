__author__ = 'adam'

import xml.etree.ElementTree as ET
from rdflib import RDF, Graph, BNode, URIRef, Literal


class Builder(object):
    URI_XML_SCHEMA_ROOT = 'http://xml-convert.com/schema#'
    CONTAINMENT = URIRef(URI_XML_SCHEMA_ROOT + 'contains')
    TEXT = URIRef(URI_XML_SCHEMA_ROOT + 'text')
    FILE = URIRef(URI_XML_SCHEMA_ROOT + 'file')
    FILENAME = URIRef(URI_XML_SCHEMA_ROOT + 'filename')
    FROM_FILE = URIRef(URI_XML_SCHEMA_ROOT + 'from_file')

    URI_FILE_SCHEMA_ROOT = 'http://this-file.com/schema#'

    def __init__(self):
        self.g = Graph()

    def parse(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Make a node for this file
        file_bnode = BNode()
        self.g.add((file_bnode, RDF.type, self.FILE))
        self.g.add((file_bnode, self.FILENAME, Literal(xml_file)))

        self.__parse_node__(root, file_bnode=file_bnode)

        return self.g

    def __parse_node__(self,
                       node,
                       parent_uri=None,
                       file_bnode=None):
        uri_concept = URIRef(self.URI_FILE_SCHEMA_ROOT + node.tag)

        bnode = BNode()
        self.g.add((bnode, RDF.type, uri_concept))

        # Link to file (if root passed in)
        if file_bnode:
            self.g.add((bnode, self.FROM_FILE, file_bnode))

        # Link to parent
        if parent_uri:
            self.g.add((parent_uri, self.CONTAINMENT, bnode))

        # Process attributes
        for k, v in node.attrib.iteritems():
            uri_attrib_concept = URIRef('{0}{1}_{2}'.format(self.URI_FILE_SCHEMA_ROOT,
                                                            node.tag,
                                                            k))
            self.g.add((bnode, uri_attrib_concept, Literal(v)))

        # Does it have content? If so, save it
        if node.text is not None and not str(node.text).isspace():
            self.g.add((bnode, self.TEXT, Literal(node.text)))

        # Process children
        for child in node.findall('./'):
            self.__parse_node__(child, bnode)

