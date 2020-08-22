# Editar y eliminar

`db.products.update({"name":"keyboard"}, {"price":99.99})` Ejemplo (busca los elementos a modificar, valores a modificar) modifica todo el documento y elimina todos los valores anteriores 

`db.products.update({"name":"laptop"}, {$set:{"description":"lg gram laptop"}})` Ejemplo modifica el documento 

`db.products.update({"name":"desktop"}, {$set:{"description":"Gaming Desktop"}}, {upsert:true})` Ejemplo modifica un documento y si no lo encuentra lo agrega 

`db.products.update({"name":"keyboard"}, {$inc:{"price":0.01}})` Ejemplo modifica un valor numérico de un documento incrementandolo 

`db.products.update({"name":"laptop"}, {$rename:{"name":"nombre"}})` Ejemplo modifica el identificador de un valor de un documento 

`db.products.remove({"nombre":"laptop"})` Ejemplo elimina el documento que coincida 

`db.products.remove({})` Ejemplo elimina todos los documentos

