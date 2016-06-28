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

Goto your google api:- <br/>
  *Create project<br/>
  *Get the application name and set it in wfh.py<br/>
  *Download json file for credentials and rename it as client_secret.json and put it in directory.<br/>

Finally ,<br/>
  TO SEND WFH TO BOTH MANAGER and PEERS<br/>
          python wfh.py<br/>
  TO SEND WFH TO MANAGER ONLY<br/>
          python wfh.py manager<br/>
  TO SEND WFH TO PEERS ONLY<br/>
          python wfh.py peer<br/>
