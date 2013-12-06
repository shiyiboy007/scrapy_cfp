scrapy_cfp
==========
-This project is a test project aiming at learning to develope useful datamining tools with "scrapy".

-The purpose is collecting "Call for papers" information of upcoming security conferences.

-The developement environement is python2.7 along with some useful tools such as virtualenv, pip, ipython and vim.

#P.S
-Activate syntax coloring in vim:
==> echo "syntax on" >> $HOME/.vimrc
-Install Ipython in virtualenv used so that scrapy shell will use it instead:
==> pip install ipython

#Libraries used
-Scrapy-mongodb : https://github.com/sebdah/scrapy-mongodb
-This module is included in cfp directory; setting.py under the project is modified consequently

#Data organisation
Item/Document is organised like this: 
==> "url":xxx
==> "event_name":xxx (!index) 
==> "detail": xxxxxxxxxxx (the description in detail)
==> "when": xxxx
==> "where": xxxx
==> "sub_dline": xxxx
==> "notif_due":xxx
==> "final_due":xx  
