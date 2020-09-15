#teste_conexao

#libraries
from speedtest import Speedtest
import schedule
import time

#declarations
st = Speedtest()
# resultado_1 = st.download()/1000000

def job():
    print('Velocidade de Download:',st.download()/1000000)
    print('Velocidade de Upload:',st.upload()/1000000)


#execution
schedule.every().minute.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)