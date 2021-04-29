def melon_delivery(day, path):
"""Given day number and path to deliveries, produce report

Opens the deliveries file at [path], processes each line, and generates a report in all uppercase"""

    print("Day", day)
    # prints the day
    delivery_log = open(path)
    #opens the file

    for line in delivery_log:
        # to loop through each line in the document
        line = line.rstrip()
        # removes the whitespace
        words = line.split('|')
        # breaks up the words in the input so they can be looked at individually

        melon = words[0]
        # says where to find the melon
        count = words[-2]
        # says where to find the count
        amount = words[-1]
        # says where to find the amount

        print("Delivered {} {}s for total of ${}".format(
         count, melon, amount))
        # prints out the report that needs to be read
    delivery_log.close()
    # closing the file


melon_delivery(1, "um-deliveries-20140519.txt")
melon_delivery(2, "um-deliveries-20140520.txt")
melon_delivery(3, "um-deliveries-20140521.txt")