from .helpers import google_analytics
from .helpers import digital_ocean
from .helpers import server_util
import threading
import traceback


def keys_to_str(input_dict):
    for key in input_dict:
        if type(input_dict[key]) == int or type(input_dict[key]) == float:
            input_dict[key] = str(input_dict[key])


def get_ga(analytics_dict):
    # Import google analytics statistics
    analytics_dict['output'] = google_analytics.main()


def get_docn(docn_dict):
    docn_dict['output'] = digital_ocean.main()


def get_util(util_dict):
    util_dict['output'] = server_util.main()


def get_admin_data(request):
    output_dict = {}

    # Pass charts data to the home admin page
    if request.META['PATH_INFO'] == '/admin/':

        # Set flag
        output_dict['is_admin_home'] = True

        # Define threads
        util_dict = dict()
        util_thread = threading.Thread(target=get_util, args=(util_dict,))

        analytics_dict = dict()
        ga_thread = threading.Thread(target=get_ga, args=(analytics_dict,))

        docn_dict = dict()
        docn_thread = threading.Thread(target=get_docn, args=(docn_dict,))

        # Start threads
        util_thread.start()
        ga_thread.start()
        docn_thread.start()

        try:
            # Join threads
            util_thread.join()
            ga_thread.join()
            docn_thread.join()

            # Merge the dictionaries of output dictionary and analytics dictionary
            output_dict = {**output_dict, **analytics_dict['output']}

            # Merge the dictionaries of output dictionary and DOCN dictionary
            output_dict = {**output_dict, **docn_dict['output']}

        except Exception:
            print(traceback.format_exc())

        # Merge the dictionaries of output dictionary and utilization dictionary
        if 'output' not in util_dict:  # If running in testing env
            util_dict['output'] = {
                'util_timestamps_labels': [],
                'cpu_percent_data': [],
                'ram_percent_data': [],
                'avg_cpu': 0,
                'max_cpu': 0,
                'max_cpu_time': None,
                'avg_ram': 0,
                'max_ram': 0,
                'max_ram_time': None,
                'storage_percentage': None,
                'used_storage_gb': 0,
            }
        output_dict = {**output_dict, **util_dict['output']}

    else:

        output_dict['is_admin_home'] = False

    # Convert integers and float values to string
    keys_to_str(input_dict=output_dict)

    return output_dict
