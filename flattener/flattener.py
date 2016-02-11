class Flattener:

    def __init__(self):
        pass

    @staticmethod
    def flatten(the_list):
        """
        Returns a flattened list of integers from an list of integers or nested list of integers
        :param the_list: A list of integers or nested list of integers
        :return: A list of integers
        """

        flat_list = []

        if the_list is None:
            return None

        if not isinstance(the_list, list):
            raise TypeError("Input is expected to be a list")

        for item in the_list:
            if isinstance(item, int):
                flat_list.append(item)
            elif isinstance(item, list):
                flat_list += Flattener.flatten(item)
            else:
                raise TypeError("All items in the input should be integers or nested lists of integers")

        return flat_list
