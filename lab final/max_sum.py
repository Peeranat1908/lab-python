words = input().split()
errorword = ['for', 'and', 'with', 'of']
result = []
for i in words:
    if i.lower() not in errorword:
        word = i.title()
    result.append(word)
final_result = ' '.join(result)
print(final_result)
