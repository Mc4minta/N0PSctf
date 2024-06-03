# N0PSctf
- [N0PSctf](#n0psctf)
- [Solved Task writeup](#solved-task-writeup)
  - [Jojo is missing! `The Rescue of Jojo`](#jojo-is-missing-the-rescue-of-jojo)
  - [Morse Me `Misc`](#morse-me-misc)
  - [Web cook `Web`](#web-cook-web)
  - [Just read `Reverse`](#just-read-reverse)
  - [Where am I 1/3 `OSINT`](#where-am-i-13-osint)
---
This is my writeup for N0PSctf via [<ins>competition link<ins>](https://ctf.nops.re/) , [<ins>ctf time link<ins>](https://ctftime.org/event/2358) <br>
Held from 1-3 June GMT+7.

![score](resource/score.png)

I was able to solve 5 task in the [Solved Folder](SOLVED/) <br>
And other problems that i try to solve but failed is in the [Unsolved Folder](UNSOLVED/)

And Each Task's Flag is in the flag.txt

Other task that i solved after the competition ended will be in the [Try Folder](TRY/)


---

# Solved Task writeup
## Jojo is missing! `The Rescue of Jojo`
![jojo-is-missing](resource/jojo-is-missing/task.png)
```
We have received a message from Jojo, join out Discord server to read it: https://discord.com/invite/xqvnaGzG6x
```

This task prompted you to join discord server via the link<br>
after that you will see this message

![discord-message](resource/jojo-is-missing/discord-message.png)<br>

you will get this hex code<br>
```
49 66 20 61 6E 79 6F 6E 65 20 72 65 61 64 73 20 69 74 2C 20 49 20 61 6D 20 4A 6F 6A 6F 2E 20 49 20 68 61 76 65 20 62 65 65 6E 20 63 61 70 74 75 72 65 64 20 62 79 20 61 20 67 72 6F 75 70 20 63 61 6C 6C 65 64 20 4A 33 4A 75 4A 34 2E 20 50 6C 65 61 73 65 20 63 6F 6D 65 20 61 6E 64 20 73 61 76 65 20 6D 65 21 0A 4E 30 50 53 7B 4A 30 4A 30 5F 31 73 5F 6D 31 53 35 31 6E 47 21 7D
```
Then I decode it with <br>
```
xxd -r -p
```
We get 
```
If anyone reads it, I am Jojo. I have been captured by a group called J3JuJ4. Please come and save me!
N0PS{J0J0_1s_m1S51nG!}
```
so i use grep to grep the flag and save it in flag.txt
```
cat discord-message.txt | xxd -r -p | grep "N0PS{.*}" > flag.txt
```
We got the flag:
``` 
N0PS{J0J0_1s_m1S51nG!}
```
## Morse Me `Misc`

![morse-me](resource/morse-me/task.png)<br>

download the [challenge.txt](/SOLVED/morse-me/challenge.txt) file<br>
```
....- ...-- -.... ..-. -.... . -.... --... --... ..--- -.... .---- --... ....- --... .- ..--- .---- ..--- ----- ..... ....- -.... ---.. -.... ..... ..--- ----- -.... -.... -.... -.-. -.... .---- -.... --... ..--- ----- -.... ----. --... ...-- ...-- .- ..--- ----- ....- . ...-- ----- ..... ----- ..... ...-- --... -... ....- -.. ...-- ----- --... ..--- ..... ...-- ...-- ...-- ..... ..-. ....- ....- ...-- ...-- -.... ...-- ...-- ----- -.... ....- ...-- ...-- ..... ..--- ..... ..-. ..... ----- --... ..--- ...-- ----- --... -..
```
Decode this via [CyberChef](https://gchq.github.io/CyberChef/)<br>

![solve](resource/morse-me/solve.png)<br>

or we can do this
```
cat morse-to-hex.txt | xxd -r -p | grep -o N0PS{.*} > flag.txt && cat flag.txt
```
We get the flag
```
N0PS{M0rS3_D3c0d3R_Pr0}
```
## Web cook `Web`

## Just read `Reverse`
## Where am I 1/3 `OSINT`
