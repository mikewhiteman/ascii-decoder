# ascii-decoder
Threat actors often utilize ASCII code conversions to obfuscate attack payloads. This is a quick (and imperfect) script that uses Python's `re` library to pull out ASCII code from a payload (such as a WAF alert) and convert it to human readable form. 

## Example
**Payload:** `id=' UNION SELECT CHAR(45,120,49,45,81,45)--`  
**Output:** `-x1-Q-`
