# x='eeefnejnfoivwioooofdvjsbfugwuwrfgrjllllll'
# def max_s(x:str):
#     max_symvol=x[0]
#     max_count=1
#     maxs_index=0

#     current_count=1
#     current_symvol=x[0]

#     for i in range(1, len(x)):
#         if x[i]==x[i-1]:
#             current_count+=1
#         else:
#             current_count=1
#             current_symvol=x[i]
#         if current_count>max_count:
#             max_count=current_count
#             max_symvol=x[i]
#             maxs_index=i-current_count+1
#     return (max_symvol, max_count, maxs_index)

# print(max_s(x))
# from collections import defaultdict


# x='eeefnejnfoivwioooofdvjsbfugwuwrfgrjllllll'
# def kolichestvo_kajdogo(x):
#     result={}
#     for i in x:
#         if i in result:
#             result[i]+=1
#         else:
#             result[i]=1
#     return result

# print(kolichestvo_kajdogo(x))


# def nepovtor(x):
#     if x[1]!=x[0]:
#         return x[0]
#     else:
#         return nepovtor(x[2:])
    
# print(nepovtor(x))


# def ubratpovtor(x):
#     new=''
#     for i in x:
#         if i not in new:
#             new+=i
#     return new

# print(ubratpovtor('eeefnejnfoivwioooofdvjsbfugwuwrfgrjllllll'))

# def ubratpovtor(x):
#     new = ""
#     for ch in x:
#         if ch not in new:
#             new += ch
#         else:
            
#     return new
# print(ubratpovtor('sdnsidngoifrosd'))




def naibolshii_povtor(x):
    if len(x)==0:
        return False
    
    max_el=x[0]
    max_count=1
    current_el=x[0]
    current_count=1
    for i in range(1, len(x)):
        if x[i]==x[i-1]:
            current_count+=1
        else:
            current_el=x[i]
            current_count=1
        if current_count>max_count:
            max_el=x[i]
            max_count=current_count
    return max_count, max_el

print(naibolshii_povtor('ffmmnnnooooovu'))

