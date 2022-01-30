import ast

def get_value(object,k):
    for key, value in object.items():
        if type(value) is dict:
            get_value(value,k)
            if key == k[-1]:
                print (value)
        else:
            if key == k[-1]:
                print (value)

nested_dictionary = {"a":{"b":{"c":"d"}}}
#nested_dictionary = input("Enter object: ")
#nested_dictionary = ast.literal_eval(nested_dictionary)
key = "a/b"
#key = input("Enter Key: a")
key = key.split('/')
get_value(nested_dictionary,key)