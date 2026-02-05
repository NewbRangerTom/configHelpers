import configparser
import json

# use this for .cfg or .ini files
def read_config(file_path):
    """
    Read from .cfg file

    Parameters
    ----------
    file_path (str) : the path to the config file

    Returns
    -------
    see configparser docstring
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    return config




def read_json(file_path):
    """
    Reads .json files

    Parameters
    ----------
    file_path (str) : the path to the json file

    Returns
    --------
    f (dict) : dictionary

    """
    with open(file_path, 'r') as f:
        return json.load(f)
