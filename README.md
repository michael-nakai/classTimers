# classTimers

Plays pre-determined sounds when you should be pushing long-cooldown buttons per class.

### File layout
The general idea for every class is to have:
 * A class file with a `get_times()` method, which returns a sorted list of tuples, each of the form:
   * `[(path_to_soundfile, time_to_play_sound), ...]`
 * The associated sound files to play under `sounds/classname/`


