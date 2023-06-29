from pathlib import Path

from users_by_access import UsersByAccess

if __name__ == '__main__':
    file1 = Path('users.json')
    task1 = UsersByAccess(file1)
    task1.ask_data()
    task1.write_data()

    file2 = Path('users.csv')
    task2 = UsersByAccess(file2)
    task2.ask_data()
    task2.write_data()
