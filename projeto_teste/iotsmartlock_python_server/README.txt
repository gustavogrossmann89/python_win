Para rodar o .py direto na inicializa��o do raspberry, basta:
-> Criar um shell script na pasta /home/pi/iotsmartlock_python_server/
-> Nome�-lo com o nome launcher.sh
-> Executando o comando: sudo crontab -e, adicionar a seguinte linha:
 @reboot /home/pi/iotsmartlock_python_server/launcher.sh > /var/log/iotsmartlockserver.log 2>&1

*** OBS: no launcher.sh, setamos um sleep de 30 segundos, para que o .py sempre rode ap�s o broker mqtt subir ***