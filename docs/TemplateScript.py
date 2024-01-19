# Template still in progress...
# hxpy stuff

def onCreate():
    # triggered when the hxpy file is started, some variables weren't created yet
    pass

def onCreatePost():
    # end of "create"
    pass

def onDestroy():
    # triggered when the hxpy file is ended (Song fade out finished)
    pass

# Gameplay/Song interactions

def onSectionHit():
    # triggered after it goes to the next section
    pass

def onBeatHit():
    # triggered 4 times per section
    pass

def onStepHit():
    # triggered 16 times per section
    pass

def onUpdate(elapsed:float):
    # start of "update", some variables weren't updated yet
    pass

def onUpdatePost(elapsed:float):
    # end of "update"
    pass

def onStartCountdown():
    # countdown started, yeh
    # return Function_Stop if you want to stop the countdown from happening (Can be used to trigger dialogues and stuff! You can trigger the countdown with startCountdown())
    # return Function_Continue
    pass

def onCountdownStarted():
    # called AFTER countdown started, if you want to stop it from starting, refer to the previous function (onStartCountdown)
    pass

def onCountdownTick(tick:Countdown, counter:int):
    match tick:
        case Countdown.THREE:
            # counter equals to 0
            pass
        case Countdown.TWO:
            # counter equals to 1
            pass
        case Countdown.ONE:
            # counter equals to 2
            pass
        case Countdown.GO:
            # counter equals to 3
            pass
        case Countdown.START:
            # counter equals to 4, this has no visual indication or anything, it's pretty much at nearly the exact time the song starts playing
            pass
    
def onSpawnNote(note:Note):
    # Read the function name and you will understand what it does
    pass

def onSongStart():
    pass

def onEndSong():
    pass

# Substate interactions

def onPause():
    # Called when you press Pause while not on a cutscene/etc
    # return Function_Stop if you want to stop the player from pausing the game
    pass

def onResume():
    # Called after the game has been resumed from a pause (WARNING: Not necessarily from the pause screen, but most likely is!!!)
    pass

def onGameover():
    pass

def onGameoverConfirm(retry:bool):
    # Called when you Press Enter/Esc on Game Over
    # If you've pressed Esc, value "retry" will be false
    pass

# Dialogue (When a dialogue is finished, it calls startCountdown again)

def onNextDialogue(line:int):
    pass

def onSkipDialogue(line:int):
    pass

# WIP

# Other function hooks

def onMoveCamera(focus:str):
    if focus == 'boyfriend':
        # called when the camera focus on boyfriend
        pass
    elif focus == 'dad':
        # called when the camera focus on dad (opponent)
        pass

# Event notes hooks

def onEvent(name:str, value1:str, value2:str, strumTime:float):
    # event note triggered
    # triggerEvent() does not call this function!!
    # print(f'Event triggered: {name}, {value1}, {value2}, {strumTime}')
    pass

def onEventPushed(name:str, value1:str, value2:str, strumTime:float):
    # Called for every event note, recommended to precache assets
    pass

def eventEarlyTrigger(name:str):
    # Here's a port of the Kill Henchmen early trigger:

    # if name == 'Kill Henchmen':
    #     return 280

    # This makes the "Kill Henchmen" event be triggered 280 miliseconds earlier so that the kill sound is perfectly timed with the song

    # write your shit under this line, the new return value will override the ones hardcoded on the engine
    pass