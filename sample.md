---
title: 'Weather Report'
place: "Paris"
wind: 33
...

## {{title}}

* The temperature in {{ place.upper() }}
  was {{temperature|default('0')}} degrees.
* The humidity was {{humidity|float * 100 }} %
* The wind speed was {{wind |default(0)}} km/h

## It works in code blocks too !


```bash
echo 'hello {{place}} !'
```
