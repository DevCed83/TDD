import os
import sys
import subprocess

class ProjectManager(object):
	"""docstring for ProjectManager"""
	def __init__(self):
		super(ProjectManager, self).__init__()
		
	def check_profile(self):
		cmd = ['powershell.exe', 'Test-Path $PROFILE']
		answer = subprocess.run(cmd, stdout = subprocess.PIPE).stdout.decode('utf-8')
		return answer

	# def get_profile_path(self):
	# 	pass

if __name__ == '__main__':
	manager = ProjectManager()
	print (manager.check_profile())
