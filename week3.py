import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QEvent

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Task 3 - F1D022005 - Dhinda Tsamara Shalsabilla")
        self.setFixedSize(550, 400)

        self.label = QLabel("Gerakkan mouse!", self)
        self.label.setStyleSheet("background-color: lightblue; padding: 5px; border-radius: 5px;")
        self.label.setFixedSize(120, 30)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(200, 150)  

        self.setMouseTracking(True)  
        self.label.installEventFilter(self)  

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        self.label.setText(f"x: {x}, y: {y}")

    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == QEvent.Enter:
            self.random_position()
        return super().eventFilter(obj, event)

    def random_position(self):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()

        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)

        colors = ["red", "blue", "green", "purple", "orange", "pink"]
        random_color = random.choice(colors)
        self.label.setStyleSheet(f"background-color: {random_color}; color: white; padding: 5px; border-radius: 5px;")

        self.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())