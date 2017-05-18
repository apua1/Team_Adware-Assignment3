import cmd
import datetime
from TwitterModule import TwitterModule

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class TwitterAnalyser(cmd.Cmd):
    timeZone = ""
    beginDate = ""
    lastDate = ""
    userId = ""

    def do_t(self,timezone):
        "t TIMEZONE (set analyse timezone)"
        if (len(timezone) == 6):
            if ((timezone[0] == '+') | (timezone[0] == '-')):
                hour = timezone[1: 2]
                min = timezone[4: ]
                if (((RepresentsInt(hour)) & (RepresentsInt(min)) & (timezone[3] == ":"))):
                    print (min)
                    if ((int(hour) <= 12) & ((int(min) == 30) | (int(min) == 0))):
                        self.timeZone = timezone
                        print ("Time zone had been set")
                    else:
                        print("Invalid time zone range")
                else:
                    print("Invalid time zone, please enter time zone in format +HH:MM or -HH:MM ")
            else:
                print("Invalid time zone, please enter time zone in format +HH:MM or -HH:MM ")
        else:
            print("Invalid time zone, please enter time zone in format +HH:MM or -HH:MM ")

    def do_a(self,date):
        "a DATE (set begin analyse date)"
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            self.beginDate = date
            print("Begin date had been set")
        except ValueError:
            print ("Invalid date, please enter date in format YYYY-MM-DD")

    def do_b(self, date):
        "b DATE (set analyse last date)"
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            self.lastDate = date
            print("Last date had been set")
        except ValueError:
            print ("Invalid date, please enter date in format YYYY-MM-DD")

    def do_i(self,id):
        "i ID (set user id to ID)"
        if (id[0] == "@"):
            self.userId = id
            print("User id had been set")
        else:
            print ("Invalid id")

    def do_g(self,line):
        "g (plot twitter graph)"
        if((self.timeZone != "") | (self.beginDate != "") | (self.lastDate != "")| (self.userId != "")):
            TwitterModule(timezone=self.timeZone, begindate= self.beginDate, lastdate= self.lastDate, id= self.userId)
        else:
            print("Error")


    def do_e(self,line):
        "e (exit program)"
        return True

if __name__ == '__main__':
    TwitterAnalyser().cmdloop()