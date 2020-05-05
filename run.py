#!/usr/bin/env python3

from os import path as os_path
from shutil import move as shutil_move
import tempfile
import argparse

import sys
sys.path.insert(0, '/home/src')
from RP2paths import build_parser as RP2paths_buildparser
from RP2paths import entrypoint as RP2paths_entrypoint



if __name__ == "__main__":

    parser = argparse.ArgumentParser('Python wrapper for the python RP2paths script')
    parser.add_argument('-_file_rp2_pathways', type=str)
    parser.add_argument('-rp2paths_pathways', type=str)
    parser.add_argument('-rp2paths_compounds', type=str)
    parser.add_argument('-timeout', type=int)
    parser.add_argument('-server_url', type=str)
    parser.add_argument('-galaxy', type=str)
    params = parser.parse_args()

    if (params.timeout < 0):
        logging.error('Time out cannot be less than 0: '+str(params.timeout))
        exit(1)

    with tempfile.TemporaryDirectory() as tmpdirname:
        args = [
            'all',
            params._file_rp2_pathways,
            '--outdir', tmpdirname,
            '--timeout', str(params.timeout)
            ]
        RP2paths_entrypoint(args)
        shutil_move(tmpdirname+'/out_paths.csv', params.rp2paths_pathways)
        shutil_move(tmpdirname+'/compounds.txt', params.rp2paths_compounds)
