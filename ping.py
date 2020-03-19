import pythonping
from pythonping import ping
retrievedPing=ping('8.8.8.8')
print(1000*retrievedPing.rtt_avg)
