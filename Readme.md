#configReaders
configReaders is a small helper library that reads .cfg, .ini or .json files that contain api keys and passwords.
I found that I was recreating the same functions to perform these takes in multiple scripts and decided to use this as a learning moment to dive into packages.

##configReaders
This is the package that contains readers.py.

##readers.py
There are methods: read_config and read_json.

###read_config(file_path)
The read_config method takes in a path to an .cfg or .ini file.
The .cfg or .ini sould be formatted into sections with your api keys and passwords.
How you segregate your keys and passwords is up to you, it is your .cfg or .ini after all.

-- usage example:
config_path = "file_name.cfg"
myKeys = read_config(config_path)

for key, value in myKeys['api_keys'].items():
    print(key + ': ' + value)

print(myKeys['api_keys']['my_key'])

###read_json(file_path)
The read_json method takes in a path to a .json file.
The .json file should be formatted into a dictionary of key/value sets.

-- usage example:
json_path = "file_name.json"
DB = read_json(json_path)
print(DB['KEYS']['api_key'])


-- config (.cfg) example:
    [keys]
    api_key1 = key_string1
    api_key2 = key_string2
    exit_keys = q, Q, exit, EXIT, quit, QUIT
    
    [passwords]
    api_pword1 = pass_string1
    api_pword2 = pass_string2

-- json (.json) example:
{
    'api1':{
        'api_key': 'key_string',
        'api_pass': 'pass_string',
    }
    'api2':{
        'api_key': 'key_string',
        'api_pass': 'pass_string',
    }
}