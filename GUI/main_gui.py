from io import BytesIO

import requests
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, image_links, texts, prices):
        super().__init__()
        self.setWindowTitle("Fortnite Shop ToDay")
        window = QMainWindow()
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        images_per_row = 10
        for i in range(0, len(image_links), images_per_row):
            row_layout = QHBoxLayout()
            for j in range(images_per_row):
                if i + j < len(image_links):
                    image_link = image_links[i + j]
                    text = texts[i + j]
                    price = prices[i + j]

                    image_label = QLabel()
                    response = requests.get(image_link)
                    image_data = BytesIO(response.content)
                    image = QPixmap()
                    image.loadFromData(image_data.read())
                    image_scaled = image.scaledToWidth(100)
                    image_label.setPixmap(image_scaled)

                    text_label = QLabel(text + " " + price + " V-Bucks")
                    text_label.setWordWrap(True)

                    image_text_layout = QVBoxLayout()
                    image_text_layout.addWidget(image_label)
                    image_text_layout.addWidget(text_label)

                    row_layout.addLayout(image_text_layout)

            main_layout.addLayout(row_layout)


