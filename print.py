# Parse arguments

import argparse
NLAYER_DISPLAY = 5
parser = argparse.ArgumentParser()
parser.add_argument("--verbose",
                    action="store_true",
                    help="Print all.")
parser.add_argument("-n",
                    dest="nlayer_display",
                    type=int,
                    default=NLAYER_DISPLAY,
                    help="Number of layers to be printed.")
args = parser.parse_args()


# Load required modules

print("Loading the required Python modules ...")
from keras.models import load_model


# Load model

print("\nLoading the model ...")
model_path = 'models/model.06-2.5489.hdf5'
model = load_model(model_path)


# Print model summary

class PrintFn():

    def __init__(self, verbose=False, nlayer_display=NLAYER_DISPLAY):
        self.nlayer = 0             # Number of layers
        self.nlayer_display = nlayer_display  # Number of layers to be displayed
        self.layer_start = False    # Index of the first layer starts
        self.layer_end = False      # Index of the last layer ends
        self.outer_border = "===="  # Keras use it to demarcate header from actual layer
        self.inner_border = "____"  # Keras use it to demarcate layers
        self.verbose = verbose
        self.summary = []           # All lines from Keras model.summary()
        self.layer_index = []       # Indexes of all layers


    def __mark_layer(self):
        self.nlayer += 1
        self.layer_index.append(len(self.summary)-1)


    def __call__(self, line):
        self.summary.append(line)

        if not self.layer_start:  # Header section
            if line.startswith(self.outer_border):
                self.layer_start = len(self.summary) - 1
                self.__mark_layer()

        elif not self.layer_end:  # Layers section
            if line.startswith(self.inner_border):
                self.__mark_layer()                

            if line.startswith(self.outer_border):  # Summary section
                self.layer_end = len(self.summary) - 1

        # Actual printing is carried out when the last line is feeded
        elif line.startswith(self.inner_border):  # Last line
            # Add number of layers to summary
            self.summary.insert(-1, "Different layers: {}".format(self.nlayer))

            # If not verbose or model.summary() is short, print all
            if self.verbose or self.nlayer < (self.nlayer_display * 2 + 3):
                print("\n".join(self.summary))
            else:  # print just the head and tail nlayer_display of model.summary()
                head = self.layer_index[self.nlayer_display] + 1
                tail = self.layer_index[self.nlayer - self.nlayer_display]

                print("\n".join(self.summary[ : head]))
                print("\n    ...\n" * 2)
                print("\n".join(self.summary[tail : ]))


model.summary(print_fn=PrintFn(verbose=args.verbose, nlayer_display=args.nlayer_display))
