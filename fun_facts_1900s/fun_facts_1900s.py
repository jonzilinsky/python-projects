tuf = True
while tuf:
    print("""
---Fun Facts From the 1900s---

Enter a number to select a decade.
0. 1900
1. 1910
2. 1920
3. 1930
4. 1940
5. 1950
6. 1960
7. 1970
8. 1980
9. 1990""")

    decade = input('>')
    if decade == '0':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('Teddy Roosevelt inspires the "Teddy Bear" (1902).')
        elif cat == '2':
            print("Wireless radio amazes everyone (1906).")
        elif cat == '3':
            print("The Great Train Robbery makes moviegoers duck (1903).")
        else:
            print("Command not recognized.")
    if decade == '1':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('WW1 brings trench coats into fashion (1914).')
        elif cat == '2':
            print("Tanks debut, slow but sturdy (1916).")
        elif cat == '3':
            print("Charlie Chaplin's slapstick delights (1914).")
        else:
            print("Command not recognized.")
    if decade == '2':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('Flappers dance through the Prohibition (1920s).')
        elif cat == '2':
            print("TV is invented, no one knows what to do with it (1928).")
        elif cat == '3':
            print("Jazz and Gatsby rule the scene (1925).")
        else:
            print("Command not recognized.")
    if decade == '3':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('The Great Depression teaches thrift (1930s).')
        elif cat == '2':
            print("Jet engines are invented (1937).")
        elif cat == '3':
            print("Gone with the Wind dazzles (1939).")
        else:
            print("Command not recognized.")
    if decade == '4':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('WWII end, the world exhales (1945).')
        elif cat == '2':
            print("ENIAC, the first computer, is huge (1945).")
        elif cat == '3':
            print("Casablanca becomes a classic (1942).")
        else:
            print("Command not recognized.")
    if decade == '5':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('Cold War spy gadgets emerge (1950s).')
        elif cat == '2':
            print("Sputnik orbits Earth, everyone watches (1957).")
        elif cat == '3':
            print("Elvis shakes things up (1950s)")
        else:
            print("Command not recognized.")
    if decade == '6':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('Civil Rights Movement reshapes America (1960s).')
        elif cat == '2':
            print("Moon landing inspires awe (1969)")
        elif cat == '3':
            print("The Beatles lead the music revolution (1963).")
        else:
            print("Command not recognized.")
    if decade == '7':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('Vietnam War ends, disco begins (1975).')
        elif cat == '2':
            print("Personal computers maker their debut (1975).")
        elif cat == '3':
            print("Star Wars revolutionizes sci-fi and cinema (1977).")
        else:
            print("Command not recognized.")
    if decade == '8':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('The Berlin Wall falls, symbolizing change (1989).')
        elif cat == '2':
            print("IBM PC changes computing (1981).")
        elif cat == '3':
            print("MTV makes music videos a thing (1981).")
        else:
            print("Command not recognized.")
    if decade == '9':
        print("Choose a category:\n1. History\n2. Technology \n3. Entertainment")
        cat = input('>')
        if cat == '1':
            print('Soviet Union dissolves, new maps needed (1991).')
        elif cat == '2':
            print("The World Wide Web goes public (1991).")
        elif cat == '3':
            print("Titanic becomes a blockbuster (1997).")
        else:
            print("Command not recognized.")


    print("\nGo again? y/n:")
    etuf = input('>')
    if etuf == 'n' or etuf == 'no':
        tuf = False

print("Thank you for trying the program!")        
