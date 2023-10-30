# 4. The build_xml_element function receives the following parameters: tag, content,
# and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def ex_4(tag, content, **key_value_args):
    string_key_values = ''
    for key, value in key_value_args.items():
        string_key_values += f' {key}="{value}"'

        xml_format = f"<{tag}{string_key_values}>{content}</{tag}>"
    return xml_format

print("EXERCICE 4")
print('The call: ex_4("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns: ')
print(ex_4("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

