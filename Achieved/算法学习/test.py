x = [ c.zfill(2) for c in str(3132165) if c < '5' ]
y = list(str(3132165))
z = { c:c.zfill(2) for c in str(3132165) if c < '5' }
print(x, ''.join(x))
print(y, ''.join(y))
print(z, "".join(z))
"".