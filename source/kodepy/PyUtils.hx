package kodepy;

import backend.WeekData;
import objects.Character;

import openfl.display.BlendMode;
import Type.ValueType;

import substates.GameOverSubstate;

typedef PyTweenOptions = {
	type:FlxTweenType,
	startDelay:Float,
	onUpdate:Null<String>,
	onStart:Null<String>,
	onComplete:Null<String>,
	loopDelay:Float,
	ease:EaseFunction
}

class PyUtils {
    public static final Function_Stop:Dynamic = "##KODEPY_FUNCTIONSTOP";
	public static final Function_Continue:Dynamic = "##KODEPY_FUNCTIONCONTINUE";
	public static final Function_StopPy:Dynamic = "##KODEPY_FUNCTIONSTOPPY";

    //WORK IN PROGRESS
}