if __name__ == '__main__':
    n = int(input("how many elements in tuple: "))
    integer_list = map(int, input("elements in tuple: ").split())
    t = tuple(integer_list)
    print("hash value is %s"%hash(t) )
