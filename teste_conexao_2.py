from speedtest import Speedtest
st = Speedtest()
mb = 10**-6
print(f"Velocidade de Download: {st.download()*mb} MB")
print(f"Velocidade de Upload: {st.upload()*mb} MB")