# Source: https://gist.github.com/miratcan/429895ef7c78a2c00cb7de9a44b11e6b
#
# Run as:
#  cd hackerrank_xor_and_sum
#  python ../hrtool.py
#
# The folder structure should be:
# - solution.py
# - inputs/{download and save inputs here}
# - outputs/{download and save outputs here}

import glob
import re
import subprocess
from os.path import exists
from sys import exit

INPUT_FOLDER = 'input/'
OUTPUT_FOLDER = 'output/'
SOLUTION_FILE = 'solution.py'

WRONG_PLACE_TO_RUN_MSG = \
    'You have to run this program under, downloaded inputs and outputs.'

REQUIRED_FOLDERS = [INPUT_FOLDER, OUTPUT_FOLDER]
NUMBER_FINDER = re.compile(r'\d+')


def get_output_filename(input_filename):
    num = NUMBER_FINDER.findall(input_filename)[0]
    return f"output/output{num}.txt"


wrong_place_to_run = False
for folder in REQUIRED_FOLDERS:
    if not exists(folder):
        print(f"Folder '{folder}' does not exists.")
        wrong_place_to_run = True

if wrong_place_to_run:
    print(WRONG_PLACE_TO_RUN_MSG)
    exit(1)

if not exists(SOLUTION_FILE):
    print('Solution must be inside solution.py, put your solution to there '
          'and run this command again.')
    exit(1)

input_files = glob.glob('input/*.txt')


for input_file in input_files:
    output_file = get_output_filename(input_file)
    cmd = 'python3 solution.py'

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        stdin=subprocess.PIPE, shell=True, encoding='utf8')

    with open(input_file) as f:
        input_data = f.read()

    with open(output_file) as f:
        output_data = f.read()

    out, err = process.communicate(input_data)

    if err:
        print("Error happened when executing your solution:")
        print("--------------------------------------------")
        print(err)
        exit(1)

    out = out[:-1]
    if out == output_data:
        print(f'{input_file}: SUCCESS')
    else:
        print(f'{input_file}: FAIL')
    print("-------OUTPUT------")
    print(out)
