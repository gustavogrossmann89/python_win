from firebase import firebase

firebase = firebase.FirebaseApplication("https://iotsmartlockgg.firebaseio.com/", None)
print firebase.get("/nodes/g2-esc/", None)

new_log = "0000000001"

result = firebase.post("/logs/", new_log, {"print": "pretty"}, {"X_FANCY_HEADER": "VERY FANCY"})
print result