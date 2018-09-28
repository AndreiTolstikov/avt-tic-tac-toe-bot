# The avtTicTacToeBot project


## 1. Introduction

The `avtTicTacToeBot` project is a Telegram's bot for playing Tic-Tac-Toe.


## 2. Requirements

The `avtTicTacToeBot` project requires the following components:

* [Python 3.6.5](https://www.python.org/) - Python is a programming language that lets you work quickly.
* [python-telegram-bot 11.1.0](https://github.com/python-telegram-bot/python-telegram-bot) - This library provides a pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots/api).


## 3. How to prepare and start using the avtTicTacToeBot project step by step

### 3.1 Fork, Clone or Download the project

### 3.2 Create and activate a new Python virtual environment

`$ python3 -m venv ./venv` 

`$ source ./venv/bin/activate` 

Use `(venv) $ deactivate` for deactivate and exit from Python virtual environment.

### 3.3 Install the requirements 

You can install or upgrade python-telegram-bot library with:

`$ pip3 install python-telegram-bot --upgrade`


### 3.4 Create a new Telegram bot with BotFather and obtain an Access Token

BotFather is a special bot for creating and managing bots in Telegram. To create a new Telegram bot and generate an Access Token, you have to talk to [@BotFather](https://telegram.me/botfather) 
and follow a few simple steps (described [here](https://core.telegram.org/bots#6-botfather)).


**Note:** Don't use `avtTicTacToeBot` name as the **Username** for your bot.

### 3.5 Replace `'<your-TOKEN>'` with your Bot's API token received from BotFather

```python
# avt-tic-tac-toe-bot/bot.py

# ...
def main():

    # Create the EventHandler and pass it your bot's token.
    updater = Updater('<your-TOKEN>')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
# ...
```

### 3.6 Running the bot written with `python-telegram-bot` library

To run the bot from command line:

`$ python3 bot.py` 

**Note:** Press Ctrl-C on the command line or send a signal to the process to stop the
bot.

### 3.7 Start interacting with the bot

> Bots can't initiate conversations with users. A user must either add them to a group or send them a message first. People can use `telegram.me/<bot_username>` links or username search to find your bot.
> - [Bots: An introduction for developers. 4. How are bots different from humans?](https://core.telegram.org/bots#4-how-are-bots-different-from-humans)

For example, for `avtTicTacToeBot`, the link to start interacting with the bot will look like this: [http://t.me/avtTicTacToeBot](http://t.me/avtTicTacToeBot).

#### 3.7.1 Commands to control the bot during the game

`/start` - start a new game.

`/rules` - get the game rules.

`/cancel` - cancel the game by user.

#### 3.7.2 Using custom keyboards

For ease of interaction with the bot during the game, it is recommended 
to use the following special custom keyboards:

* to select a game letter (X or O) 

![avtTicTacToeBot. Custom keyboard to select a game letter (X or O)](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_custom_keyboard_X_or_O_507x523-291x300.png)

* to perform the next move on the board (from 1 to 9)

![avtTicTacToeBot. Custom keyboard to perform the next move on the board (from 1 to 9)](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_custom_keyboard_1_9_510x585-262x300.png)


- to answer the question of the completion or the beginning of a new game (yes or no)

![avtTicTacToeBot. Custom keyboard to answer the question of the completion or the beginning of a new game (yes or no)](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_custom_keyboard_yes_no_508x582-262x300.png)


## 4. Example of the Tic-Tac-Toe game session with avtTicTacToeBot


### 4.1 Used [http://t.me/avtTicTacToeBot](http://t.me/avtTicTacToeBot) short link to start interacting with bot


![avtTicTacToeBot. Game session. Step 1. Used `http://t.me/avtTicTacToeBot` short link to start interacting with bot](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_1_514x647.png)


### 4.2 Used `/start` command to start game session with avtTicToeBot

![avtTicTacToeBot. Game session. avtTicTacToeBot in list of bots in Telegram Desktop](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_in_list_of_bots_in_Telegram_Desktop_283x57.png)


![avtTicTacToeBot. Game session. Step 2. Used `/start` command to start game session with avtTicToeBot](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_2_511x524.png)


### 4.3 User choice 'X' for game (in this case). By random selection, the user is given the right of first move

![avtTicTacToeBot. Game session. Step 3. User choice 'X' for game (in this case). By random selection, the user is given the right of first move](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_3_516x581.png)


### 4.4 The game loop, when the user and the bot perform moves in turn

![avtTicTacToeBot. Game session. Step 4. The game cycle, when the user and the bot perform moves in turn](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_4_512x560.png)

![avtTicTacToeBot. Game session. Step 5. The game cycle, when the user and the bot perform moves in turn](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_5_509x568.png)


![avtTicTacToeBot. Game session. Step 6. The game cycle, when the user and the bot perform moves in turn](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_6_507x564.png)

![avtTicTacToeBot. Game session. Step 7. The game cycle, when the user and the bot perform moves in turn](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_7_505x564.png)

### 4.5 The completion of the game in a draw and the proposal to play again

![avtTicTacToeBot. Game session. Step 8. The completion of the game in a draw and the proposal to play again](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_8_506x417.png)


### 4.6 The game is over

![avtTicTacToeBot. Game session. Step 9. The game is over](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_game_session_step_9_513x127.png)


### 4.7 Example of using `/rules` command

![avtTicTacToeBot. Example of using `/rules` command](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_rules_command_part_1_513x589.png)


![avtTicTacToeBot. Example of using `/rules` command](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_rules_command_part_2_509x380.png)



### 4.8 Example of using `/cancel` command

![avtTicTacToeBot. Example of using `/cancel` command](https://software.avt.dn.ua/wp-content/uploads/2018/09/avtsoft_avtTicTacToeBot_cancel_command_504x131.png)


*We wish victories in the Tic-Tac-Toe game with the `avtTicTacToeBot`*!

― A.V.T. Software (Andrei Tolstikov, Vita Tolstikova)







