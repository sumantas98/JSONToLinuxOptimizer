import time
import sys


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


def case_study3_and_case_study4_case_study5_case_study6(json_data, flag, reverse=False, sort_t=False, filter_s=''):
    contents = json_data.get('contents', [])
    # Case Study 5 Start
    if sort_t:
        contents = sorted(contents, key=lambda x: x['time_modified'], reverse=False)
    # Case Study 5 end
    result = []
    for item in contents:
        if flag == '-l' and item['name'].startswith('.'):
            continue

        if filter_s == 'dir':
            if "." not in item['name'] and "LICENSE" not in item['name']:
                dt = f"{item['permissions']} {item['size']} {format_time(item['time_modified'])} {item['name']}"
                result.append(dt)
        elif filter_s == 'file':
            if "." in item['name'] or "LICENSE" in item['name']:
                dt = f"{item['permissions']} {item['size']} {format_time(item['time_modified'])} {item['name']}"
                result.append(dt)

        elif filter_s == 'folder':
            print(f"error: 'folder' is not a valid filter criteria. Available filters are 'dir' and 'file'")
            sys.exit(1)

        else:
            dt = f"{item['permissions']} {item['size']} {format_time(item['time_modified'])} {item['name']}"
            result.append(dt)
    # Case Study 4 Start
    if reverse:
        return result[::-1]
    else:
        return result
