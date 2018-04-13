import csv
from tempfile import NamedTemporaryFile
import shutil


#This is a basic function for writing csv files
def write_file(option, account): #OPTIONS: 1 = UPDATE/CHANGE , 2 = ADD USER, 3 = DELETE USER
    tempfile = NamedTemporaryFile(mode ='w', delete=False, newline='')
    fields = ["account number", "name", "pin", "type", "cc#", "balance", "translog"]

    with open('account.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames= fields)
        writer = csv.DictWriter(tempfile, fieldnames= fields)
        for row in reader:
            if option == 1:
                if row['account number'] == account[0]:
                    row['account number'], row['name'],row['pin'],row['type'],row['cc#'],row['balance'],row['translog'] = account[0],account[1],account[2],account[3],account[4],account[5],account[6]
            row = {'account number': row['account number'], 'name': row['name'], 'pin': row['pin'],'type': row['type'],"cc#": row['cc#'],"balance": row['balance'], "translog": row['translog']}
            if option == 3 and row['account number'] == account[0]:
                continue
            else:
                writer.writerow(row)
        if option == 2:
            row['account number'], row['name'], row['pin'], row['type'], row['cc#'], row['balance'], row['translog'] = \
            account[0], account[1], account[2], account[3], account[4], account[5], account[6]
            row = {'account number': row['account number'], 'name': row['name'], 'pin': row['pin'], 'type': row['type'],
                   "cc#": row['cc#'], "balance": row['balance'], "translog": row['translog']}
            writer.writerow(row)
    shutil.move(tempfile.name, 'account.csv')


if __name__ == "__main__":
    write_file(1,['10004','Justin Salisi','1996', 'savings','12345678901234569','30000','10004.csv'])
    write_file(2, ['10005', 'Travis Chan', '1999', 'savings', '12345678901234570', '29000', '10005.csv'])
    write_file(3, ['10005', 'Travis Chan', '1999', 'savings', '12345678901234570', '29000', '10005.csv'])