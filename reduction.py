from csv import reader, writer
from os.path import splitext
from sys import argv

path_in = argv[1]
path_out = argv[2] if len(argv) > 2 else '%s_out%s' % splitext(path)

indexes = None

metric_dict = {}
errors = 0

with open(path_in) as file_in:
    csv_reader = reader(file_in)
    with open(path_out, 'wb') as file_out:
        csv_writer = writer(file_out)
        fieldnames = csv_reader.next()
        csv_writer.writerow([]) # headers
        indexes = {f[1]: f[0] for f in enumerate(fieldnames)}

        for r, row in enumerate(csv_reader):
            print row 
            try :
                concatenated_metrics = # 
                if concatenated_metrics in metric_dict:
                    metric_dict[concatenated_metrics]['metric'] = int(metric_dict[concatenated_metrics]['metric']) + int(row[indexes['metric']])
                else:
                    metric_dict[concatenated_metrics] = {
                        "metric": row[indexes["metric"]],
                    }
            except: 
                errors = errors + 1

        rows = []

        for row in metric_dict:
            rows.append([metric_dict[row]["metric"]])
        rows.sort(key=lambda x: int(x[1]))

        for row in rows:
            csv_writer.writerow(row)

        print metric_dict
