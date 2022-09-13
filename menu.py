# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import chunk_that_csv
import platform
import socket
import os
from dotenv import load_dotenv

def get_security_check():
    """
    
    :return:
    """
    platform.node() # otenv
    platform.uname() # username
    platform.system() # system version
    platform.machine() # which processor
    platform.processor() #
    socket.gethostname()
    'bob-host'
    os.environ['COMPUTERNAME']
    'bob-computer'

def run_security_check():
    n1 = platform.node()
    n2 = socket.gethostname()
    n3 = os.environ["USER"]
    n4 = os.environ["HOME"]
    n5 = os.environ["LOGNAME"]
    if n1 == n2 or n1 == n3:
        return n1
    elif n2 == n3:
        return n2 else:
        raise Exception("Computer names are not equal to each other")
        (n1 instead of n2


def main():
    get_security_check()
    get_user_name(username)
    get_data(username, filename)

def get_user_name(username):
    # Use a breakpoint in the code line below to debug your script.
    username = input("Hello what is your name?")
    print(f"Hi, {username}")  # Press ⌘F8 to toggle the breakpoint.


def get_data(username, filename):
    filename = input(f"Hello {username} please type in the file name with extension of the file that is too big, for example voters.csv?")
    print(f"Hi, {filename}")
    chunk_that_csv.get_whole_file(filename)


def save_csv_sqlite():


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    username = str
    filename = str
    socket_gethostname = socket.gethostname
    os_environ_user = os.environ['USER']
    platform_uname = platform.uname()
    platform_node = platform.node()
    platform_machine = platform.machine()
    platform_system = platform.system()
    os_environ_user = os.environ['USER']
    os_environ_home = os.environ['HOME']
    os_environ_logname = os.environ['LOGNAME']
    dot_env_path = PATH_TO_ENV
    users
    main()
    load_dotenv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
