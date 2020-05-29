import os
import argparse
import jinja2
import pdb
import sys

from lxml import etree

sys.path.insert(0, 'FrameworkInternals')  # this is quasar's FrameworkInternals

from transformDesign import transformDesign
import quasar_basic_utils

quasar_namespaces = {'d':'http://cern.ch/quasar/Design'}

def get_list_classes(design_file_name):
    ''' returns a dict where keys are classes and values are lists of cache-variables '''
    f = file(design_file_name,'r')
    tree = etree.parse(f)
    classes_cachevariables = tree.xpath('d:class', namespaces = quasar_namespaces)
    classes_cachevariables = map(lambda x: x.attrib['name'], classes_cachevariables)
    out_dict = {}
    for className in classes_cachevariables:
        cache_vars = tree.xpath("d:class[@name='{0}']/d:cachevariable".format(className), namespaces = quasar_namespaces)
        cache_vars = map(lambda x: x.attrib['name'], cache_vars)
        out_dict[className] = cache_vars
    return out_dict

parser = argparse.ArgumentParser(description='Generate design-dependent part of Poverty')
parser.add_argument('--output_dir', help='Where to put the output', required=True)

args = parser.parse_args()

try:
    transformDesign(
        os.path.join('Poverty', 'templates', 'Poverty.hpp.jinja'),
        outputFile=os.path.join(args.output_dir, 'Poverty.hpp'),
        requiresMerge=False,
        astyleRun=True,
        additionalParam=None)
        
    transformDesign(
        os.path.join('Poverty', 'templates', 'Poverty.cpp.jinja'),
        outputFile=os.path.join(args.output_dir, 'Poverty.cpp'),
        requiresMerge=False,
        astyleRun=True,
        additionalParam=None)
        
    transformDesign(
        os.path.join('Poverty', 'templates', 'PovertyPythonModule.cpp.jinja'),
        outputFile=os.path.join(args.output_dir, 'PovertyPythonModule.cpp'),
        requiresMerge=False,
        astyleRun=True,
        additionalParam=None)
except:
    quasar_basic_utils.quasaric_exception_handler()
