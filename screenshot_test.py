# Author: Adam RochS

import datetime
import json
import os
import time

from PIL import ImageGrab


def run():
    result = ""
    error_message = ""
    info = ""

    start_time = time.time()

    try:
        path = screenshot_test()
        info = path

    except OSError:
        result = "FAILURE"
        error_message = "python encountered an OSError"
        end_time = time.time()
        results = build_results_obj(result, start_time,
                                    end_time, error_message,
                                    info)
        print(results)

    except SystemError:
        result = "FAILURE"
        error_message = "python encountered an SystemError"
        end_time = time.time()
        results = build_results_obj(result, start_time,
                                    end_time, error_message,
                                    info)
        print(results)

    except Exception as e:
        result = "FAILURE"
        error_message = "python encountered an exception"
        info = "the exception was: " + sanitize(str(type(e))) + str(e)
        end_time = time.time()
        results = build_results_obj(result, start_time,
                                    end_time, error_message,
                                    info)
        print(results)

    else:
        result = "SUCCESS"
        end_time = time.time()
        results = build_results_obj(result, start_time,
                                    end_time, error_message,
                                    info)
        print(results)


def screenshot_test():
    # take a screenshot of the current screen
    snapshot = ImageGrab.grab()

    target_path = build_target_path()

    # save the screenshot. we need to save it so that it will have a path.
    # before we save it, it is not a file-like object, but an Image object.
    snapshot.save(target_path)

    snapshot_size = get_file_size(target_path)

    # snapshot_size = 0  # trigger an exception

    if snapshot_size <= 0:
        raise Exception("snapshot had file size of zero or less.")

    return target_path


def build_target_path():
    current_file = __file__  # special python variable, is the current file

    current_directory = os.path.dirname(current_file)  # current directory

    # we could've done this on one line: currentDirectory = os.path.dirname(__file__)

    up_one_directory = os.path.dirname(current_directory)  # gets us to testx_python

    date_string = build_date_string()

    # we want to now go down into the screenshots directory
    target_path = up_one_directory + "\\screenshots\\" + date_string + ".png"

    return target_path


def build_date_string():
    dt = datetime.datetime

    now = dt.now()

    date_string = (str(now.month) + "-" + str(now.day) + "-" + str(now.year)
                   + "," +
                   (str(now.hour) if now.hour < 12 else str(now.hour - 12))
                   + "_" +
                   (str(now.minute) if now.minute >= 10 else '0' +
                                                             str(now.minute)) + (
                       'AM' if now.hour < 12 else 'PM'))

    return date_string


def get_file_size(path):
    # snapshotInfo is a stat object with various data about the file
    file_info = os.stat(path)

    # snapshotSize is the file's size in bytes
    file_size = file_info.st_size

    return file_size


def build_results_obj(result, start_time, end_time,
                      error_message, info):
    results = {"result": result,
               "testStartDateTime": start_time,
               "testFinishDateTime": end_time,
               "errorMessage": error_message,
               "info": info}

    results_json = json.dumps(results)

    return results_json


def sanitize(string):
    index = string.find('\'')
    sanitized = string[:index] + '\'' + string[index:] + '\''
    return sanitized


run()
