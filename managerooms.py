import MySQLdb
import sys
import getpass
try:
    if len(sys.argv) == 2:
        credits_user = sys.argv[1]
        credits_psw = getpass.getpass("Enter password:")
        conn = MySQLdb.connect(host="localhost",
                               user=credits_user,
                               passwd=credits_psw,
                               db="digitallogbook")
        c = conn.cursor()
        while True:
            choice = int(raw_input("-------------------------\nklef log book\n-------------------------\n1.Create New Room\n2.Delete Room\n3.Show all Room\n4.Exit\nplease choose an option:"))
            if choice > 0 and choice < 5:
                if choice == 1:
                    room = raw_input("Enter the Room number:")
                    c.execute("SELECT * FROM rooms where room='{}'".format(room))
                    if len(c.fetchall()) < 1:
                        c.execute("INSERT INTO rooms(room) VALUES('{}')".format(room))
                        c.execute("CREATE TABLE {}(userId INT NOT NULL,purpose VARCHAR(30),equipmentid VARCHAR(20),datecol date NOT NULL,intime time NOT NULL,outtime time)".format(room))
                    else:
                        print "The Room number is already existed"
                elif choice == 2:
                    room = raw_input("Enter the Room number you want to delete:")
                    c.execute("SELECT room FROM rooms where room='{}'".format(room))
                    if len(c.fetchall()) > 0:
                        c.execute("DELETE FROM rooms where room='{}'".format(room))
                        c.execute("DROP TABLE {}".format(room))
                    else:
                        print "Room number not existed"
                elif choice == 3:
                    c.execute("SELECT room FROM rooms")
                    print "----------------------\nRooms\n----------------------\n"
                    for row in c.fetchall():
                        print row[0]
                else:
                    break
            else:
                print "please choose a valid option"
        conn.commit()
        c.close()
        conn.close()
    else:
        print "USAGE: python manageusers.py [sqlusername]"
except Exception as e:
    print e
