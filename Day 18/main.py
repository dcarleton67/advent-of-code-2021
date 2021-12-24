with open('Day 18/input.txt') as f:
    snailfish_strings = f.read().strip().split('\n')

class Snailfish:
    def __init__(self, val):
        self.val = int(val) if val != '[' else val
        self.is_leaf = val != '['
        self.left_child = None
        self.right_child = None
        self.parent = None

    def check_is_leaf(self):
        if self.is_leaf: return True
        return self.left_child and self.left_child.check_is_leaf() and self.right_child and self.right_child.check_is_leaf()
        
    # Returns the Snailfish number for the inserted value
    def insert(self, val):
        if not self.left_child:
            self.left_child = Snailfish(val)
            self.left_child.parent = self
            return self.left_child

        if not self.left_child.check_is_leaf():
            return self.left_child.insert(val)

        if not self.right_child:
            self.right_child = Snailfish(val)
            self.right_child.parent = self
            return self.right_child

        return self.right_child.insert(val)

    # returns the regular number immediately to the left if one exists
    def get_immediate_left(self):
        if self.parent is None: return None
        # if we are our parents right child then the immediate left regular number is the rightmost leaf of our parents left child
        if self.parent.right_child is self: 
            node = self.parent.left_child
            while not node.is_leaf: node = node.right_child
            return node
        return self.parent.get_immediate_left()

    # returns the regular node immediately to the right if one exists
    def get_immediate_right(self):
        if self.parent is None: return None
        if self.parent.left_child is self:
            node = self.parent.right_child
            while not node.is_leaf: node = node.left_child
            return node
        return self.parent.get_immediate_right()

    def check_depth(self, cur_depth=0):
        if self.val != '[': return None
        if cur_depth == 4: return self

        left_too_deep = self.left_child.check_depth(cur_depth + 1)
        if left_too_deep: return left_too_deep

        return self.right_child.check_depth(cur_depth + 1)

    def check_regular_size(self):
        if self.val != '[': return self if self.val > 9 else None

        regular_left_check = self.left_child.check_regular_size()
        if regular_left_check: return regular_left_check

        return self.right_child.check_regular_size()

    def magnitude(self):
        if self.val != '[': return self.val
        return 3 * self.left_child.magnitude() + 2 * self.right_child.magnitude()

def print_snailfish(snailfish_num):
    if snailfish_num is None:
        return
    print(snailfish_num.val)
    if snailfish_num.is_leaf:
        print('Leaf: Ending')
        return 
    print('Left Child')
    print_snailfish(snailfish_num.left_child)
    print('Right Child')
    print_snailfish(snailfish_num.right_child)

def process_snailfish_string(snailfish_str):
    snailfish_str = snailfish_str[1:-1]
    snailfish = Snailfish('[')
    for char in snailfish_str:
        if char not in [',',']']:
            snailfish.insert(char)
            
    return snailfish

def add_snailfish(l, r):
    snailfish = Snailfish('[')
    snailfish.left_child = l
    snailfish.right_child = r

    snailfish.left_child.parent = snailfish
    snailfish.right_child.parent = snailfish
    return snailfish

def explode_pair(pair_node):
    left = pair_node.get_immediate_left()
    right = pair_node.get_immediate_right()

    if left is not None: left.val += pair_node.left_child.val
    if right is not None: right.val += pair_node.right_child.val

    pair_node.left_child = None
    pair_node.right_child = None
    pair_node.val = 0
    pair_node.is_leaf = True

def split_regular(regular_node):
    left_val = regular_node.val // 2
    right_val = regular_node.val - left_val

    regular_node.val = '['
    regular_node.left_child = Snailfish(left_val)
    regular_node.right_child = Snailfish(right_val)
    regular_node.is_leaf = False
    regular_node.left_child.parent = regular_node
    regular_node.right_child.parent = regular_node

def reduce_snailfish(snailfish):
    depth_check = snailfish.check_depth(0)
    if depth_check:
        explode_pair(depth_check)
        return True

    size_check = snailfish.check_regular_size()
    if size_check:
        split_regular(size_check)
        return True

    return False

snailfish_sum = [process_snailfish_string(snailfish_str) for snailfish_str in snailfish_strings]

snailfish_total = snailfish_sum[0]
for snailfish in snailfish_sum[1:]:
    snailfish_total = add_snailfish(snailfish_total, snailfish)
    while reduce_snailfish(snailfish_total): pass

print(snailfish_total.magnitude())

def copy_snailfish(snailfish):
    if snailfish is None: return None
    copy = Snailfish(snailfish.val)
    if snailfish.val != '[': return copy
    copy.left_child = copy_snailfish(snailfish.left_child)
    copy.right_child = copy_snailfish(snailfish.right_child)
    copy.left_child.parent = copy
    copy.right_child.parent = copy
    return copy

max_magnitude = 0
snailfish_sum = [process_snailfish_string(snailfish_str) for snailfish_str in snailfish_strings]

for snailfish_a in snailfish_sum:
    for snailfish_b in snailfish_sum:
        if snailfish_a is snailfish_b: continue

        left = copy_snailfish(snailfish_a)
        right = copy_snailfish(snailfish_b)

        snail_sum = add_snailfish(left, right)
        while reduce_snailfish(snail_sum): pass

        cur_magnitude = snail_sum.magnitude()
        if cur_magnitude > max_magnitude:
            max_magnitude = cur_magnitude
            
print(max_magnitude)
