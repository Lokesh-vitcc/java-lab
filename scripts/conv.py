import sys

className = sys.argv[1]
code = open("Main.java").read().replace("Main",className)
fileName ="JAVA/"+ className+".java"
with open(fileName,"w") as f:
    f.write(code)