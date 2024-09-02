def convert_To_directory(json_data, ind=''):
    print(f"{ind}{json_data['name']}")
    if 'contents' in json_data:
        for content in json_data['contents']:
            convert_To_directory(content, ind=ind + '    |-- ')


def case_study1_and_case_study2(json_data, flag='N'):
    contents = json_data.get('contents', [])
    # print(contents)
    for item in contents:
        # print(item)
        # print("Gap \n")
        if flag == 'N' and item['name'].startswith('.'):
            continue
        print(item['name'], end=' ')
