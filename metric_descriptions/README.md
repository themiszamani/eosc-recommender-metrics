# Metric Descriptions folder

This folder is meant to contained detailed yaml files defining in structure the implementation details of each metric
To add a new detailed description in this folder please consult the first file added here: diversity.yml and structure
the information accordingly

### Important Note on filenames
The filename should correspond to the name of the metric used in `metrics.json` output and the extension `.yml` 
So for the metric Shannon Diversity the short name used in `metrics.json` is `diversity` thus the filename is `diversity.yml`

### Multiline values
In yaml fields that you need to support multiline string content please use the `>` operator  
