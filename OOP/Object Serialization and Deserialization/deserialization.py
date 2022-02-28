import pickle
from writing_an_object_to_file import Person

with open("serialization.dat", "rb") as f:
    print(pickle.load(f))
