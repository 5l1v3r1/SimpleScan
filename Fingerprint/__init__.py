from Fingerprint.scanner import scanner
from Fingerprint.servicetoDB import store_servicedetail


def get_fingerprint(port_list, task_id):
    report_file = scanner(port_list, task_id)
    result = store_servicedetail(port_list, task_id, report_file)
    return result
