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

//Agregar documentos
function add_user() {
    first_name = document.getElementById('first_name').value;
    last_name = document.getElementById('last_name').value;
    year = document.getElementById('year').value;
    db.collection("users").add({
        first: first_name,
        last: last_name,
        born: year
    }).then(function (docRef) {
        console.log("Document written with ID: ", docRef.id);
        document.getElementById('year').value = document.getElementById('last_name').value = document.getElementById('first_name').value = '';
    }).catch(function (error) {
        console.error("Error adding document: ", error);
    });
}

//Leer documentos
db.collection("users").onSnapshot((querySnapshot) => {
    document.getElementById('data').innerHTML = '';
    querySnapshot.forEach((doc) => {
        document.getElementById('data').innerHTML += `
        <tr>
        <th scope="row">${doc.id}</th>
        <th>${doc.data().first}</th>
        <th>${doc.data().last}</th>
        <th>${doc.data().born}</th>
        <th><button type="button" class="btn btn-warning" onclick="edit_user('${doc.id}','${doc.data().first}','${doc.data().last}','${doc.data().born}')">Editar</button></th>
        <th><button type="button" class="btn btn-danger" onclick="delete_user('${doc.id}')">Eliminar</button></th>
        </tr>`
    });
});

//Eliminar documentos
function delete_user(id){
    db.collection("users").doc(id).delete().then(function () {
        console.log("Document successfully deleted!");
    }).catch(function (error) {
        console.error("Error removing document: ", error);
    });
}

//Editar documentos
function edit_user(id, first_name, last_name, year){
    console.log(id, first_name)
    var userRef = db.collection("users").doc(id);

    document.getElementById('first_name').value = first_name;
    document.getElementById('last_name').value = last_name;
    document.getElementById('year').value = year;
    button = document.getElementById('btn_add');
    button.innerHTML = 'Editar';
    button.onclick = () => {
        first_name = document.getElementById('first_name').value;
        last_name = document.getElementById('last_name').value;
        year = document.getElementById('year').value;
        return userRef.update({
            first: first_name,
            last: last_name,
            born: year
        })
        .then(function() {
            console.log("Document successfully updated!");
        })
        .catch(function(error) {
            // The document probably doesn't exist.
            console.error("Error updating document: ", error);
        })
        .finally(() => {
            document.getElementById('year').value = document.getElementById('last_name').value = document.getElementById('first_name').value = '';
            button = document.getElementById('btn_add');
            button.onclick = add_user
            button.innerHTML = 'Agregar usuario';
        });
    }
}