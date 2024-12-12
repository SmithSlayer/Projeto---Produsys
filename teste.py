from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy, QListWidget, QListWidgetItem
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferramentas e Cálculo")
        self.setGeometry(100, 100, 800, 400)

        # Layout principal
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Menu à esquerda
        self.menu_layout = QVBoxLayout()
        self.create_menu_buttons()

        # Lista de itens selecionados
        self.item_list = QListWidget()

        # Espaço de entrada de dados
        self.input_layout = QVBoxLayout()
        self.create_input_area()

        # Espaço de saída de dados
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        # Adicionando os layouts no layout principal
        main_layout.addLayout(self.menu_layout)
        main_layout.addWidget(self.item_list)
        main_layout.addLayout(self.input_layout)
        main_layout.addWidget(self.output_area)

    def create_menu_buttons(self):
        # Adicionando botões para o menu
        tools = ["Martelo", "Prego", "Serrote", "Chave de Fenda"]
        for tool in tools:
            button = QPushButton(tool)
            button.clicked.connect(self.select_tool)
            self.menu_layout.addWidget(button)

        # Adicionando espaço extra no final
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.menu_layout.addItem(spacer)

    def create_input_area(self):
        # Rótulo para indicar o campo
        self.label = QLabel("Selecionar uma ferramenta no menu à esquerda")
        self.input_layout.addWidget(self.label)

        # Campo de entrada para a quantidade
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Digite a quantidade")
        self.input_layout.addWidget(self.input_field)

        # Botões de ação
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Adicionar")
        self.add_button.clicked.connect(self.add_to_list)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.calculate_button)
        self.input_layout.addLayout(button_layout)

    def select_tool(self):
        # Obter o botão clicado
        sender = self.sender()
        selected_tool = sender.text()
        self.label.setText(f"Ferramenta selecionada: {selected_tool}")

    def add_to_list(self):
        # Adicionar ferramenta e quantidade à lista
        selected_tool = self.label.text().replace("Ferramenta selecionada: ", "")
        quantity = self.input_field.text()

        if not selected_tool or selected_tool == "Selecionar uma ferramenta no menu à esquerda":
            self.output_area.setText("Por favor, selecione uma ferramenta.")
            return

        if not quantity.isdigit():
            self.output_area.setText("Digite uma quantidade válida.")
            return
        
        total = quantity + quantity

        item_text = f"{selected_tool} - Quantidade: {quantity} - Total: {total}"
        self.item_list.addItem(item_text)
        self.input_field.clear()

    def calculate(self):
        # Exibir todos os itens da lista na área de saída
        
        
        
        total_items = self.item_list.count()

        if total_items == 0:
            self.output_area.setText("Nenhum item foi adicionado.")
            return

        result = "Itens selecionados:\n"
        for i in range(total_items):
            result += f"{self.item_list.item(i).text()}\n"

        self.output_area.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
