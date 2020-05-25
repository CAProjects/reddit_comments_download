# reddit_comments_download
Python code to download all public available archives of reddit comments from https://files.pushshift.io/reddit/comments/

The Python code will do the following
- Loop though a json list i created myself
- check if the file exists 
- if it exists it will check the SHA of the file
  - if the hash does not match then it will re-download the file
  - if the hash does match then it will move to the next
  
To use, edit the variable `loc = 'F:\\LOCATION\\TO\\DOWNLOAD\\FILES\\TO\\'` to the location you want to download all the archives to including the double backslash at the end

If you do not want all the archives then edit rc_filelist.json to only contain the archives to download

After downloading, re-run just to make sure all files downloaded correctly and is complete
