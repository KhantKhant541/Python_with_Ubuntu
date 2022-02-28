import pickle


def write_data(obj, file):
    with open(f"{file}.dat", "ab") as f:
        pickle.dump(obj, f)


def read_data(file):
    data = []

    try:
        with open(f"{file}.dat", "rb") as f:
            data.append(pickle.load(f))
    except EOFError:
        pass

    return data


def check_data(file):
    with open(f"{file}.dat", "rb")as f:
        try:
            while True:
                obj = pickle.load(f)
                obj.display()

        except EOFError:
            print("Nothing Found!")
