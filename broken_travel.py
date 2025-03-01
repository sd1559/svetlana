# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))#== changed to = , comparative operator not used and its input statement-edited by svetlana
                  #. changed to parenthesis after int (, double quotation mark closed with single has been corrected-edited by svetlana

if year < 1900:#colon added and <= changed to < accordingly-edited by svetlana
    print ("Woah, that's the past!")#single quotation changed to double quotation-edited by svetlana
elif year > 1900 and year < 2020: #&& operator is not used instead use and-edited by svetlana
    print ("That's totally the present!")
else:#elif changed to else statement-edited by svetlana
    print ("Far out, that's the future!!")
