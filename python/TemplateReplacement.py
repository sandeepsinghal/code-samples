import string

def perform_template_replacement (file_location, variable_map):

    # Read from the file
    file = open(file_location, "r+")
    file_data = file.read()

    # Get the template object and do replacement
    template_obj = string.Template(file_data)
    replaced_data = template_obj.substitute(variable_map)

    # Write the replaced text into the file
    file.seek(0)
    file.write(replaced_data)
    file.truncate()
    file.close()

    return replaced_data


