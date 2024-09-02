import patternWriter


def router(raw_data, *args):
    argument_count = len(args)
    if argument_count == 0:
        patternWriter.case_study1_and_case_study2(raw_data)
    elif argument_count == 1:
        key_1 = args[0]
        if key_1 == 'tree':
            patternWriter.convert_To_directory(raw_data)
        elif key_1 == '-A':
            patternWriter.case_study1_and_case_study2(raw_data, key_1)
        elif key_1 == '-l':
            res = patternWriter.case_study3_To_case_study9(raw_data, key_1, False)
            for i in res:
                print(i)
    elif argument_count == 2:
        key_1, key_2 = args[0], args[1]

        if key_1 == '-l' and key_2 == '-r':
            res = patternWriter.case_study3_To_case_study9(raw_data, key_1, True)
            for i in res:
                print(i)

        elif key_1 == '-l' and len(key_2) > 1:
            res = patternWriter.case_study3_To_case_study9(raw_data, key_1, True, True, '',
                                                           'B')
            for i in res:
                print(i)

        elif key_1 == '-l' and key_2 != '-r':
            val = search_dir(raw_data, key_2)
            print(val)
            if val is None:
                print(f"error: cannot access '{key_2}': No such file or directory")
            else:
                patternWriter.case_study3_To_case_study9(val, key_1, True)
    elif argument_count == 3:
        key_1, key_2, key_3 = args[0], args[1], args[2]
        if key_1 == '-l' and key_2 == '-r' and key_3 == '-t':
            res = patternWriter.case_study3_To_case_study9(raw_data, key_1, True, True)
            for i in res:
                print(i)
    elif argument_count == 4:
        key_1, key_2, key_3, key_4 = args[0], args[1], args[2], args[3]
        if key_1 == '-l' and key_2 == '-r' and key_3 == '-t':
            res = patternWriter.case_study3_To_case_study9(raw_data, key_1, True, True, key_4)
            for i in res:
                print(i)
    else:
        pass


def search_dir(raw_data, path):
    parts = path.strip("./").split('/')
    current = [raw_data]
    # print(current)
    for part in parts:
        found = None
        for item in current:
            # print(item)
            if item['name'] == part:
                found = item
                break
        if found is None:
            return None
        if 'contents' in found:
            current = found['contents']
        else:
            current = found
            break

    return current
