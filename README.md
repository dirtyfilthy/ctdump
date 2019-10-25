# ctdump.py

    ----.|  |_.--|  |.--.--.--------.-----.  .-----.--.--.
    |  __||   _|  _  ||  |  |        |  _  |__|  _  |  |  |
    |____||____|_____||_____|__|__|__|   __|__|   __|___  |
                                     |__|     |__|  |_____|

	
Version 0.1 Made by Caleb Anderson (alhazred)

Dump certificate transparency subdomains from the Entrust API for pentesting passive recon.

crt.sh wasn't working at the time...

Heavily based on https://github.com/UnaPibaGeek/ctfr by UnaPibaGeek

## Requirements

Python 3, standard modules only

## Usage

  usage: ctdump.py [-h] [-o OUTPUT] domain

  positional arguments:
    domain                Target domain.
  
  optional arguments:
    -h, --help            show this help message and exit
    -o OUTPUT, --output OUTPUT
                          Output file.
