import keyboard
import time

text = ''' Woo
(Tsunami)
Spider, SEX
Yeah, yeah (woo)
Yeah (woo), yeah (yeah)
Yeah (yeah), yeah
Yeah (yeah), yeah (yeah)
The price I want for a show, you gon' need three promoters (woo)
I got the body from Jim Ellis, but I had switched the motor (skrrt)
I got these badass bitches riding 'round this bitch and they all the coldest (yeah)
I just told her make a store run (yeah)
I just bought all the Trojans (yeah), yeah (yeah)
I told her stay out my mentions (yeah)
I told her stop telling everything she seen and told her, "Meet me at the Ritz" (let's go)
I got baguettes in the back of my ring and I wasn't even tryna hit (tryna hit, yeah, yeah)
I told her she gotta run through the team
Before she can talk to the leader ('fore she can talk to the, yeah)
Lamb chop, I just pulled up with some food (skrrt, skrrt)
I told lil' mama, "Tie all my shoes" (my shoes)
Showed her two million cash, now she woozy (woah)
20 watches and I'm still snoozin' (20)
I had came up out the trenches, then I had beat a few bodies like Boosie
She said, "You murk 'em, I show you my coochie" (woo)
I had to sing to this bitch like lil' Toosii (woo, woah, woah, yee, woo)
Yeah, yeah (woo)
Yeah, yeah (ski)
Yeah, yeah (ski)
Yeah, yeah (let's go)
Bitch got a Backwood on her nightstand
She must be fuckin' with Gunna (yeah, yeah)
I fuck with slatts and we come to eat racks
And I came with some fuckin' piranhas (yeah)
All this Biscotti I got in my 'Wood, need somebody grow me a tree (tree)
Came out the hood, now my trunk got a hood, now I crank up the car with no keys
Beat it, she for the street-neet-neets
Only once, she got hit at the 'spinini
I feel a lil' rich this week, to influence my family to not be cheap (be cheap)
I tote an FN on me, call Neechie-Neech, just a Glocky key
Duke Rollin' 60's, he locked in C's
We roll in that coupe with the bucket seats (bucket seats)
Got out that mud like a football cleat
I used to trap out of that four-door Jeep (four-door)
Call up the plug and he know what I need (know what I need)
Stay on her knees so we hardly speak (hardly speak, yeah)
I'm in New York counting shmoney (yeah)
Ain't the stuntman, but I'm stuntin' (yeah)
Wunna, these vibes wanna love me (yeah)
Not wifey, and no lovey-dovey
Yeah, yeah (woo)
Yeah, yeah (ski)
Yeah, yeah (ski)
Yeah, yeah (let's go)
Bitch had an Act' stain on her jeans
I know she fucking with Thugger (yeah, yeah)
I fuck with slatts and we come to eat racks
And I came with some fuckin' piranhas (yeah) '''

lines = text.split('\n')

while True:
    if keyboard.is_pressed('esc'):
        break


for line in lines:
    keyboard.write(line)
    keyboard.press_and_release('enter')
    time.sleep(.1)

