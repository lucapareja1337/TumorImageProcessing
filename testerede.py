
from fastai.vision.all import *

imported_learner = load_learner(Path("export.pkl"))

print(imported_learner.predict(Path("brain_tumor_dataset/no/10 no.jpg")))