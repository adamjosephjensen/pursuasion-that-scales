# Persuasion that Scales

This project matters because good ideas don't have enough proponents.

## About

Talking to one person face-to-face is an inefficient way for good ideas to spread.  It doesn't scale.

This project exists to test the hypothesis: some individuals will be persuaded to change their minds as a result of interacting with a chatbot.

## Setup For Humans

This project requires:

* python3 and pip3
* slackclient

Most installations of python3 include pip3.

### Humans on Mac

```
brew install python3
pip3 install slackclient
```

### Humans Ubuntu/Debian

```
sudo apt-get install -y python3
pip3 install slackclient
```

### Bonus

In order to push without entering your password, upload an ssh key to github and make sure that your origin url is set to the ssh version using:

`git remote set-url origin git@github.com:<Username>/<Project>.git`

## Setup for Virtual Machines

Make sure the container has an ssh key recognized by github!

```
sudo apt-get install -y git
sudo apt-get install -y python3
sudo pip3 install slackclient
```

```
git clone git@github.com:toothlessdragon/pursuasion-that-scales.git
nohup python3 bot.py &
```
### todo
* Figure out how to keep the bot alive overnight.  It seems to not survive two days.
