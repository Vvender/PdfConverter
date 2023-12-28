import sys
from PyQt5.QtWidgets import QApplication, QWidget
from EventHandler.event_handler import EventHandler
from Converter.converter import Converter
from Gui.ui_pdf_converter import Ui_ConverterForm


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_ConverterForm()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.event_handler = EventHandler(self.app, self.ui)
        self.converter = Converter(self.app, self.ui)

        # Main Button Events
        self.ui.btn_github.clicked.connect(self.event_handler.event_handler)
        self.ui.btn_linkedin.clicked.connect(self.event_handler.event_handler)
        self.ui.btn_cv.clicked.connect(self.event_handler.event_handler)
        self.ui.btn_email.clicked.connect(self.event_handler.event_handler)
        self.ui.btn_info_return.clicked.connect(self.event_handler.event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # Converter Button Event
        self.ui.btn_file_location.clicked.connect(self.converter.select_location)
        self.ui.btn_convert.clicked.connect(self.converter.call_convert)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
