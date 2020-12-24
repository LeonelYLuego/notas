# Buttons

## RaisedButton

~~~dart
String _value;

_onPressed(value) {
    setState((){
        _value = value;
    })
}

Text($_value),
RaisedButton(
	onPressed: () => _onPressed('Hello World'),
    child: Text('Click me'),
),
~~~

## FlatButton

~~~dart
String _value;

_onPressed() {
    setState(() {
       _value = DateTime.now().toString(); 
    });
}

Text($_value),
FlatButton(
	onPressed: _onPressed,
    child: Text('Click me'),
),
~~~

## IconButton

~~~dart
int _value;

_onPressed() {
    setState(() {
        _value++;
    });
}

Text($_value),
IconButton(
	icon: Icon(Icons.add),
    onPressed: _onPressed,
),
~~~

