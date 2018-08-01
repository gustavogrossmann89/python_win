from firebase import firebase

firebase = firebase.FirebaseApplication("https://iotsmartlockgg.firebaseio.com/", None)
print firebase.get("/nodes/g2-esc/", None)