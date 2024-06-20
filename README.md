# Intelligence artificielle pour Handberton

pip install tensorflow pandas scikit-learn nltk


AI features to the robotic hand using Tensorflow 2 and Keras. 

The index number of thumb is 1 , index number of the index finger is 2, of the middle is 3, of the ring is 4, and of the pinky is 5. The string variable of thumb is "thumb" , index number "index", of the middle is "middle", the ring is "ring", and of the pinky is "pinky". 

The Flex sensor is for each finger is between 10Ω ( when a finger is closed) to 30/50Ω (and when a finger is fully extended)


The AI receives instructions through a chat interface where the user inputs the command and the finger's shoud respond automatically.

Here are the list of commands:

Intent: countdown (n) seconds. 
Funtion: Performs a coutdown for n seconds starting from index 1. All fingers remain closed at the beginning and fingers gets extended one by one as per the value of n, staring from index 1 (thumb)
Note: n ranges from 1 to 5

Intent: (nb) +/-/*/÷ (nb) = (nb) 
Funtion: Performs a calculatins between n variables. All fingers remain closed at the beginning and starting from index 1, the fingers which have the value upto the index number which is of the same value as the result (nb), will open while the rest remain closed. If reslt n is equal to zeo all fingers will remain partially open.
Note: nb ranges from 0 to 5

Intent: Raise the (x) finger
Function: Raises finger which has the corresponds to the string variable of x . All fingers remain closed at the beginning
Note: x is a string variable that stands for any of the four values: "thumb" , "index" , "middle" , "ring" , "pinky"

Intent: Respond "yes" with only the thumb raised or the index finger raised questions.
All fingers remain closed at the begining. Only Thumb raises if the answer is yes whereas whereas all other fingers remain closed or will close if they are not. If the answer is no, Only the index raises if the answer is no whereas whereas all other fingers remain closed or will close if they are not.
Question string: "Are you a robot ?"
Answer : yes
Question string: "Do you have AI ?"
Answer : yes
Question string : "Are you a threat ?"
Answer : no

Intent: rock n roll.
Function: All fingers remain closed. Only the index and middle fingers are raised

Intent: "hello"
Function: all fingers will open

Intent: "goodbye"
Function: all fingers will close.


liste d'instruction interessante

11:49
pour les calculs je souhaite que tout calcul de  0 a 5 peut etre effectué exemple "how much is 2 + 2"  ou l'ia sera capable de faire donner la reponse a la main

11:50
gerer un compte a rebour de 0 a 5 seconde ex "countdown 3 seconds"

11:54
etre capable de levé un doigt entierement ou a moitié quand il lui est demandé ex "raise the index finger completely"

11:54
faire la difference entre chaque doigts

11:56
repondre oui avec le pouce ah des yes no answer

11:58
repondre non avec l'index a des yes no answer

12:02
au moin 1 easter eggs comme repondre :i_love_you_hand_sign: a "rock n roll"

12:03
etre capable de fermer et ouvrir le poing quand on lui dira "say hello/goodbye"

12:06
voila! on a deja une idée de ce que pourra demandé en general (je me suis permis de mettre comment la main réagirait pour anticiper)
