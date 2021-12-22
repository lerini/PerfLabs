import json
from pprint import pprint

report_1 = None  # tests
report_2 = None  # values
report = {}  # result

with open('tests.json') as tests_file:
    loaded_tests_file = json.load(tests_file)
with open('values.json') as values_file:
    loaded_values_file = json.load(values_file)

for key, value in loaded_tests_file.items():
    report_1 = value

for key, value in loaded_values_file.items():
    report_2 = value


def combine(some_list):
    for i in range(len(some_list)):
        for j in range(len(report_2)):
            if (some_list[i])['id'] == (report_2[j])['id']:
                (some_list[i])['value'] = (report_2[j])['value']
        if "values" in some_list[i]:
            combine(some_list[i]['values'])


combine(report_1)
report['report'] = report_1
pprint(report)
with open('report.json', 'w') as outfile:
    json.dump(report, outfile)
