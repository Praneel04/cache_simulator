import math
class Cache:
    def __init__(self, cache_size, block_size):
        self.cache_size = cache_size
        self.block_size = block_size
        self.cache_lines = cache_size // block_size
        self.cache = [(None, None)] * self.cache_lines  # Initialize cache with (tag, block_no) tuples


    def direct_mapping(self, memory_address,no_of_words,tag_bits,block_bits,word_bits):
        block_no=get_block_no(get_block_bits(memory_address,block_bits,word_bits))
        tag_no=get_tag_no(get_tag_bits(memory_address,tag_bits))
        
        cache_index = block_no % self.cache_lines  # Map block number to a cache line
        
        if self.cache[cache_index][0] == tag_no:
            print(f"Cache hit for memory address {memory_address}.")
        else:
            print(f"Cache miss for memory address {memory_address}.")
            self.cache[cache_index] = (tag_no, block_no)  # Update cache with new tag and block number

    def print_cache(self):
        print("Cache:")
        print("Block Number\tTag")
        for i, (tag, block_no) in enumerate(self.cache):
            tag_str = f"{tag}" if tag is not None else "-"
            block_no_str = str(block_no) if block_no is not None else "-"
            print(f"{i}\t{block_no_str}\t\t{tag_str}")
def get_word_bits(memory,no_of_words):
    return memory[-no_of_words:]
def get_block_no(block_bits):
    return int(block_bits, 2)
def get_tag_no(tag_bits):
    return int(tag_bits, 2)
def get_block_bits(memory,block_bits,word_bits):
    return memory[-(block_bits+word_bits):-(word_bits)]
def get_tag_bits(memory,tag_bits):
    return memory[0:tag_bits]
def main():
    main_memory = int(input("Enter the main memory: "))
    cache_memory = int(input("Enter the cache memory: "))
    block_size = int(input("Enter the block size: "))
    total_bits = int(math.log2(main_memory))
    word_bits_count = int(math.log2(block_size))
    block_bits_count = int(math.log2(cache_memory / block_size))
    tag_bits_count = total_bits - block_bits_count - word_bits_count
    cache=Cache(cache_memory,block_size)
    # Convert decimal input to binary
    try:
        input_str = input("Enter memory address(es) separated by spaces: ")
        memory_addresses = [int(addr) for addr in input_str.split()]

        # Validate memory addresses
        for memory_address in memory_addresses:
            if memory_address >= main_memory:
                print(f"Error: Memory address {memory_address} exceeds main memory size.")
                return

            memory_address_binary = ([format(addr, f'0{total_bits}b') for addr in memory_addresses])            
            

            
    except ValueError:
        print("Error: Invalid input. Please enter valid decimal numbers separated by spaces.")
        return
    for memory in memory_address_binary:
        cache.direct_mapping(memory,block_size,tag_bits_count,block_bits_count,word_bits_count)
        cache.print_cache()
    

    # Print cache
    


    
    

if __name__ == "__main__":
    main()
