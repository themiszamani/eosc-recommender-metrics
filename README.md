# eosc-recommender-metrics
A framework for counting the recommender metrics

# Preprocessor v.1.0
<p align="center">
<a href="https://github.com/nikosT/Gisola">
<img src="https://github.com/nikosT/eosc-recommender-metrics/blob/master/docs/Preprocessor.png" width="70%"/>
</a>
</p>

# RS metrics v.1.0
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

## Utilities

### Get service catalog script (./get_service_catalog.py)

This script contacts EOSC Marketplace catalog and generates a csv with a list of all available services, their name, id and url

To execute the script issue:
```
chmod u+x ./get_service_catalog.py
./get_service_catalog.py
```

_Tested with python 3.9_