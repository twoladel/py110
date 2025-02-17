def calculate_leftover_blocks(block_count):
    current_layer = 0
    remaining_blocks = block_count
    current_layer += 1
    blocks_for_next_layer = current_layer ** 2

    while remaining_blocks >= blocks_for_next_layer:
        remaining_blocks -= blocks_for_next_layer
        current_layer += 1
        blocks_for_next_layer = current_layer ** 2

    return remaining_blocks


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
