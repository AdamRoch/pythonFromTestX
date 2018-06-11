# ==============================================================
# Sample Python code for simple CPU excercise program
#
#   Creates a list of LIST_SIZE length and populates the list
#   with random numbers.  Does this TIMES_TO_BUILD times.
#   Set the THREAD_COUNT variable to the number of threads.
#
# ==============================================================

import time
import random
import threading
import json

LIST_SIZE = 1024 * 1024  # Set the size random number list
THREAD_COUNT = 2  # How many threads to run
TIMES_TO_BUILD = 1  # How many times each thread should create the list


# -----------------------------------------------------
# Program entry point
# -----------------------------------------------------
def run():
    result = ""
    error_message = ""
    info = ""
    try:

        # Get the start datetime
        #
        start_time = time.time()

        # Create THREAD_COUNT number of threads
        # that call the cpu_test()  function
        #
        threads = []
        for i in range(THREAD_COUNT):
            t = threading.Thread(target=cpu_test)
            threads.append(t)
            t.start()

        # Wait for all of the threads to finish
        for x in threads:
            x.join()

        end_time = time.time()

        info += "thread count was: " + str(THREAD_COUNT)

    except MemoryError:
        result = "FAILURE"
        error_message = "python encountered a MemoryError"
        end_time = time.time()
        results = build_results_obj(result, start_time,
                                    end_time, error_message,
                                    info)
        print(results)


    except Exception as e:
        result = "FAILURE"
        error_message = "python encountered an exception"
        info = "the exception was: " + sanitize(str(type(e)))
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


# -------------------------------------------------------------
# cpu_test()
# Creates a list of LIST_SIZE and populates each position
# with a random number.  Does this TIMES_TO_BUILD times
# -------------------------------------------------------------
def cpu_test():
    # print("Starting thread...")
    for i in range(TIMES_TO_BUILD):

        # Create a new list
        #
        myRandoms = []

        # Write some random numbers to the list
        # Convert to strings to make the CPU work a little harder
        #
        for i in range(0, LIST_SIZE):
            randomNum = str(random.random())
            myRandoms.append(randomNum)


            # print("Ending thread.")


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
