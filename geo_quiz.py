"""
Create a program with a hash of countries & capitals - don't worry I'll give it to you:

cos_n_caps = {"USA":"Washington, DC", "Canada":"Ottawa", "United Kingdom":"London", "France":"Paris", "Germany":"Berlin", "Egypt":"Cairo", "Ghana":"Accra", "Kenya":"Nairobi", "Somalia":"Mogadishu", "Sudan":"Khartoum", "Tunisia":"Tunis", "Japan":"Tokyo", "China":"Beijing", "Thailand":"Bangkok", "India":"New Delhi", "Philippines":"Manila", "Australia":"Canberra", "Kyrgyzstan":"Bishkek"}

Ask the user for the capital of each country, and tell them if they are Correct or Wrong. Also, keep score and give their score at the end of the quiz. Maybe have some smart-alecky comments about their score (see example below).
"""

cos_n_caps = {"USA": "Washington, DC", "Canada": "Ottawa", "United Kingdom": "London", "France": "Paris", "Germany": "Berlin", "Egypt": "Cairo", "Ghana": "Accra", "Kenya": "Nairobi", "Somalia": "Mogadishu", "Sudan": "Khartoum", "Tunisia": "Tunis", "Japan": "Tokyo", "China": "Beijing", "Thailand": "Bangkok", "India": "New Delhi", "Philippines": "Manila", "Australia": "Canberra", "Kyrgyzstan": "Bishkek"}

print "Let's play Geo Quiz!"
print "I'll give you a country, you give me the capital."

score = 0

for key in cos_n_caps:
    ans = (raw_input("What is the capital of " + key + "? ")).lower().capitalize()

    if ans == "New delhi" or ans == "Delhi":
        ans = "New Delhi"
    elif ans == "Washington, dc" or ans == "Washington dc" or ans == "Washington":
        ans = "Washington, DC"

    if ans == cos_n_caps[key]:
        print "Correct!"
        score += 1
    else:
        print "Wrong!"

print ""
print "You got %d out of %d" % (score, len(cos_n_caps))
if score > (len(cos_n_caps)/2):
    print "You're a geo-whiz!"
else:
    print "Not gonna be getting that job at the UN, are we?"
