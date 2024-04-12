import sys

from PyQt6.QtWidgets import QApplication

from GUI.main_gui import MainWindow

from Parser.main import name_list, price_list, picture_list

if __name__ == '__main__':
    app = QApplication(sys.argv)

    image_links = picture_list
    texts = name_list
    prices = price_list

    image_text_app = MainWindow(image_links, texts, prices)

    image_text_app.show()

    sys.exit(app.exec())
