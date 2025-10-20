def get_even_numbers(lst):
    even_list=[]
    for num in lst:
        if num%2==0:
            even_list.append(num)
    print(even_list)
numbers=[1,2,3,4,5,6,7,8,9]
get_even_numbers(numbers)
