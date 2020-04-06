# ascii-decoder
Attackers often utilize ASCII/Unicode code conversions to obfuscate payloads. This is a quick (and imperfect) script that uses Python's `re` library to pull out relevnat ASCII/Unicode values from a payload (such as a WAF alert) and convert it to human readable form. 

## Examples
**Payload:** `id=' UNION SELECT CHAR(45,120,49,45,81,45)--`  
**Output:** `-x1-Q-`  

**Payload:** `"><script >alert(String.fromCharCode(88,83,83))</script>`  
**Output:** `XSS`

## Usage
Run `python3 ascii_decoder.py` and supply the payload in the input prompt. Will convert this to a command line arg soon. 
