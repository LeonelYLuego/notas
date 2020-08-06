firebase.initializeApp({
    apiKey: "AIzaSyApUO8l6IgXzn1z97SXHYXUrpq8RhhgBsk",
    authDomain: "aprendiendo-d1e03.firebaseapp.com",
    databaseURL: "https://aprendiendo-d1e03.firebaseio.com",
    projectId: "aprendiendo-d1e03",
    storageBucket: "aprendiendo-d1e03.appspot.com",
    messagingSenderId: "511055168754",
    appId: "1:511055168754:web:eaaae5a7d21073bfe6bc6b",
    measurementId: "G-RC61TL8B03"
});
var db = firebase.firestore();

function add_user(){
    first_name = document.getElementById('first_name').value;
    last_name = document.getElementById('last_name').value;
    year = document.getElementById('year').value;
    db.collection("users").add({
        first: first_name,
        last: last_name,
        born: year
    })
    .then(function(docRef) {
        console.log("Document written with ID: ", docRef.id);
    })
    .catch(function(error) {
        console.error("Error adding document: ", error);
    });
}