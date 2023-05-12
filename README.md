<img align="right" height="145" src=".meow/nori.fi.svg">

# nori.ni

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

### Main commands

| Command     | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| `0`-`9`     | Push the corrisponding number                                         |
| `!`         | Pop the last value                                                    |
| `N`         | Push numeric user input                                               |
| `I`         | Push user input                                                       |
| `,`         | Push the user input as an ASCII value                                 |
| `O`         | Output the last value to the console then pop it                      |
| `o`         | Output the last value to the console then pop it w/newline            |
| `X`         | Clear the console                                                     |
| `.`         | Output the last ASCII value to the console then pop it                |
| `@`         | Swap the last two values                                              |
| `$`         | Reverse the whole stack                                               |
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
| `r`         | Push a random number                                                  |
| `b`         | Push a random bit (either 0 or 1)                                     |
| `?`         | The next instruction is only executed if the popped value is non-zero |
| `#`         | Wait 1ms                                                              |

nori.ni arithmetic is NOS × TOS, meaning that `>32*;`, for example, will duplicate 3 (2nd value) by 2 (last value)

### Strings

You can define strings using `''` brackets, for example, `>'Hi'o;` pushes the string *Hi*, then outputs it, and ends the program

## Example programs

Here are some example programs! There are a lot of them (send help they spawn every single nanosecond I breathe)

*Please note that currently, the IP is space-sensitive(?), it can't travel through empty spaces*

### Cat program

```>IO;```

### Infinite cat program

```nii
> IO v
^    <
```

### Numerical cat program

```>NO;```

### Truth machine

```nii
>N?v0o;
   v<
   1 
   O 
   >^
```

### Bit inverter

```1@-```

### Hello world

```>'Hello, world!'o;```

### Cool adder

```NN@:O ' + ' O:O+ ' = ' OO```

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

### nioOS

A very small os made in under an hour

```nii
> X 'nioOS'o v                                                                v                          <
             > 0. '1 - Calculator'o '0 - nibble'o '^C - Exit'o ··· '-> 'O N ?v>X b:Ob:O 0. 1@-1@-OO 0. # ^
                                                                             > 0. NNX@:O ' + ' O:O+ ' = ' OO 0. v
             ^                                                                                                  <
```
