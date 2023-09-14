if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/kyojuro6engoku/chatgtp.git /chatgtp
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /chatgtp
fi
cd /chatgtp
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
