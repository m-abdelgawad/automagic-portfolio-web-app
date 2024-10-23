import os
import yaml
import traceback
from .packages.file import file
from .packages.logger import logger
from .packages.postgredb import postgredb
from .packages.datetimetools import datetimetools


# Initiate logger
log = logger.get(app_name='logs', enable_logs_file=False)


def main():

    log.info('Start program execution')

    project_abs_path = file.caller_dir_path()

    # Import configurations
    config_path = os.path.join(project_abs_path, 'config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    # Read the query
    query = file.read(
        path=os.path.join(
            project_abs_path, config['query']['path']
        )
    )

    # Initialize the output dictionary
    output_dict = {
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
    }

    # Create a database instance
    db = postgredb.PostgreSQLDB(
        host = os.getenv('DB_HOSTNAME'),
        db_name = os.getenv('DB_NAME'),
        username = os.getenv('DB_USERNAME'),
        password = os.getenv('DB_PASSWORD')
    )

    # Execute the query
    db.run_query(query=query)

    # Fetch the results
    results = db.fetch_results()

    if len(results) > 0:
        for row in results:
            print(row)
            row_timestamp = row['timestamp']
            output_dict['util_timestamps_labels'].append(row_timestamp)

            row_cpu = row['cpu_percentage']
            if row_cpu >= output_dict['max_cpu']:
                output_dict['max_cpu'] = row_cpu
                output_dict['max_cpu_time'] = row_timestamp

            row_ram = row['ram_percentage']
            if row_ram >= output_dict['max_ram']:
                output_dict['max_ram'] = row_ram
                output_dict['max_ram_time'] = row_timestamp

            output_dict['cpu_percent_data'].append(row_cpu)
            output_dict['ram_percent_data'].append(row_ram)

            output_dict['storage_percentage'] = row['storage_usage_percent']
            output_dict['used_storage_gb'] = row['used_storage_gb']
            output_dict['free_storage_gb'] = row['free_storage_gb']
    else:
        output_dict['max_ram'] = None
        output_dict['max_ram_time'] = None
        output_dict['storage_percentage'] = None
        output_dict['used_storage_gb'] = None
        output_dict['free_storage_gb'] = None

    # Reformat max CPU and RAM timestamps
    if output_dict['max_cpu_time']:
        output_dict['max_cpu_time'] = datetimetools.format_str_date(
            input_date=output_dict['max_cpu_time'],
            current_format='%Y-%m-%d %H:%M:%S',
            target_format='%d %b %Y %H:%M'
        )
    else:
        output_dict['max_cpu_time'] = None

    if output_dict['max_ram_time']:
        output_dict['max_ram_time'] = datetimetools.format_str_date(
            input_date=output_dict['max_ram_time'],
            current_format='%Y-%m-%d %H:%M:%S',
            target_format='%d %b %Y %H:%M'
        )
    else:
        output_dict['max_ram_time'] = None

    # Average CPU
    if output_dict['cpu_percent_data'] and output_dict['cpu_percent_data']:
        output_dict['avg_cpu'] = \
            sum(output_dict['cpu_percent_data']) / len(output_dict['cpu_percent_data'])
        output_dict['avg_cpu'] = round(output_dict['avg_cpu'], 2)
    else:
        output_dict['cpu_percent_data'] = None
        output_dict['cpu_percent_data'] = None

    # Average RAM
    if output_dict['ram_percent_data'] and output_dict['ram_percent_data']:
        output_dict['avg_ram'] = \
            sum(output_dict['ram_percent_data']) / len(
                output_dict['ram_percent_data'])
    else:
        output_dict['ram_percent_data'] = None
        output_dict['ram_percent_data'] = None

    if output_dict['avg_ram']:
        output_dict['avg_ram'] = round(output_dict['avg_ram'], 2)
    else:
        output_dict['avg_ram'] = None

    log.info('Finished program execution')

    return output_dict


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.error(e)
        log.error('Error Traceback: \n {0}'.format(traceback.format_exc()))
