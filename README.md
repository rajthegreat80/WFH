# WFH
A fun script for Jugaad

This Script is for those lazy people who are lazy enough to not even send a "Work from Home" mail.

Set the  mail id of your manager in manager.txt
Set the mail id of your peers in peer.txt(each email_id in seperate line)

Be sure that you have installed these python library:-

  *apiclient(google)
  
  *oauth2client
  
  *email
  
  *mimetypes

Goto your google api:- 
  *Create project
  *Get the application name and set it in wfh.py
  *Download json file for credentials and rename it as client_secret.json and put it in directory.

Finally ,
  TO SEND WFH TO BOTH MANAGER and PEERS
          python wfh.py
  TO SEND WFH TO MANAGER ONLY
          python wfh.py manager
  TO SEND WFH TO PEERS ONLY
          python wfh.py peer
