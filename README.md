To use this bot you should download this executable ffmpeg.org/download.html and create new folder "FFmpeg"

# Discord-bot

# requirements
```no-highlight
pip install discord
pip install requests 
pip install youtube_dl
pip install PyNaCl
pip install config
```
# config.py

```Python
settings = {
    'token': 'Your token',
    'bot': 'Bot name',
    'id': Client ID without quotes,
    'prefix': 'Your bot prefix',
    'ffmpeg_path': 'ffmpeg',
    'bot_channel_name' : 'Channel Name'
}
```
# functions
```
| Name of the function | Discription | Input |
| Ban | Banning some suspicious user | Name |
| Unban | Unbanning some suspicious user | Name |
| Hello | Literally Hello | - | 
| F*ckU | Naughty bot... | - |
| Joke | TODO | - |
| add | Calculating 2 numbers | First and second number | 
| roll | Throwing into the chat random number | Limit |
| roll100 | Rolling with limit of 100 | - |
| roll2 | Rolling number in interval between 2 input numbers | First and second number | 
| choose | Choose between choices | List of input words to choose |
| repeat | Repeating your input X times | integer X and your input after | 
|  | Youtube |  |
| play | Playing the youtube video in voice chat | Youtube link |
| playNext | Playing next video in the queue | - |
| pause | Pausing the audio | - |
| resume | Resuming the audio | - |
| skip | Skipping to the next video in the queue | - |
| addQueue | Adding video from Youtube to the queue | Youtube link |
| removeQueue | Removing video from the queue | Number in the queue | 
| clearQueue | Clearing queue | - |
| stop | disconnecting the bot from channel | - | 
```