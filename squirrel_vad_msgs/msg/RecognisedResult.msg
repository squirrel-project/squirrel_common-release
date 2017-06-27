#This message is used for two topics: "/arousal" and "/valence"
#header includes time of frame
Header header

#label includes an output of prediction, which has a range of [-1.0, +1.0] (closed range).
#-1.0 indicates non-speech for both arousal and valence. 
#For arousal, higher number means higher arousal
#For valence, higher number means more positive, lower number means more negative
float32 label

#prob is not provided yet
float32 prob


