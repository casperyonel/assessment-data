log_file = open("um-server-01.txt")
# this is opening the file, allowing us to access it with python, and then setting it to log_file for ease of access.

def sales_reports(log_file):
    # this is creating a function with the parameter being the file we want to grab. 
    for line in log_file:
        # this is a for loop that grabs each line within the .txt file
        line = line.rstrip()
        # this creates a new var called line that is similar to trim in JS where it gets rid of all of the whitespaces
        day = line[0:3]
        # this creates a new var called day that isolates the line so that only the first 3 letters show up, which we are going to comapre to our "Tue" on the next line
        if day == "Mon":
            print(line)
        # here we are comparing the first 3 letters of the line we stored in "day" to "Tue", and returnign that line if it's true. 

sales_reports(log_file)
