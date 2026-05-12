
def solution(num_list):
    total = 0
    total2 = 0
    
    for i in num_list:
        if i % 2 == 0:
            total += 1
        else:
            total2 += 1
    answer = [total, total2]
    return answer

result = solution([1, 2, 3, 4, 5])
print(result)
