import time
class SMS_store:
    def __init__(self):
        self.mailbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS, has_been_viewed = False):
        massage_info = (has_been_viewed, from_number, time_arrived, text_of_SMS)
        self.mailbox.append(massage_info)
        print(self.mailbox)
        

    def mail_count(self):
        return "{0} messages in your mailbox".format(len(self.mailbox))

    def get_unread_indexes(self):
        unread = []
        for index, message in enumerate(self.mailbox):
            if False in message:
                unread.append(index)
        return "Unread mail in:", unread

    def get_message(self, index):
        message = list(self.mailbox[index])
        message[0] = True
        self.mailbox[index] = tuple(message)
        return message[1:]

    def delete(self, index):
        del self.mailbox[index]
        return "Delete mail", index

    def clear(self):
        self.mailbox = []
        return "clear mailbox"

my_inbox = SMS_store() #instantiate an object 'store' for class
my_inbox.add_new_arrival("01055553333", time.ctime(), "Hello its me") #instance of store object
my_inbox.add_new_arrival("01033345523", time.ctime(), "Nice to meet you")
my_inbox.get_message(1)
my_inbox.mail_count()
my_inbox.get_unread_indexes()
my_inbox.delete(1)

