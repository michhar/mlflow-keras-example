
import pandas as pd

from mlflow.pyfunc import load_pyfunc
from mlflow.utils import get_jsonable_obj
import keras


def init():
    global model
    import keras
    model = load_pyfunc("model")


def run(s):
    import keras
    input_df = pd.read_json(s, orient="records")
    return get_jsonable_obj(model.predict(input_df))

