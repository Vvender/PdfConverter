import aspose.pdf as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog


class Converter:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.pdf_path = ""

    def select_location(self):
        try:
            self.pdf_path, _ = QFileDialog.getOpenFileName(None, "Select PDF File", "", "PDF Files (*.pdf)")
            if self.pdf_path:
                print("Selected file path:", self.pdf_path)
                self.pdf_path = self.pdf_path  # Store the selected PDF file path
                self.button_icon_changer("pdf_image.png")
            else:
                print("No file selected")
                self.button_icon_changer("file-plus.svg")

        except Exception as e:
            handle_error("An error occurred during selecting file location", e)

    def button_icon_changer(self, icon):
        try:
            icon_pdf = create_icon(f":/Icons/{icon}")
            self.ui.btn_file_location.setIcon(icon_pdf)
        except Exception as e:
            handle_error("An error occurred during button icon change", e)

    def label_info_changer(self, result):
        try:
            messages = {
                0: "Please check\nthe file types \nyou want to \nconvert.",
                1: "Please select\nthe file \nyou want to convert.",
                2: "Your file\nsuccessfully \nconverted!"
            }
            icons = {
                0: "x-square.svg",
                1: "x-square.svg",
                2: "check-circle .svg"
            }
            self.ui.lbl_info.setText(messages.get(result, ""))
            icon_path = f":/Icons/{icons.get(result, '')}"
            pixmap = QtGui.QPixmap(icon_path)  # Create a QPixmap from the icon path
            self.ui.lbl_icon_converted.setPixmap(pixmap)  # Set the QPixmap as the label's pixmap
            self.ui.pages.setCurrentIndex(1)
        except Exception as e:
            handle_error("An error occurred during info icon change", e)

    def call_convert(self):
        selected_pdf_path = self.pdf_path
        try:
            if selected_pdf_path:
                if self.ui.cb_excel.isChecked():
                    self.convert_to_excel()
                if self.ui.cb_word.isChecked():
                    self.convert_to_word()  # Call the convert_to_word method if Word conversion is selected
                if not self.ui.cb_excel.isChecked() and not self.ui.cb_word.isChecked():
                    self.label_info_changer(0)  # Set the error icon and message
            else:
                self.label_info_changer(1)  # Set the error icon and message
        except Exception as e:
            handle_error("An error occurred during converting pdf", e)

    def convert_to_excel(self):
        selected_pdf_path = self.pdf_path
        try:
            # Instantiate a Document object using the input PDF file
            pdf_document = pd.Document(selected_pdf_path)

            # Create an instance of ExcelSaveOptions to customize the settings for PDF to XLSX conversion
            options = pd.ExcelSaveOptions()

            # Save the PDF document as XLSX
            excel_file_path = selected_pdf_path.replace('.pdf', '.xlsx')
            pdf_document.save(excel_file_path, options)

            print("PDF converted to XLSX")
            self.label_info_changer(2)  # Set the success icon and message
        except Exception as e:
            handle_error("An error occurred during converting file to XLSX", e)

    def convert_to_word(self):
        selected_pdf_path = self.pdf_path
        try:
            # Perform the conversion to Word
            # Add the code for converting PDF to Word here
            print("PDF converted to Word", selected_pdf_path)
            pass

        except Exception as e:
            handle_error("An error occurred during converting file to word", e)


def handle_error(message, error):
    print(f"{message}: {error}")


def create_icon(path):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon
