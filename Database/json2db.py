import sqlite3
import json
import unicodedata

######## CHANGE FILENAME, CREATETABLE, INSERTTABLE AND COUPON[IMAG], COUPON[FEATURE] FOR DIFFERENT JSON FILES #########

'''
traffic = json.load(open('xxx.json'))
db = sqlite3.connect("fluxos.sqlite")

query = "insert into medicoes values (?,?,?,?,?,?,?)"
columns = ['local', 'coord', 'sentido', 'veiculos', 'modalidade', 'pistas']
for timestamp, data in traffic.iteritems():
    keys = (timestamp,) + tuple(data[c] for c in columns)
    c = db.cursor()
    c.execute(query, keys)
    c.close()
'''
#tweet = json.load(open('example.json'))

# dealmoon
coupon_filename = 'newcouponModified.json'

# dealsea
coupon_filename1 = 'newcouponModified1.json'

# slickdeal
coupon_filename2 = 'newcouponModified2.json'


coupon_file = open(coupon_filename, "r")
coupon_file1 = open(coupon_filename1, "r")
coupon_file2 = open(coupon_filename2, "r")
'''
_data = []
with open('coupons.json') as f:
    for line in f:
        _data.append(json.load(line))

for line in _data:
    print line
'''
db = sqlite3.connect('deals.sqlite')
'''
with open('coupons.json', 'r') as json_data:
    traffic = json.load(json_data)
'''

#columns = ['item', 'link', 'description']

c = db.cursor()
try:
    # dealmoon
	#c.execute('''CREATE TABLE dealmoon(item varchar(200), image varchar(200), link varchar(200), description varchar(200), feature varchar(200))''')

    # dealsea
    #c.execute('''CREATE TABLE dealsea(item varchar(200), image varchar(200), link varchar(200), description varchar(200), feature varchar(200))''')

    # slickdeal
    c.execute('''CREATE TABLE slickdeal(item varchar(200), image varchar(200), link varchar(200), description varchar(300), feature varchar(200))''')
except:
	pass

try:
    # dealmoon
    #c.execute('''CREATE TABLE dealmoon(item varchar(200), image varchar(200), link varchar(200), description varchar(200), feature varchar(200))''')

    # dealsea
    c.execute('''CREATE TABLE dealsea(item varchar(200), image varchar(200), link varchar(200), description varchar(300), feature varchar(200))''')

    # slickdeal
    #c.execute('''CREATE TABLE slickdeal(item varchar(200), image varchar(200), link varchar(200), description varchar(200), feature varchar(200))''')
except:
    pass

try:
    # dealmoon
    c.execute('''CREATE TABLE dealmoon(item varchar(200), image varchar(200), link varchar(200), description varchar(300), feature varchar(200))''')

    # dealsea
    #c.execute('''CREATE TABLE dealsea(item varchar(200), image varchar(200), link varchar(200), description varchar(200), feature varchar(200))''')

    # slickdeal
    #c.execute('''CREATE TABLE slickdeal(item varchar(200), image varchar(200), link varchar(200), description varchar(200), feature varchar(200))''')
except:
    pass

def emptyTABLE(name):
	return "DELETE FROM " + str(name)

def deleteTABLE(name):
	return "DROP TABLE " + str(name)

def insertTABLE(name1, name2, name3, name4, name5):
	return "INSERT into dealmoon values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"
    #return "INSERT into dealsea values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"
    #return "INSERT into slickdeal values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"

def insertTABLE1(name1, name2, name3, name4, name5):
    #return "INSERT into dealmoon values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"
    return "INSERT into dealsea values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"
    #return "INSERT into slickdeal values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"

def insertTABLE2(name1, name2, name3, name4, name5):
    #return "INSERT into dealmoon values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"
    #return "INSERT into dealsea values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"
    return "INSERT into slickdeal values ('" + str(name1) + "','" + str(name2) + "','" + str(name3) + "','" + str(name4) + "','" + str(name5) + "')"

#query = "insert into coupon values (?,?,?)"
#columns = ['id', 'brand', 'couponcode']

#CREATE TABLE "coupon" ("timestamp" TEXT PRIMARY KEY  NOT NULL , "brand" TEXT, "couponcode" TEXT)

