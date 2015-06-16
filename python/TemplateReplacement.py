import string

def perform_template_replacement (file_location, variable_map):
    file = open(file_location, "r")
    data = file.read()
    template = string.Template(data)
    print template.substitute(variable_map)

