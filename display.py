print("Loading required Python modules ...")

from keras.utils import plot_model
import subprocess
from utils import get_predict_api


print("\nLoading model ...")

graph_file = "cache/model_graph.png"
_, model = get_predict_api()
plot_model(model, to_file=graph_file)


subprocess.Popen(
    "xdg-open " + graph_file,
    shell=True,
    stderr=subprocess.PIPE)
