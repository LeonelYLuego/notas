# Agregar y buscar

`db.<Colección>.insert({})` Inserta un documento en la colección (si la colección no existe la crea) 

`db.<Colección>.find()` Regresa todos los documentos de la colección 

`db.<Colección>.find().pretty()` Regresa todos los documentos de la colección bonitos 

`db.<Colección>.insert([{}, {}])` Inserta varios documentos 

`db.products.find({name:"mouse"})` Ejemplo de buscar un sólo producto 

`db.products.find({"tags":"computers", "name":"monitor"}).pretty()` Ejemplo de buscar con varios atributos 

`db.products.findOne({})` Devuelve el primer documento 

`db.products.findOne({"tags":"computers"}, {"name":1, "description":1, "_id":0})` Ejemplo de sólo mostrar unos atributos 

`db.products.find({"tags":"computers"}).sort({"name": 1}).pretty()` Ejemplo de ordenar los datos 

`db.products.find().limit(2)` Ejemplo de sólo mostrar unos cuantos datos 

`db.products.count()` Devuelve el número de documentos 

`db.products.find().forEach(product => print("Product Name: " + product.name))` Ejemplo `forEach` recorre todos los documentos uno por uno 