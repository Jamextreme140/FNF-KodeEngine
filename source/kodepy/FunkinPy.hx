package kodepy;

import flixel.FlxBasic;
import objects.Character;
import psychlua.LuaUtils;
import psychlua.CustomSubstate;

#if LUA_ALLOWED
import psychlua.FunkinLua;
#end

#if HXPY_ALLOWED
import hxpy.*;
import hxpy.Python.File;

class FunkinPy extends Python
{
    //WORK IN PROGRESS
    //public var py:Python = null;

    public function new(?parent:Dynamic, ?file:String, ?varsToBring:Any = null) {
        
        //Python.initialize();
        haxe.Log.trace('Python Code still Unimplemented...', null);
    }

}
#end