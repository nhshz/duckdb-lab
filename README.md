# Pandas and Python

This is to aid in a talk and live-demo around Python/Pandas/data analysis, assuming no prior knowledge.

## Setup

### Prerequisites

- Requires Python 3.9 to be installed. You can check which version you have by running `python --version`.
  - [pyenv](https://github.com/pyenv/pyenv) can be used for Python version management.
- Also required [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today), used for python package management

### Virtual environment

- We will use a python virtual environment to create a self contained collection
of the dependencies needed for this workshop.

To create a virtual environment, install dependencies, and activate it, run:

```sh
./tasks devenv
pipenv shell
```

The following Python packages will be installed:

- [Pandas](https://pandas.pydata.org/docs/) - the main focus of this workshop.
- [Boto3](https://pypi.org/project/boto3/) - provides us with interface to Amazon
  Web Services. We will be using this to fetch datasets from S3.
- [PyArrow](https://pypi.org/project/pyarrow/) - used to read parquet files.
- [JupyterLab](https://jupyter.org/install) - used to start the Jupyter server.
- [Matplotlib](https://pypi.org/project/matplotlib/) - used to create data visualisations in Python

To deactivate the virtual environment:
```sh
(venv)$ deactivate
```

To remove the virtual environment and clear cache, run:
```sh
pipenv --rm && pipenv --clear
```

## Downloading datasets

We will be using the Amazon review dataset to explore the capabilities of Pandas.

Unless you have a very fast internet connection, you will probably want to only
download a subset of this data. This can be accomplished using the
`dataset-download` command, which is available once inside the projects
virtual environment.

Using the [table of product categories](product_categories.md), select a
product category and run the downloader. For example, to download reviews of
only digital videos, run:

```sh
dataset-download path/to/download --product-category Digital_Video_Download
```

However, if you wish to download the full 50GB dataset, simply omit a product
category.

```sh
dataset-download path/to/download
```

## Jupyter and Pandas

To start the Jupyter server, run:

```sh
jupyter-lab
```

## Demo

In order to run the demo notebook, or to play around with pandas, do the following steps:

1. Ensure you have Python 3.9 installed, and activate your virtual environment by following the [Setup steps](#setup)
2. The demo notebook uses Digital_Video_Download data (by running `dataset-download data/review_data --product-category Digital_Video_Download`)
3. Start the Jupyter server by running `jupyter-lab`
4. Open up the `notebooks/demo.pynb` file in the web browser, and you can start to do your own analysis
  - Or have a look at [`demo-completed.ipynb`](./notebooks/demo-completed.ipynb) which is the completed analysis done as part of the live demo.
  - There is also [`other-insights.ipynb`](./notebooks/other-insights.ipynb) which is further analysis done on the dataset.

### Credits

Thanks to @jfgreen-nhs and @RKJa for contributions to the live demo material.