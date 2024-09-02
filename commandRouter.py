import patternWriter


def router(raw_data, *args):
    argument_count = len(args)
    print(args)
    if argument_count == 0:
        patternWriter.case_study1_and_case_study2(raw_data)
    elif argument_count == 1:
        key_1 = args[0]
        if key_1 == 'tree':
            patternWriter.convert_To_directory(raw_data)
        elif key_1 == '-A':
            patternWriter.case_study1_and_case_study2(raw_data, key_1)
        elif key_1 == '-l':
            patternWriter.case_study3_and_case_study4(raw_data, key_1, False)
    elif argument_count == 2:
        key_1, key_2 = args[0], args[1]
        if key_1 == '-l' and key_2 == '-r':
            patternWriter.case_study3_and_case_study4(raw_data, key_1, True)
    else:
        pass
