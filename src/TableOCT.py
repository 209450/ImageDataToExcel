import os
import subprocess
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog
from openpyxl import Workbook

from TableOCTSingleFile import process_file, PyProcessor

if __name__ == '__main__':
    print("TableOCT started")
    print(f"current dir: {os.getcwd()}")

    app = QApplication(sys.argv)
    directory_path = QFileDialog.getExistingDirectory()
    output_file_path, _ = QFileDialog.getSaveFileName()

    if not os.path.isfile(output_file_path):
        work_book = Workbook()
        work_book.save(output_file_path)
        # open(output_file_path, "x")

    files_names = os.listdir(directory_path)
    files_paths = [os.path.join(directory_path, file_name) for file_name in files_names]

    py_processor = PyProcessor()
    for input_file in files_paths:
        py_processor.process(input_file, output_file_path)

        # command = f"python TableOCTSingleFile.py --input {file_path} --output {directory_path}"
        # command_split = command.split()
        # p = subprocess.Popen(command_split, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # if p.returncode != 0:
        #     print(f"error occured: {file_path}")