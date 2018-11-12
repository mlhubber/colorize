print("Loading required Python modules ...")
from keras.utils import plot_model
from keras.models import load_model
import subprocess
from utils import MODEL_FILE

print("\nLoading model ...")
graph_file = "cache/model_graph.png"
model = load_model(MODEL_FILE)
plot_model(model, to_file=graph_file)


subprocess.Popen(
    "xdg-open " + graph_file,
    shell=True,
    stderr=subprocess.PIPE)
