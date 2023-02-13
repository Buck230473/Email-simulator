# Compulsary task

class Email(object):
    # class variables
    user_email = "user@gmail.com"
    has_been_read = False
    box_type = "inbox"

    # Constructor method initialising email_index, has_been_read, email_contents, from_address, to_address, subject, box_type
    def __init__(self, email_index, has_been_read, email_contents, from_address, to_address, subject, box_type):
        self.has_been_read = has_been_read
        self.email_contents = email_contents
        self.from_address = from_address
        self.to_address = to_address
        self.subject = subject
        self.box_type = box_type
        self.email_index = email_index
    
    # method to set the Email object to READ
    def mark_as_read(self):
        self.has_been_read = True

    # method to mark the Email object as spam and display message to user
    def mark_as_spam(self):
        self.box_type = "spam"
        print("Successfully marked as Spam\n")

# initialising the inbox and sent lists
inbox = []
sent = []

# Main menu
def menu1():
    user_choice = ""

    while user_choice != "quit":
        user_choice = input("\nWhere would you like to go? - inbox/sent/spam/send email/quit?\n")
        if user_choice == "inbox":
            get_inbox()
        elif user_choice == "sent":
            get_sent_emails()
        elif user_choice == "spam":
            get_spam_emails()
        elif user_choice == "send email":
            send_email()
        elif user_choice == "quit":
            exit()
        else:
            print("Oops - incorrect input")

# sub menu
def menu2(folder):
    user_choice = ""
    while user_choice != "quit":
        # display menu to user based on which folder they are in
        if folder == "inbox":
            msg = "\nWhat would you like to do? - read/mark spam/delete/back/quit?\n"
        else:
            msg = "\nWhat would you like to do? - read/delete/back/quit?\n"
        user_choice = input(msg)

        # if the user selects read or delete then pass through which folder they are working in (inbox, spam, sent)
        if user_choice == "read":
            get_email(folder)
        elif user_choice == "mark spam":
            set_spam()
        elif user_choice == "delete":
            delete(folder)
        elif user_choice == "back":
            menu1()
        elif user_choice == "quit":
            exit()
        else:
            print("Oops - incorrect input")

# add some sample emails into the inbox for testing purposes
def add_emails():
    email1 = Email(len(inbox)+1, Email.has_been_read, "Some Sample Content1", "from1@gmail.com", Email.user_email, "Subject1", Email.box_type)
    inbox.append(email1)
    email2 = Email(len(inbox)+1, Email.has_been_read, "Some Sample Content2", "from2@gmail.com", Email.user_email, "Subject2", Email.box_type)
    inbox.append(email2)
    email3 = Email(len(inbox)+1, Email.has_been_read, "Some Sample Content3", "from3@gmail.com", Email.user_email, "Subject3", Email.box_type)
    inbox.append(email3)
    email4 = Email(len(inbox)+1, Email.has_been_read, "Some Sample Content4", "from4@gmail.com", Email.user_email, "Subject4", Email.box_type)
    inbox.append(email4)

# count how many emails in the corresponding folder
def get_count(folder):
    if folder == "inbox":
        total_emails = str((len(inbox)))
    if folder == "sent":
        total_emails = str((len(sent)))
    if folder == "spam":
        count = 0
        for email in inbox:
            if email.box_type == "spam":
                count +=1
        total_emails = str(count)
    return(total_emails)

# display an email to be read by the user
def get_email(folder):
    while True:
        # make sure there are emails in that folder and if not display message to user
        if int(get_count(folder)) > 0:     
            try:
                # get the email number from the user and store in email_index
                email_index = (int(input("Please enter an email number to return the email contents\n")))
            except ValueError:
                print("Please enter a valid number!") 
                break
        else:
            print("There are no emails to read")
            menu1()

        # make sure we are dealing with inbox or spam
        if folder == "inbox" or folder == "spam":
            # loop through the emails in the inbox list
            for count, email in enumerate(inbox, 0):
                if folder == "inbox":
                    # compare the email_index of the email object being looped through to the email_index give by the user
                    # if they match then display the from_address and the email_contents of the Email object.
                    # active the mark_as_read function and return to menu1
                    if email.email_index == email_index and email.box_type == "inbox":
                        print(inbox[count].from_address + "\n" + inbox[count].email_contents)
                        inbox[count].mark_as_read()
                        menu1()

                if folder == "spam":
                    # compare the email_index of the email object being looped through to the email_index give by the user
                    # if they match then display the from_address and the email_contents of the Email object.
                    # active the mark_as_read function and return to menu1                    
                    if email.email_index == email_index and email.box_type == "spam":
                        print(inbox[count].from_address + "\n" + inbox[count].email_contents)
                        inbox[count].mark_as_read()
                        menu1()

        # make sure we are dealing with sent folder
        if folder == "sent":
            # loop through the emails in the sent list
            for count, email in enumerate(sent, 0):
                # compare the email_index of the email object being looped through to the email_index give by the user
                # if they match then display the from_address and the email_contents of the Email object.
                # active the mark_as_read function and return to menu1                
                if email.email_index == email_index:
                    print(sent[count].to_address + "\n" + sent[count].email_contents)
                    menu1()

