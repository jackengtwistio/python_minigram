punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(data,punctuation_chars=punctuation_chars):
    result = data
    for e in data:
        if e in punctuation_chars:
            result = result.replace(e,' ')
    return(result)


def factor_appeares_times(text, factor): 
    words = strip_punctuation(text) 
    words = words.split()
    count = 0
    for word in words:
        if word.lower() in factor.lower():
            count+=1
    return count

def add_factors_counts(row,factors,result,text_positions,reserved_position):
    for factor in factors:
        factor_num=0
        for tp in text_positions:
            factor_num += factor_appeares_times(row[int(tp)],factor)
        result+=(str(factor_num)+',')
    if(reserved_position):
        for rp in reserved_position:
            result+=row[int(rp)]
    result.pop()
    result+='\n'
    
text_positions = input('indexes of text you are querying in each row, seperated by comma')
reserved_positions = input('indexes of text you want to reserve from original file by each row, seperated by comma')

def factors_countor(file_path, text_positions, factors_file_path, header='', reserved_positions=[]): 
    
    """counts every factor of factors(list) found in particular text strings(specify by text_positions) from each row of data(csv table, header is assumed), generates a new file(csv), with numbers of factors found in each row of data. you can specify which original columns to add to new file by reserved_position, they appear after counted factor numbers"""
    with open(file_path, 'r') as file:
        file = file.read()
        data = file.split('\n')
    with open(factors_file_path, 'r') as file:
        file = file.read()
        factors = file.split(',')
        factors = file.split('')
    result = []
    
    text_position = text_positions.split(',')
    reserved_positions = reserved_positions.split(',')
    if header:
        for h in header:
            result+=(h+',')
        result.pop()
        result+='\n'
        for row in data[1:-1]:
            add_factors_counts(row,factors,result,text_position,reserved_positions)
    else:
        for row in data[1:-1]:
            add_factors_counts(row,factors,result,text_position,reserved_positions)
    """counts every factor of factors(list) found in particular text strings(specify by text_positions) from each row of data(csv table)"""
    
    f = open("results.csv", "w")
    result = ''.join(result)
    f.write(result)
    f.close()
    
file = open('project_twitter_data.csv','r')
file = file.read()
file = file.split('\n')
    