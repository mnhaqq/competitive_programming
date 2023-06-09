def solve():   
    # n is the number of patterns 
    n = int(input())

    patterns = [input() for _ in range(n)] 
    ans = ''
    # loop for iterating through each character in the pattern
    for i in range(len(patterns[0])):
        prev_char = ""
        prev_cnt = 0
        #count mark counts the number of question marks
        count_mark = 0  
        # for loop for iterating through patterns
        for j in range(n):
            #increases count of question marks
            if patterns[j][i] == '?':
                count_mark += 1 
            
            elif patterns[j][i] == prev_char or prev_char == '':
                prev_char = patterns[j][i] 
                prev_cnt += 1 
        
        if count_mark == n:
            ans += 'a' 
        elif prev_cnt == n or prev_cnt + count_mark == n:
            ans += prev_char   
        else:
            ans += '?' 
    print(ans)
 
solve()