import os.path
import sys
import pytest

IO_FOLDER_RELATIVE_PATH = "ailab_ner/tests/inputs_outputs/"

TEST_MODE = True
''' TEST_MODE says that this module will be imported and used for
test files only, so it'll move the execution directory to the scripts
src folder so they can be tested. See end of this file for more
details '''


def change_execution_directory(relative_path_directory_to_execute_from):
    ''' Receives a string of a relative path to a directory to execute this
    code from. It's useful for testing libraries in other folders '''
    print(os.getcwd())
    PACKAGE_PARENT = relative_path_directory_to_execute_from
    SCRIPT_DIR = os.path.dirname(
        os.path.realpath(
            os.path.join(
                os.getcwd(),
                os.path.expanduser(__file__)
                        )))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

@pytest.fixture
def load_expected_io(request):
    ''' Fixture created to safely load expected inputs and outputs from
        IO folder '''
    input_filename, output_filename = request.param
    relative_path_to_file = IO_FOLDER_RELATIVE_PATH + input_filename
    with open(relative_path_to_file) as f:
        input_file_content = f.read()

    relative_path_to_file = IO_FOLDER_RELATIVE_PATH + output_filename
    with open(relative_path_to_file) as f:
        output_file_content = f.read()

    return input_file_content, output_file_content


if TEST_MODE:
    change_execution_directory('../')