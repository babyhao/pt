import yaml

def get_yaml_data(filename):
    with open('../data/' + filename + '.yml', 'r') as f:
        return yaml.load(stream=f)


# if __name__ == '__main__':
#     data = get_yaml_data('search_data')
#     print(type(data))
#     print(data)