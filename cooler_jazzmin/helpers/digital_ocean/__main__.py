import os
import yaml
import traceback
from .packages.file import file
from .packages.logger import logger
from .packages.digitalOcean import digitalOcean
import threading

# Initiate logger
log = logger.get(app_name='digital-ocean', enable_logs_file=False)


def get_balance(docn, output_dict):
    # Get the balance info of the account and add the results dictionary to
    # the output dictionary
    balance_results_dict = docn.get_balance()
    output_dict['balance'] = balance_results_dict


def get_last_invoice(docn, output_dict):
    # Get last invoice
    invoice_results_dict = docn.get_last_invoice()
    output_dict['last_invoice'] = invoice_results_dict


def get_last_payment(docn, output_dict):
    # Get last payment
    payment_results_dict = docn.get_last_payment()
    output_dict['last_payment'] = payment_results_dict


def get_droplet_specs(docn, output_dict, config):
    # Get droplet specs
    droplet_results_dict = docn.get_droplet_specs(
        droplet_name=config['digitalOcean']['droplet_name']
    )
    output_dict['droplet_specs'] = droplet_results_dict


def main():
    log.info('Start program execution')

    project_abs_path = file.caller_dir_path()

    # Import configurations
    config_path = os.path.join(project_abs_path, 'config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)
    config['digitalOcean']['bearer_token'] = os.getenv("DIGITAL_OCEAN_TOKEN")

    # Initiate an empty dictionary that will be returned from this program
    output_dict = dict()

    # Create an instance of DigitalOcean
    docn = digitalOcean.DigitalOcean(
        bearer_token=config['digitalOcean']['bearer_token']
    )

    # Define threads
    balance_thread = threading.Thread(
        target=get_balance,
        args=(docn, output_dict)
    )
    last_invoice_thread = threading.Thread(
        target=get_last_invoice,
        args=(docn, output_dict)
    )
    last_payment_thread = threading.Thread(
        target=get_last_payment,
        args=(docn, output_dict)
    )
    droplet_specs_thread = threading.Thread(
        target=get_droplet_specs,
        args=(docn, output_dict, config)
    )

    # Start threads
    balance_thread.start()
    last_invoice_thread.start()
    last_payment_thread.start()
    droplet_specs_thread.start()

    # Join threads
    balance_thread.join()
    last_invoice_thread.join()
    last_payment_thread.join()
    droplet_specs_thread.join()

    log.info('Finished program execution')

    # Return the output dictionary
    print("Digital ocean script dict out: {}".format(output_dict))
    return output_dict


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.error(e)
        log.error('Error Traceback: \n {0}'.format(traceback.format_exc()))
