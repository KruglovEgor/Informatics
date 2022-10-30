import yaml


def start(input_file, output_file):
    with open(input_file, 'r') as f1:
        with open(output_file, 'w') as f2:
            f2.write(str(yaml.load(f1, Loader=yaml.FullLoader)).replace('"', r'\"').replace("'", '"').replace('None', 'null'))

start('Lr4.yaml', 'Lr4_3.json')