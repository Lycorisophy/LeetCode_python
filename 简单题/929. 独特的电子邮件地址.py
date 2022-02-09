def numUniqueEmails(emails: [str]) -> int:
    res = set()
    for email in emails:
        true_email = ''
        flag = 0
        for letter in email:
            if letter == '.':
                if flag == 2:
                    true_email += letter
            elif letter == '+':
                flag = 1
            elif letter == '@':
                flag = 2
                true_email += letter
            else:
                if flag != 1:
                    true_email += letter
        res.add(true_email)
    return res.__len__()


if __name__ == '__main__':
    print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

