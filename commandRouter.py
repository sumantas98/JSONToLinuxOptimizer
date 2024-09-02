import patternWriter


def router(raw_data, *args):
    argument_count = len(args)
    # print(args)
    if argument_count == 0:
        patternWriter.case_study1_and_case_study2(raw_data)
    elif argument_count == 1:
        key_1 = args[0]
        if key_1 == 'tree':
            patternWriter.convert_To_directory(raw_data)
        elif key_1 == '-A':
            patternWriter.case_study1_and_case_study2(raw_data, 'Y')
    elif argument_count == 2:
        pass
    else:
        pass
