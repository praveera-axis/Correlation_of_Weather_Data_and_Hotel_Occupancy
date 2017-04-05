from pymongo import MongoClient
import json
import datetime

client = MongoClient('localhost:27017')
db = client.axis_project

with open('data1.json') as in_f:
    data = json.loads(in_f.read())


for item in data:
        for i in range(len(item['stays'])):
                for j in range(len(item['stays'][i]['room_details'])):
                        stay_date = []
                        Check_in = item['stays'][i]['check_in']
                        Check_out = item['stays'][i]['check_out']
                        start = datetime.datetime.strptime(Check_in, "%Y-%m-%d")
                        end = datetime.datetime.strptime(Check_out, "%Y-%m-%d")
                        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
                        for date in date_generated:
                            stay_date.append(date.strftime("%Y-%m-%d"))
                        db.cochin.insert_one(
                                        {
                                        "Property_id": item['stays'][i]['property_id'],
                                        "Room_details": item['stays'][i]['room_details'][j]['id'],
                                        "Room_name": item['stays'][i]['room_details'][j]['name'],
                                        "Booking_date": item['booking_date'],
                                        "Check_in": item['stays'][i]['check_in'],
                                        "Check_out": item['stays'][i]['check_out'],
                                        "Room_rate": item['stays'][i]['room_details'][j]['pricing_detail']['room_rate'],
                                        "Stay_date": stay_date,
                                        "Channel": item['channel'],
                                        "Booking_status": item['stays'][i]['room_details'][j]['booking_status']
                                        })
                        
                        
                        
                            
        
