import ftplib
import io
ftp_host = '167.114.216.155'
ftp_user = 'mine100bros@gmail.com.26374'
ftp_pass = 'kekrun-fefRu1'
server = ftplib.FTP()
server.connect(ftp_host, 21)
server.login(ftp_user, ftp_pass)
server.cwd("logs")

class ChatParser:

    def parse_msg(self, message):
        temp = message.split(" ")
        str = ""
        for x in range (3, len(temp)):
            if x != len(temp) - 1:
                str += temp[x] + " "
            elif x == len(temp) - 1:
                str += temp[x]
        return str

    def get_log(self):

        filename = 'latest.log'

        localfile = open(filename, 'wb')
        server.retrbinary('RETR ' + filename, localfile.write, 1024)
        localfile.close()

    def save(self, lines):
        chat_log = open("chat.log", "w+")
        for x in lines:
            chat_log.write(x)
    def parsed_log(self):
        f = open("latest.log", "r")
        tempLines = f.readlines()
        temp = []
        for x in tempLines:
            if "[Server thread/INFO]: <" in x:
                msg = self.parse_msg(x)
                temp.append(msg)
        return temp

    def read_log(self):
        log = self.parsed_log()
        prev_lines = open("chat.log", "r").readlines()
        msgSent = []
        for msg in range(len(log) - 16, len(log)):
            if msg < len(prev_lines):
                if log[msg] != prev_lines[msg]:
                    print (log[msg])
                    msgSent.append(log[msg])
            else:
                print (log[msg])
                msgSent.append(log[msg].rstrip("\n\r"))
        self.save(log)
        return msgSent
# Save last sent message to a file, something called chat_log
# Check if next message to send is equal to the one in chat_log
# if it is don't send
# otherwise do
# ok goodnight atom and goodnight python
