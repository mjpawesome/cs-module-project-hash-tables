class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        # create storage of size "capacity"
        self.storage = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
    
        load_factor = self.size/self.capacity

        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # 64bit FNV prime and offset values
        FNVPrime = 109951162821
        hash_value = 14695981039346656037

        # Key is a string...
        key = key.encode()

        for i in key:         
            hash_value = i * FNVPrime
            # modulo
            hash_value = hash_value % i

        return hash_value

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # get the index
        index = self.hash_index(key)

        # store current node
        cur_node = self.storage[index]

        # look through the list and check for key.
        while cur_node is not None and cur_node.key != key:
            next_node = cur_node
            cur_node = next_node.next

        # if current node is not none, we found the key.  Update its value.
        if cur_node is not None:
            cur_node.value = value

        # otherwise create a new node and insert it at the head.
        else:
            new_node = HashTableEntry(key, value)
            new_node.next = self.storage[index]
            self.storage[index] = new_node
            # increase size
            self.size += 1

        # check load factor
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)
                
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        cur_node = self.storage[index]

        # if we're at the head. 
        if cur_node.key == key:
            # store next value at our current index.
            self.storage[index] = cur_node.next
            # delete value at our current node.
            cur_node.value = None
        
        prev_node = cur_node
        cur_node = cur_node.next

        while cur_node is not None:
            if cur_node.key == key:
                prev_node.next = cur_node.next
                cur_node.next = None

                return cur_node

            else:
                prev_node = prev_node.next
                cur_node = cur_node.next
                
        # reduce size value
        self.size -= 1

        #if load factor decreases below .2 then resize.
        load_factor = self.get_load_factor()
        if load_factor < .2:
            self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]

        # iterate through the storage until we either find or don't find our key value
        while node is not None and node.key != key:
            node = node.next
         # return none if key not found
        if node == None:
            return None
        
        # return the value we found
        else:
            return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # take our new_capacity and set it to self.capacity.
        self.capacity =  new_capacity
        # save our old data
        old_storage = self.storage
        # create a new list with our new capacity
        self.storage = [None] * self.capacity
        # reset size value
        self.size = 0

        # iterate through our data from old storage and put it into the new storage.
        for cur in old_storage:
            while cur != None:
                self.put(cur.key, cur.value)
                cur = cur.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