# mark the email as spam
def set_spam():
    while True:
        # Ask user which number email he wants to mark as spam and save to email_index
        email_index = (int(input("Please enter an index number of the email you wish to mark as spam\n")))

        # loop through the inbox
        # call the mark_as_spam method when the email_index matches the email_index of the email object
        for count, email in enumerate(inbox, 0):
            if email.email_index == email_index:
                try:
                    inbox[count].mark_as_spam()
                    menu1()
                    break
                except IndexError:
                    print("Incorrect input - Try again")
                except ValueError:
                    print("Incorrect input - Try again")            

# display emails in the inbox
def get_inbox():
    # tells user if there are no messages
    if get_count("inbox") == 0:
        print("No emails to read")
        menu1()
    else:
        # display a message depending on if there are 1 message or multiple messages
        if get_count("inbox") == "1":
            print("INBOX - you have " + get_count("inbox") + " email")
        else:
            print("INBOX - you have " + get_count("inbox") + " emails") 
        # display headings   
        print("EMAIL NUMBER\t\tFROM\t\t\t\tSUBJECT\t\t\tREAD/UNREAD")
        # loop through inbox and display UNREAD messages at the top and READ messages underneath
        for email in inbox:
            if email.box_type == "inbox" and email.has_been_read == False:
                print(str(email.email_index) + "\t\t\t" + email.from_address + "\t\t\t" + email.subject + "\t\tUNREAD")
        for email in inbox:
            if email.box_type == "inbox" and email.has_been_read == True:
                print(str(email.email_index) + "\t\t\t" + email.from_address + "\t\t\t" + email.subject + "\t\tREAD")
        print()
        # call the sub-menu passing in the folder type
        menu2("inbox")

# display emails in the spam folder
def get_spam_emails():
    # headings
    print("\nSPAM")
    print("EMAIL NUMBER\t\tFROM\t\t\tSUBJECT\t\t\tREAD/UNREAD")
    # loop through inbox and display all the spam emails
    for email in inbox:
        if email.box_type == "spam" and email.has_been_read == False:
            print(str(email.email_index) + "\t\t\t" + email.from_address + "\t\t" + email.subject + "\t\tUNREAD")
    for email in inbox:
        if email.box_type == "spam" and email.has_been_read == True:
            print(str(email.email_index) + "\t\t\t" + email.from_address + "\t\t" + email.subject + "\t\tREAD")    
    print()
    # call the sub-menu passing in the folder type    
    menu2("spam")

# display all the sent emails
def get_sent_emails():
    print()
    # display a message to user based on how many emails there are.
    if get_count("sent") == "1":
        print("SENT - you have " + get_count("sent") + " email")
    else:
        print("SENT - you have " + get_count("sent") + " emails")
    # display headings
    print("EMAIL NUMBER\tFROM\t\t\tTO\t\t\t\tSUBJECT")
    # loop through the emails in the sent list and display the sent emails
    for email in sent:
        if email.box_type == "sent":
            print(str(email.email_index) + "\t\t" + email.from_address + "\t\t" + email.to_address + "\t" + email.subject)
    # call sub-menu passing through the folder type
    menu2("sent")

# send an email
def send_email():
    # get the email address, subject and content from user and store in variables and add to the sent list
    to = input("\nPlease enter the email address you wish to send to\n")
    subject = input("\nPlease enter the subject here\n")
    content = input("\nPlease type email content here\n")
    sent.append(Email(len(sent)+1, Email.has_been_read, content, Email.user_email, to, subject, "sent"))
    print("\nEmail sent!")
    menu1()

# delete an email
def delete(folder):
    while True:
        # make sure there are emails to be deleted, otherwise display message to tell user there are no emails to delete
        if int(get_count(folder)) > 0:
            try:
                # ask the user for the email number they wish to delete and store the answer in del_select
                del_select = int(input("which number email would you like to delete?\n"))
            except ValueError:
                print("\nPlease enter a valid number")
                continue
        else:
            print("There are no emails to delete")
            menu1()
        
        # check the folder type
        if folder == "inbox" or folder == "spam":
            # loop through the emails in the inbox list
            for count, email in enumerate(inbox, 0):
                # check the inbox folder
                if folder == "inbox":
                    # check to see if the user input (del_select) matches the email_index of the email object and the box_type is also set to inbox
                    if del_select == email.email_index and email.box_type == "inbox":
                        try:
                            # delete the corresponding email from the inbox and display success message or error message
                            del inbox[count]
                            print("Email has been successfully deleted!")
                            menu1()
                        except IndexError:
                            print("Incorrect Input - please try again") 
                        except ValueError:
                            print("Incorrect Input - please try again")
                
                # check the spam folder
                if folder == "spam":
                    # check to see if the user input (del_select) matches the email_index of the email object and the box_type is also set to spam                
                    if del_select == email.email_index and email.box_type == "spam":
                        try:
                            # delete the corresponding email from the inbox and display success message or error message
                            del inbox[count]
                            print("Email has been successfully deleted!")
                            menu1()
                        except IndexError:
                            print("Incorrect Input - please try again") 
                        except ValueError:
                            print("Incorrect Input - please try again")

        # check the sent folder
        else:
            # loop through the emails in the sent list
            for count, email in enumerate(sent, 0):
                # check to see if the user input (del_select) matches the email_index of the email object
                if email.email_index == del_select:
                    try:
                        # delete the corresponding email from the inbox and display success message or error message
                        del sent[count]
                        print("Email has been successfully deleted!")
                        menu1()
                        break
                    except IndexError:
                        print("Incorrect Input - please try again") 
                    except ValueError:
                        print("Incorrect Input - please try again")

# populate the inbox with some test emails
add_emails()

# go to main menu to start
menu1()