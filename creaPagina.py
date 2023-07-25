t1 = '''
 <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>

<style>
body {
    font: normal 20px Verdana, Arial, sans-serif;
}
</style>

</head>
<body>
'''

t2= '''
<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
'''

fi = open('p1.txt', 'r')
t2 = fi.read()

t3= '''
</body>
</html> 
'''

fo = open('pagina1.html', 'w')

fo.write(t1)
fo.write(t2)
fo.write(t3)

fo.close()


