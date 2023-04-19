def rotate_90(arr, arr_sz):
    new_arr = [[0]*arr_sz for _ in range(arr_sz)]
    for y in range(arr_sz):
        for x in range(arr_sz):
            new_arr[x][arr_sz-1-y] = arr[y][x]
    
    return new_arr

def solution(key, lock):
    key_sz = len(key)
    lock_sz = len(lock)
    padded_sz = key_sz*2+lock_sz
    padded_lock = [[0]*(padded_sz) for _ in range(padded_sz)]
    for y in range(lock_sz):
        for x in range(lock_sz):
            padded_lock[y+key_sz][x+key_sz] = lock[y][x]
    for i in range(4):
        for y in range(padded_sz-key_sz):
            for x in range(padded_sz-key_sz):
                arr = []
                for key_y in range(key_sz):
                    for key_x in range(key_sz):
                        if padded_lock[y+key_y][x+key_x] == 0 and key[key_y][key_x] == 1:
                            padded_lock[y+key_y][x+key_x] = 1
                            arr.append((y+key_y, x+key_x, 0))
                        elif padded_lock[y+key_y][x+key_x] == 1 and key[key_y][key_x] == 1:
                            padded_lock[y+key_y][x+key_x] = 0
                            arr.append((y+key_y, x+key_x, 1))
                for row in padded_lock:
                    print(row)
                print("-----------------")
                good = True
                for cy in range(lock_sz):
                    for cx in range(lock_sz):
                        if padded_lock[cy+key_sz][cx+key_sz] == 0:
                            good = False
                            break
                if good:
                    return True
                else:
                    for _y, _x, v in arr:
                        padded_lock[_y][_x] = v
    
        key = rotate_90(key, key_sz)
    return False

if __name__ == '__main__':
    print(
        solution(
            # [
            #     [0, 0, 0], 
            #     [1, 0, 0], 
            #     [0, 1, 1]
            # ], 
            # [
            #     [1, 1, 1], 
            #     [1, 1, 0], 
            #     [1, 0, 1]
            # ]
            [
                [1, 1],
                [1, 0],
            ], 
            [
                [1, 0],
                [0, 1]
            ]
        )
    )