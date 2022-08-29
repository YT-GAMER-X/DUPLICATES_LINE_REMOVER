 #!/usr/bin/python
# remove duplicates line in a text file
#TOOL MADE BY YT GAMER X
import os
os.system ("clear")
os.system("sleep 0.10")
print ("\033[1;92mTOOL\033[1;91m_\033[1;92mBY   <\033[1;91m=\033[1;92m> \033[1;92mYT\033[1;91m_\033[1;92mGAMER\033[1;91m_\033[1;92mX")
os.system("sleep 0.10")
print ("\033[1;92mYOU\033[1;91m_\033[1;92mTUBE  <\033[1;91m=\033[1;92m> \033[1;92m@YT\033[1;91m_\033[1;92mGAMER\033[1;91m_\033[1;92mX")
os.system("sleep 0.10")
print ("\033[1;92mGIT\033[1;91m_\033[1;92mHUB   <\033[1;91m=\033[1;92m> \033[1;92m@YT\033[1;91m_\033[1;92mGAMER\033[1;91m_\033[1;92mX")
os.system("sleep 0.10")
print ("\033[1;92mTELE\033[1;91m_\033[1;92mGRAM <\033[1;91m=\033[1;92m> \033[1;92m@YT\033[1;91m_\033[1;92mGAMER\033[1;91m_\033[1;92mX")
os.system("sleep 0.10")
print ("")
os.system("sleep 0.10")
YT_GAMER_X_INPUT=raw_input("\033[1;32;40mINPUT FILE PATH \033[1;36;40m=> \033[1;32;40m")
YT_GAMER_X_OUTPUT=raw_input("\033[1;32;40mOUTPUT FILE PATH \033[1;36;40m=> \033[1;32;40m")
if __name__ == "__main__":
	f = open(YT_GAMER_X_OUTPUT,"w+")
	flag = False
        print ""
        print "\033[1;36;40mPLEASE WAIT\033[1;31;40m. . .\033[1;36;40m FILE IN PROCESS\033[1;31;40m. . ."
        print ""
        os.system("sleep 3")
	with open(YT_GAMER_X_INPUT) as fp:
		for line in fp:
			for temp in f:
				if temp == line:
					flag = True
					print("\033[1;32;40mDUPLICATE_FOUND\033[1;31;40m...\033[1;32;40m!")
					break
			if flag == False:
				f.write(line)
			elif flag == True:
				flag = False
			f.seek(0)
		f.close()
print "\033[1;33;40mPROCESS COMPLETED\033[1;31;40m."
os.system("sleep 0.10")
print "\033[1;33;40mPROCESS COMPLETED\033[1;31;40m. ."
os.system("sleep 0.10")
print "\033[1;33;40mPROCESS COMPLETED\033[1;31;40m. . ."
os.system("sleep 0.10")
print "\033[1;33;40mPROCESS COMPLETED\033[1;31;40m. . . ."
os.system("sleep 0.10")
print "\033[1;33;40mPROCESS COMPLETED\033[1;31;40m. . . . ."
os.system("sleep 0.10")
print "\033[1;33;40mPROCESS COMPLETED\033[1;31;40m. . . . . ."
os.system("sleep 0.10")
print ""
