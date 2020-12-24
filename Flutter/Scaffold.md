# Scaffold

## AppBar

~~~dart
int _value = 0;

void _add() => setState(() => _value++);
void _remove() => setState(() => _value--);

appBar: AppBar(
	title: Text('My First Application'),
    backgroundColor: Colors.deepPurple,
    actions: <Widget> [
        IconButton(
        	icon: Icon(Icons.add),
            onPressed: _add,
        ),
        IconButton(
        	icon: Icon(Icons.remove),
            onPressed: _remove
        ),
    ],
),
body: Container(
	padding: EdgeInsets.all(32.0),
    child: Text(_value),
),
~~~

## Floating Action Button

~~~dart
String _value = '';

void _onPressed() => setState(() => _value = DateTime.now().toString());

floatingActionButton: FloatingActionButton(
	onPressed: _onPressed,
    backgroundColor: Colors.red,
    mini: true,
    child: Icon(Icons.timer),
),
body: Container(
	padding: EdgeInsets.all(32.0),
    child: Text(_value),
),
~~~

## Drawer

~~~dart
drawer: Drawer(
	child: Container(
    	padding: EdgeInsets.all(32.0),
        child: Column(
        	children: <Widget> [
              Text('Hello Drawer'),
              RaisedButton(
              	onPressed: () => Navigator.pop(context),
                child: Text('Close'),
              ),
            ],
        ),
    ),
),
~~~

## Footer Buttons

~~~dart
String _value = '';

void _onPressed(String value) => setState(() => _value = value);

persistentFooterButtons: <Widget> [
    IconButton(
    	icon: Icon(Icons.timer),
        onPressed: () => _onPressed('Button 1'),
    ),
    IconButton(
    	icon: Icon(Icons.people),
        onPressed: () => _onPressed('Button 2'),
    ),
    IconButton(
    	icon: Icon(Icons.map),
        onPressed: () => _onPressed('Button 3'),
    ),
],
body: Container(
	padding: EdgeInsets.all(32.0),
    child: Text(_value),
),
~~~

## Bottom Navigation Bar

~~~dart
List <BottomNavigationBarItem> _items;
String _value = '';
int _index = 0;

@override
void initState(){
    _items = List();
    _items.add(BottomNavigationBarItem(
    	icon: Icon(Icons.people),
        label: 'People',
    ));
    _items.add(BottomNavigationBarItem(
    	icon: Icon(Icons.weekend),
        label: 'Weekend',
    ));
    _items.add(BottomNavigationBarItem(
    	icon: Icon(Icons.message),
        label: 'Message',
    ));
    super.initState();
}

bottomNavigationBar: BottomNavigationBar(
	items: _items,
    fixedColor: Colors.blue,
    currentIndex: _index,
    onTap: (int item) {
        setState(() {
           _index = item;
           _value = 'Current value is: ${_index.toString()}';
        });
    },
),
body: Container(
	padding: EdgeInsets.all(32.0),
    child: Text(_value),
),
~~~

