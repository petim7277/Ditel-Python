def my_reverse_function(tuple_list:tuple):
    """
          This function reverses elements in a tuple
    e.g (10, 20, 30, 40, 50) when reversed will be
    reversed as (50, 40, 30, 20, 10)
    A tuple has indices that tell the position of an element
    Within a list and every element in a tuple has an index
    the tuple list shown above has an index of 0
    """
    new_tuple = list(tuple_list)
    reverse = ()
    for i in range(len(new_tuple) - 1, -1, -1):
        reverse += new_tuple[i],
    return reverse