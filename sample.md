---
title: 'Weather Report'
place: "Paris"
wind: 33
humidity: 0.5
...

## {{title}}

* The temperature in {{ place | upper }}
  was {{temperature|default('Unknown')}} degrees.
* The humidity was {{humidity|float * 100 }} %
* The wind speed was {{wind |default(0)}} km/h

