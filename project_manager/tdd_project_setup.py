import os
import subprocess
import sys
import unittest
# os.system(['powershell.exe', cd ..])
class ProjectManagerTest(unittest.TestCase):
	"""docstring for ProjectManagerTest"""
		
	def test_check_profile(self):
		# Trying to get the value of a shell command, we want to make sure it's available as a string. 
		cmd = ['powershell.exe', 'Test-Path $PROFILE']
		answer = subprocess.run(cmd, stdout = subprocess.PIPE).stdout.decode('utf-8')
		self.assertEqual(type(answer), str)
		 # expect string
		#proc = subprocess.Popen(cmd, stdout=sys.stdout, shell = True)
		#print (value)

if __name__ == '__main__':
	unittest.main()

# # bashCommand = "Test-Path $Profile"
# # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# # output, error = process.communicate()