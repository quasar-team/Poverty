import os
import argparse
import jinja2
import pdb

from lxml import etree

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
parser.add_argument('--design', help='Path to your Design.xml', required=True)
parser.add_argument('--output_dir', help='Where to put the output', required=True)

args = parser.parse_args()

classes_cachevariables = get_list_classes(args.design)

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

fout = file(os.path.join(args.output_dir,'PovertyPythonModule.cpp'), 'w')
fout.write(env.get_template('PovertyPythonModule.jinja.cpp').render({'classes_cachevariables':classes_cachevariables}))
fout = file(os.path.join(args.output_dir,'Poverty.hpp'), 'w')
fout.write(env.get_template('Poverty.jinja.hpp').render({'classes_cachevariables':classes_cachevariables}))
fout = file(os.path.join(args.output_dir,'Poverty.cpp'), 'w')
fout.write(env.get_template('Poverty.jinja.cpp').render({'classes_cachevariables':classes_cachevariables}))
