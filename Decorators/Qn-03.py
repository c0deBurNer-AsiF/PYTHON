#define a decorator to display "Good Bye" message at the end


def good_bye(hii_function):
    def print_text():
        hii_function()
        print("Good Bye!")
    return print_text    


@good_bye
def hii():
    print("Hey User!..Welcome!")

#hii()
