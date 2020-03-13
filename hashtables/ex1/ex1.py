#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, len(weights)):
        if hash_table_retrieve(ht, limit - weights[i]) != None:
            return (i, hash_table_retrieve(ht, limit - weights[i]))
        hash_table_insert(ht, int(weights[i]), i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

