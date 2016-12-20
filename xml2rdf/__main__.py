__author__ = 'adam'

import argparse
from builder import Builder
import time
from os.path import basename
from rdflib import Graph

parser = argparse.ArgumentParser(description='Convert some data')
parser.add_argument('xml_files',
                    metavar='files',
                    type=str,
                    help='xml files',
                    nargs='+')
parser.add_argument('--consolidate',
                    action='store_true',
                    help='consolidate findings into one ttl file')

args = parser.parse_args()

if args.consolidate:
    g_consolidated = Graph()
    builder = Builder()

    for xml_file in args.xml_files:
        start = time.time()
        g = builder.parse(xml_file)
        end = time.time()
        print ('Loaded {} in {} sec'.format(xml_file, end - start))
        g_consolidated += g

    with open('consolidated.ttl', 'w') as ttl:
        start = time.time()
        g_consolidated.serialize(ttl, format='turtle')
        end = time.time()
        print ('Serialized in {} sec'.format(end - start))


# else:
#     with open(basename(xml_file) + '.ttl', 'w') as ttl:
#         g.serialize(ttl, format='turtle')

