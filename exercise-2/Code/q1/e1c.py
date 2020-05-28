def is_prime(p):
    return (1 < p) and not any(p % i == 0 for i in range(2,int(p)//2+1))

if __name__ == '__main__':
    import sys
    print(is_prime(int(sys.argv[1])))    
    sys.exit()
