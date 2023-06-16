import os
import subprocess
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog
from openpyxl import Workbook

from TableOCTSingleFile import process_file
from gui.continue_program_dialog import ContinueProgramDialog

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
    number_file_paths = len(files_paths)
    for file_index, input_file in enumerate(files_paths, 1):
        file_name = os.path.basename(input_file)
        print(f"Processing {file_name}, {file_index}/{number_file_paths}")

        dialog = ContinueProgramDialog(f"Do you want to continue with file {file_name}")
        dialog.show()

        dialog_result = dialog.exec_()
        if not dialog_result:
            break

        try:
            result = process_file(input_file, output_file_path)
        except Exception:
            result = -1

        if result != 0:
            errors.append(input_file)

    print(errors)
