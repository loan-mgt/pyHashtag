# pyHashtag 
<img src="https://developer.fedoraproject.org/static/logo/python.png" style="height:200px;float:left;">




## About
pyHashtag is a python lib made to insert hashtag into text. This lib was made originaly for [Twitter](twitter.com), but hashtag are fairly universal.

Here is a small exemple of what it does:

		Clearest Shot of Mars ever taken from space.
    
		to
    
		Clearest Shot of #Mars ever taken from #Space.

## Install
Installing this python lib is as simple as runing this command in your terminal :

`pip install git+https://github.com/Qypol342/Hashtag-lib.git`

If you want to verify the install way succesfull you can do :

`pip show pyHashtag`

## Help

Your help is welcome, you can help us to enlarge our database of usefull hashtag.

Here is the structure of the database:

`"<word to be replace>" : "#<the Hashtag>",`

:warning: The word detection is not case sensitive

Here is a exemple of a line of the database

`"nasa" : "#NASA",`

You can edit de database [here](https://github.com/Qypol342/pyHashtag/edit/main/pyHashtag/hashtag_list.json) 


