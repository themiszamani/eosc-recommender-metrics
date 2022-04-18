# eosc-recommender-metrics
A framework for counting the recommender metrics

# Preprocessor v.0.2
<p align="center">
<a href="https://github.com/nikosT/Gisola">
<img src="https://github.com/nikosT/eosc-recommender-metrics/blob/master/docs/Preprocessor.png" width="70%"/>
</a>
</p>

# RS metrics v.0.2
<p align="center">
<a href="https://github.com/nikosT/Gisola">
<img src="https://github.com/nikosT/eosc-recommender-metrics/blob/master/docs/RSmetrics.png" width="70%"/>
</a>
</p>




# Dependencies
1. Install Conda from here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html. Tested on conda v 4.10.3.
2. Run from terminal: `conda env create -f rsmetrics_env.yml`
3. Run from terminal: `conda activate rsmetrics`
4. Run from terminal: `chmod +x ./preprocessor.py ./rsmetrics.py`

# Usage
7. Run from terminal: `./preprocessor.py` in order to prepare the data for the RSmetrics
8. Run from terminal: `./rsmetrics.py` to run RSmetrics


## Reporting

The reporting script generates an evalutation report in html format automatically served from a spawed localserver (default: http://localhost:8080)
and automatically opens the default browser to present the report. 

To execute the script issue:
```
chmod u+X ./report.py
report.py
```
The script will automatically look for evaulation result files in the default folder `./data` and will output the report in the default folder: `./report`

#### Additional script usage with parameters

The `report.py` script can be used with the `--input` parameter: a path to a folder that the results from the evaluation process have been generated (default folder:`./data`). The report script can also take an `--output` parameter: a path to an output folder where the generated report will be served automatically.

_Note:_ the script copies to the output folder all the necessary files such as `pre_metrics.json`, `metrics.json` as well as `report.html.prototype` renamed to `index.html` 

```
usage: report.py [-h] [-i STRING] [-o STRING] [-a STRING] [-p STRING]

Generate report

optional arguments:
  -h, --help            show this help message and exit
  -i STRING, --input STRING
                        Input folder
  -o STRING, --output STRING
                        Output report folder
  -a STRING, --address STRING
                        Address to bind and serve the report
  -p STRING, --port STRING
                        Port to bind and serve the report
```

## Utilities

### Get service catalog script (./get_service_catalog.py)

This script contacts EOSC Marketplace catalog and generates a csv with a list of all available services, their name, id and url

To execute the script issue:
```
chmod u+x ./get_service_catalog.py
./get_service_catalog.py
```

_Tested with python 3.9_
