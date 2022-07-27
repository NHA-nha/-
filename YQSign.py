from dgut_requests.dgut import dgutIllness


#  "is_in_school":0-是，松山湖校区 3-否，校外
# data = {"latest_acid_test": "2022-07-18", "is_in_school": "3"}
data = {"latest_acid_test": "2022-07-18"}
u = dgutIllness("201941412124", "NHA2019nha")
print(u.report(custom_data=data).get("message"))
# print(u.report(custom_data=data))
