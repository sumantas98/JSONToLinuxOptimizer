import patternWriter


def router(raw_data, *args):
    argument_count = len(args)
    if argument_count == 0:
        pass
    elif argument_count == 1:
        key_1 = args[0]
        if key_1 == 'tree':
            patternWriter.convert_To_directory(raw_data)
    elif argument_count == 2:
        pass
    else:
        pass
