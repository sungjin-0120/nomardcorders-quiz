numbers = [
    1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 
    13, "💖", 14, "🔥", 15, "⭐️", 16
    ]
num_int=[]
for num in numbers:
    if type(num) == int:
        num_int.append(num)
print(sum(num_int))
        
#데이터 타입확인 type()확인 for루프를 통해 풀이