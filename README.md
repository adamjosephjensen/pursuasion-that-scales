# Persuasion that Scales

This project matters because good ideas don't have enough proponents.

## About

Talking to one person face-to-face is an inefficient way for good ideas to spread.  It doesn't scale.

This project exists to test whether a bot can engage with a human and **achieve more accurate expectations about using oil and gas**.  Beginning a process that results in more accurate expectations eventually, (such as buying a book or joining a mailing list) will also be counted as a win.

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

## Talk to Anyone about Energy

Discussions are like games, they have goals and rules.

The rules always apply.  Both parties in a discussion are players and referees.

**Don't allow the rules to be broken**.  Use them to reinforce the right method as you explain your position.

A mindfulness: Focus on **method** rather than **content**.

### Rule 0: Discussions have a Goal

The goal is not:
* to look or feel smarter
* defend your starting position to the death

and is also not necessarily:
* to get the person to admit they are wrong
* to persuade the other person

The goal is for two people two get a better understanding of an important issue.

Put slightly differently, the goal is to **achieve accurate expectations for important future experiences**.  See [Making Beliefs Pay Rent (in Anticipate Experiences)](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiL5vb0htTOAhUW0mMKHaGyB7AQFggeMAA&url=http%3A%2F%2Flesswrong.com%2Flw%2Fi3%2Fmaking_beliefs_pay_rent_in_anticipated_experiences%2F&usg=AFQjCNEThJZR-QBNODFKFpaqlOQplmJN9g)

After a discussion, you may have new information and/or have helped & influenced someone by giving them information.

### Rule 1: Be clear on the issue / question

What question are we trying to answer?

**Rule 1.1: No 'answers' until the question is clear to both people**.

Snappy responses before re-stating the question and getting agreement are a violation of etiquette.

**Rule 1.2: One question at a time**

You don't help other people or yourself by jumping from question to question.  Be careful of rising to bait or following tangents.  Bonus: this prevents 'death by a thousand issues' or 'swarm attacks.'

Snippet: "Absolutely I am happy to talk about that, just so I'm clear you mentioned X, Y and Z (e.g. fracking or global warming)."

### Rule 2: Agree to think big picture

I: "Let's talk about groundwater."
A: "Great.  It's important to investigate risks fracking poses to groundwater.  Would you agree that it's also important to investigate any risks other forms of energy pose to groundwater?  For example, if you found out that manufacturing windmills was poisoning the groundwater you'd be concerned about that too?"
I: "Yes."
A: Would you agree that for every form of energy we have to look carefully at the positive and negative impacts, accurately?  So if fracking were crucial to millions of people having warm homes in winter we'd factor that in, just like if they were using solar or wind to heat their homes.

Formula: Affirm local concern.  Introduce big picture, locally.  Example of big picture locally.  Conceptualize and broaden.  Example.

Affirming the concern is important because it is disarming.

Result: **Conversation is further pre-structured and I am more credible as someone who is concerned with the big picture**.

### Rule 3: Agree on the moral standard

Agree that the outcome we're after is to maximize human flourishing.

Put another way, we want to find the strategy that **maximizes positive human experiences over the long term**.

People might say: 'you only believe X is good because you work in X.'  It is useful to personalize this attack because when you do, people don't want to pursue it.  Saying: 'Wow, I could have worked in a lot of areas and I chose this one because I believe it is the right thing to do can be very disarming'

Snippet:
"...what's going to benefit human life now and in the future..."

Result: **gained credibility as a humanist**

### Rule 4: Be honest about what you know and don't know

It is ultra-common to make accusations or claims with no understanding of the issue.  This is unacceptable.  This rule applies to both parties in a discussion.

When people act like experts without knowing much, that cannot be allowed.

This one is particularly hard for the bot to follow because it's hard to know what is a good explanation and what isn't.  However, if people admit they don't know much immediately that could be a first thing.

Result: **transitioned from attacker to student**

### Rule 5: Admit our mistakes (content and method) and the mistakes of those we cite

If someone disagrees with the idea that it's important to know something about a process before expressing an strong expectation or evaluation, that's not responsible and they ought to admit that.  Things aren't going to go well if the person isn't willing to admit this.

Result: **transition to step-by-step process of learning**

### Rule 6: Respect people's mental autonomy

When you can tell a story instead of making an assertion, **do it**.

Assertions breed defensiveness and attempts to contradict.

Stories breed interest, even if they are short.

With a story, you can share your method and ask if the other party agrees with it.  Humans feel more comfortable considering an idea if you affirm their autonomy i.e. recognize their right to make up their own mind.

Snippet: I looked around for books about heroes and Atlas Shrugged has some good ones.

Two stories in MCFF: false predictions and the climate issue.

### Rule 7: the 80:20, 64:4, 51:1 Rule

Good to look for outrageously high-leverage things.

People will appreciate you if you respect their time.

Recommended resources are a great way to time-efficiently end a conversation in a way that will result in more learning over time.

Share MCFF and when you share, **make it personal**.  Share www.moralcaseforfossilfuels.com/ as soon as you are established as a thoughtful person capable of giving constructive recommendations**.  Clarify an issue, then recommend.  Know what you are doing at all times.

Snippet: "There's a book on this topic that gave me the big-picture like nothing else did.  I'm telling you this is the best way to learn about the whole issue.  If you don't want to learn that's fine but there's no point in me explaining it worse than the book."

### Other Dos and Don'ts

#### Follow the rules

It is good for both parties to follow the rules.  It cuts down on digressions, and it enables you to stay on track and reach the goal.

#### Increase your empathy

If you are attempting to cover the inferential distance between point A and point B; you need to know as much as you can about *both A and B*.

If you understand the best case for point A, then you will be a lot clearer.  Every false idea has a potential real issue behind it.

#### Increase your clarity

The most effective persuaders are characterized by deep clarity and conviction.

To get from A to B, you need to know exactly what the point B is and what steps lead there.

Take clarity seriously.  You can't mess around and spout a lot of haphazard stuff that you don't understand the evidence for.  Have a mental idea of when you are being clear and when you are not.

#### Understand the structure of the effective conversation

1. establish the right method
1. establish the right content
1. reject the wrong content
1. reject the wrong method

#### Building your material

Alex has a good story, example, analogy, fact, and one liner for **every key issue**.

####
