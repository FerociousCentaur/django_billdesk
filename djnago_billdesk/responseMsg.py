from .checksum import Checksum

class ResponseMessage:
    def findNthOccur(self, string, ch, N):
        occur = 0

        # Loop to find the Nth
        # occurence of the character
        for i in range(len(string)):
            if (string[i] == ch):
                occur += 1

            if (occur == N):
                return i

        return -1

    def get_mode(self, s):
        if s == '01':
            return 'Netbanking'
        elif s == '02':
            return 'Credit Card'
        elif s == '03':
            return 'Debit Card'
        elif s == '04':
            return 'Cash Card'
        elif s == '05':
            return 'Mobile Wallet'
        elif s == '06':
            return 'IMPS'
        elif s == '07':
            return 'Reward Points'
        elif s == '08':
            return 'Rupay'
        elif s == '09':
            return 'Others'
        elif s == '10':
            return 'UPI'

    def respMsg(self, response):
        response = response['msg'].strip('()')
        response = response.strip('\n')
        # print(response)
        valid_payment = Checksum().verify_checksum(response)
        if not valid_payment:
            return False
        pipeind1 = self.findNthOccur(response, '|', 1)
        pipeind2 = self.findNthOccur(response, '|', 2)
        pipeind3 = self.findNthOccur(response, '|', 3)
        pipeind4 = self.findNthOccur(response, '|', 4)
        pipeind5 = self.findNthOccur(response, '|', 5)
        pipeind7 = self.findNthOccur(response, '|', 7)
        pipeind8 = self.findNthOccur(response, '|', 8)
        pipeind9 = self.findNthOccur(response, '|', 9)
        pipeind10 = self.findNthOccur(response, '|', 10)
        pipeind12 = self.findNthOccur(response, '|', 13)
        pipeind13 = self.findNthOccur(response, '|', 14)
        pipeind14 = self.findNthOccur(response, '|', 15)
        mid = response[:pipeind1]
        oid = response[pipeind1 + 1:pipeind2]
        txnid = response[pipeind2 + 1:pipeind3]
        amnt = response[pipeind4 + 1:pipeind5]
        tstat = response[pipeind13 + 1:pipeind14]
        dnt = response[pipeind12 + 1:pipeind13]
        mode = response[pipeind7 + 1:pipeind8]
        mode = self.get_mode(mode)
        return {'MID': mid, 'OrderID': oid, 'TaxnNo': txnid, 'AMNT': amnt, 'TStat': tstat, 'DnT': dnt, 'TMode': mode}