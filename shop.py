from PyQt5.QtWidgets import *
from view import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args: object, **kwargs: object) -> None:
        '''
        Constructor to create the main window
        :param args: Connects main window to PyQt5 library
        :param kwargs: Connects main window to the gui built in view.py
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # Sets up four basic variables for handling cart totals
        self.cookies = 0
        self.corn = 0
        self.pizza = 0
        self.water = 0
        self.total = 0   # Initializes a total variable for use in calculating the cart total
        # The following connections sets each button to a corresponding functon
        self.ClearButton.clicked.connect(lambda: self.clear("clear"))   # Clear and purchase buttons send their purpose as an argument
        self.PurchaseButton.clicked.connect(lambda: self.clear("purchase"))
        self.tabWidget.currentChanged.connect(lambda: self.refreshShop())   # For optimization, sets each tab to refresh when clicked onto
        self.CookiesPushUp.clicked.connect(lambda:self.buttonClick("cookiesUp"))    # buttonName set to the name
        self.CookiesPushDown.clicked.connect(lambda:self.buttonClick("cookiesDown"))
        self.CornPushUp.clicked.connect(lambda:self.buttonClick("cornUp"))
        self.CornPushDown.clicked.connect(lambda:self.buttonClick("cornDown"))
        self.PizzaPushUp.clicked.connect(lambda:self.buttonClick("pizzaUp"))
        self.PizzaPushDown.clicked.connect(lambda:self.buttonClick("pizzaDown"))
        self.WaterPushUp.clicked.connect(lambda:self.buttonClick("waterUp"))
        self.WaterPushDown.clicked.connect(lambda:self.buttonClick("waterDown"))
        self.tabWidget.setCurrentIndex(0)   # Code to ensure starting tab is the shop page

    def refreshShop(self) -> None:
        '''
        Used to update labels and displays to output current variables
        :return: None
        '''
        # Detects current tab before updating displays in order to optimize the refreshShop function
        if self.tabWidget.currentIndex() == 0:
            self.CookiesCounter.display(self.cookies)
            self.CornCounter.display(self.corn)
            self.PizzaCounter.display(self.pizza)
            self.WaterCounter.display(self.water)
        if self.tabWidget.currentIndex() == 1:
            self.CookieTotalAmount.setText(f'{self.cookies} = ${(self.cookies * 1.25):.2f}')
            self.CornTotalAmount.setText(f'{self.corn} = ${(self.corn * 1):.2f}')
            self.PizzaTotalAmount.setText(f'{self.pizza} = ${(self.pizza * 2):.2f}')
            self.WaterTotalAmount.setText(f'{self.water} = ${(self.water * .5):.2f}')
            self.total = self.cookies * 1.25 + self.corn + self.pizza * 2 + self.water * .5     # total used in clear()
            self.CartTotalAmount.setText(f'${self.total:.2f}')

    def buttonClick(self, buttonName: str) -> None:
        '''
        Centralized area for handling button presses on the shop page
        :param buttonName: Name for the button pressed in correspondence to the variable name
        :return: None
        '''
        if buttonName == "cookiesUp":
            self.cookies += 1
        if buttonName == "cookiesDown":
            if self.cookies > 0:    # Detects if value is above 0 to avoid negative variables
                self.cookies -= 1
        if buttonName == "cornUp":
            self.corn += 1
        if buttonName == "cornDown":
            if self.corn > 0:
                self.corn -= 1
        if buttonName == "pizzaUp":
            self.pizza += 1
        if buttonName == "pizzaDown":
            if self.pizza > 0:
                self.pizza -= 1
        if buttonName == "waterUp":
            self.water += 1
        if buttonName == "waterDown":
            if self.water > 0:
                self.water -= 1
        self.refreshShop()      # Refreshes shop to update displays after each button press

    def clear(self, purpose: str) -> None:
        '''
        Sets variables to 0, then opens a dialog box depending on purpose
        :param purpose: Inputs either clear or purchase to determine correct dialog box
        :return: None
        '''
        tempTotal = self.total      # Sets a temporary total in order to clear variables before dialog box
        self.cookies = 0
        self.corn = 0
        self.pizza = 0
        self.water = 0
        self.refreshShop()
        dlg = QMessageBox(self)     # Sets name for dialog box
        dlg.setWindowTitle("Jeremy's Shop")
        if purpose == "clear":      # Uses purpose argument to determine clear or purchase button
            dlg.setText("Cart Cleared!")
        else:
            if tempTotal == 0:      # Detects if the cart is empty and throws an exception
                dlg.setText("Error: Cart Empty")
            else:
                dlg.setText(f"Transaction Complete! Total Comes Out To ${tempTotal:.2f}")
                self.tabWidget.setCurrentIndex(0)  # Brings the user back to the shop page if transaction was successful
        button = dlg.exec()

