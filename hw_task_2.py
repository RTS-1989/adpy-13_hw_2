import hashlib

def get_hash_md5(file_string) -> hex:
    hash_object = hashlib.md5(file_string.encode())
    return hash_object.hexdigest()

def get_strings(file_path, start, end):

    string_list = []
    
    with open(file_path, 'r', encoding='utf8') as fi:
        for line in fi.readlines():
            string_list.append(line)

    return string_list

def string_hash_generator(start, end, file_path):

    try:
        while start <= end:
            strings_list = get_strings(file_path, start, end)
            yield get_hash_md5(strings_list[start])
            start += 1
    except:
        print('Index is out of range')        

end = len((get_strings('some_text.txt', 0, -1)))-1

for item in string_hash_generator(0, end, 'some_text.txt'):
    print(item)
