#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    head = None

    for ticket in tickets:
        if ticket.source == "NONE":
            head = ticket.destination

        hash_table_insert(hashtable, str(ticket.source), str(ticket.destination))

    for i in range(len(tickets)):
        route[i] = head
        head = hash_table_retrieve(hashtable, head)

    return route[:-1]

