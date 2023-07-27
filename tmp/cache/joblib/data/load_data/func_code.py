# first line: 127
@MEMORY.cache
def load_data(key):
    """
    Load the data for the given key.
    :param key: The name of the dataset.
    :return: A dictionary with the following keys:
        - name: the name of the dataset
        - train: a tuple of (text, labels)
        - test: a tuple of (text, labels)
        - label_dict: a dictionary mapping labels to integers
    """
    dataset = {"name": key}
    print(key)
    if key == 'MR':
        load_MR(dataset)
    elif key == 'R8':
        load_R8(dataset)
    elif key == 'SearchSnippets':
        load_SearchSnippets(dataset)
    elif key == 'Twitter':
        load_Twitter(dataset)
    elif key == 'TREC':
        load_TREC(dataset)
    elif key == 'SST2':
        load_SST2(dataset)
    elif key == 'NICE':
        load_NICE(dataset)
    elif key == 'NICE2':
        load_NICE2(dataset)
    elif key == 'STOPS':
        load_STOPS(dataset)
    elif key == 'STOPS2':
        load_STOPS2(dataset)
    else:
        raise ValueError(f"Unknown dataset: {key}")

    return dataset
