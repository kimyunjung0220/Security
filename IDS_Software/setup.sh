USER_NAME=$(whoami)

sudo apt install wireshark -y
sudo usermod -aG wireshark "$USER_NAME"
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo pip3 install pyshark
sudo pip3 install flask
