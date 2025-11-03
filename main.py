from ui.cli import UserInterface
from utils.io_utils import create_sample_csv

def main():
    create_sample_csv()
    ui = UserInterface()
    ui.run()



if __name__ == "__main__":
    main()