def converter(user_input,original,desired):
    result = []
    for e in user_input: 
        if e in original: 
            e = desired
            result.append(e)
            print(e)
        else: 
            result.append(e)
    return "".join(result)

user_input = input('input\n')
original = input('original\n')
desired = input('desired\n')

result = converter(user_input,original,desired)
print(result)