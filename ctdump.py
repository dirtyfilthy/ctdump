#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
	ctdump.py - Caleb Anderson (alhazred)
------------------------------------------------------------------------------
"""

version="0.1"

## # LIBRARIES # ##
import re
import requests



def banner_str():
	global version
	b = '''
       __      __                                      
 .----.|  |_.--|  |.--.--.--------.-----.  .-----.--.--.
 |  __||   _|  _  ||  |  |        |  _  |__|  _  |  |  |
 |____||____|_____||_____|__|__|__|   __|__|   __|___  |
                                  |__|     |__|  |_____|

	
  Version {v} Made by Caleb Anderson (alhazred)

  Dump subdomains from Entrust certificate transparency
  logs.

  Heavily based on https://github.com/UnaPibaGeek/ctfr 
  by UnaPibaGeek
	'''.format(v=version)
	return b

def parse_args():
	import argparse
	parser = argparse.ArgumentParser(description=banner_str(),formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('domain', nargs=1, type=str, help="Target domain.")
	parser.add_argument('-o', '--output', type=str, help="Output file.")

	return parser.parse_args()

def clear_url(target):
	return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
	with open(output_file,"a") as f:
		f.write(subdomain + '\n')
		f.close()

def main():
	args = parse_args()
	args.domain = args.domain[0]
	subdomains = []
	target = clear_url(args.domain)
	output = args.output
	url = "https://ctsearch.entrust.com/api/v1/certificates?fields=subjectCNReversed&domain={d}&includeExpired=false&exactMatch=false&limit=1000".format(d=target)
	req = requests.get(url)

	if req.status_code != 200:
		print("[X] Information not available! (code={})".format(req.status_code)) 
		exit(1)

	for (key,value) in enumerate(req.json()):
		subdomains.append(value['subjectCNReversed'][::-1])

	subdomains = sorted(set(subdomains))

	for subdomain in subdomains:
		print("{s}".format(s=subdomain))
		if output is not None:
			save_subdomains(subdomain,output)

main()

