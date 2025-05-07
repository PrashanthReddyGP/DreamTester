from PySide6.QtWidgets import (QMainWindow, QComboBox, QPushButton, QTextEdit, 
                          QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpinBox, 
                          QDoubleSpinBox, QCheckBox, QGroupBox)
from PySide6.QtCore import Qt

class CustomUiMLFeatures(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Machine Learning Features")
        self.setGeometry(100, 100, 1000, 800)
        self.setupUi()
        self.custom_setup()

    def setupUi(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Feature Engineering Section
        self.feature_group = QGroupBox("Feature Engineering")
        feature_layout = QVBoxLayout()

        # Technical Indicators
        tech_layout = QHBoxLayout()
        tech_label = QLabel("Technical Indicators:")
        self.tech_indicators = QComboBox()
        self.tech_indicators.addItems([
            "RSI", "MACD", "Bollinger Bands", "Moving Averages",
            "Stochastic", "ATR", "OBV", "MFI"
        ])
        self.add_indicator_btn = QPushButton("Add")
        tech_layout.addWidget(tech_label)
        tech_layout.addWidget(self.tech_indicators)
        tech_layout.addWidget(self.add_indicator_btn)
        feature_layout.addLayout(tech_layout)

        # Price Action Features
        price_layout = QHBoxLayout()
        price_label = QLabel("Price Action:")
        self.price_features = QComboBox()
        self.price_features.addItems([
            "Candlestick Patterns", "Support/Resistance", 
            "Price Channels", "Volatility"
        ])
        self.add_price_btn = QPushButton("Add")
        price_layout.addWidget(price_label)
        price_layout.addWidget(self.price_features)
        price_layout.addWidget(self.add_price_btn)
        feature_layout.addLayout(price_layout)

        self.feature_group.setLayout(feature_layout)
        self.layout.addWidget(self.feature_group)

        # Model Selection and Configuration
        self.model_group = QGroupBox("Model Configuration")
        model_layout = QVBoxLayout()

        # Model Type Selection
        model_type_layout = QHBoxLayout()
        model_label = QLabel("Model Type:")
        self.model_selection = QComboBox()
        self.model_selection.addItems([
            "Neural Network", "Decision Tree", "Random Forest", 
            "Reinforcement Learning", "XGBoost", "LightGBM"
        ])
        model_type_layout.addWidget(model_label)
        model_type_layout.addWidget(self.model_selection)
        model_layout.addLayout(model_type_layout)

        # Hyperparameters
        hyper_layout = QHBoxLayout()
        self.epochs_spin = QSpinBox()
        self.epochs_spin.setRange(1, 1000)
        self.epochs_spin.setValue(100)
        self.epochs_spin.setPrefix("Epochs: ")
        
        self.batch_spin = QSpinBox()
        self.batch_spin.setRange(8, 512)
        self.batch_spin.setValue(32)
        self.batch_spin.setPrefix("Batch Size: ")
        
        self.learning_rate = QDoubleSpinBox()
        self.learning_rate.setRange(0.0001, 0.1)
        self.learning_rate.setValue(0.001)
        self.learning_rate.setPrefix("Learning Rate: ")
        
        hyper_layout.addWidget(self.epochs_spin)
        hyper_layout.addWidget(self.batch_spin)
        hyper_layout.addWidget(self.learning_rate)
        model_layout.addLayout(hyper_layout)

        # Training Options
        options_layout = QHBoxLayout()
        self.use_gpu = QCheckBox("Use GPU")
        self.cross_validate = QCheckBox("Cross Validation")
        self.early_stopping = QCheckBox("Early Stopping")
        options_layout.addWidget(self.use_gpu)
        options_layout.addWidget(self.cross_validate)
        options_layout.addWidget(self.early_stopping)
        model_layout.addLayout(options_layout)

        self.model_group.setLayout(model_layout)
        self.layout.addWidget(self.model_group)

        # Training and Testing Buttons
        button_layout = QHBoxLayout()
        self.train_button = QPushButton("Train Model")
        self.test_button = QPushButton("Test Model")
        self.save_model_button = QPushButton("Save Model")
        button_layout.addWidget(self.train_button)
        button_layout.addWidget(self.test_button)
        button_layout.addWidget(self.save_model_button)
        self.layout.addLayout(button_layout)

        # Results Display
        self.results_textedit = QTextEdit()
        self.results_textedit.setReadOnly(True)
        self.layout.addWidget(self.results_textedit)

    def custom_setup(self):
        self.train_button.clicked.connect(self.train_model)
        self.test_button.clicked.connect(self.test_model)
        self.save_model_button.clicked.connect(self.save_model)
        self.add_indicator_btn.clicked.connect(self.add_indicator)
        self.add_price_btn.clicked.connect(self.add_price_feature)
        self.model_selection.currentIndexChanged.connect(self.update_hyperparameters)

    def train_model(self):
        model_type = self.model_selection.currentText()
        epochs = self.epochs_spin.value()
        batch_size = self.batch_spin.value()
        learning_rate = self.learning_rate.value()
        
        self.results_textedit.append(f"Training {model_type} model...")
        self.results_textedit.append(f"Epochs: {epochs}")
        self.results_textedit.append(f"Batch Size: {batch_size}")
        self.results_textedit.append(f"Learning Rate: {learning_rate}")

    def test_model(self):
        self.results_textedit.append("Testing the model...")

    def save_model(self):
        self.results_textedit.append("Saving model...")

    def add_indicator(self):
        indicator = self.tech_indicators.currentText()
        self.results_textedit.append(f"Adding {indicator} to feature set...")

    def add_price_feature(self):
        feature = self.price_features.currentText()
        self.results_textedit.append(f"Adding {feature} to feature set...")

    def update_hyperparameters(self):
        model_type = self.model_selection.currentText()
        # Update hyperparameter ranges based on model type
        if model_type == "Neural Network":
            self.epochs_spin.setRange(1, 1000)
            self.batch_spin.setRange(8, 512)
        elif model_type == "Random Forest":
            self.epochs_spin.setRange(1, 200)
            self.batch_spin.setRange(32, 256)
        # Add more model-specific configurations as needed
