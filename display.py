print("Loading required Python modules ...")
from keras.utils import plot_model
from keras.models import load_model
import subprocess

print("\nLoading model ...")
graph_file = "model_graph.png"
model_path = 'models/model.06-2.5489.hdf5'
model = load_model(model_path)
plot_model(model, to_file=graph_file)


subprocess.Popen(
    "xdg-open " + graph_file,
    shell=True,
    stderr=subprocess.PIPE)
