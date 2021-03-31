days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eigth", "ninth", "tenth", "eleventh", "twelfth"]
        
presents = ["a partridge in a pear tree.", "two turtle doves and",
            "three french hens,", "four calling birds,", "five gold rings,",
            "six geese a laying,", "seven swans a swimming,",
            "eight maids a milking,", "nine ladies dancing,",
            "ten lords a leaping,", "eleven pipers piping,",
            "twelve drummers drumming,"]

for day_index in range(0, len(days)):
    print(f"One the {days[day_index]} day of Christmas my true love gave to me...")
    for present_index in range(day_index, -1, -1):
        print(f"{presents[present_index]}")
