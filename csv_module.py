import csv

header = ['name','genre','instagram','inumber','twitter','tnumber','patreon','pnumber','money','youtube','ynumber']
data = ['asas','aef','HYPERLINK("https://www.patreon.com/neutralparty";"LINK")']
datadict = {'name' 		: '',
			'genre' 	: '',
			'instagram' : '',
			'inumber' 	: '',
			'twitter' 	: '',
			'tnumber' 	: '',
			'patreon' 	: '',
			'pnumber' 	: '',
			'money' 	: '',
			'youtube' 	: '',
			'ynumber' 	: ''}

with open('data.csv','w', encoding='UTF8') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerow(data)

	writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(datadict)