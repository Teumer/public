import os
import sys
import subprocess


def console_output(notice_type, message):
    """
    Print [notice type] Message to the terminal
    :param notice_type: type of notice to give
    :param message: message to print out
    """
    if str(notice_type).lower() == "info":
        # Blue text
        output_text = "[ " + "\033[94m" + "INFO" + "\033[0m" + " ] "
    elif str(notice_type).lower() == "warn":
        # Yellow text
        output_text = "[ " + "\033[93m" + "WARN" + "\033[0m" + " ] "
    elif str(notice_type).lower() == "fail":
        # Red text
        output_text = "[ " + "\033[91m" + "FAIL" + "\033[0m" + " ] "
    elif str(notice_type).lower() == "exit":
        # Red text
        output_text = "[ " + "\033[91m" + "EXIT" + "\033[0m" + " ] "
    elif str(notice_type).lower() == "pass":
        # Green text
        output_text = "[ " + "\033[92m" + "PASS" + "\033[0m" + " ] "
    elif str(notice_type).lower() == "note":
        # Purple text
        output_text = "[ " + "\033[95m" + "NOTE" + "\033[0m" + " ] "
    elif str(notice_type).lower() == "dash_break":
        output_text = " - - - - - - - - - - - - - - - - - - - - - - - - - -"
    else:
        # Normal text
        output_text = "[ " + "\033[0m" + "????" + "\033[0m" + " ] "

    print("{0}{1}".format(output_text, message))
    sys.stdout.flush()


def console_binary(command_to_run):
    """
    Function to execute an OS command and return the stdout text.
    Convert b'binary to str
    :param command_to_run: run this command in the OS
    :return: command output
    :rtype: console_text as str
    """
    osstdout = subprocess.Popen(command_to_run,
                                shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                close_fds=True)
    console_text = osstdout.stdout.read()
    console_text = bytes(console_text).decode().strip()
    console_text = console_text.strip()
    return console_text


def console_binary_return_code(command_to_run):
    """
    Function to execute an OS command and return the stdout text and the return code of the command run.
    :param command_to_run: run this command in the OS
    :return: return command output and the return code of command
    :rtype: console_text as str, returncode as int
    """
    osstdout = subprocess.Popen(command_to_run,
                                shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                close_fds=True)
    console_text = osstdout.communicate()[0]
    console_text = bytes(console_text).decode().strip()
    return console_text, osstdout.returncode


def console_real_time(command_to_run):
    """
    Function to execute an OS command and print output in real time and return the stdout text and the return code of
    the command run
    :param command_to_run: command to run
    :return: stdout and exit code
    """
    osstdout = subprocess.Popen(command_to_run,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    while osstdout.poll() is None:
        out = osstdout.stdout.read(1)
        sys.stdout.write(bytes(out).decode())
        sys.stdout.flush()

    console_text = osstdout.communicate()[0]
    console_text = str(console_text).strip()
    return console_text, osstdout.returncode


def clear_terminal():
    """
    Function to clear the terminal
    """
    os.system('clear')