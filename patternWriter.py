import time


def format_time(timestamp):
    return time.strftime("%b %d %H:%M", time.localtime(timestamp))


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


def case_study3_and_case_study4(json_data, flag, reverse=False):
    contents = json_data.get('contents', [])
    result = []
    for item in contents:
        if flag == '-l' and item['name'].startswith('.'):
            continue
        dt = f"{item['permissions']} {item['size']} {format_time(item['time_modified'])} {item['name']}"
        result.append(dt)
    if reverse:
        for res in result[::-1]:
            print(res)
    else:
        for res in result:
            print(res)
