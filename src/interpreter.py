# Run a .rusted file
import sys 
import rustedscript

with open(sys.argv[1]) as rustedfile: # open the rusted file
	print("    Running {}".format(sys.argv[1])+'...\n')
	lines = rustedfile.readlines()
	for line in lines:
		indexOfComment = int( line.find("//") )
		if indexOfComment == -1:
			indexOfComment = int( line.find("#") )
		if indexOfComment == -1:
			indexOfComment = int( line.find("/*") )
		if indexOfComment != -1:
			newline=line[0:indexOfComment-1]
		else:
			newline=line
		if newline:
			result, error = rustedscript.run('<stdin>', newline[0:len(line)-1])
			if error:
				print(error.as_string())
				print("\n---- \n FATAL: Process exited with non-zero exit code")
				sys.exit(1)
			elif result:
				print(result)
				print("\n---- \n SUCCESS: {} ran successfully".format(sys.argv[1]))
				sys.exit(0)



