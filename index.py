#!/usr/bin/env python3

import os
from pathlib import Path

from PyQt4.QtGui import *

from views.MainWindow import MainWindow
from helpers.api_handler import SERVER_NAME_VARIABLE, USER_NAME_VARIABLE, USER_PASSWORD_VARIABLE
from helpers.input_question import input_default


def process_env_variable(variable, message, default):
    if variable not in os.environ:
        server_name = input_default(
            message,
            default
        )
        os.environ[variable] = server_name
        return True

    return False


# TODO: Add a default value?
def process_configuration_environments():

    did_change = {
        SERVER_NAME_VARIABLE: process_env_variable(
                SERVER_NAME_VARIABLE,
                'The Environment variable for Server Name is not defined. Type a value for it',
                'http://localhost:3000/'
            ),

        USER_NAME_VARIABLE: process_env_variable(
                USER_NAME_VARIABLE,
                'The Environment variable for User Name is not defined. Type a value for it',
                'user'
            ),

        USER_PASSWORD_VARIABLE: process_env_variable(
                USER_PASSWORD_VARIABLE,
                'The Environment variable for User Password is not defined. Type a value for it',
                'password   '
            )
    }

    for value in did_change.values():
        if not value:
            return

    answer = input_default("Do you want to save the changes to a file? (y/N)", None)
    if answer and  answer.lower() in ['y', 'yes']:
        file_name = input_default('Type the file to save', '{}/.profile'.format(str(Path.home())))
        with open(file_name, 'a') as file:
            file.write('\n# Flipermercado configuration variables:\n')
            for key in did_change.keys():
                if did_change[key]:
                    file.write('export {}={}\n'.format(key, os.environ[key]))
            file.write('\n##############################################\n')


if __name__ == "__main__":
    process_configuration_environments()

    print("Initializing application")
    app = QApplication([])

    main_widget = MainWindow()

    main_widget.show()
    print("Exiting application")
    app.exec_()
