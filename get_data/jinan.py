import numpy as np
import pandas as pd
import eikon as ek

def eikon_init():
    app_key = pd.read_csv('get_data/app_key.csv')
    ek.set_app_key(app_key['app_key'][0])

eikon_init()


