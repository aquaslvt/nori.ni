<img align="right" height="145" src=".meow/nori.fi.svg">

# nori.ni [<img src="https://nukocities.neocities.org/nuko/sets/cat325.gif">](https://nukocities.neocities.org/)

nori.ni (aka nori.fi) is basically a sequel to [nori.io](https://github.com/mkukiro/nori.io)

It is a 2D, stack-based esolang which like nori.io, was named after Nori, a beautiful stray cat that I'm planning to adopt!

To run `main.nii` just type `python main.py`, if you want to run another file, use `python main.py path/to/file`

## Commands

The interpreter ignores every other character than these, making them no-op

### IP direction commands

| Arrow | Direction |
| ----- | --------- |
| `<`   | Left      |
| `>`   | Right     |
| `^`   | Up        |
| `v`   | Down      |
| `Q`   | Random    |

### Main commands

| Command     | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| `0`-`F`     | Push the corrisponding hex number as an integer                       |
| `!`         | Pop the last value                                                    |
| `N`         | Push numeric user input                                               |
| `I`         | Push user input                                                       |
| `,`         | Push the user input as an ASCII value                                 |
| `k`         | Push the binary user input as an integer                              |
| `O`         | Output the last value to the console then pop it                      |
| `o`         | Output the last value to the console then pop it w/newline            |
| `.`         | Output the last ASCII value to the console then pop it                |
| `K`         | Output the last value to the console as binary                        |
| `X`         | Clear the console                                                     |
| `@`         | Swap the last two values                                              |
| `$`         | Reverse the whole stack                                               |
| `V`         | Move the last value on the stack to the bottom                        |
| `W`         | Move the bottom value on the stack to the top                         |
| `:`         | Duplicate the top value                                               |
| `+`         | Add last two values together, leaving only the result                 |
| `-`         | Subtract last two values together, leaving only the result            |
| `*`         | Multiply last two values together, leaving only the result            |
| `/`         | Divide last two values together, leaving only the result              |
| `°`         | Raise last two values together, leaving only the result               |
| `z`         | Square root the last value, leaving only the result                   |
| `%`         | Modulo last two values together, leaving only the result              |
| `c`         | Ceil the last number                                                  |
| `f`         | Floor the last number                                                 |
| `r`         | Push a random number (0-15)                                           |
| `b`         | Push a random bit (either 0 or 1)                                     |
| `\|`        | Bitwise OR                                                            |
| `&`         | Bitwise AND                                                           |
| `~`         | Birwise XOR                                                           |
| `?`         | The next instruction is only executed if the popped value is non-zero |
| `=`         | The next instruction is only executed if the popped values are equal  |
| `#`         | Wait 1ms                                                              |

nori.ni arithmetic is NOS × TOS, meaning that `>32*;`, for example, will duplicate 3 (2nd value) by 2 (last value)

### Strings

You can define strings using `''` brackets, for example, `>'Hi'o;` pushes the string *Hi*, then outputs it, and ends the program

## Example programs

Here are some example programs! There are a lot of them (send help they spawn every single nanosecond I breathe)

### Cat program [<img src="https://nukocities.neocities.org/nuko/act/cat1.gif">](https://github.com/mkukiro/nori.ni/tree/develop#cat-program-)

```nii
>IO;
```

### Infinite cat program

```nii
> IO v

^    <
```

### Numerical cat program

```nii
>NO;
```

### Truth machine

```nii
>N?v0o;
   v<
   1 
   O 
   >^
```

### Bit inverter

```nii
1@-
```

### Hello world

```nii
>'Hello, world!'o;
```

### Cool adder

```nii
NN@:O ' + ' O:O+ ' = ' OO
```

### Transgender cube

```nii
> 1969  v
🏳️‍⚧️🏳️‍⚧️🏳️‍⚧️🏳️‍⚧️
🏳️‍⚧️🏳️‍⚧️🏳️‍⚧️🏳️‍⚧️
; OOOO$ <
```

### Random binary sequence screensaver

```nii
> X > bO v
    #     
    ^    <
```

### Switchy bit

```nii
> Xbo v
#      
^     <
```

### Mirrored switchy nibble

```nii
v                          <
>X b:Ob:O 0. 1@-1@-OO 0. # ^
```

### Bitwise AND game

Guess what happens to these numbers when you operate & on them!

```nii
>X r:K r:K &   k=v'Wrong!'o;
                 >'Right!'o v

^                     ##### <
```

### nioOS

A very small os made in under an hour

```nii
> X 'nioOS'o v                                                                v                          <
             > 0. '1 - Calculator'o '0 - nibble'o '^C - Exit'o ··· '-> 'O N ?v>X b:Ob:O 0. 1@-1@-OO 0. # ^
                                                                             > 0. NNX@:O ' + ' O:O+ ' = ' OO 0. v
             ^                                                                                                  <
```

### nioOS 2nd pak

nioOS but with different more useless, playful programs

```nii
> X 'nioOS'o v
             > 0. '1 - Screensaver'o '0 - print!'o '^C - Exit'o ··· '-> 'O N ?v_;
                                                                              > X > bO v
                                                                                  #     
                                                                                  ^    <
```

### nioOS 3rd pak

nioOS but with games!

```nii
> X 'nioOS'o v
             > 0. '1 - AND& 'o '0 - !field'o '^C - Exit'o ··· '-> 'O N ?v_;
                                                                        > X > bO v
                                                                            #     
                                                                            ^    <
```

<p align="center"><img src="https://nukocities.neocities.org/nuko/sets/cat80.gif"></img></p>
