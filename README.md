# ascii-decoder
Attackers often utilize ASCII code conversions to obfuscate payloads. This is a quick (and imperfect) script that uses Python's `re` library to pull out ASCII code from a payload (such as a WAF alert) and convert it to human readable form. 

## Examples
**Payload:** `id=' UNION SELECT CHAR(45,120,49,45,81,45)--`  
**Output:** `-x1-Q-`  

**Payload:** `"><script >alert(String.fromCharCode(88,83,83))</script>`  
**Output:** `XSS`
