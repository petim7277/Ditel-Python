def menu_functions():
    print("\n'Enter a number to start operation'\t")
    print("""
    1. Phone book
    2. Messages
    3. Chat
    4. Call Register
    5. Tones
    6. Settings
    7. Call Divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
          """)
    user_input = int(input("Enter a number: "))
    match user_input:
        case 1:
            print(phone_book())
        case 2:
            print(messages())
        case 3:
            print(chat())
        case 4:
            print(call_register())
        case 5:
            print(tones())
        case 6:
            settings()
        case 7:
            call_divert()
        case 8:
            games()
        case 9:
            calculator()
        case 10:
            reminders()
        case 11:
            clock()
        case 12:
            profiles()
        case 13:
            sim_services()
    return


def phone_book():
    print("""
    1. Search
    2. Service Nos. 1
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b’card
    8. Options
    9. Speed dials
    10. Voice tags
    
          """)
    user_input = int(input("Enter a number: "))
    if 0 < user_input < 2:
        print("Search")
    elif 7 < user_input <= 9:
        print("""
        1. Type of view
        2. Memory status
              """)
        print("Enter 0 to return to list of menu functions")
    if user_input == 0:
        menu_functions()

        return


def messages():
    print("""
     1. Write messages
     2. Inbox
     3. Outbox
     4. Picture messages
     5. Templates
     6. Smileys
     7. Message settings
     8. Info service
     9. Voice mailbox number
    10.Service command editor
          """)
    user_input = int(input("Enter a number:  "))
    if 6 < user_input < 8:
        print("""
         1.Set1
         1. Message centre number
         2. Messages sent as
         3. Message validity
              """)
        print("""
        2. Common 3
        1. Delivery reports
        2. Reply via same centre
        3. Character support   n
              """)
        print("Enter 0 to return to list of menu functions")
        if user_input == 0:
            menu_functions()
        return


def chat():
    print("Enter 0 to return to list of menu functions")
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        menu_functions()
    return


def call_register():
    print("""
    1. Missed calls
    2. Received calls
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call cost
    7. Call cost settings
    8. Prepaid credit
          """)
    user_input = int(input("Enter a number :"))
    if 4 < user_input < 6:
        print("""
        1. Last call duration
        2. All calls’ duration
        3. Received calls’ duration
        4. Dialled calls’ duration
        5. Clear timers
              """)
    elif 5 < user_input < 7:
        print("""
        1. Last call cost
        2. All calls’ cost
        3. Clear counters
              """)
    elif 6 < user_input < 8:
        print("""
        1. Call cost limit
        2. Show costs in
              """)
        print("Enter 0 to return to list of menu functions")
        if user_input == 0:
            menu_functions()
        return


def tones():
    pass


def settings():
    print("""
    1. Call settings
    2. Phone settings
    3. Security settings
    4. Restore factory settings
          """)
    user_input = int(input("Enter a number: "))
    if user_input == 1:
        print("""
        1. Automatic redial
        2. Speed dialling
        3. Call waiting options
        4. Own number sending
        5. Phone line in use
        6. Automatic answer 1
              """)
    elif user_input == 2:
        print("""
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Lights2
        6. Confirm SIM service actions
              """)
    elif user_input == 3:
        print("""
        1. PIN code request
        2. Call barring service
        3. Fixed dialling
        4. Closed user group
        5. Phone security
        6. Change access codes
             """)
        print("Enter 0 to return to list of menu functions")
        if user_input == 0:
            menu_functions()
    return


def call_divert():
    pass


def games():
    pass


def calculator():
    pass


def reminders():
    pass


def clock():
    print("""
    1. Alarm clock
    2. Clock settings
    3. Date setting
    4. Stopwatch
    5. Countdown timer
    6. Auto update of date and time
          """)
    user_input = int(input("Enter a number: "))
    print("Enter 0 to return to list of menu functions")
    if -1 < user_input < 1:
        menu_functions()
    return


def profiles():
    pass


def sim_services():
    pass


if __name__ == '__main__':
    menu_functions()
