# Input Widgets

## TextField

~~~dart
String _value = '';

_onChanged(String value) {
	setState(() {
		_value = 'Change: $value';
	});
}

_onSubmitted(String value) {
	setState(() {
		_value = 'Submit: $value';
	});
}

Text('$_value'),
TextField(
	onChanged: _onChanged,
	onSubmitted: _onSubmitted,
	autocorrect: true,
	autofocus: true,
	//keyBoardType: TextInputType.number,
	keyBoardType: TextInputType.text,
	decoration: InputDecoration(
		labeltext: 'Name',
		hintText: 'Type your name',
		icon: Icon(Icons.people),
	),
),
~~~

## Checkbox

~~~dart
bool _value1 = false, _value2 = false;

_onChanged1(bool value) => setState(() => _value1 = value);
_onChanged2(bool value) => setState(() => _value2 = value);

Checkbox(
	value: _value1,
    onChanged: _onChanged1,
),
CheckboxListTile(
	value: _value2,
    onChanged: _onChanged2,
    title: Text('Title'),
    contronAffinity: ListTileControlAffinity.leading,
    subtitle: Text('Subtitle'),
    secondary: Icon(Icons.archive),
    activeColor: Colors.red,
),
~~~

## Radio

~~~dart
int _value1 = 0, _value2 = 0;

void _onChanged1(int value) => setState(() => _value1 = value);
void _onChanged2(int value) => setState(() => _value2 = value);

Witdget makeRadios(){
    List <Widget> list = List();
    
    for(int i = 0; i < 3; i++){
        list.add(Radio(
        	value: i,
            groupValue: _value1,
            onChanged: _onChanged1,
        ));
    }
    
    Column column = Column(children: list,);
    return column;
}

Widget makeRadiosTiles(){
    List <Widget> list = List();
    
    for(int i = 0; i < 3; i++){
        list.add(Radio(
        	value: i,
            groupValue: _value2,
            onChanged: _onCanged2,
            title: Text('${i + 1}'),
            activeColor: Colors.green,
            controlAffinity: ListTileControlAffinity.leading,
            subtitle: Text('subtitle'),
        ));
    }
    
    Column column = Column(children: list,);
    return column;
}

makeRadios(),
makeRadiosTiles(),
~~~

## Switch

~~~dart
bool _value1 = false, _value2 = false;

_onChanged1(bool value) => setState(() => _value1 = value);
_onChanged2(bool value) => setState(() => _value2 = value);

Switch(
	value: _value1,
    onChanged: _onChanged1,
),
SwitchListTile(
	value: _value2,
    onChanged: _onChanged2,
    title: Text(
    	'Switch',
        style: TextStyle(
        	fontWeight: FontWeight.bold,
            color: Colors.red,
        ),
    ),
    activeColor: Colors.amber,
    controlAffinity: ListTileControlAffinity.leading,
),
~~~

## Slider

~~~dart
double _value = 0.0;

_onChanged(double value) => setState(() => _value = value);

Text('${(_value * 100).round()}'),
Slider(
	value: _value,
    onChanged: _onChanged,
),
~~~

## DatePicker

~~~dart
#import 'dart/async';

String _value = '';

Future _selectDate() async {
    DateTime picked = await showDatePicker(
    	context: context,
        initialDate: DateTime.now(),
        firstDate: DateTime(2016),
        lastDate: DateTime(2050),
    );
    if(picked != null)
        setState(() => _value = picked.toString());
}

Text(_value),
RaisedButton(
	onPressed: _selectDate,
    child: Text('Click me')
),
~~~

