import pandas as pd
import requests
import json

braze_track = "https://rest.iad-05.braze.com/users/track"

track_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 6b019fd6-2373-45c7-bcb7-07ccd969dd8b"
}

df = pd.read_csv("default_address_upload_2.csv")
# print(df.values)

all_data = []
for x in range(len(df.values)):
    dic = json.loads(df.values[x][1])
    dic["external_id"] = df.values[x][0]
    all_data.append(dic)

# print(all_data)

# n = 0
# new_df = pd.DataFrame(columns=["external_id", "default_address"])
# for x in all_data[::]:
#     n += 1
#     track = {
#         "attributes":
#             [{
#                 "external_id": x["external_id"],
#                 "upload_segment": "default_address_upload_1",
#                 "default_address": {
#                     "country": x["country"] if "country" in x.keys() else "",
#                     "state": x["province"] if "province" in x.keys() else "",
#                     "city": x["city"] if "city" in x.keys() else "",
#                     "address_line1": x["address1"] if "address1" in x.keys() else "",
#                     "address_line2": x["address2"] if "address2" in x.keys() else "",
#                     "zip_code": x["zip"] if "zip" in x.keys() else ""
#                 }
#             }]
#     }


def get_value(dic, key):
    return dic[key] if key in dic.keys() else ""


n = 0
new_df = pd.DataFrame(columns=["external_id", "default_address"])
for x in all_data[::]:
    n += 1
    track = {
        "attributes":
            [{
                "external_id": x["external_id"],
                "upload_segment": "default_address_upload_2",
                "default_address": {
                    "country": get_value(x, "country"),
                    "state": get_value(x, "province"),
                    "city": get_value(x, "city"),
                    "address_line1": get_value(x, "address1"),
                    "address_line2": get_value(x, "address2"),
                    "zip_code": get_value(x, "zip")
                }
            }]
    }

    track_user = json.dumps(track)
    # print(f"Row {n}:", track_user)

    response = requests.post(url=braze_track, data=track_user, headers=track_headers)
    print(f"Row {n}: {x['external_id']} Response: ", response.json())

    # new_df.loc[len(new_df.index)] = [x["external_id"], address_data]

# print(new_df)
# new_df.to_csv("default_address_upload1.csv", index=False)

