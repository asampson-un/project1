from logic import *

def main() -> None:
    """
    Create window from logic (and gui)
    """
    application :QApplication = QApplication([])
    window :Logic = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()