import dbus, dbus.glib, dbus.decorators, gobject 
bus = dbus.SessionBus() 
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject") 
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface") 

account_name = "grotiiy@jabber.org" # Must already be logged on.
account_protocol = 'prpl-jabber' # List of protocols: http://developer.pidgin.im/wiki/prpl_id
message_to_send = "test" # Change this with your spam

account = purple.PurpleAccountsFind(account_name, account_protocol) # Get the account information

buddylist = purple.PurpleFindBuddies(account,'') # Get a list of all buddies


for buddy in buddylist: # Sending a message to all buddy list
    if purple.PurpleBuddyIsOnline(buddy): 
        message_to = purple.PurpleBuddyGetName(buddy) # Message receiver
        conversation = purple.PurpleConversationNew(1, account, message_to) # Create a new conversation with the receiver
        purple.PurpleConvImSend(purple.PurpleConvIm(conversation), message_to_send) # Send the message to that conversation