#someitem = tweet.itervalues().next()
#columns = list(someitem.keys())
'''
for data in traffic.iteritems():
    if 'item' in data:
        query = insertTABLE(data['item'], "null", "null")
        c.execute(query)
        db.commit()

'''
for line in coupon_file:
    try:
        # Read in one line of the file, convert it into a json object 
        coupon = json.loads(line.strip())
        if 'item' in coupon: # only messages contains 'text' field is a tweet
            temp1 = ""
            temp2 = ""
            temp3 = ""
            temp4 = ""
            temp5 = ""
            #print coupon['item']
            #print type(coupon['item'])
            for i in coupon['item']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp1 += (str(i) + " ")
            # for dealmoon and dealsea
            
            for i in coupon['imag']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp2 += str(i)
            

            # for slickdeal
            '''
            for i in coupon['imag']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                if str(i)[-9:] == "blank.gif":
                    pass
                else:
                    temp2 += str(i)
            '''
            for i in coupon['link']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp3 += str(i)
            for i in coupon['description']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp4 += str(i)
            # for dealmoon
            
            for i in coupon['feature']:
                if i != " | ":
                    if i[0:2] == ": ":
                        i = i[2:]
                        unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                        temp5 += str(i)
            

            # for dealsea and slickdeal
            #temp5 = ""

            
            query = insertTABLE(temp1, temp2, temp3, temp4, temp5)
            c.execute(query)
            db.commit()
            

            #query = insertTABLE("1", "null", "null")
        	#c.execute(query)
        	#db.commit()
        	#i += 1
        	#print query
        	#i = i+1
            #print tweet['id'] # This is the tweet's id
            #print tweet['created_at'] # when the tweet posted
            #print tweet['text'] # content of the tweet
            #print tweet['user']['id'] # id of the user who posted the tweet
            #print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
           # print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

            #hashtags = []
            #for hashtag in tweet['entities']['hashtags']:
            #    hashtags.append(hashtag['text'])
            #print hashtags
        
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue

for line in coupon_file1:
    try:
        # Read in one line of the file, convert it into a json object 
        coupon = json.loads(line.strip())
        if 'item' in coupon: # only messages contains 'text' field is a tweet
            temp1 = ""
            temp2 = ""
            temp3 = ""
            temp4 = ""
            temp5 = ""
            #print coupon['item']
            #print type(coupon['item'])
            for i in coupon['item']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp1 += (str(i) + " ")
            # for dealmoon and dealsea
            
            for i in coupon['imag']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp2 += str(i)
            

            # for slickdeal
            '''
            for i in coupon['imag']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                if str(i)[-9:] == "blank.gif":
                    pass
                else:
                    temp2 += str(i)
            '''
            for i in coupon['link']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp3 += str(i)
            for i in coupon['description']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp4 += str(i)
            # for dealmoon
            '''
            for i in coupon['feature']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp5 += str(i)
            '''

            # for dealsea and slickdeal
            temp5 = ""

            
            query = insertTABLE1(temp1, temp2, temp3, temp4, temp5)
            c.execute(query)
            db.commit()
            

            #query = insertTABLE("1", "null", "null")
            #c.execute(query)
            #db.commit()
            #i += 1
            #print query
            #i = i+1
            #print tweet['id'] # This is the tweet's id
            #print tweet['created_at'] # when the tweet posted
            #print tweet['text'] # content of the tweet
            #print tweet['user']['id'] # id of the user who posted the tweet
            #print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
           # print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

            #hashtags = []
            #for hashtag in tweet['entities']['hashtags']:
            #    hashtags.append(hashtag['text'])
            #print hashtags
        
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue

for line in coupon_file2:
    try:
        # Read in one line of the file, convert it into a json object 
        coupon = json.loads(line.strip())
        if 'item' in coupon: # only messages contains 'text' field is a tweet
            temp1 = ""
            temp2 = ""
            temp3 = ""
            temp4 = ""
            temp5 = ""
            #print coupon['item']
            #print type(coupon['item'])
            for i in coupon['item']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp1 += (str(i) + " ")
            # for dealmoon and dealsea
            '''
            for i in coupon['imag']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp2 += str(i)
            '''

            # for slickdeal
            for i in coupon['imag']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                if str(i)[-9:] == "blank.gif":
                    pass
                else:
                    temp2 += str(i)

            for i in coupon['link']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp3 += str(i)
            for i in coupon['description']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp4 += str(i)
            # for dealmoon
            '''
            for i in coupon['feature']:
                unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                temp5 += str(i)
            '''

            # for dealsea and slickdeal
            temp5 = ""

            
            query = insertTABLE2(temp1, temp2, temp3, temp4, temp5)
            c.execute(query)
            db.commit()
            

            #query = insertTABLE("1", "null", "null")
            #c.execute(query)
            #db.commit()
            #i += 1
            #print query
            #i = i+1
            #print tweet['id'] # This is the tweet's id
            #print tweet['created_at'] # when the tweet posted
            #print tweet['text'] # content of the tweet
            #print tweet['user']['id'] # id of the user who posted the tweet
            #print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
           # print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

            #hashtags = []
            #for hashtag in tweet['entities']['hashtags']:
            #    hashtags.append(hashtag['text'])
            #print hashtags
        
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
c.close()
db.close()

