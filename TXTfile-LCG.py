# Random Number Generator using Linear Congruential Generator and takes input from txt file

# importing libraries 
import smtplib
import time
import numpy

# Welcoming user
print("\nWelcome to my Pseudo RANDOM Number Generator program")
time.sleep(0.5)
print("By:")
time.sleep(0.5)
print("------>Nour")
time.sleep(0.5)
print("------------>Sharaky")

# opens and reads a number(input/seed) from a text file
with open('number.txt') as f:
    contents = int(f.read())
 
# ask user to input how many values they want
n=int(input("How many random numbers do you want? "))

# set values for the modulus, multiplier and increment (all odd values for better results)
m = (2**31)-1
a = 2147483629
c = 2147483587

# open an array to store the (output) numbers
box = [0]*n

# define a function that calculates the random numbers using a linear congruential generator
def lcg(contents, n, m, a, c):
    
    x=contents
    
    # store the (output) numbers in a string to use later when printing them out (easier to read than in printed arrays) 
    results=""

    # for loop to calcualte n values and store them in the array and string(results)
    for i in range(n):
            value = ( ( x * a ) + c ) % m
            results += str(value) + " "
            box[i] = value
            x = value
    print()
    print("LCG Results: \n"+results, "\n")    

# E X T R A S
    # extra feature 1    
    # calculating some statistical data to verify the randomness of the data
    
    # calculating the average (mean)
    mean= int(numpy.mean(box))
    
    # calculating how spread out the numbers are
    standard_deviation= int(numpy.std(box))
    
    # calculating the average of the squared differences from the mean
    variance= int(numpy.var(box))

    time.sleep(1)
    
    print(*'*Extra Features:*')
    print("============================= \n")
    print("1. Statistics: \n","Mean:", mean, "\n Standard deviation:", standard_deviation, "\n Variance:", variance)
    return box

# calling the function with the seed(txt file content), n (number of expected output values), m (modulus), a (multiplier), and c (increment)
answer = lcg(contents, n, m, a, c)

time.sleep(1)
# extra feature 2
# applying an application of true random number generators: email verification codes

print("\n2. Real-life application - Email verification codes:  ")

# define a function that calculates a verification code amd sends a verification email to user
def emailFun():
    
    # verification code will me the median
    # calculate the median(middle_value) in case of even or odd n
    global answer
    if n%2!= 0:
        middle_value = answer[int( n/2 )]
        
    else:
        middle_value = int((answer[int( n/2 )]+answer[int( n/2 )-1 ]) /2 )
        
    global verification_code
    # calling the median verification code for ease of understanding
    verification_code = middle_value

    # assigning the email sender and reciever(s)
    
    # sender's credentials
    gmail_user = "assignment.randomcode@gmail.com"
    gmail_password = "Nour.Sharaky.1"
    
    # ask user to enter a valid gmail address
    gmail = input(" Please enter a valid gmail address to recieve your verification code: ")

    # organising the mail content
    sent_from = gmail_user
    to = [gmail]
    subject = "Nour Sharaky - Email verification code"
    body = 'Your verification code is: '+ str(verification_code)

    email_text = "From: "+sent_from+"\nTo:,"+str(to)+"\nSubject:"+subject+"\n\n"+body
    
    # to check whether the gmail address input was valid or not
    try:
        # establish SMTP connection using smtp.gmail.com as server and 587 as port number
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        # identify client
        mail.ehlo()
        # start transport layer security to encode the message
        mail.starttls()
        # log in using sender's credentials
        mail.login(gmail_user, gmail_password)
        # send the mail
        mail.sendmail(sent_from, to, email_text)
        mail.close()
        print()
        print (" Email sent! :) \n") 
        verify()
     
    except:
        # invalid gmail input response
        print()
        print (" Something went wrong...Please try again :( \n")
        emailFun()
    finally:
        print()

# final surprise output
def verify() :
    code = int(input(" Enter the verification number to unlock surprise: "))    
    if code == verification_code:
        print("""                                              _   _
               _______________                        |*\_/*|________
              |  ___________  |     .-.     .-.      ||_/-\_|______  |
              | |           | |    .****. .****.     | |           | |
              | |   0   0   | |    .*****.*****.     | |   0   0   | |
              | |     -     | |     .*********.      | |     -     | |
              | |   \___/   | |      .*******.       | |   \___/   | |
              | |___     ___| |       .*****.        | |___________| |
              |_____|\_/|_____|        .***.         |_______________|
                _|__|/ \|_|_.............*.............._|________|_
    
    
                                                          _   _
                _______________                          |*\_/*|________
               |  ___________  |                        ||_/-\_|______  |
               | |           | |                        | |           | |
               | |   0   0   | |                        | |   0   0   | |
               | |     -     | |       /~`~\/~`~\.      | |     -     | |
               | |   \___/   | |      (  Thank   )      | |   \___/   | |
               | |___     ___| |      `\   You  /       | |___________| |
               |_____|\_/|_____|        `\    /'        |_______________|
                 _|__|/ \|_|_.............`\/'............._|________|_
        """)
    else:
        print("""
             .-'''''''-.
           .'           '.
          /   O      O   \
         :                :   incorrect....try again
         |                |      
         :    .------.    :
          \  '        '  /
           '.          .'
             '-......-'""")


        verify()
            

emailFun()



