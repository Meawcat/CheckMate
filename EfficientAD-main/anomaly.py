# Import the datamodule
from anomalib.data import Folder
from anomalib.data.utils import TestSplitMode

# Import the required modules
from anomalib.models import Patchcore
from anomalib.engine import Engine
HF_HUB_DISABLE_SYMLINKS_WARNING=1

# Create the datamodule
datamodule = Folder(
    name="erazer",
    root="EfficientAD-main/datasets/erazer",
    normal_dir="good",
    test_split_mode=TestSplitMode.SYNTHETIC,
    task="classification",
)

# Setup the datamodule
datamodule.setup()

# Import the model and engine
from anomalib.models import Patchcore
from anomalib.engine import Engine

# Create the model and engine
model = Patchcore()
engine = Engine(task="classification")

# Train a Patchcore model on the given datamodule
engine.train(datamodule=datamodule, model=model)