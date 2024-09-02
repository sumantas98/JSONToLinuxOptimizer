def convert_To_directory(json_data, ind=''):
    print(f"{ind}{json_data['name']}")
    if 'contents' in json_data:
        for content in json_data['contents']:
            convert_To_directory(content, ind=ind + '    |-- ')