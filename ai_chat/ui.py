import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QScrollArea
import chatbot
from PyQt5.QtCore import Qt

class ChatUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Chat UI')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Create a scroll area
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable horizontal scrolling

        # Create label to display conversation
        self.dialogLabel = QLabel(self)
        self.dialogLabel.setWordWrap(True)
        self.dialogLabel.setFixedSize(360, 275)  # Set a fixed size for the label
        self.dialogLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # Align text to top-left
        scrollArea.setWidget(self.dialogLabel)
        layout.addWidget(scrollArea)

        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        self.sendButton = QPushButton('Send', self)
        self.sendButton.clicked.connect(self.onSendButtonClick)
        layout.addWidget(self.sendButton)

        self.setLayout(layout)

    def onSendButtonClick(self):
        user_input = self.textEdit.toPlainText()
        ai_response = chatbot.chat_completion(user_input)
        self.updateDialogLabel(f"AI:\n{ai_response}")
        self.textEdit.clear()

    def updateDialogLabel(self, str):
        self.dialogLabel.setText(str)

if __name__ != '__main__':
    app = QApplication(sys.argv)
    chat_ui = ChatUI()
    chat_ui.show()
    sys.exit(app.exec_())