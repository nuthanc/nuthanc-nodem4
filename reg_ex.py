import re
import json


with open('docs/ConfigurationApi.md', 'r') as f:
    config_file = f.read()


# Can be made more efficient by mmap or opening file only once
def get_config_code(method_name, entire=False):
    pattern = r"(# \*\*" + method_name + "\*\*[\w\W]+?python)(([\w\W]+?)(try:[\w\W]+?" + method_name + ": %s.*?e.))"
    api_code = re.search(pattern, config_file, re.M)
    # print(api_code.group())
    if entire is True:
        return api_code.group(2)
    else:
        return api_code.group(3)


def camel_to_snake(text):
    snake = re.sub('(.+?)([A-Z])', r'\1_\2', text).lower()
    return snake


# Get schema file from .py file
def get_schema_class_name(string):
    schema_class = re.search("\.(\w+)Schema\(\)", string, re.M)
    if schema_class is not None:
        return schema_class.group(1)


# Get schema files in dictString
def extract_schema_classes_from_dict_string(string):
    return re.findall("(\w+Schema\w*)", string, re.M)


# Get all types from .py file
def get_dict_string_from_models_file(file_name):
    with open('swagger_client/models/' + file_name, 'r') as f:
        schema_file = f.read()
        cont = re.search("swagger_types = ({[\n\s\'\w:,\[\]]+?})", schema_file).group(1)
        return cont
        # For Conversion from string to dictionary
        # schema_dict = eval(cont)


def remove_literal_list(string):
    list_pattern = r"'list\[(.*?)\]'"
    return re.sub(list_pattern, r"['\1']", string)


def first_lower(match):
    return match.group(1).lower() + match.group(2)


# Used to get either dictionary or string of schema type
def schema_dict_string_from_method(method_name):
    schemas_gen = get_config_code(method_name)
    schemas = get_schema_class_name(schemas_gen)
    if schemas is not None:
        schema_class_snake = camel_to_snake(schemas)
        schema_class_file = schema_class_snake + "_schema.py"
        cont = get_dict_string_from_models_file(schema_class_file)
        cont = remove_literal_list(cont)
        return cont
    else:
        print("There is no Schema defined for this method")



def build_final_schema(dict_string):
    regex = r"(\w+Schema\w*)"
    schema_class = re.search(regex,dict_string,re.M)
    if schema_class is not None:
        schema_class = schema_class.group(1)
    # print("Dict string before:",dict_string)
    # print(schema_class)

    # Base condition
    if schema_class is None:
        return dict_string

    else:
        schema_class_snake = camel_to_snake(schema_class)
        if 'iagent' in schema_class_snake:
            schema_class_snake = re.sub('iagent','i_agent',schema_class_snake)
        schema_class_file = schema_class_snake + ".py"
        value = get_dict_string_from_models_file(schema_class_file)
        value = remove_literal_list(value)
        # print(value)
        # print("schema_class",schema_class)
        value = value.replace('_','-')
        dict_string = dict_string.replace("'"+schema_class+"'",value)
        # print("Dict string after:",dict_string)
        dict_string = build_final_schema(dict_string)
        return dict_string


# Starting function
def main(method_name):
    main_schema_dict_string = schema_dict_string_from_method(method_name)
    if main_schema_dict_string is not None:
        final_dict_string = build_final_schema(main_schema_dict_string)

        final_dict_string = final_dict_string.replace('ERRORUNKNOWN','')
        print("Final nested dictionary")
        # print(final_dict_string)
        final_dict = eval(final_dict_string)
        with open('get_info_for_api.json','w') as outfile:
            json.dump(final_dict, outfile, sort_keys=True, indent=4)


method_name = 'create_iceberg_device_device_by_id'
robot_method_name = 'create_device'

main(method_name)
