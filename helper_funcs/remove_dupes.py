def remove_dupes(main_list, list_to_dedupe):
    """
    Removes duplicaate times from the list_to_dedupe. Doesn't change main_list.

    :param main_list: A list of tuples.
    :param list_to_dedupe: A list of tuples.
    :return: The deduplicated list_to_dedupe.
    """
    main_list_times = [y for x, y in main_list]
    new_list = [(x, y) for x, y in list_to_dedupe if y not in main_list_times]
    return new_list
