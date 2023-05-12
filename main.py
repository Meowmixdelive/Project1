from shop import *

# Idea gotten from lab #1
def main() -> None:
    '''
    Initializes the program, brings up the gui window, and begins the application
    :return: None
    '''
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
