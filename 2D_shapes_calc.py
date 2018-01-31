import math

#calculates rectangle or square aera
def rectangle_aera(w, l):
    return w * l
#calculates rectangle, square or parallelogram perimeter
def rectangle_per(w, l):
    return 2 * w + 2 * l
#calculates circle perimeter
def circle_per(r):
    return round(2 * math.pi * r, 2)
#calculates ellipse or circle aera
def ellipse_aera(a, b):
    return round(math.pi * a * b, 2)
#calculates triangle aera
def triangle_aera(b,h):
    return b * h * 0.5
#calcualtes truangle perimeter
def triangle_per(a, b, c):
    return a + b + c
#calculates parallelogram aera
def parallelogram_aera(b, h):
    return b * h
#calculates trapezoid aera
def trapezoid_aera(a, b, h):
    return (a + b) * 0.5 * h
#calculates trapezoid perimeter
def trapezoid_per(a, b, c, d):
    return a + b + c + d

print ("Welcome! This application can calculate aera and perimeter of two-dimensional shapes.\n")
x = "" #used to store input from user concerning shape to calculate or to quit program (main loop)
#main program loop, continues until user types in "exit" in shape selection menu
while x != "exit":
    print ("Here are the shapes you can choose from:")
    print ("1) Square  2) Rectangle  3) Circle 4) Ellipse")
    print ("5) Triangle 6) Parallelogram 7) Trapezoid\n")
    x = input ("Please enter the number of shape or type 'exit' to quit: ")
    if x == "1":
        print ("\nYou selected Square")
        y = "" #used to store input from user concerning which to calculate: aera or perimeter
        while y != "a" and y != "p": #loop to let user choose which to calculate: aera or perimeter, continues until valid choice is made
            y = input ("Type 'a' for aera or 'p' for perimeter: ")
            if y == "a":
                while True:
                    s = input ("\nPlease provide lenght of squares side: s=")
                    try:
                        s = float(s)
                        if s < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            s = abs(s)
                        print ("\nA = ", rectangle_aera(s, s))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            elif y == "p":
                while True:
                    s = input ("\nPlease provide lenght of squares side: s=")
                    try:
                        s = float(s)
                        if s < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            s = abs(s)
                        print ("\nP = ", rectangle_per(s, s))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            else:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "2":
        print ("\nYou selected Rectangle")
        y = "" #used to store input from user concerning which to calculate: aera or perimeter
        while y != "a" and y != "p": #loop to let user choose which to calculate: aera or perimeter, continues until valid choice is made
            y = input ("Type 'a' for aera or 'p' for perimeter: ")
            if y == "a":
                while True:
                    w = input ("\nPlease provide lenght of first rectangle side: w=")
                    l = input ("Please provide lenght of second rectangle side: l=")
                    try:
                        w = float(w)
                        l = float(l)
                        if w < 0 or l < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            w = abs(w)
                            l = abs(l)
                        print ("\nA = ", rectangle_aera(w, l))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            elif y == "p":
                while True:
                    w = input ("\nPlease provide lenght of first rectangle side: w=")
                    l = input ("Please provide lenght of second rectangle side: l=")
                    try:
                        w = float(w)
                        l = float(l)
                        if w < 0 or l < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            w = abs(w)
                            l = abs(l)
                        print ("\nP = ", rectangle_per(w, l))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            else:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "3":
        print ("\nYou selected Circle")
        y = "" #used to store input from user concerning which to calculate: aera or perimeter
        while y != "a" and y != "p": #loop to let user choose which to calculate: aera or perimeter, continues until valid choice is made
            y = input ("Type 'a' for aera or 'p' for perimeter: ")
            if y == "a":
                while True:
                    r = input ("\nPlease provide lenght of circle radius: r=")
                    try:
                        r = float(r)
                        if r < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            r = abs(r)
                        print ("\nA = ", ellipse_aera(r, r))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            elif y == "p":
                while True:
                    r = input ("\nPlease provide lenght of circle radius: r=")
                    try:
                        r = float(r)
                        if r < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            r = abs(r)
                        print ("\nP = ", circle_per(r))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            else:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "4":
        print ("\nYou have selected Ellipse (only aera is available)\n")
        while True:
            a = input ("Please provide lenght of the semi-major: a=")
            b = input ("Please provide lenght of the semi-minor: b=")
            try:
                a = float(a)
                b = float(b)
                if a < 0 or b < 0:
                    print ("\nYou provided a negative value, converting to positive.")
                    a = abs(a)
                    b = abs(b)
                print ("\nA = ", ellipse_aera(a, b))
                input ("Press Enter to continue...\n")
                break
            except ValueError:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "5":
        print ("\nYou selected Triangle")
        y = "" #used to store input from user concerning which to calculate: aera or perimeter
        while y != "a" and y != "p": #loop to let user choose which to calculate: aera or perimeter, continues until valid choice is made
            y = input ("Type 'a' for aera or 'p' for perimeter: ")
            if y == "a":
                while True:
                    b = input ("\nPlease provide lenght of triangle base: b=")
                    h = input ("Please provide lenght of triangle height: h=")
                    try:
                        b = float(b)
                        h = float(h)
                        if b < 0 or h < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            b = abs(b)
                            h = abs(h)
                        print ("\nA = ", triangle_aera(b, h))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            elif y == "p":
                while True:
                    a = input ("\nPlease provide lenght of first triangle side: a=")
                    b = input ("Please provide lenght of second triangle side: b=")
                    c = input ("Please provide lenght of third triangle side: c=")
                    try:
                        a = float(a)
                        b = float(b)
                        c = float(c)
                        if a < 0 or b < 0 or c < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            a = abs(a)
                            b = abs(b)
                            c = abs(c)
                        print ("\nP = ", triangle_per(a, b, c))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            else:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "6":
        print ("\nYou selected Parallelogram")
        y = "" #used to store input from user concerning which to calculate: aera or perimeter
        while y != "a" and y != "p": #loop to let user choose which to calculate: aera or perimeter, continues until valid choice is made
            y = input ("Type 'a' for aera or 'p' for perimeter: ")
            if y == "a":
                while True:
                    b = input ("\nPlease provide lenght of parallelogram base: b=")
                    h = input ("Please provide lenght of parallelogram height: h=")
                    try:
                        b = float(b)
                        h = float(h)
                        if b < 0 or h < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            b = abs(b)
                            h = abs(h)
                        print ("\nA = ", parallelogram_aera(b, h))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            elif y == "p":
                while True:
                    b = input ("\nPlease provide lenght of parallelogram base: b=")
                    a = input ("Please provide lenght of parallelogram side: a=")
                    try:
                        b = float(b)
                        a = float(a)
                        if b < 0 or a < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            b = abs(b)
                            a = abs(a)
                        print ("\nP = ", rectangle_per(b, a))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            else:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "7":
        print ("\nYou selected Trapezoid")
        y = "" #used to store input from user concerning which to calculate: aera or perimeter
        while y != "a" and y != "p": #loop to let user choose which to calculate: aera or perimeter, continues until valid choice is made
            y = input ("Type 'a' for aera or 'p' for perimeter: ")
            if y == "a":
                while True:
                    a = input ("\nPlease provide lenght of first trapezoid base: a=")
                    b = input ("Please provide lenght of second trapezoid base: b=")
                    h = input ("Please provide lenght of trapezoid height: h=")
                    try:
                        a = float(a)
                        b = float(b)
                        h = float(h)
                        if a < 0 or b < 0 or h < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            a = abs(a)
                            b = abs(b)
                            h = abs(h)
                        print ("\nA = ", trapezoid_aera(a, b, h))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            elif y == "p":
                while True:
                    a = input ("\nPlease provide lenght of first trapezoid base: a=")
                    b = input ("Please provide lenght of second trapezoid base: b=")
                    c = input ("Please provide lenght of first trapezoid side: c=")
                    d = input ("Please provide lenght of second trapezoid side: d=")
                    try:
                        a = float(a)
                        b = float(b)
                        c = float(c)
                        d = float(d)
                        if a < 0 or b < 0 or c < 0 or d < 0:
                            print ("\nYou provided a negative value, converting to positive.")
                            a = abs(a)
                            b = abs(b)
                            c = abs(c)
                            d = abs(d)
                        print ("\nP = ", trapezoid_per(a, b, c, d))
                        input ("Press Enter to continue...\n")
                        break
                    except ValueError:
                        print ("\nThats not a valid input, try again.")
                        input ("Press Enter to continue...\n")
            else:
                print ("\nThats not a valid input, try again.")
                input ("Press Enter to continue...\n")
    elif x == "exit":
        continue
    else:
        print ("\nThats not a valid input, try again.")
        input ("Press Enter to continue...\n")
