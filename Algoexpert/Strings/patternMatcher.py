def patternMatcher(pattern, string):
    # Write your code here.
    # pattern = 'xxyxxy'
    # string = 'gogopowerrangergogopowerranger'
    
    my_keys = {k:pattern.count(k) for k in pattern}
    str_len = len(string)
    if 'y' in my_keys:
        frst_y = pattern.index('y')
    else:
        frst_y = None
    if 'x' in my_keys:
        frst_x = pattern.index('x')
    else:
        frst_x = None
    
    second, second_letter_idx = get_second(frst_x, frst_y)
    # print(frst_x, frst_y, second, second_letter_idx)
    
    for i in range(1, len(pattern)):
        if second == 'y':
            xlen = i
            yidx = frst_y * xlen
            ylen = (str_len - (xlen*my_keys['x']))//my_keys['y']
            x = string[0:xlen]
            y = string[yidx:yidx+ylen]
            total_len = (xlen * my_keys['x']) + (my_keys['y'] * (ylen))
            # print('frst is x, ', 4*i,2*ylen,total_len)
            print(x,y)
        else: # second is x
            if frst_y is not None:
                ylen = i
                xidx = frst_x * ylen
                xlen = (str_len - (ylen*my_keys['y']))//my_keys['x']
                print('xlen is ', xlen)
                y = string[0:ylen]
                x = string[xidx:xidx+xlen]
                # print('first is y, ', 4*i,2*ylen,total_len)
                print(x,y)
            
        # total_len = (xlen * my_keys['x']) + (my_keys['y'] * (ylen))
        # print(4*i,2*ylen,total_len)
        # print(string[0:xlen],string[yidx:yidx+ylen])
        
        final_word = ''
        for char in pattern:
            if char == 'x':
                final_word += x
            else:
                final_word += y
        print(final_word)
            
        if final_word == string:
            return [x,y]
    return []
            
def get_second(x_idx, y_idx):
    if x_idx == 0 and y_idx is not None:
        return 'y', y_idx
    if y_idx == 0 and x_idx is not None:
        return 'x', x_idx
    if x_idx == x and y_idx is None:
        return x


pattern = "xxxx"
string = "testtesttesttest"
patternMatcher(pattern, string)