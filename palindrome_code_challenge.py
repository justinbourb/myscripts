input_list=["abcbd", "abba", "abcbdeffe"]
output_list=["bcb","abba","effe"]

def palindromeFunc(string):
    answer=""
    potential_match=[]
    reverse=""
    match_list=[]
    occurence_dict=characterCountFunc(string)
    '''slices string over potential match range (range character appears twice in string)'''
    for key,values in occurence_dict.items():
        if values[0]>1:
            potential_match.append(string[values[1]:values[2]+1])
    '''takes potential match and reverses it so we can test if it is a palindrome'''
    for match_string in potential_match:
        for i in range(1,len(match_string)+1):
            reverse+=match_string[i*-1]
            """if it is a palindrome add to match list (in case more than one palindrome per string)"""
            if reverse==match_string:
                match_list.append(match_string)
        """reset reverse for next loop"""
        reverse=""
    """find the longest match"""
    for i in match_list:
        if len(i)>len(answer):
            answer=i
    print(answer)

"""
TODO:
    1_refactor palindrome func into palindrome and longestPalindrome
    2_refactor main body to call functions and return results to next function
    instead of calling functions inside one another"""



def characterCountFunc(string):
    '''this function accepts a string and returns the number of times each character appears
    and their distance apart so string does not have to be queried twice'''
    occurence_dict={}
    for i in range(len(string)):
        if not string[i] in occurence_dict:
            occurence_dict[string[i]] = [1,i]
        else:
            occurence_dict[string[i]][0] += 1
            occurence_dict[string[i]].append(i)
    return occurence_dict

if __name__=="__main__":

    palindromeFunc("abcbdeffe")
