#teste_conexao

#libraries
from speedtest import Speedtest
import schedule
import time
from datetime import datetime

#declarations
st = Speedtest()
# resultado_1 = st.download()/1000000

def job():
    print('Velocidade de Download:',st.download()/1000000,datetime.now())
    print('Velocidade de Upload:',st.upload()/1000000,datetime.now())


#execution
schedule.every().minute.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)