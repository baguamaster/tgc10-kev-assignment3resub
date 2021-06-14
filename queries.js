show databases
use sample_airbnb
show collections
// display all docs from a collection
//db.<collection>.find()
db.listingsAndReviews.find().pretty()
//projecting
db.listingsAndReviews.find({},{
    name: 1,
    address: 1
}).pretty()