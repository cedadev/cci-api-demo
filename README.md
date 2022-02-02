# CCI API Demo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cedadev/cci-opensearch-demo/HEAD?labpath=notebooks/index.ipynb)

This repository acts to demonstrate API interactions with the [CCI Open Data Portal](https://climate.esa.int/en/explore/access-climate-data/)

The Opensearch API is provided by CEDA at [https://archive.opensearch.ceda.ac.uk/opensearch/description.xml](https://archive.opensearch.ceda.ac.uk/opensearch/description.xml).

You can run the demo in a Jupyter Notebook using binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cedadev/cci-opensearch-demo/HEAD?labpath=notebooks/index.ipynb)


## Opensearch Clients
[This project](https://github.com/edsu/opensearch) provide an opensearch client. Untested.

## Developing

To develop the notebooks:

1. Create a virtual environment
    ```
    python -m venv venv
    ```
2. Install jupyterlab
    ```
    pip install -r dev_requirements.txt
    ```
3. Start the notebook server
    ```
    jupyter-lab
    ```