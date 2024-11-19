def save_to_file(filename, shape):
    with open(filename, 'w') as f:
        for line in shape.get_2d_representation():
            f.write(line + "\n")