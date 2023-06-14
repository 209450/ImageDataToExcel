import os
import subprocess
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog
from openpyxl import Workbook

from TableOCTSingleFile import process_file

if __name__ == '__main__':
    print("TableOCT started")
    print(f"current dir: {os.getcwd()}")

    app = QApplication(sys.argv)
    directory_path = QFileDialog.getExistingDirectory()
    output_file_path, _ = QFileDialog.getSaveFileName()

    if not os.path.isfile(output_file_path):
        work_book = Workbook()
        work_book.save(output_file_path)

    files_names = os.listdir(directory_path)
    files_paths = [os.path.join(directory_path, file_name) for file_name in files_names]

    errors = []
    for input_file in files_paths:
        result = process_file(input_file, output_file_path)

        if result != 0:
            errors.append(input_file)

    print(errors)
