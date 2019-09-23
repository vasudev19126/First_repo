def checkit(x,a):
        z=len(a)-1
        y=z % x
        print(z - y)
        return (len(a)%2==0 or (len(a)) > x)

checkit(2,"chqvjhjcj")
