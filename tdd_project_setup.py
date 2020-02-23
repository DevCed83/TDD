import os
import subprocess
import sys
from ./project_manager import project_manager.ProjectManager
import unittest
# os.system(['powershell.exe', cd ..])
class ProjectManagerTest(unittest.TestCase):
	"""docstring for ProjectManagerTest"""
		
	def test_check_profile(self):
		# Trying to get the value of a shell command, we want to make sure it's available as a string. 
		cmd = ['powershell.exe', 'Test-Path $PROFILE']
		answer = subprocess.run(cmd, stdout = subprocess.PIPE).stdout.decode('utf-8')
		self.assertEqual(type(answer), str)

	def test_get_profile_path(self):
		manager = ProjectManager()
		manager.get_profile_path()
		self.assertTrue(manager.get_profile_path)

if __name__ == '__main__':
	unittest.main()

# # bashCommand = "Test-Path $Profile"
# # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# # output, error = process.communicate()