#teste_conexao

#libraries
from speedtest import Speedtest
import schedule
import time

#declarations
st = Speedtest()

def job():
    print('Velocidade de Download:',st.download())
    print('Velocidade de Upload:',st.upload())


#execution
schedule.every().minute.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)